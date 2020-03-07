# РЕШЕНИЕ ПРАКТИКИ ПРОСТОЕ:
# там просто 6 инпутов, который потом помещаются в один список, который будет становиться экземпляром класса
# надо будет подключится к sqlite3 и по шаблону помещать зареганные данные

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Указываем способ подключения к базе данных
DB_PATH = "sqlite:///sochi_athletes.sqlite3"

# Создаём базовый класс моделей таблиц
Base = declarative_base()

class User(Base):
	"""
	Описывает структуру таблицы user
	"""
	# Указываем имя таблицы
	__tablename__ = "user"

	# Задаем колонки:
	id = sa.Column(sa.Integer, primary_key = True)
	first_name = sa.Column(sa.TEXT)
	last_name = sa.Column(sa.TEXT)
	gender = sa.Column(sa.TEXT)
	email = sa.Column(sa.TEXT)
	birthdate = sa.Column(sa.TEXT)
	height = sa.Column(sa.TEXT)

def connection():
	"""
	Тут всё логично, просто крафтим соединение
	Дла удобства помещаем в функцию
	"""
	engine = sa.create_engine(DB_PATH)
	Base.metadata.create_all(engine)
	session = sessionmaker(engine)
	return session()

def input_for_athlete():
	"""
	Крафтим спрашивалку, которая будет запрашивать данные
	"""
	id = sa.Column(sa.String(36), primary_key=True)
	name = input("Введите своё имя: ")
	surname = input("Введите свою фамилию: ")
	gender = input("Введите пол(Male, Female): ")
	email = input("Email: ")
	birthdate = input("Введите дату рождения в формате ГГГГ-ММ-ДД: ")
	height = input("И свой рост(в метрах): ")
	# А теперь сэйвим это всё в экземпляр класса User:
	user = User(
		first_name = name,
		last_name = surname,
		gender = gender,
		email = email,
		birthdate = birthdate,
		height = height,
		)
	# И возвращаем нашего юзера
	return user

def saver():
	"""
	Сохраняет данные
	"""
	session = connection()
	user = input_for_athlete()
	session.add(user)
	session.commit()
	print("Данные сохронены.")
