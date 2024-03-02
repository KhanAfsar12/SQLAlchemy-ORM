from sqlalchemy.orm import sessionmaker
from models import User, engine


Session = sessionmaker(bind=engine)
session = Session()

# retriving by ascending & descending
users = session.query(User).order_by(User.name, User.age).all()
for user in users:
    print(f"User age: {user.age}, name: {user.name}, id: {user.id}")