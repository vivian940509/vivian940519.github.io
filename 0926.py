import requests
import webbrowser
import os

url=""
resp = requests.get(url=url)
print(resp)
print(resp.status_code,resp.ok)
if(resp.ok== True):
    page = resp.text
    print(resp.url)
    print(resp.headers)
    print(resp.cookies)
    path = "./0926.test.html"
    with open(path,mode="w",encoding="utf-8")as f:
        f.write(page)
    print(f"html:{path}")
    size = os.path.getsize(path)
    print(size)
else:
    print(resp)
resp.close()
