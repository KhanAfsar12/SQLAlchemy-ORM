from sqlalchemy.orm import sessionmaker
from models import User, engine


Session = sessionmaker(bind=engine)
session = Session()

# Use filter() function
# users_all = session.query(User).all()
# users_filtered = (
#     session.query(User).filter(User.age > 40, User.name == 'Nawaz').all()
#     )
# print("All users: ",len(users_all))
# print("users_filtered", len(users_filtered))


# filter_by() function
# users = session.query(User).filter_by(age = 24).all()
# for user in users:
#     print(f"user age: {user.age}")


# where() function

users = session.query(User).
