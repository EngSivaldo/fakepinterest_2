#importar do init
from fakepinterest import database, app

#comonado que criar o bd
with app.app_context():
  database.create_all()