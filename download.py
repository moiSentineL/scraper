import main 
import re
import requests
import os

for l in main.data("2024"):
    for s in l["link"]:
        url = re.sub('/edit.*', '/export?format=pdf', s["url"])
        r = requests.get(url, allow_redirects=True)
        if os.path.exists(path := os.path.join(os.path.dirname(__file__) + f"/files/{l["heading"]}")):
            print(path + l["heading"])
            open(f"{path}/{s["text"]}.pdf", "wb").write(r.content)
        else:
            print(path + "else" + l["heading"])
            # print(os.path.join(os.path.dirname(__file__) + f"/files/{l["heading"]}"))
            os.makedirs(os.path.join(os.path.dirname(__file__) + f"/files/{l["heading"]}"))
            open(f"{path}/{s["text"]}.pdf", "wb").write(r.content)
        # print(re.sub('/edit.*', '/export?format=pdf', s["url"]))