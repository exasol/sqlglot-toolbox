import pyexasol


def test_number_of_rows_in_my_table(backend_aware_database_params):
    with pyexasol.connect(**backend_aware_database_params, schema="MY_SCHEMA") as conn:
        num_of_rows = conn.execute("SELECT COUNT(*) FROM MY_TABLE;").fetchval()
        assert num_of_rows == 5
