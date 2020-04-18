import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = r"sqlite:///D:\\Skillfactory\\Тестовые задания\\python\\4.12\\sochi_athletes.sqlite3"

Base = declarative_base()

class User(Base):

    __tablename__ = 'user'
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.Float)

def connect_db():

    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)

    return session()

def request_data():

    print("Введи данные")
    first_name = input("Введи имя")
    last_name = input("Введи фамилию")
    gender = input("Введи пол(Male, Female)")
    email = input("Введи адрес электронной почты")
    birthdate = input("Введи дату рождения (ГГГГ-ММ-ДД)")
    height = input("Введи рост(например 1.73")

    user = User(
        first_name = first_name,
        last_name = last_name,
        gender = gender,
        email = email,
        birthdate = birthdate,
        height = height
    )
    return user

def main():

     session = connect_db()
     user = request_data()
     session.add(user)
     session.commit()
     print("Данные сохранены")


if __name__ == "__main__":
    main()

