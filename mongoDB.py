import vehicle
import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient('mongodb+srv://bherrera:y3p1EcmoqsrtzLCj@webscrapingdatabase.6yrgtql.mongodb.net/?retryWrites=true&w=majority')
wsdb = client["WebScrapingDB"]
carCol = wsdb["Car_Info"]
histCol = wsdb["Car_History"]
ownerCol = wsdb["Owner_History"]

def insertCarInfo(carInfoDict): #inserts a dictionary into database as a record
        carCol.insert_one(carInfoDict)

def createCarInfoDict(vehicleInfo, vinDict): #gets a vehicle and turns it into a dictionary
        tempCarDict = dict(manufacturer = vehicleInfo.company, modelName = vehicleInfo.model, vin = vehicleInfo.vin_history_url,
        color = vehicleInfo.color, year = vehicleInfo.year, mileage = vehicleInfo.miles, transType = vehicleInfo.transmission_type,
        price = vehicleInfo.price, fuelType = vehicleInfo.fuel, image = vehicleInfo.image, url = vehicleInfo.url,
        VINHist = vinDict)
        return tempCarDict

def createVINHistInfoDict(vehicleInfo): #gets new updated info from scraper
        tempVINHistDict = dict(numberOfOwners = vehicleInfo.num_owners, numberOfAccidents = vehicleInfo.accidents,
                               lastState = vehicleInfo.last_state, regularOilChanges = vehicleInfo.regular_oil_changes,
                               usage = vehicleInfo.usage, vin = vehicleInfo.vin)
        return tempVINHistDict

def alreadyExists(carURL): #checks if vehicle is in database
        numdocs = carCol.count_documents({'url': {"$in": [carURL]}})
        if numdocs > 0:
                print("Car already in database")
                return True
        else:
                print("Car not in database")
                return False
        
def updateDB(carURL, newDoc): #updates database record with any new info
        myQuery = {'url': {"$in": [carURL]}}
        carCol.replace_one(myQuery, newDoc)

def getRecords():#Returns all records in the database
       return list(carCol.find())

def getRecordLimit(limitSize):#Set a limit on the number of records you want returned
        return list(carCol.find().limit(limitSize))

def filterQuery(myQuery):#Sets a query in order for use in queries
        return list(carCol.find(myQuery))

def querySearchText(ylist, mlist, text):
        myQuery = {}

        for x in text.split():
                if (x in ylist):
                        myQuery["year"] = int(x)

                elif(x in mlist):
                        myQuery["manufacturer"] = str(x)
                else:
                        myQuery["modelName"] = str(x)

        return list(carCol.find(myQuery))
      