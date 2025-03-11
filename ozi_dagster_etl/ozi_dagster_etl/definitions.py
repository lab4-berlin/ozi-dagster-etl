from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import ozi_etl_dbt_assets
from .project import ozi_etl_project
from .schedules import schedules

defs = Definitions(
    assets=[ozi_etl_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=ozi_etl_project),
    },
)

