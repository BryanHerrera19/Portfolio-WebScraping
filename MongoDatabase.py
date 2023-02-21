import vehicle
import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient('mongodb+srv://bherrera:y3p1EcmoqsrtzLCj@webscrapingdatabase.6yrgtql.mongodb.net/?retryWrites=true&w=majority')
wsdb = client["WebScrapingDB"]
carCol = wsdb["Car_Info"]
histCol = wsdb["Car_History"]
ownerCol = wsdb["Owner_History"]

def insertCarInfo(carInfoDict):
    carInfo = carCol.insert_one(carInfoDict)

#Can use dictionary function to simplify
#Format: newDict = dict(manufacturer = x, modelName = y, vin = z, color = a, year = b, currentMileage = c)
#Above can then be imported directly to DB

def createCarInfoDict(vehicleInfo):
    tempCarDict = dict(manufacturer = vehicle.company, modelName = vehicle.model, vin = vehicle.vin,
    color = vehicle.color, year = vehicle.year, mileage = vehicle.mileage)