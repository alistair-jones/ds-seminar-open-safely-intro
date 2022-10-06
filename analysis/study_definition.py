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
        "input/dummy_data/dummy_hes_apc_1415.csv",
        "input/schemas/hes_apc_schema.csv"
    )
)
