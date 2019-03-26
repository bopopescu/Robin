import urllib
import urllib.request
import json
import sys
import os
from googleapiclient.discovery import build

def google_search(search_term, api_key, cse_id, **kwargs):
    try:
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        results = res['items']
        for result in results:
            return result['link']
    except Exception as e:
        return "Algo de errado não está certo aqui...Search"

def substring_after(s, delim):
    try:
        res = s.partition(delim)[2]
        return res
    except Exception as e:
        print (e)
        return "Algo de errado não está certo aqui...Partition"
