# URI: mongodb+srv://[username]:[password]@[projectname]-gktww.gcp.mongodb.net/[authDB]

import pymongo


CONNECTION_STRING = "mongodb+srv://admin:admin@cluster0-8vzpx.gcp.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
unemployment_data = client.get_database('unemployment_data')
unemployment_rate = unemployment_data.get_collection('unemployment_rate')
