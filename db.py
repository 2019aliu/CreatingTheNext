# URI: mongodb+srv://[username]:[password]@[projectname]-gktww.gcp.mongodb.net/[authDB]

import pymongo


CONNECTION_STRING = "mongodb+srv://admin:admin@cluster0-8vzpx.gcp.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
unemployment_data = client.get_database('unemployment_data')
unemployment_rate = unemployment_data.get_collection('unemployment_rate')


def getCollection(name):
    return unemployment_data.get_collection(name)

unemployment_rate = getCollection('unemployment_rate')
print(unemployment_rate.find_one({'date': '1948-06-01'})['unemployment'])