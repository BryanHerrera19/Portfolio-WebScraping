import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient('mongodb+srv://bherrera:y3p1EcmoqsrtzLCj@webscrapingdatabase.6yrgtql.mongodb.net/?retryWrites=true&w=majority')
wsdb = client["WebScrapingDB"]
carCol = wsdb["Car_Info"]
histCol = wsdb["Car_History"]
ownerCol = wsdb["Owner_History"]

def insertCarInfo(carInfoDict):
    carInfo = carCol.insert_one(carInfoDict)
def insertHistInfo(carHistDict):
    carHist = histCol.insert_one(carHistDict)
def insertOwnerInfo(ownerHistDict):
    ownerHist = ownerCol.insert_one(ownerHistDict)