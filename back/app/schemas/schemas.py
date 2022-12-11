from datetime import datetime, date

from pydantic import BaseModel
from typing import Union


class Poule(BaseModel):
    id: int
    nom: str
    url: str

    class Config:
        orm_mode = True


class Division(BaseModel):
    id: int
    nom: str
    url: str

    class Config:
        orm_mode = True


class Gymnase(BaseModel):
    id: int
    lat: float
    long: float
    nom: str
    adresse: str
    CP: str
    ville: str
    matchs: str

    class Config:
        orm_mode = True


class Match(BaseModel):
    id: Union[int, None] = 25087
    poule: Union[Poule, None] = {'id': 00, 'nom': 'Betlic Elite'}
    gymnase: Union[Gymnase, None] = {'id': 34000000916, 'lat': 48.82091, 'long': 2.3682,'nom': 'HALLE CARPENTIER', 'adresse': 'Boulevard Masséna','CP':'75013', 'ville': 'Paris'}
    nom_eq_dom: Union[str, None] = 'PARIS BASKETBALL'
    nom_eq_ext: Union[str, None] = 'SASP ESSM LE PORTEL BASKET BALL COTE DOPALE'
    jour: Union[date, None] = '2022-12-15'
    heure: Union[datetime, None] = None
    resultat: Union[str, None] = None
    nb_j: Union[str, None] = '10'

    class Config:
        orm_mode = True
