from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()
# Inserting data into talble
# user = User(name="Afsar Khan", age=21)
# session.add(user)
# session.commit()
# session.close()


# Reading data
# users = session.query(User).all()
# for user in  users:
#     print(f"User Id:{user.id}  name:{user.name}  age:{user.age}")


# Updating data
# user = session.query(User).filter_by(id=2).one_or_none()
# user.name = "Abrar Khan"
# print(user.name)
# session.commit()


# delete data
user = session.query(User).filter_by(id=4).one_or_none()
session.delete(user)
session.commit()