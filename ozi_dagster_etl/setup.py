from setuptools import find_packages, setup

setup(
    name="ozi_dagster_etl",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        "ozi_dagster_etl": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-postgres<1.10",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)

