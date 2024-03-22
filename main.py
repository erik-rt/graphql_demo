import requests
import pprint

url = "https://api.goldsky.com/api/public/project_clrhmyxsvvuao01tu4aqj653e/subgraphs/supswap-exchange-v3/1.0.0/gn"

schema_query = """
{
  __schema {
    queryType {
        fields {
            name
            type {
                name
                fields {
                    name
                    type {
                        name
                        kind
                    }
                }
            }
        }
    }
  }
}

"""

query = """
{
  supDayDatas {
    id
    volumeUSD
    txCount
  }
}

"""
headers = {"Content-Type": "application/json"}

response = requests.post(url, json={"query": query}, headers=headers)

if response.status_code == 200:
    data = response.json()

    supDayDatas = data["data"]["supDayDatas"]
    pprint.pprint(supDayDatas)

    total_vol = sum(float(day["volumeUSD"]) for day in supDayDatas)
    total_tx = sum(int(day["txCount"]) for day in supDayDatas)

    print(f"Total Volume (USD): {total_vol}")
    print(f"Total Daily Swap Counts: {total_tx}")
else:
    print(
        "Query failed to run by returning code of {}. {}".format(
            response.status_code, query
        )
    )
