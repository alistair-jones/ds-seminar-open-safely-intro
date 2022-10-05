from cohortextractor import StudyDefinition, patients  # NOQA
from utils import get_dummy_data_fields


study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.8,
    },

    population=patients.all(),

    **get_dummy_data_fields(
        "artificial_data/artificial_hes_apc_1415.csv",
        "schemas/hes_apc_schema.csv"
    )
)
