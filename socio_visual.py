import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import pymongo
import io


sns.set(style='ticks')
client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0-8vzpx.gcp.mongodb.net/test?retryWrites=true&w=majority")
database = client.unemployment_data

def do_plot():
    SE = database.socioeconomic_data
    SE_data = pd.DataFrame(list(SE.find()))

    dtypes = SE_data.dtypes
    int_columns = SE_data.select_dtypes(include=['int64'])

    sns.lmplot(x='par_pctile', y='count_black_pooled', data=SE_data)

    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image
