"""
Exasol SQLGlot dialect extensions for the SQLGlot Toolbox.

This module extends the base SQLGlot Exasol dialect with additional
date and time format mappings.
"""

from sqlglot.dialects.exasol import Exasol


class ExasolExtended(Exasol):
    """
    Extended Exasol dialect for SQLGlot Toolbox.

    Adds additional datetime format mappings on top of the base
    SQLGlot Exasol dialect.
    """

    TIME_MAPPING = {
        **Exasol.TIME_MAPPING,
        "Mon": "%b",
        "Month": "%B",
        "Dy": Exasol.TIME_MAPPING["DY"],
        "Day": Exasol.TIME_MAPPING["DAY"],
    }
