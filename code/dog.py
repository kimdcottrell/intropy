import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # janky, but I don't have venv yet so PYTHONPATH isn't an option

from intropy import dog

oreo = dog.Dog('Oreo')

oreo.add_trick('sit')
oreo.add_trick('down')
oreo.add_trick('high five')

oreo.add_owner('Kim')

print(oreo.description())
