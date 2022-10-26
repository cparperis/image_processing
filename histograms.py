#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:00:17 2020

@author: Christopher
"""
#%%
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
#%%
df0ag_0drop = pd.read_csv("/Users/Christopher/Documents/Code/0ag_0droplet.csv")
df0ag_20drop = pd.read_csv('/Users/Christopher/Documents/Code/0ag_20droplet.csv')
df0ag_40drop = pd.read_csv('/Users/Christopher/Documents/Code/0ag_40droplet.csv')

df20ag_0drop = pd.read_csv('/Users/Christopher/Documents/Code/20ag_0droplet.csv')
df20ag_20drop = pd.read_csv('/Users/Christopher/Documents/Code/20ag_20droplet.csv')
df20ag_40drop = pd.read_csv('/Users/Christopher/Documents/Code/20ag_40droplet.csv')

df40ag_0drop = pd.read_csv('/Users/Christopher/Documents/Code/40ag_0droplet.csv')
df40ag_20drop = pd.read_csv('/Users/Christopher/Documents/Code/40ag_20droplet.csv')
df40ag_40drop = pd.read_csv('/Users/Christopher/Documents/Code/40ag_40droplet.csv')
#%%
#sns.distplot(df0ag_0drop['signal'], axlabel='Image Contrast (%)')
#sns.distplot(df0ag_20drop['signal'], axlabel='Image Contrast (%)')
#sns.distplot(df0ag_40drop['signal'], axlabel='Image Contrast (%)')

#sns.distplot(df20ag_0drop['signal'], axlabel='Image Contrast (%)')
#sns.distplot(df20ag_20drop['signal'], axlabel='Image Contrast (%)')
#sns.distplot(df20ag_40drop['signal'], axlabel='Image Contrast (%)')

#sns.distplot(df40ag_0drop['signal'], axlabel='Image Contrast (%)')
#sns.distplot(df40ag_20drop['signal'], axlabel='Image Contrast (%)')
#sns.distplot(df40ag_40drop['signal'], axlabel='Image Contrast (%)')

#%%


import joypy
#%%

df=pd.read_csv('/Users/Christopher/Documents/Code/Python/RI Difference Experiments/Histograms1.csv')


#%%



plt.figure(dpi= 380)
#%%

fig, axes = joypy.joyplot(df, by='Droplet %', color=['#FC642D','#484848','#00A699'],alpha=0.8, ylim='own', x_range=[0,40], legend=True, figsize=(12,8), title='Image Contrast Histograms for Antibiotin-coated \n 40 nm Au NPs with Varying Glycerol \n Concentration (% v/v) Either Side of Bilayer')

plt.show()
######## Decoration

#plt.rc("font", size=20)
plt.xlabel('Image Contrast (%)')
#plt.ylabel('Data Scientist', fontsize=26,  color='grey', alpha=0.8)
























