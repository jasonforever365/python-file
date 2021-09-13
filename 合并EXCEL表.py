# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 17:07:11 2020

@author: zhou jian
"""


import numpy as np
import pandas as pd
df_main = pd.read_csv(r"C:\Users\zhou jian\Desktop\datasets\main.csv", skiprows=1)
df_sub1 = pd.read_csv(r"C:\Users\zhou jian\Desktop\datasets\sub1.csv", skiprows=1)
df_sub2 = pd.read_csv(r"C:\Users\zhou jian\Desktop\datasets\sub2.csv", skiprows=1)
df_sub3 = pd.read_csv(r"C:\Users\zhou jian\Desktop\datasets\sub3.csv", skiprows=1)

def get_bal_day_end(df):
    df["Date"] = pd.to_datetime(df_main.Date)
    df = df.sort_values(by = "Date")
    df["date"] = df.Date.dt.date
    return df[["date", "Balance"]].groupby("date").last()

df = get_bal_day_end(df_main)
df1 = get_bal_day_end(df_sub1)
df2 = get_bal_day_end(df_sub2)
df3 = get_bal_day_end(df_sub3)

tmp1 = pd.merge(df, df1, how= "outer", left_index = True, right_index = True,
                suffixes = ("_main", "_sub1"))
tmp2 = pd.merge(df2, df3, how= "outer", left_index = True, right_index = True,
                suffixes = ("_sub2", "_sub3"))
df_total = pd.merge(tmp1, tmp2, how= "outer", left_index = True, right_index = True)
df_total.iloc[0] = df_total.iloc[0].fillna(0)
df_total = df_total.fillna(method = "ffill")
df_total["total"] = df_total.sum(axis = 1)
deposit = df_main[df_main.Type == "deposit"][["Date", "Change"]]
deposit["date"] = deposit.Date.dt.date
deposit = deposit.set_index("date")
del deposit["Date"]
results = pd.merge(df_total, deposit, how = "outer", left_index = True, 
                    right_index = True)
results["Change"] = results.Change.fillna(0)
results["pnl"] = (results.total.diff() - results.Change).fillna(0)
results["pnl_acc"] = results.pnl.cumsum()
print (results.pnl_acc.plot())


