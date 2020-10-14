import tabula
import pandas as pd
from datetime import datetime
url = ("CSBV_BOM_2020-2021_1306_15354.pdf")

df = tabula.read_pdf(url,pages='all')
print(len(df))
frame=[]
result = pd.DataFrame()

for i in range(len(df)):
    frame.append(df[i])

result = pd.concat(frame, axis=1, sort=False)
result1 = result.to_dict('series')
print(result1)

'''
dateTimeObj = datetime.now()
timeStr = dateTimeObj.strftime("%H%M%S%f")
new = "sample" + timeStr + ".csv"
result.to_csv(new,index=False)'''
