import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///./source.db")
users = pd.DataFrame([
    {"id": 1, "email": "a@example.com", "name": "Alice"},
    {"id": 2, "email": "b@example.com", "name": "Bob"},
])
users.to_sql("users", engine, if_exists="replace", index=False)
print("Seeded users")
