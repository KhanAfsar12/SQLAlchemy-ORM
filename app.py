from sqlalchemy.orm import sessionmaker
from models import User, engine
from sqlalchemy import or_, and_, not_


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
users = session.query(User).where(
    or_(
    not_(User.name=="Ishtiyaque"),
    and_(
        User.age > 35,
        User.age < 60
    )
    )
    ).all()
for i in users:
    print(f"User age:{i.age} - {i.name}")
