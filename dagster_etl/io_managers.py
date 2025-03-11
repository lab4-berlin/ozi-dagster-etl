# dagster_etl/io_managers.py

from dagster import IOManager, io_manager


class PostgresIOManager(IOManager):
    def __init__(self, conn):
        self.conn = conn

    def handle_output(self, context, obj):
        """Inserts data into PostgreSQL without using Pandas"""
        table_name = context.asset_key.path[-1]

        with self.conn.cursor() as cursor:
            for row in obj:
                cursor.execute(f"INSERT INTO {table_name} VALUES {tuple(row)}")
        self.conn.commit()

    def load_input(self, context):
        """Loads data from PostgreSQL as a list of dictionaries"""
        table_name = context.asset_key.path[-1]

        with self.conn.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {table_name}")
            columns = [desc[0] for desc in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]


@io_manager(required_resource_keys={"postgres"})
def postgres_io_manager(context):
    return PostgresIOManager(context.resources.postgres)