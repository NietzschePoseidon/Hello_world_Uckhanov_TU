from datetime import datetime

username: str = input("Введите имя пользователя: ")
studyear = int(input("Введите год вашего поступления: "))
now = datetime.now()

print(f"========================\nДобро пожаловать, {username}!\nСтудент {now.year - studyear} курса {now.year}\nУдачи в обучении!\n========================")