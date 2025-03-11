from dagster import Definitions, load_assets_from_package_module
from . import assets  # This imports `dagster_etl/assets.py`
from etl.db_resource import db_connection

all_assets = load_assets_from_package_module(assets)

defs = Definitions(
    assets=all_assets,
    resources={"db": db_connection}
)
