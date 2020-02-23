import pandas as pd

govspend = pd.read_csv('unemployment/govspend.csv')
gdp = pd.read_csv('unemployment/gdp.csv')
cpi = pd.read_csv('unemployment/cpi.csv')
unemp = pd.read_csv('unemployment/unemployment_rate.csv')

govspendDates = govspend['DATE']
gdpDates = gdp['DATE']
cpiDates = cpi['DATE']
unempDates = unemp['date']

rows_list = []
print(len(cpi))

for i in range(len(cpi)):
    a = cpi.iloc[i]['DATE']
    b = cpi.iloc[i]['CPIAUCSL']

    count = 0
    for j in range(len(gdp)):
        c = gdp.iloc[j]['DATE']
        d = gdp.iloc[j]['GDPC1']
        if a == c:
            count += 1
            break
    for k in range(len(govspend)):
        e = govspend.iloc[k]['DATE']
        f = govspend.iloc[k]['G160761A027NBEA']
        if a == e:
            count += 1
            break
    for l in range(len(unemp)):
        g = unemp.iloc[l]['date']
        h = unemp.iloc[l]['unemployment_rate']
        if a == g:
            count += 1
            break

    if count == 3:
        print(a)
        rows_list.append([a, b, d, f, h])


df = pd.DataFrame(rows_list)
df.to_csv('model_data.csv', sep='\t')
