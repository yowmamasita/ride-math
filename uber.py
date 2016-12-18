from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from pymongo import MongoClient
import time

SERVER_TOKEN = '0aJfSOxv5kCGYD4uf8u-LbJrE4jJPKVMEblJkSmV'

house = {'x': 14.6003243, 'y': 121.0163078}
work = {'x': 14.5552639, 'y': 121.0439924}

mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client.uber_fares


def save_to_db(e):
    collection = db[e['display_name']]
    eid = collection.insert_one(e).inserted_id
    print eid


def segregate(items, callback):
    for i in items:
        i['date'] = int(time.time())
        callback(i)


def main():
    session = Session(server_token=SERVER_TOKEN)
    client = UberRidesClient(session)

    print "home to work.."
    response = client.get_price_estimates(
        start_latitude=house['x'],
        start_longitude=house['y'],
        end_latitude=work['x'],
        end_longitude=work['y'],
        seat_count=1
    )
    estimate = response.json.get('prices')
    segregate(estimate, save_to_db)

    print "work to home.."
    response = client.get_price_estimates(
        start_latitude=work['x'],
        start_longitude=work['y'],
        end_latitude=house['x'],
        end_longitude=house['y'],
        seat_count=1
    )
    estimate = response.json.get('prices')
    segregate(estimate, save_to_db)


if __name__ == "__main__": main()
