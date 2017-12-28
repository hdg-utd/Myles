from flask import Flask
import sqlite3

from American_Airlines.american_airlines import AmericanAirlines
from Delta_Airlines.delta_airlines import DeltaAirlines
from Southwest_Airlines.southwest_airlines import SouthwestAirlines
from United_Airlines.united_airlines import UnitedAirlines

from common.db_setup import AirlineDatabase

print(AmericanAirlines.get_aa_raw())
print(DeltaAirlines.get_delta_raw())
print(UnitedAirlines.get_united_raw())
print(SouthwestAirlines.get_southwest_raw())
