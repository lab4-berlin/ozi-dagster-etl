# dagster_etl/repository.py

from dagster import Definitions
from dagster_etl.assets import stats_1d
from dagster_etl.resources import postgres_resource
from dagster_etl.io_managers import postgres_io_manager

defs = Definitions(
    assets=[stats_1d],
    resources={
        "postgres": postgres_resource,
        "postgres_io_manager": postgres_io_manager,
    },
)