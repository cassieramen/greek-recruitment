from recruitment import settings          #project settings file
from django.core.management  import setup_environ     #environment setup function

setup_environ(settings)

from pnm.models import PNM

def decisionTree():
	pnms = PNM.all()
	