from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from .project import ozi_etl_project


@dbt_assets(manifest=ozi_etl_project.manifest_path)
def ozi_etl_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    

