# from lesson_1.app_01 import app
# from lesson_3.app_15 import app
from seminar_3.app_all import app


if __name__ == "__main__":
    app.run(debug=True)

    # flask --app Flask_FastAPI/lesson_1/app_01.py run - запуск из командной строки
# flask --app Flask_FastAPI/lesson_3/app_05.py init-db - запуск инициализации БД из командной строки
# в папке var создались папки instance по наименованиям app

# путь к БД C:/Users/sonym/project/venv/Flask_FastAPI/lesson_3/app_05-instance/mydatabase.db