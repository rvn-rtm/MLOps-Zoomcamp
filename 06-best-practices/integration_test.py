import os
import pandas as pd
import subprocess
from batch import get_storage_options

def save_data(df, output_file):
    df.to_parquet(
        output_file,
        engine='pyarrow',
        index=False,
        storage_options=get_storage_options()
    )

def read_data(input_file):
    return pd.read_parquet(input_file, storage_options=get_storage_options())

def run_batch_script():
    subprocess.run(["python", "batch.py", "2023", "01"], check=True)

def verify_result(output_file):
    df_result = read_data(output_file)
    sum_predicted_duration = df_result['predicted_duration'].sum()
    print(f"Sum of predicted durations: {sum_predicted_duration}")
    return sum_predicted_duration

def main():
    run_batch_script()

    output_file = 's3://nyc-duration/out/2023-01.parquet'
    verify_result(output_file)

if __name__ == "__main__":
    main()
