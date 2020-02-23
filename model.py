from sklearn import linear_model
import pandas as pd
import matplotlib as plt
import seaborn as sns
import pymongo

CONNECTION_STRING = "mongodb+srv://admin:admin@cluster0-8vzpx.gcp.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
unemployment_data = client.get_database('unemployment_data')

sns.set(color_codes=True)
unemployment_rate = unemployment_data.get_collection('unemployment_rate')
df_unemployment_rate = pd.DataFrame(list(unemployment_rate.find()))
df_unemployment_rate['date'] = df_unemployment_rate['date'].astype('datetime64[ns]')
sns.relplot(x="date", y="unemployment", data=df_unemployment_rate)

ols = linear_model.LinearRegression()
model = ols.fit(df_unemployment_rate['date'].reshape(-1,1), df_unemployment_rate['unemployment'].reshape(-1,1))

print(model.predict(pd.DataFrame(data={'col1': ['2019-01-01']})[0:5]))
