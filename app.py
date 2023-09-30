from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, UpdatePetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet-adoption-db'
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.app_context().push()

connect_db(app)

debug = DebugToolbarExtension(app)

@app.route('/')
def get_pets():
    """ View all pets. """
    pets = db.session.query(Pet).all()
    return render_template('get_pets.html', pets=pets)

@app.route('/<int:id>', methods=['GET', 'POST'])
def get_pet(id):
    """ View and update a pet. """
    pet = db.session.query(Pet).get(id)
    form = UpdatePetForm(obj=pet)

    if form.validate_on_submit():
        pet.available = form.available.data
        pet.notes = form.notes.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template('get_pet.html', form=form, pet=pet)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """ Add a new pet to the adoption agency. """
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(
            name = name,
            species = species,
            photo_url = photo_url,
            age = age,
            notes = notes
        )
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet.html', form=form)