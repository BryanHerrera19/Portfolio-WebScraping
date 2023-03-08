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

def createCarInfoDict(vehicleInfo):
        tempCarDict = dict(manufacturer = vehicleInfo.company, modelName = vehicleInfo.model, vin = vehicleInfo.vin_history_url,
        color = vehicleInfo.color, year = vehicleInfo.year, mileage = vehicleInfo.miles, transType = vehicleInfo.transmission_type,
        price = vehicleInfo.price, fuelType = vehicleInfo.fuel, image = vehicleInfo.image, url = vehicleInfo.url)
        return tempCarDict

def alreadyExists(carURL):
        numdocs = carCol.count_documents({'url': {"$in": [carURL]}})
        if numdocs > 0:
                print("Car already in database")
                return True
        else:
                print("Car not in database")
                return False