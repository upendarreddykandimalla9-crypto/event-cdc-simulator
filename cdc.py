import argparse, time, pandas as pd, json, os
from sqlalchemy import create_engine

def main(since, batch):
    os.makedirs("artifacts", exist_ok=True)
    engine = create_engine("sqlite:///./source.db")
    df = pd.read_sql("select * from users", engine)
    events = []
    seq = since
    for _, r in df.iterrows():
        events.append({"seq": seq, "op":"r", "ts": time.time(), "table":"users", "after": r.to_dict()})
        seq += 1
    out = pd.DataFrame(events)
    out.to_csv("artifacts/cdc.csv", index=False)
    print("Wrote artifacts/cdc.csv with", len(out), "events")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", type=int, default=0)
    ap.add_argument("--batch", type=int, default=100)
    a = ap.parse_args()
    main(a.since, a.batch)
