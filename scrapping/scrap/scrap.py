import requests
import asyncio
from requests_html import HTMLSession, HTML
import time


url_start = 'https://resultats.ffbb.com/'

def hexa_sum(hexa,n): #faire des sommes hexadecimales avec des strings
    nb = hexa[-1]
    if n == 0:
        return hexa

    if n >0:
        if nb == '9':
            hexa = hexa[:-1]+'a'
        elif nb == 'f':
            if len(hexa[:-1]) > 0:
                hexa = hexa_sum(hexa[:-1],1) + '0'
            else :
                hexa = hexa_sum("0",1)+ '0'
        else:
            hexa = hexa[:-1]+chr(ord(nb) + 1)
    return(hexa_sum(hexa, n-1))

def recup_div(url_start = url_start): #retourne la liste des divisions, la liste des urls des divisions et le type de division

    r = requests.get(url_start + 'menu.html')
    r_text = r.content.decode("utf-8")
    r.close()

    L = r_text.split('</a>') #Liste de transit pour recupérer les url --> string "url NOM_CHAMP"

    for i_elem in range(len(L)):
        elem = L[i_elem]

        i_deb = elem.find("<a") #Recherche d'url
        if i_deb != -1 :
            elem = elem[i_deb + 3:]

            elem = elem.replace('href=', '') #Nettoyage d'url
            elem = elem.replace('class="menu"', '')
            elem = elem.replace('target="_parent">', '')
            elem = elem.replace('&Eacute;', 'É')
        L[i_elem] = elem

    L = L[:len(L)-1]

    L_div = [] #Liste nom championnat
    L_div_urls = []
    L_div_types = []

    for i_elem in range(len(L)): #Création des L_div
        elem = L[i_elem]
        i_split = elem.rfind('"')
        div = elem[i_split+1:]
        while div[0] == ' ':
            div = div[1:]
        url = elem[1:i_split]

        if url.find('championnat') != -1: #Gestion type simple : 0 et complexe : 1
            type = 0
        else :
            type = 1

        L_div.append(div)
        L_div_urls.append(url_start + url)
        L_div_types.append(type)

    return L_div, L_div_urls, L_div_types

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

def recup_poules(url_champ0):  #recupère les différentes poules d'une division
    r = requests.get(url_champ0)
    r_text = r.content.decode("utf-8")
    r.close()

    text = r_text[r_text.find('<td id="idTableCoupeChampionnat">')+33:]

    text = text[text.find('var coupes = new Array();')+25:]

    text = text[:text.find(';</script>')]

    if text.find(';') != -1:
        #text = text.split(';')
        #text[0] = text[0][text[0].find(' = ')+3:]
        #text[1] = text[1][text[1].find(' = ')+3:]
        idot = text.find(';')
        text = text[:idot]

    #else :
    text = text[text.find(' = ')+3:]
    text = text.replace('[[','')
    text = text.replace(']]','')

    if text.find('],[') != -1:
        text = text.split('],[')

    else :
        text = [text]

    for i in range(len(text)) :
        text[i] = text[i].replace("'", "")
        i_deb = text[i].find(',') + 1
        text[i] = text[i][i_deb:]

    return text

def recup_nb_journee(key, url_start = url_start): #recupere le nb de journée d'une poule

    url_journee = url_start + "championnat/journees/" + key

    r = requests.get(url_journee)
    r_text = r.content.decode("utf-8")
    r.close()

    nb_journee = r_text[r_text.rfind('javascript:openJournee'):]
    nb_journee = nb_journee[nb_journee.find('">') + 2:]
    nb_journee = nb_journee[:nb_journee.find('</a>')]

    return int(nb_journee)

def clean_row_class(row_c): #nettoie une ligne de classement
    row_c = row_c.replace('</a></td><td align="center">', ';')
    row_c = row_c.replace('</td><td align="center">', ';')
    row_c = row_c.replace(';&nbsp;;', ';')
    i_stop = row_c.find('</td>')
    row_c = row_c[:i_stop]
    L_row_c = row_c.split(';')
    return L_row_c

def recup_classement(key, url_start = url_start): #recupère le classement de toutes les divs + poules

    url_classement = url_start + "championnat/classements/" + key
    r = requests.get(url_classement)
    r_text = r.content.decode("utf-8")
    r.close()
    i_tab = r_text.find('<table class="liste"')
    r_tab = r_text[i_tab + len('<table class="liste"'):]
    L_classement = r_tab.split('class="tableau">')

    Lgd = L_classement[0]

    L_classement = L_classement[1:]

    for i in range(len(L_classement)):
        L_classement[i] = clean_row_class(L_classement[i])

    return L_classement

def clean_row_match(row_match): #nettoie une ligne de journée de match
    row_match = row_match.replace('<td class="gauche" align="center">', '')
    row_match = row_match.replace('</td><td align="center">', ';')
    row_match = row_match.replace('</td><td align="center" style="color : red">', ';')
    i_deb = row_match.find('</td><td><a href="')
    i_fin = row_match.find('class="tableau">') + len('class="tableau">')
    row_match = row_match[:i_deb] +';'+row_match[i_fin:]
    i_deb = row_match.find('</a></td><td><a href="')
    i_fin = row_match.find('class="tableau">') + len('class="tableau">')
    row_match = row_match[:i_deb] +';'+row_match[i_fin:]
    row_match = row_match.replace('</a>', '')
    row_match = row_match.replace('<a href="javascript:openHere(', '')
    row_match = row_match.replace("\'", '')
    i_fin = row_match.find(')"')
    row_match = row_match[:i_fin]
    L_row_match = row_match.split(';')
    return L_row_match

def recup_result_journee(key, nb_j, url_start = url_start): #

    hexa_nb_j = hexa_sum("0",nb_j)

    url_journee = url_start + "championnat/rencontres/" + key[:-5] + hexa_nb_j + '.html'

    r = requests.get(url_journee)
    r_text = r.content.decode("utf-8")
    r.close()
    i_tab = r_text.find('<table class="liste"')
    r_tab = r_text[i_tab + len('<table class="liste"'):]
    L_div_matchs = r_tab.split('altern-2">')
    L_div_matchs = L_div_matchs[1::2]
    for i in range(len(L_div_matchs)):
        L_div_matchs[i] = clean_row_match(L_div_matchs[i])

    return L_div_matchs

def recup_gymnase(key_g):
    url = "https://resultats.ffbb.com/here/here_popup.php?id=" + key_g

    r = requests.get(url)
    r_text = r.content.decode("utf-8")
    r.close()
    i_deb = r_text.find("cartoFbi={") + 10
    i_fin = r_text.find(',"errors":[]}')
    r_text = r_text[i_deb : i_fin]
    r_text = r_text.replace('"','')
    gymnase = r_text.split(',')
    for i in range(len(gymnase)) :
        i_deb = gymnase[i].find(':') + 1
        gymnase[i] = gymnase[i][i_deb:]
    gymnase[0] = float(gymnase[0])
    gymnase[1] = float(gymnase[1])

    return [key_g] + gymnase