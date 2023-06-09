import mysql.connector
from functools import wraps


def DBConnection(func):
    connection = mysql.connector.connect(
        host='sql9.freemysqlhosting.net',
        port=3306,
        user='sql9607914',
        password='uWzaFxXgrH',
        database='sql9607914'
    )

    @wraps(func)
    def wrapper(*args, **kwargs):
        fv = func(*args, **kwargs, database=connection)
        return fv
    return wrapper
