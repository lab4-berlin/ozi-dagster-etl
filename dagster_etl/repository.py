from dagster import Definitions, repository
from etl.etl_load_stats_1d import etl_load_stats_1d
from etl.db_resource import db_connection
from assets import all_assets

defs = Definitions(
    assets=[etl_load_stats_1d],
    resources={"db": db_connection}
)


@repository
def ozi_repo():
    return [all_assets]