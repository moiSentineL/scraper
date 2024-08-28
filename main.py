from bs4 import BeautifulSoup
import requests
import re

req = requests.get("https://sharadkvs11.wordpress.com/2727-2/")

soup = BeautifulSoup(req.text, "html.parser")

elements = soup.find_all(["h3", "a"])



# current = None

def data(regex=r"(20\d{2})(?:-(\d{2}))?", subject=r"") -> list:
    data= []
    for element in elements:
        if re.search(fr"{regex}", element.text) != None:
            if element.name == "h3":
                current = element.text
                data.append({"heading": current, "link": []})
            else:
                if current and re.search(fr"{subject}", element.text) != None:
                    data[-1]["link"].append({"text": element.text, "url": element.get("href")})

    return data

# print(data)

# data("(2024)")
for section in data("(2024-25)"):
    print(f"\n{section['heading']}")
    for link in section['link']:
        print(f"  Text: {link['text']} - URL: {link['url']}")


# for stuff in data:
#     print(stuff)


# for h in headings: 
#     if re.search(r"(20\d{2})-(\d{2})", h.text) != None:
#         print(h.text)


# links = soup.find_all("a")

# for l in links:
#     print(l.text + l.get("href"))
