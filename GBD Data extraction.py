import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os




data=pd.read_csv("D:/NCDRC/GBD/2019/data2019.csv")



data=data[(data["measure_name"]=="Deaths") |
          (data["measure_name"]=="DALYs (Disability-Adjusted Life Years)") |
          (data["measure_name"]=="YLDs (Years Lived with Disability)") |
          (data["measure_name"]=="YLLs (Years of Life Lost)")]



print(data["cause_name"].unique())



for x in data["cause_name"].unique():
    df=data[(data["cause_id"]==data[data["cause_name"]==x]["cause_id"].iloc[10]) &
         (data["age_id"]==27) &
         (data["location_id"]==142) &
         #(data["year"]==2019) &
         (data["metric_name"]=="Rate") &
         (data["year_start"]==1990) &
         (data["year_end"]==2019)]
    df.reset_index(drop=True,inplace=True)
    index_list=[2,0,1,5,3,4,11,9,10,8,6,7]
    df2=df.reindex(index_list, copy=False)
    df3=df2.loc[:, ['val','lower','upper']].round(2)
    df3.reset_index(drop=True,inplace=True)
    sample_data=pd.DataFrame()
    a=0
    for row in df3.index:
        sample_list=[]
        sample_list.append("%s (%s to %s)" % (df3.iloc[row,0],df3.iloc[row,1],df3.iloc[row,2]))
        sample_data=pd.concat([sample_data, pd.Series(sample_list, name=a)], axis=1)
        a+=1

        sample_data.rename(columns={0:"%s B Death"%x,1:"%s M Death"%x,2:"%s F Death"%x,
                               3:"%s B DALY"%x,4:"%s M DALY"%x,5:"%s F DALY"%x,
                               6:"%s B YLL"%x,7:"%s M YLL"%x,8:"%s F YLL"%x,
                               9:"%s B YLD"%x,10:"%s M YLD"%x,11:"%s F YLD"%x}, inplace=True)
        if a==12:
            print(sample_data)


