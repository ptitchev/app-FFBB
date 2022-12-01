from datetime import datetime

from pydantic import BaseModel


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
    id: int
    poule: Poule
    gymnase: Gymnase
    nom_eq_dom: str
    nom_eq_ext: str
    jour: datetime
    heure: datetime
    resultat: str
    nb_j: str

    class Config:
        orm_mode = True
