def churn_risk(tenure):
    if tenure < 12:
        return "High risk"
    return "Low risk"


def main():
    customer_db = {
        101: {"name": "raju", "tenure": 5},
        102: {"name": "ravi", "tenure": 15},
        103: {"name": "ram", "tenure": 8},
        104: {"name": "rinku", "tenure": 20},
    }

    lookup_ids = (101, 103, 105, 102)

    for cid in lookup_ids:
        try:
            customer = customer_db[cid]
            risk = churn_risk(customer["tenure"])
            print(
                f"Customer {customer['name']} (ID: {cid}) has a {risk} of churn."
            )
        except KeyError:
            print(f"Customer ID {cid} not found in the database.")


if __name__ == "__main__":
    main()
