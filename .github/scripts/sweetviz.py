import pandas as pd
import argparse
from pandas_profiling import ProfileReport


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    parser.add_argument("--header", default="infer")

    args = parser.parse_args()

    df = pd.read_csv(args.file, header=args.header, index_col=[0])
    report = sv.analyze(df, "Label")
    # save file in html format
    report.show_html(f"{args.file}.html")
