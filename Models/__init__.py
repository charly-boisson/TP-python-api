from Models.Candidate import Candidate
from Models.Client import Client
from Models.Interview import Interview
from Models.Position import Position
from Models.Recruiter import Recruiter
from Models.Review import Review
from Models.initDB import init_database

# Ce fichier permet d'importer tous les modeles en important juste le dossier
__all__ = [Candidate,Client,Interview,Position,Recruiter,Review,init_database]
