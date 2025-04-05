# Devscale Task

- Change to Postgres
- Use Tailwind
- Add Task Queue

<!-- create docker image & connect with the app -->
1. run docker
2. remove db.sqlite 3
3. pip install python-dotenv psycopg2-binary
4. import dotenv & set the load_dotenv(override=True)
5. set DATABASE same with the app-name
6. run `manage.py showmigrations to check if app is connected
7. makemigrations > migrate