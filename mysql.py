import mysql.connector
def connection(): 
      mysql.connector.connect(
      host="86.92.137.228",
      user="admin_li_contact",
      password="Lolbroeken12!",
      database="admin_li_contact")

def query():
      connection.cursor()
