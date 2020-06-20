# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 12:00:01 2020

@author: Andy
"""

import json
import requests

response = requests.get('https://api.kawalcorona.com/indonesia')
data_corona = response.json()[0]
print("\n")
print("Jumlah Pasien Covid-19\n")
print("\t Negara\t: "+data_corona['name'])
print("\t Positif\t: "+data_corona['positif'])
print("\t Sembuh\t\t: "+data_corona['sembuh'])
print("\t Meninggal\t: "+data_corona['meninggal'])
print("\t Dirawat\t: "+data_corona['dirawat'])
print("\n")
print("Data from = https://api.kawalcorona.com/indonesia")
print("Created By = Andi Surya Firmansyah")