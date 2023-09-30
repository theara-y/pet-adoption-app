from models import db, Pet
from app import app

db.drop_all()
db.create_all()

trooper = Pet(
    name='Trooper',
    age=2,
    species='dog',
    available=True,
    photo_url='https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/69079274/1/?bust=1695945916&width=720',
    notes='I''m Trooper, the rescue dog with a heart of gold and a wag that can light up any room.'
)

zoe = Pet(
    name='Zoe',
    age=None,
    species='cat',
    available=True,
    photo_url='https://dl5zpyw5k3jeb.cloudfront.net/photos/pets/60045350/4/?bust=1677079274&width=720',
    notes='She''s a bit obsessed with the water and like to hang out in the sink or check out the shower after it''s been used!'
)

kit_kat = Pet(
    name='Kit Kat',
    age=9,
    species='porcupine',
    available=True,
    photo_url='https://alaskawildlife.org/wp-content/uploads/2016/12/AWCC-Nov-3-2017-Kit-Porcupine14-100x100.jpeg',
    notes='He is often found munching on walnuts or climbing over the logs in his enclosure!'
)

db.session.add_all([
    trooper,
    zoe,
    kit_kat
])

db.session.commit()