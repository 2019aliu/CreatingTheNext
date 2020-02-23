import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0-8vzpx.gcp.mongodb.net/test?retryWrites=true&w=majority")

# database name
unemployment_data = client.get_database('unemployment_data')


def getCollection(name):
    return unemployment_data.get_collection(name)

unemployment_rate = getCollection('unemployment_rate')
print(unemployment_rate.find_one({'date': '1948-06-01'})['unemployment'])
