import pandas as pd
import argparse
from pandas_profiling import ProfileReport



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    parser.add_argument("--header", default="infer")


    args = parser.parse_args()

    df= pd.read_csv(args.file,header=args.header,index_col=[0])
    profile = ProfileReport(df, minimal=True,explorative=True)
    # for large dataset minimal is True, and explorative as True
    profile.widgets()
    # Saving file to in JSON and HTML format
    # To HTML
    profile.to_file(f"{args.file}.html")