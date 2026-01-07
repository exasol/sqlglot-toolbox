"""Tests for the Exasol SQLGlot dialect extensions."""

# pylint: disable=too-few-public-methods

from exasol.sqlglot_toolbox.dialects.exasol import ExasolExtended

from .utils.validator import Validator


class TestExasol(Validator):
    """Tests for Exasol datetime format mappings."""

    dialect = ExasolExtended
    maxDiff = None

    def test_exasol_datetime_format_mapping(self):
        """Validate Exasol ↔ Databricks ↔ Oracle datetime formats."""
        test_cases = [
            ("Dy", "EEE", "DY"),
            ("Mon", "MMM", "MON"),
        ]

        for exasol_fmt, databricks_fmt, oracle_fmt in test_cases:
            self.validate_all(
                "SELECT TO_CHAR("
                "CAST('2024-07-14 02:40:00' AS TIMESTAMP), "
                f"'{exasol_fmt}')",
                read={
                    "databricks": (
                        "SELECT DATE_FORMAT("
                        "CAST('2024-07-14 02:40:00' AS TIMESTAMP), "
                        f"'{databricks_fmt}')"
                    )
                },
                write={
                    "oracle": (
                        "SELECT TO_CHAR("
                        "CAST('2024-07-14 02:40:00' AS TIMESTAMP), "
                        f"'{oracle_fmt}')"
                    ),
                    "databricks": (
                        "SELECT DATE_FORMAT("
                        "CAST('2024-07-14 02:40:00' AS TIMESTAMP), "
                        f"'{databricks_fmt}')"
                    ),
                },
            )
