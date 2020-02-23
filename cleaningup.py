import pymongo

CONNECTION_STRING = "mongodb+srv://admin:admin@cluster0-8vzpx.gcp.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
unemployment_data = client.get_database('unemployment_data')
homeless = unemployment_data.get_collection('homeless')

homeless.aggregate([{'unset': 'Sheltered Total Homeless, 2019'}])
