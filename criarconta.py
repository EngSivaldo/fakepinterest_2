#importar do init
from fakepinterest import database, app
from fakepinterest.models import Usuario, Foto

#comonado que criar o bd
with app.app_context():
  database.create_all()