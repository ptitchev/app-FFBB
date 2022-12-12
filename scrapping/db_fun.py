#db_fun.py --> fonction de création et de mise a jour de la base

from db_log.form_log import log_info
from scrap.scrap import *
from db_gest.conn_db import *

user, password = log_info()

L_div, L_div_urls, L_div_types = recup_div(url_start)

L_div_keys = []
size = len(L_div)
for i in range(size):
    if L_div_types[i] == 0:
        key = 0
        c = 0 
        while (key == 0) and (c < 10):
            try:
                key = recup_div_key(L_div_urls[i])
            except :
                print('fail - restart (' + str(i+1) + '/' + str(size) + ')')
        L_div_keys.append(key)
        if c > 10 :
            print("after 10 consecutive fails, execution stoped")
    else :
        L_div_keys.append(False)

print('1 - clés récupérées')


L_div_poules =[]
for i in range(len(L_div)):
    if L_div_keys[i] :
        L_div_poules.append(recup_poules(L_div_urls[i]))
    else :
        L_div_poules.append(False)

L_div_nb_journees = []
for i in range(len(L_div)):

    if L_div_keys[i] :
        L_poule_nb_journees = []
        
        for j in range(len(L_div_poules[i])):
            key = hexa_sum(L_div_keys[i][:-5],j)+'.html'
            L_poule_nb_journees.append(recup_nb_journee(key, url_start = url_start))
            
    else :
       L_poule_nb_journees = False
    L_div_nb_journees.append(L_poule_nb_journees)

L_div_classement = []
for i in range(len(L_div)):

    if L_div_keys[i] :
        L_poule_classement = []
        
        for j in range(len(L_div_poules[i])):
            key = hexa_sum(L_div_keys[i][:-5],j)+'.html'
            L_poule_classement.append(recup_classement(key, url_start = url_start))
            
    else :
        L_poule_classement = False
       
    L_div_classement.append(L_poule_classement)

L_div_all_journees = []

L_gym_key = []

for i in range(len(L_div)):
    
    if L_div_keys[i] :
        
        L_poule_all_journees = []

        for j in range(len(L_div_poules[i])):
            
            key = hexa_sum(L_div_keys[i][:-5],j)+'.html'
            L_poule_journees = []
            for k in range(L_div_nb_journees[i][j]):
                
                L_poule_journees.append(recup_result_journee(key, k + 1))

                for match in L_poule_journees[0] :
                    key_gym = match[-1]

                    if key_gym not in L_gym_key :

                        L_gym_key.append(key_gym)

            L_poule_all_journees.append(L_poule_journees)

    else :
       L_poule_all_journees = False
       
    L_div_all_journees.append(L_poule_all_journees)

print('2 - données récupérées')

LT_div = []

for i in range(len(L_div)):
    if L_div_poules[i] :  
        div = [i, L_div[i], L_div_urls[i], L_div_keys[i], "etat"]
        LT_div.append(div)

LT_poule = []

for i in range(len(L_div)):
    if L_div_poules[i] : 
        for j in range(len(L_div_poules[i])):
            poule = [str(i) + str(j), i,  L_div_poules[i][j], L_div_nb_journees[i][j],"etat"]
            LT_poule.append(poule)

LT_match = []

for i in range(len(L_div)):
    if L_div_poules[i] : 
        for j in range(len(L_div_poules[i])):
            for k in range(len(L_div_all_journees[i][j])):
                for l in range(len(L_div_all_journees[i][j][k])):
                    match =  L_div_all_journees[i][j][k][l] + [str(i) + str(j), k + 1]
                    LT_match.append(match)

LT_gymnase = []

for key_g in L_gym_key:
    LT_gymnase.append(recup_gymnase(key_g))

LT_equipe = []

for i in range(len(L_div)):
    if L_div_poules[i] : 
        for j in range(len(L_div_poules[i])):
            for k in range(len(L_div_classement[i][j])):
                equipe = [str(i) + str(j) + str(k), str(i) + str(j), k + 1] + L_div_classement[i][j][k] + L_div_all_journees[1][0][0][0]
                LT_equipe.append(equipe)

print('3 - données nettoyées')

create_tb_match(user, password)
create_tb_div(user, password)
create_tb_poule(user, password)
create_tb_gym(user, password)

multi_add(user, password, LT_match, add_match)
multi_add(user, password, LT_div, add_div)
multi_add(user, password, LT_poule, add_poule)
multi_add(user, password, LT_gymnase, add_gym)

print('4 - données ajoutées à Postgre')