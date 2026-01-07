"""Pytest helper utilities for SQLGlot dialect validation."""

# pylint: disable=too-many-arguments, too-many-positional-arguments

import logging

import pytest
from sqlglot import (
    ErrorLevel,
    UnsupportedError,
    parse_one,
)
from sqlglot.parser import logger as parser_logger


class Validator:
    """Reusable validator for SQLGlot dialect transpilation tests."""

    dialect = None

    def parse_one(self, sql, **kwargs):
        """Parse SQL using the configured dialect."""
        return parse_one(sql, read=self.dialect, **kwargs)

    def validate_identity(
        self,
        sql,
        write_sql=None,
        pretty=False,
        check_command_warning=False,
        identify=False,
        caplog=None,
    ):
        """Validate that a SQL statement round-trips unchanged."""
        if check_command_warning:
            assert caplog is not None, "caplog fixture is required for log assertions"
            with caplog.at_level(logging.WARNING, logger=parser_logger.name):
                expression = self.parse_one(sql)
                assert f"'{sql[:100]}' contains unsupported syntax" in caplog.text
        else:
            expression = self.parse_one(sql)

        assert expression.sql(
            dialect=self.dialect,
            pretty=pretty,
            identify=identify,
        ) == (write_sql or sql)

        return expression

    def validate_all(self, sql, read=None, write=None, pretty=False, identify=False):
        """
        Validate bidirectional SQL transpilation.

        - `read`: other dialects → canonical SQL
        - `write`: canonical SQL → other dialects
        """
        expression = self.parse_one(sql)

        for read_dialect, read_sql in (read or {}).items():
            result = parse_one(read_sql, read=read_dialect).sql(
                self.dialect,
                unsupported_level=ErrorLevel.IGNORE,
                pretty=pretty,
                identify=identify,
            )
            assert result == sql, f"{read_dialect} -> {sql} failed"

        for write_dialect, write_sql in (write or {}).items():
            if write_sql is UnsupportedError:
                with pytest.raises(UnsupportedError):
                    expression.sql(
                        write_dialect,
                        unsupported_level=ErrorLevel.RAISE,
                    )
            else:
                result = expression.sql(
                    write_dialect,
                    unsupported_level=ErrorLevel.IGNORE,
                    pretty=pretty,
                    identify=identify,
                )
                assert result == write_sql, f"{sql} -> {write_dialect} failed"
