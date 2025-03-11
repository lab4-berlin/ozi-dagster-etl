# dagster_etl/resources.py

from dagster import resource
import psycopg2

@resource(
    config_schema={
        "host": str,
        "port": int,
        "dbname": str,
        "user": str,
        "password": str,
    }
)
def postgres_resource(context):
    config = context.resource_config
    conn = psycopg2.connect(
        host=config["host"],
        port=config["port"],
        dbname=config["dbname"],
        user=config["user"],
        password=config["password"],
    )
    return conn