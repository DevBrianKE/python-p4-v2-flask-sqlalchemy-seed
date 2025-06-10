#!/usr/bin/env python3
# server/seed.py

from random import choice as rc
from faker import Faker
from app import app
from models import db, Pet

with app.app_context():
    # Initialize Faker
    fake = Faker()

    # Delete existing data
    Pet.query.delete()

    # Create empty list
    pets = []

    # Possible species
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    # Generate 10 random pets
    for _ in range(10):
        pet = Pet(
            name=fake.first_name(),  # Random first name
            species=rc(species)     # Random species
        )
        pets.append(pet)

    # Add and commit all pets at once
    db.session.add_all(pets)
    db.session.commit()

    
    print("\nDemonstration queries:")
    print("All cats:", Pet.query.filter_by(species='Cat').all())
    print("Number of dogs:", Pet.query.filter_by(species='Dog').count())
    print("Pets ordered by name:", Pet.query.order_by('name').all())
    print("First 3 pets:", Pet.query.limit(3).all())