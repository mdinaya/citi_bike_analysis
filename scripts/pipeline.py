import pandas as pd
import os
import glob


def extract_data(path_name="../data"):
    """
    :param path_name (str): the path to where data stored
    returns: dataframe of concatenated data
    """
    all_files = glob.glob(os.path.join(path_name, "*csv"))
    df_list = []

    if not all_files:
        print("No CSV files...")

    for filename in all_files:
        print(f"Loading: {filename}...")
        df = pd.read_csv(filename)
        df_list.append(df)

    # merged immediately
    master_df = pd.concat(df_list, axis=0, ignore_index=True)
    print("Succesfully merged!")
    return master_df


def generate_report(df):
    """prints a quick health check of the dataframe."""
    print("\n" + "=" * 30)
    print("DATA QUALITY REPORT")
    print("=" * 30)
    print(f"Total Rows: {len(df)}")
    print(f"Total Columns: {len(df.columns)}")
    print("\n--- Missing Values ---")
    print(
        df.isna().sum()[df.isna().sum() > 0]
        if df.isna().any().any()
        else "No missing values!"
    )
    print("\n--- Data Types ---")
    print(df.dtypes)
    print("=" * 30 + "\n")


def clean_data(df):
    """
    :param df (DataFrame): df that needs cleaning
    returns: cleaned data frame
    """
    if df.empty:
        return df
    print("Cleaning data...")
    # fill missing data with "Unknown"
    df = df.fillna("Unknown")

    # define column mappings
    cat_cols = ["member_casual", "rideable_type"]
    float_cols = ["start_lat", "start_lng", "end_lat", "end_lng"]
    str_cols = [
        "start_station_id",
        "end_station_id",
        "start_station_name",
        "end_station_name",
        "ride_id",
    ]
    time_cols = ["started_at", "ended_at"]
    # change each column depending on its mapping
    for col in df.columns:
        if col in cat_cols:
            df[col] = df[col].astype("category")
        elif col in float_cols:
            df[col] = pd.to_numeric(df[col], errors="coerce").astype("float64")
        elif col in str_cols:
            df[col] = df[col].astype("string")
        elif col in time_cols:
            df[col] = pd.to_datetime(df[col])
            # check if already localized to avoid errors
            if df[col].dt.tz is None:
                df[col] = df[col].dt.tz_localize("UTC")

    return df


def save_data(df, filename="cleaned_data.parquet"):
    """
    :param df: dataframe that needs to be saved as .parquet
    :param filename: the name of the file with data to be saved
    """
    output_dir = os.path.join("..", "data", "processed")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, filename)
    df.to_parquet(output_path, engine="pyarrow", index=False)
    print(f"File saved to {output_path}")


# ----- EXECUTION -----
if __name__ == "__main__":
    raw_df = extract_data("../data")

    if not raw_df.empty:
        # check data before cleaning
        generate_report(raw_df)
        # clean data
        processed_df = clean_data(raw_df)
        # check data after cleaning
        generate_report(processed_df)
        save_data(processed_df, "test_data.parquet")
