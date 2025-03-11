# dagster_etl/assets/__init__.py
from dagster import load_assets_from_modules

# Import all modules that contain assets
from . import (
    stats_1d,
    # Add ALL other asset modules here
)

# Load and export all assets
all_assets = load_assets_from_modules([
    stats_1d,
    # Include all modules listed above
])