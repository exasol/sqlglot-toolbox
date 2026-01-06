from test.utils.test_dialect import Validator

from exasol.sqlglot_toolbox.dialects.exasol import ExasolToolBox


class TestExasol(Validator):
    dialect = ExasolToolBox
    maxDiff = None

    def test_exasol_datetime_format_mapping(self):
        test_cases = [
            ("Dy", "EEE", "DY"),
            ("Mon", "MMM", "MON"),
        ]

        for exasol_fmt, databricks_fmt, oracle_fmt in test_cases:
            with self.subTest(format=exasol_fmt):
                self.validate_all(
                    f"SELECT TO_CHAR(CAST('2024-07-14 02:40:00' AS TIMESTAMP), '{exasol_fmt}')",
                    read={
                        "databricks": f"SELECT date_format(CAST('2024-07-14 02:40:00' AS TIMESTAMP), '{databricks_fmt}')",
                    },
                    write={
                        "oracle": f"SELECT TO_CHAR(CAST('2024-07-14 02:40:00' AS TIMESTAMP), '{oracle_fmt}')",
                        "databricks": f"SELECT DATE_FORMAT(CAST('2024-07-14 02:40:00' AS TIMESTAMP), '{databricks_fmt}')",
                    },
                )
