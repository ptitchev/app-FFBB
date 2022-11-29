import psycopg2


def conn_db(user, password):
    conn = psycopg2.connect(
        host="localhost",
        database='ffbb',
        user=user,
        password=password
    )
    return conn


def create_tb_match(user, password):
    conn = conn_db(user, password)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS match(
    id serial PRIMARY KEY,
    id_poule INT NOT NULL,
    id_gymnase INT NOT NULL,
    nom_eq_dom varchar(200),
    nom_eq_ext varchar(200),
    jour DATE,
    heure TIME,
    resultat varchar(12),
    nb_j int,
    FOREIGN KEY (id_poule) REFERENCES poule (id),
    FOREIGN KEY (id_gymnase) REFERENCES gymnase (id)
     );""")
    conn.commit()
    cur.close()
    conn.close()


def add_match(match):
    L = match[1].split("/")
    date_m = psycopg2.Date(int(L[2]), int(L[1]), int(L[0]))
    L = match[2].split(":")
    heure_m = psycopg2.Time(int(L[0]), int(L[1]), 00)
    params = (match[0], match[7], match[6], match[3], match[4], date_m, heure_m, match[5], match[8])
    req = "INSERT INTO match VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    return params, req


def create_tb_poule(user, password):
    conn = conn_db(user, password)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS poule(
    id serial PRIMARY KEY,
    id_div INT NOT NULL,
    nom varchar(40),
    nb_j int );""")
    conn.commit()
    cur.close()
    conn.close()


def add_poule(poule):
    params = (poule[0], poule[1], poule[2], poule[3])
    req = "INSERT INTO poule VALUES (%s, %s, %s, %s)"
    return params, req


def create_tb_div(user, password):
    conn = conn_db(user, password)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS division(
    id  serial PRIMARY KEY,
    nom varchar(40),
    url varchar(80),
    cle varchar(40) );""")
    conn.commit()
    cur.close()
    conn.close()


def add_div(div):
    params = (div[0], div[1], div[2], div[3])
    req = "INSERT INTO division VALUES (%s, %s, %s, %s)"
    return params, req


def create_tb_gym(user, password):
    conn = conn_db(user, password)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS gymnase(
    id serial PRIMARY KEY,
    lat real,
    long real,
    nom varchar(200),
    adresse varchar(200),
    CP varchar(10),
    ville varchar(200) );""")
    conn.commit()
    cur.close()
    conn.close()


def add_gym(gym):
    params = (gym[0], gym[1], gym[2], gym[3], gym[4], gym[5], gym[6])
    req = "INSERT INTO gymnase VALUES (%s, %s, %s, %s, %s, %s, %s)"
    return params, req


def multi_add(user, password, LT, ft):
    conn = conn_db(user, password)
    L_insert = []
    for elem in LT:
        params, req = ft(elem)
        L_insert.append(params)
    cur = conn.cursor()
    cur.executemany(req, L_insert)
    conn.commit()
    cur.close()
    conn.close()
