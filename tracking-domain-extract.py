# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 05:39:16 2021

@author: shekh
"""
import json
import tldextract
f = open("C:\\Users\\shekh\\IOT\\sam_new.json", encoding='utf-8')
json_data = json.load(f)
ad_f = open("C:\\Users\\shekh\\IOT\\disconnect-tracking-protection-master\\entities.json", encoding='utf-8')
json_data_ads = json.load(ad_f)
dom_list = [each_string.lower() for each_string in json_data_ads['entities'].keys()]
lst = 0
for packet in json_data:
    try:
     k = list(packet['_source']['layers']['dns']['Queries'].keys())
     qry = k[0][0:k[0].index(':')]
     dom = tldextract.extract(qry).domain
     
     if dom.strip() in dom_list :
         ans = list(packet['_source']['layers']['dns']['Answers'].keys())
         print("-----TRACKING DOMAIN DNS PACKET-------")
         print(ans)
         print("----DOMAIN NAME---")
         print(dom)
    except KeyError:
        pass        