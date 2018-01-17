from flask import Flask
import sqlite3, json

from American_Airlines.american_airlines import AmericanAirlines
from Delta_Airlines.delta_airlines import DeltaAirlines
from Southwest_Airlines.southwest_airlines import SouthwestAirlines
from United_Airlines.united_airlines import UnitedAirlines

from common.db_setup import AirlineDatabase


airline_data = {}
aa_data = {}
delta_data = {}
united_data = {}
southwest_data = {}

for item in AmericanAirlines.get_aa_raw():
    #print(list(item.keys()))
    aa_data[list(item.keys())[0]] = item[list(item.keys())[0]]
for item in DeltaAirlines.get_delta_raw():
    #print(list(item.keys()))
    delta_data[list(item.keys())[0]] = item[list(item.keys())[0]]
for item in UnitedAirlines.get_united_raw():
    #print(list(item.keys()))
    united_data[list(item.keys())[0]] = item[list(item.keys())[0]]
for item in SouthwestAirlines.get_southwest_raw():
    #print(list(item.keys()))
    southwest_data[list(item.keys())[0]] = item[list(item.keys())[0]]

airline_data["aa"] = aa_data
airline_data["delta"] = delta_data
airline_data["united"] = united_data
airline_data["southwest"] = southwest_data

with open('./result_db.json', 'w') as fp:
    json.dump(airline_data, fp)
