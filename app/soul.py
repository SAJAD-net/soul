#!/usr/bin/python3.9

import requests
from bs4 import BeautifulSoup
import sys, os
import argparse
import time

ap = argparse.ArgumentParser()
ap.add_argument("-u","--url",required=False,help="url of target")
#ap.add_argument("-i", "--info",nargs="?",required=True,help="information gathering")
args=vars(ap.parse_args())
def header_gathering(url):
    agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"+\
    " (KHTML, like Gecko) Chrome/88.0.4324.182"
    stime=time.time()
    if "http://" and "https://" not in url:
        url="http://"+url
    if url.endswith("/") == False:
        url=url+"/"
    print("Target URL --> "+url)
    try:
        h={'user-agent':agent}
        result=requests.get("%s"% url,headers=h)
        etime=time.time() - stime
        if result.status_code != 200:
            print("[!]- Error --> check your url !")
            print("total time --> %1.2f"%etime)
            exit()
        print("[+]- OK ,Query 1 Successfully !")
        print("Information :\n")
        for k,v in result.headers.items():
            print("\t %s --> %s"%(k,v))
        print("total time --> %1.2f"%etime)
    except:
        print("[!]- Connection Error !")
        
def APP():
    os.system("clear") if os.name == "posix" else os.system("cls")
    print("""
            ███████╗ ██████╗ ██╗   ██╗██╗     
            ██╔════╝██╔═══██╗██║   ██║██║     
            ███████╗██║   ██║██║   ██║██║     
            ╚════██║██║   ██║██║   ██║██║     
            ███████║╚██████╔╝╚██████╔╝███████╗
            ╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝""")
    print("\n\t * WELCOME TO SOUL APP --> H4CK3R V1.0 *\n")
    url=input("soul --> >>> ")
    if url == "quit":
        exit()
    print("Please wite ...")
    header_gathering(url)
    
def RUN():
    if url:=args["url"]:
        header_gathering(url)
    else:
        APP()

RUN()
