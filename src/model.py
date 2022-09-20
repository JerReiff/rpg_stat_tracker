import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

mydb = mysql.connector.connect(
    host='localhost',
    user=os.environ.get('mysql_user'),
    password=os.environ.get('mysql_password'),
    database='rpg_stat_tracker'
)