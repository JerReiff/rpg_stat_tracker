import mysql.connector
from dotenv import load_dotenv
import os
import json

load_dotenv()

mydb = mysql.connector.connect(
    host='localhost',
    user=os.environ.get('mysql_user'),
    password=os.environ.get('mysql_password'),
    database='rpg_stat_tracker_test'
)

cursor = mydb.cursor(dictionary=True,buffered=True)

cursor.execute("SELECT * FROM discord_server;")
sql_servers = json.dumps(cursor.fetchall())
cursor.execute("SELECT * FROM campaign;")
sql_campaigns = json.dumps(cursor.fetchall()) 
cursor.execute("SELECT * FROM discord_server_user;")
sql_users = json.dumps(cursor.fetchall() )
cursor.execute("SELECT * FROM rpg_character;")
sql_chars = json.dumps(cursor.fetchall()) 

print("SERVERS:")
print(sql_servers)
print("CAMPAIGNS:")
print(sql_campaigns)
print("USERS:")
print(sql_users)
print("CHARACTERS:")
print(sql_chars)