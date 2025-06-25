import dagster as dg
from dagster_essentials.resources import database_resource
from dagster_essentials.schedules import trip_update_schedule, weekly_update_schedule
from dagster_essentials.jobs import trip_update_job, weekly_update_job


from dagster_essentials.assets import metrics, trips

trip_assets = dg.load_assets_from_modules([trips])
metric_assets = dg.load_assets_from_modules([metrics])
all_jobs = [trip_update_job, weekly_update_job]
all_schedules = [trip_update_schedule, weekly_update_schedule]


defs = dg.Definitions(
    assets=[*trip_assets, *metric_assets],
    resources={
        "database": database_resource,
    },
    jobs=all_jobs,
    schedules=all_schedules
)
