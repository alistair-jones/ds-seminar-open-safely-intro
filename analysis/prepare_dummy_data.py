import pathlib
import pandas as pd

INPUT_PATH = pathlib.Path("input")
HES_PATIENT_ID_FIELD = "PSEUDO_HESID"
HES_EPISODE_KEY_FIELD = "EPIKEY"


def get_artificial_hes_data() -> pd.DataFrame:
    artificial_hes_path = INPUT_PATH / "artificial_data" / "artificial_hes_apc_1415.csv"
    artificial_df = pd.read_csv(artificial_hes_path)
    return artificial_df


def assign_hes_patient_id_field(df: pd.DataFrame) -> pd.DataFrame:
    # Assign row number over dataset id field as patient_id
    df = df.assign(patient_id=df[HES_PATIENT_ID_FIELD].rank(method="min"))
    df["patient_id"] += df.groupby([HES_PATIENT_ID_FIELD, "patient_id"])[HES_EPISODE_KEY_FIELD].rank(ascending=False) - 1
    df["patient_id"] = df["patient_id"].astype(int)
    return df


def write_dummy_hes_data(dummy_df: pd.DataFrame) -> None:
    dummy_hes_path = INPUT_PATH / "dummy_data" / "dummy_hes_apc_1415.csv"
    dummy_df.to_csv(dummy_hes_path, index=False)


if __name__ == "__main__":
    artificial_df = get_artificial_hes_data()
    dummy_df = assign_hes_patient_id_field(artificial_df)
    write_dummy_hes_data(dummy_df)
