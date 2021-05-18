# -*- coding: utf-8 -*-
"""
Created on Tue May  4 22:40:49 2021

@author: shekh
This file successfully edits the HTTP host parameter but is unable to edit the Query parameters in the HTTP GET requests to Brightcove tracking domain
"""

from mitmproxy import http
from mitmproxy import ctx
def request(flow: http.HTTPFlow) -> None:
    ctx.log.info("In HttP request")
    if "metrics.brightcove.com" in flow.request.pretty_url:
        ctx.log.info(flow.request.url)
        ctx.log.info("found brightcove")
        str = flow.request.pretty_url
        x = str.split("/")
        y = x[4].split("&")
        y[4] = "account=000000"
        y[1] = "device_manufacturer=ABCD"
        x[4] = y
        str1 = ""
        str2 = ""
        for cn in range(len(y)-1):
            str2 = str2 + y[cn] + "&"
        str2 = str2 + y[-1]
        for cnt in range(len(x)-1):
            str1 = str1+x[cnt]+"/" 
        str1 = str1+str2
        ctx.log.info(flow.request.url)
        ctx.log.info(flow.request.url)
        ctx.log.info("str1")
        ctx.log.info(str1)
        flow.request.url = str1
        flow.request.host = "mitmproxy.org"
        ctx.log.info("newurl")
        ctx.log.info(flow.request.url)
      
      
      
      
      
      
      
