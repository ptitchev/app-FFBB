from requests_html import HTMLSession, HTMLSession

url = "https://resultats.ffbb.com/championnat/b5e6211fb092.html"

def recup_div_key(url_champ0):
    session = HTMLSession()
    r = session.get(url_champ0)
    r.html.render()
    r_text = r.html.raw_html
    r.close()
    session.close()
    r_text = r_text.decode("utf-8")

    key = r_text[r_text.find("idIframeJournee") + 15:]
    key = key[key.find('src="journees/') + 14:]
    key = key[:key.find(".html") + 5]

    return key

print(recup_div_key(url))