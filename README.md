

# Event CDC Simulator

Simulate change-data-capture style events from a SQLite source to a sink (CSV), with lightweight schema registry and replay.

## Quickstart
```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python seed.py
python cdc.py --since 0 --batch 100
python replay.py --from 0 --to 50
```


---

## Contributing
PRs welcome.

