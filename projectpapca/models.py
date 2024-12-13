# projectpapca/models.py

from MOJIZA.models.base import Model, Field

class User(Model):
    username = Field('string')
    email = Field('string')
    password = Field('string')

# Yana boshqa modellarni shu yerda ta’riflash mumkin
