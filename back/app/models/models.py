from sqlalchemy import Column, ForeignKey, Integer, String, Date, Time, Float
from sqlalchemy.orm import relationship

from ..database import Base


class Match(Base):
    __tablename__ = "match"
    id = Column(Integer, primary_key=True)

    id_poule = Column(Integer, ForeignKey("poule.id"))
    poule = relationship("Poule", back_populates="matchs")

    id_gymnase = Column(Integer, ForeignKey("gymnase.id"))
    gymnase = relationship("Gymnase", back_populates="matchs")

    nom_eq_dom = Column(String(200))
    nom_eq_ext = Column(String(200))
    jour = Column(Date)
    heure = Column(Time)
    resultat = Column(String(12))
    nb_j = Column(Integer)


class Poule(Base):
    __tablename__ = "poule"
    id = Column(Integer, primary_key=True)
    nom = Column(String(40))
    url = Column(String(80))
    matchs = relationship("Match", back_populates="poule")


class Division(Base):
    __tablename__ = "division"
    id = Column(Integer, primary_key=True)
    nom = Column(String(40))
    url = Column(String(80))
    cle = Column(String(40))


class Gymnase(Base):
    __tablename__ = "gymnase"
    id = Column(Integer, primary_key=True)
    lat = Column(Float)
    long = Column(Float)
    nom = Column(String(200))
    adresse = Column(String(200))
    CP = Column(String(10))
    ville = Column(String(200))
    matchs = relationship("Match", back_populates="gymnase")
