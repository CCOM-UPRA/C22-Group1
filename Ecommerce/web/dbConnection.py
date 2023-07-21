import mysql.connector
from functools import wraps

connection = mysql.connector.connect(
        host='sql9.freemysqlhosting.net',
        port=3306,
        user='sql9607914',
        password='uWzaFxXgrH',
        database='sql9607914',
        buffered=True
    )


def DBConnection(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        fv = func(*args, **kwargs, database=connection)
        return fv
    return wrapper
