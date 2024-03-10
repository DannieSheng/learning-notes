# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: time_series_forecasting
#     language: python
#     name: python3
# ---

# %%
import pandas as pd
import numpy as np

# %% [markdown]
# # 股价数据分析

# %%
# 读入数据
## date: 日期
## company: 公司代码
## price: 股价
df = pd.read_csv('data/stock_price.csv')
df.head(2)

# %% [markdown]
# 第一问答案：
# 主键是date, company

# %%
#查看日期范围
df['date'].min(), df['date'].max()

# %% [markdown]
# 第二问答案：时间颗粒度为天， 时间范围为2012-05-18到2022-04-06

# %%
# 检查主键重复
df.shape[0] == df[['date','company']].drop_duplicates().shape[0]

# %% [markdown]
# 第三问答案：不存在主键重复的数据

# %%
# 一共有多少条时间序列
df[['company']].drop_duplicates().shape[0]

# %% [markdown]
# 第四问答案：一共有5条时间序列

# %%
# 是否每条时间序列都连续
df['date'] = pd.to_datetime( df['date'] )
date_summary = df.groupby(['company'])['date'].agg(['min','max','nunique']).reset_index()
date_summary['date_miss'] = (date_summary['max'] - date_summary['min']).dt.days+1 - date_summary['nunique']
date_summary[ date_summary['date_miss']>0 ]

# %% [markdown]
# 第五问答案：每一条时间序列都不连续

# %% [markdown]
# # 销售数据分析

# %%
# 读入数据
# store:门店编号
# dept: 商品部门编号
# week: 每周周一的日期 
# sales: 销售金额
df = pd.read_csv('data/store_sales.csv')
df.head(2)

# %% [markdown]
# 第一问答案：
# 主键是week, store, dept

# %%
#查看日期范围
df['week'].min(), df['week'].max()

# %% [markdown]
# 第二问答案：时间颗粒度为周， 时间范围为2010-02-01到2012-10-22

# %%
# 检查主键重复
df.shape[0] == df[['week','store','dept']].drop_duplicates().shape[0]

# %% [markdown]
# 第三问答案：不存在主键重复的数据

# %%
# 一共有多少条时间序列
df[['store','dept']].drop_duplicates().shape[0]

# %% [markdown]
# 第四问答案：一共有3331条时间序列

# %%
# 是否每条时间序列都连续
df['week'] = pd.to_datetime( df['week'] )
date_summary = df.groupby(['store','dept'])['week'].agg(['min','max','nunique']).reset_index()
date_summary['date_miss'] = (date_summary['max'] - date_summary['min']).dt.days//7+1 - date_summary['nunique']
date_summary[ date_summary['date_miss']>0 ]

# %% [markdown]
# 第五问答案：有605条时间序列不连续

# %%
