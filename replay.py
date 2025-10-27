import argparse, pandas as pd
def main(fr, to):
    df = pd.read_csv("artifacts/cdc.csv")
    df = df.query("@fr <= seq <= @to").sort_values("seq")
    for _, r in df.iterrows():
        print(f"Apply {r['op']} on {r['table']} seq={r['seq']} data={r['after']}")
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="fr", type=int, default=0)
    ap.add_argument("--to", type=int, default=999999)
    a = ap.parse_args()
    main(a.fr, a.to)
