from pathlib import Path

from dagster_dbt import DbtProject

ozi_etl_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..", "..").resolve(),
    packaged_project_dir=Path(__file__).joinpath("..", "..", "dbt-project").resolve(),
)
ozi_etl_project.prepare_if_dev()

