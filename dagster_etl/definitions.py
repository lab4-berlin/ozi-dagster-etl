from dagster import Definitions, load_assets_from_modules
from dagster_etl import assets  # Import the `assets` package
from etl.db_resource import db_connection

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    resources={"db": db_connection}
)
