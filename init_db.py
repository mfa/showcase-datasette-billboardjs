import datetime
import random

from sqlite_utils import Database


def main():
    db = Database("demo.db")

    # create tables
    table = db["reports"]
    if not table.exists():
        table.create(
            {
                "created": str,
                "delta_sec": float,
            }
        )

    # add some demo data
    dt = datetime.datetime.utcnow()
    for index in range(1, 1000):
        table.insert(
            {
                "created": dt - datetime.timedelta(minutes=index),
                "delta_sec": random.randint(100, 800) / 1000,
            }
        )


if __name__ == "__main__":
    main()
