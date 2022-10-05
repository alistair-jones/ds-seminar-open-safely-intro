from typing import Dict
import pandas as pd
from cohortextractor import patients


def get_dummy_data_fields(
    dummy_data_path: str,
    schema_path: str
) -> Dict:
    schema = pd.read_csv(schema_path)

    return {
        x["FIELD_NAME"]: patients.with_value_from_file(
            dummy_data_path,
            returning=x["FIELD_NAME"],
            returning_type=x["PYTHON_TYPE"],
        )
        for x in schema.to_dict(orient="records")
        if x["FIELD_NAME"] != "patient_id"
    }
