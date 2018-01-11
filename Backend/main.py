from flask import Flask
import sqlite3, json

from American_Airlines.american_airlines import AmericanAirlines
from Delta_Airlines.delta_airlines import DeltaAirlines
from Southwest_Airlines.southwest_airlines import SouthwestAirlines
from United_Airlines.united_airlines import UnitedAirlines

from common.db_setup import AirlineDatabase

airline_data = {}
airline_data["aa"] = AmericanAirlines.get_aa_raw()
airline_data["delta"] = DeltaAirlines.get_delta_raw()
airline_data["united"] = UnitedAirlines.get_united_raw()
airline_data["southwest"] = SouthwestAirlines.get_southwest_raw()

with open('./result_db.json', 'w') as fp:
    json.dump(airline_data, fp)
