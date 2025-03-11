from dagster import Definitions, load_assets_from_modules
from .assets import __init__ as assets  # Import the package, not a module
from etl.db_resource import db_connection

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    resources={"db": db_connection}
)