from sqlalchemy.orm import sessionmaker
from models import User, engine
from sqlalchemy import or_, and_, not_, func


Session = sessionmaker(bind=engine)
session = Session()

# Grouping
# users = session.query(User.name, func.count(User.id)).group_by(User.name).all()
# print(users)


# Chaining
# users_tuple = session.query(User.age, func.count(User.id)).filter(User.age > 26).order_by(User.age).filter(User.age < 55).group_by(User.age).all()
# for age, count in users_tuple:
#     print(f"age:{age} ---> count:{count}")

# Conditional chaining
only_iron_man = True
group_by_age = True

users = session.query(User)

if only_iron_man:
    users = users.filter(User.name == "Farman")
if group_by_age:
    users = users.group_by(User.age)
users = users.all()

for i in users:
    print(i.age,"-->", i.name)
