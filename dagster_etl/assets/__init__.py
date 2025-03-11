from dagster import load_assets_from_modules, AssetsDefinition

from . import (
    load_stats_1d
)

all_assets = load_assets_from_modules([
    load_stats_1d,
])