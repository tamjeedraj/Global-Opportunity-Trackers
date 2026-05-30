
# import requests
# from bs4 import BeautifulSoup

## def fetch_opportunities():
#     url = "https://www.opportunitydesk.org/feed/"
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, "html.parser")  # html.parser इस्तेमाल किया

#     opportunities = []
#     for item in soup.find_all("item"):
#         title = item.find("title").get_text(strip=True)
#         link = item.find("link").get_text(strip=True)
#         opportunities.append({
#             "title": title,
#             "link": link
#         })

#     return opportunities

# if __name__ == "__main__":
#     data = fetch_opportunities()
#     print(f"Found {len(data)} opportunities")
#     for opp in data[:10]:
#         print(opp)

## import requests
# from bs4 import BeautifulSoup

# def fetch_opportunities():
#     url = "https://www.opportunitydesk.org/feed/"
#     page = requests.get(url)
#     #soup = BeautifulSoup(page.content, "html.parser")
#     soup = BeautifulSoup(page.content, "xml")

#     opportunities = []
#     for item in soup.find_all("item"):
#         title = item.find("title").get_text(strip=True)
#         # link कभी <link> में होता है, कभी <guid> में
#         link_tag = item.find("link")
#         if link_tag and link_tag.get_text(strip=True):
#             link = link_tag.get_text(strip=True)
#         else:
#             guid_tag = item.find("guid")
#             link = guid_tag.get_text(strip=True) if guid_tag else ""

#         opportunities.append({
#             "title": title,
#             "link": link
#         })

#     return opportunities

# if __name__ == "__main__":
#     data = fetch_opportunities()
#     print(f"Found {len(data)} opportunities")
#     for opp in data[:10]:
#         print(opp)


import requests
from bs4 import BeautifulSoup

def fetch_description(url: str) -> str:
    """हर opportunity link से description निकालने का function"""
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        # Example: पहला paragraph को description मान लें
        paragraph = soup.find("p")
        return paragraph.get_text(strip=True) if paragraph else ""
    except Exception:
        return ""

def fetch_opportunities():
    url = "https://www.opportunitydesk.org/feed/"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "xml")

    opportunities = []
    for item in soup.find_all("item"):
        title = item.find("title").get_text(strip=True)

        # link कभी <link> में होता है, कभी <guid> में
        link_tag = item.find("link")
        if link_tag and link_tag.get_text(strip=True):
            link = link_tag.get_text(strip=True)
        else:
            guid_tag = item.find("guid")
            link = guid_tag.get_text(strip=True) if guid_tag else ""

        # अब description भी scrape करें
        description = fetch_description(link)

        opportunities.append({
            "title": title,
            "link": link,
            "description": description
        })

    return opportunities

if __name__ == "__main__":
    data = fetch_opportunities()
    print(f"Found {len(data)} opportunities")
    for opp in data[:10]:   # सिर्फ 10 print करें demo के लिए
        print(opp)
