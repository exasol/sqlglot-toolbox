from sqlglot.dialects.exasol import Exasol



class ExasolToolBox(Exasol):
    TIME_MAPPING = {
        **Exasol.TIME_MAPPING,
        "Mon": "%b",
        "Month": "%B",
        "Dy": Exasol.TIME_MAPPING["DY"],
        "Day": Exasol.TIME_MAPPING["DAY"],
    }


