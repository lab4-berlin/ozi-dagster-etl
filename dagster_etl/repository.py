# dagster_etl/repository.py
from dagster import repository

from dagster_etl.assets import all_assets

@repository
def ozi_repo():
    """Repository for Ozi data assets."""
    return [all_assets]