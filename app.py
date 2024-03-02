from sqlalchemy.orm import sessionmaker
from models import User, engine
import random

Session = sessionmaker(bind=engine)
session = Session()

# Add random data
names = ["Ishtiyaque", "Nawaz", "Farman", "sadique"]
ages = [12,45,32,54,23,76,44,34,9]
for x in range(20):
    user = User(name=random.choice(names), age=random.choice(ages))
    session.add(user)
session.commit()