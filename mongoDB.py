import vehicle
import pymongo
from pymongo import MongoClient



client = pymongo.MongoClient('mongodb+srv://bherrera:y3p1EcmoqsrtzLCj@webscrapingdatabase.6yrgtql.mongodb.net/?retryWrites=true&w=majority')
wsdb = client["WebScrapingDB"]
carCol = wsdb["Car_Info"]
histCol = wsdb["Car_History"]
ownerCol = wsdb["Owner_History"]

def insertCarInfo(carInfoDict): #inserts a dictionary into database as a record
        carInfo = carCol.insert_one(carInfoDict)

def createCarInfoDict(vehicleInfo, vinDict): #gets a vehicle and turns it into a dictionary
        tempCarDict = dict(manufacturer = vehicleInfo.company, modelName = vehicleInfo.model, vin = vehicleInfo.vin_history_url,
        color = vehicleInfo.color, year = vehicleInfo.year, mileage = vehicleInfo.miles, transType = vehicleInfo.transmission_type,
        price = vehicleInfo.price, fuelType = vehicleInfo.fuel, image = vehicleInfo.image, url = vehicleInfo.url,
        VINHist = vinDict)
        return tempCarDict

def createVINHistInfoDict(vehicleInfo): #gets new updated info from scraper
        tempVINHistDict = dict(numberOfOwners = vehicleInfo.num_owners, numberOfAccidents = vehicleInfo.accidents,
                               lastState = vehicleInfo.last_state, regularOilChanges = vehicleInfo.regular_oil_changes,
                               usage = vehicleInfo.usage)
        return tempVINHistDict

def alreadyExists(carURL): #checks if vehicle is in database
        numdocs = carCol.count_documents({'url': {"$in": [carURL]}})
        if numdocs > 0:
                print("Car already in database")
                return True
        else:
                print("Car not in database")
                return False
        
def updateDB(carURL, newInfo): #updates database record with any new info
        myQuery = {'url': {"$in": [carURL]}}
        newCarHist = {"$set": {"carHist": newInfo}}
        carCol.update_one(myQuery, newCarHist)

def getRecords():#Returns all records in the database
       return list(carCol.find())

def getRecordLimit(limitSize):#Set a limit on the number of records you want returned
        return list(carCol.find().limit(limitSize))

def setPriceQuery(priceQuery):#Sets a query in order for use in queries
        print("Reached Here!")
        stringList = priceQuery.split()
        if(stringList[0] == "$lt" or stringList[0] == "$gt"):
            myQuery = { "price" : { stringList[0] : int(stringList[1])}}  
        else:
                myQuery = { "$and" : [{"price" : { "$lt" : int(stringList[1]) }},
                                      {"price" : { "$gt" : int(stringList[0]) }}]}
        return list(carCol.find(myQuery))

def setMileQuery(mileQuery):#Sets a query in order for use in queries
        print("Reached Here!")
        stringList = mileQuery.split()
        if(stringList[0] == "$lt" or stringList[0] == "$gt"):
            myQuery = { "mileage" : { stringList[0] : int(stringList[1])}}  
        else:
                myQuery = { "$and" : [{"mileage" : { "$lt" : int(stringList[1]) }},
                                      {"mileage" : { "$gt" : int(stringList[0]) }}]}
        return list(carCol.find(myQuery))

def setYearQuery(yearQuery):#Sets a query in order for use in queries
        stringList = yearQuery.split()
        myQuery = { "$and" : [{"year" : { "$lt" : int(stringList[1]) }},
                                {"year" : { "$gt" : int(stringList[0]) }}]}
        return list(carCol.find(myQuery))

def setBrandQuery(brandQuery):#Sets a query in order for use in queries
        myQuery = { "manufacturer" : brandQuery }
        return list(carCol.find(myQuery))