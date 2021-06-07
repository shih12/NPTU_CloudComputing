from typing import Collection
import requests
from bs4 import BeautifulSoup
import json


def repyile(page):
    url = "https://www.ptt.cc/bbs/Gossiping/index.html";
    data = []
    for i in range(page):

        res = rs.get(url)
        soup = BeautifulSoup(res.text,"html.parser")
        sel = soup.select("div.title a")
        u = soup.select("div.btn-group.btn-group-paging a")
        url = "https://www.ptt.cc"+u[1]["href"]
        
        for s in sel:
            data.append({'url': "https://www.ptt.cc"+s["href"], 'title':s.text})

    s = json.dumps(data,ensure_ascii=False)

    return s

repyile(2)