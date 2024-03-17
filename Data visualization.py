import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("D:/NCDRC/GBD/2019/data2019.csv")




data=data[(data["measure_name"]=="Deaths") |
          (data["measure_name"]=="DALYs (Disability-Adjusted Life Years)") |
          (data["measure_name"]=="YLDs (Years Lived with Disability)") |
          (data["measure_name"]=="YLLs (Years of Life Lost)")]





pd.options.display.float_format = '{:.2f}'.format

for x in data["cause_name"].unique():
    df1=data[(data["cause_id"]==data[data["cause_name"]==x]["cause_id"].iloc[10]) &
        (data["age_id"]==27) &
        (data["location_id"]==142) &
        (data["metric_name"]=="Rate") &
        (data["year"].notnull())]
    a=[v for k, v in df1.groupby('sex_name')]
    for i,val in enumerate(a):
        globals()['b'+str(i)] = [v for k, v in a[i].groupby('measure_name')]
    for i in range(3):
        for j in range(4):
            globals()['b'+str(i)][j]= globals()['b'+str(i)][j].loc[:,["year",
                                                                      "val",
                                                                      "upper",
                                                                      "lower",
                                                                      "cause_name",
                                                                      "measure_name", 
                                                                      "sex_name"]].sort_values(by=["year"])
        
        
        
    plt.style.use("seaborn-dark")
    fig, ax = plt.subplots(2,2, figsize=(20,12))
    fig.tight_layout(pad=3.5)
    a=0
    for i in range(2):
        for j in range(2):
            ax[i,j].plot(b0[a]["year"], b0[a]["val"], "navy", linewidth=1)
            ax[i,j].plot(b0[a]["year"], b0[a]["upper"], "violet", linewidth=0.4)
            ax[i,j].plot(b0[a]["year"], b0[a]["lower"], "violet", linewidth=0.4)
            ax[i,j].fill_between(b0[a]["year"], b0[a]["val"], b0[a]["upper"], color="violet", alpha=0.2, linewidth=0.5)
            ax[i,j].fill_between(b0[a]["year"], b0[a]["val"], b0[a]["lower"], color="violet", alpha=0.2, linewidth=0.5)
            ax[i,j].plot(b1[a]["year"], b1[a]["val"], "navy", linewidth=1, ls="--")
            ax[i,j].plot(b1[a]["year"], b1[a]["upper"], "lightgreen", linewidth=0.4)
            ax[i,j].plot(b1[a]["year"], b1[a]["lower"], "lightgreen", linewidth=0.4)
            ax[i,j].fill_between(b1[a]["year"], b1[a]["val"], b1[a]["upper"], color="lightgreen", alpha=0.2, linewidth=0.5)
            ax[i,j].fill_between(b1[a]["year"], b1[a]["val"], b1[a]["lower"], color="lightgreen", alpha=0.2, linewidth=0.5)
            ax[i,j].plot(b2[a]["year"], b2[a]["val"], "navy", linewidth=1, ls=":")
            ax[i,j].plot(b2[a]["year"], b2[a]["upper"], "lightsalmon", linewidth=0.4)
            ax[i,j].plot(b2[a]["year"], b2[a]["lower"], "lightsalmon", linewidth=0.4)
            ax[i,j].fill_between(b2[a]["year"], b2[a]["val"], b2[a]["upper"], color="lightsalmon", alpha=0.2, linewidth=0.5)
            ax[i,j].fill_between(b2[a]["year"], b2[a]["val"], b2[a]["lower"], color="lightsalmon", alpha=0.2, linewidth=0.5)
            ax[i,j].tick_params(axis="both", which="major", labelsize=6)
            ax[i,j].tick_params(axis="y", rotation=90)
            ax[i,j].grid(axis="y", c="silver")
            ax[i,j].set_axisbelow(True)
            ax[i,j].set_facecolor("w")
            ax[i,j].set_xlabel("Year", fontsize=8)
            ax[i,j].set_ylabel("Age Standardized rate (per 100,000)", fontsize=8)
            ax[i,j].ticklabel_format(style = 'plain')
            ax[i,j].margins(False)
            a+=1
        
    ax[0,0].set_title("DALYs (Disability-Adjusted Life Years)", fontsize=10, weight="bold")
    #ax[0,0].set_ylim([200,750])
    ax[1,0].set_title("YLDs (Years Lived with Disability)", fontsize=10, weight="bold")
    #ax[1,0].set_ylim([200,750])
    ax[0,1].set_title("Deaths", fontsize=10, weight="bold")
    ax[1,1].set_title("YLLs (Years of Life Lost)", fontsize=10, weight="bold")

    line = plt.Line2D([0],[0], color="violet", linewidth=1, linestyle='-')
    dot = plt.Line2D([0],[0], color="lightsalmon", linewidth=1, linestyle=':')
    dot_line = plt.Line2D([0],[0], color="lightgreen", linewidth=1, linestyle='--')
    fig.legend(handles=[line,dot,dot_line], labels=["Both","Male","Female"], loc=(0.45,0.45), fontsize=8, ncol=3, frameon=True)
    plt.suptitle(x, fontsize=15, weight="bold", y=1.05)
    plt.show()


    #plt.savefig("D:/NCDRC/GBD/2019/graphs/%s" % x, bbox_inches='tight')






