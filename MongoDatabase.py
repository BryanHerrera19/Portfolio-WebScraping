import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient('mongodb+srv://bherrera:y3p1EcmoqsrtzLCj@webscrapingdatabase.6yrgtql.mongodb.net/?retryWrites=true&w=majority')
wsdb = client["WebScrapingDB"]
carCol = wsdb["Car_Info"]

testDict = dict(manufacturer = "Ford", modelName = "Raptor", vin = 1564823, color = "Red", year = 2021, currentMileage = 10000)

def insertCarInfo(carInfoDict):
    carInfo = carCol.insert_one(carInfoDict)

insertCarInfo(testDict)