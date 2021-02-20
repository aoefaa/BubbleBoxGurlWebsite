from flask import jsonify
from config import app, db

def getUsers():
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM login")
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'userid':obj[0],'namalengkap':obj[1],'email':obj[2],'password':obj[3],'notelp':obj[4],'alamat':obj[5],'tgljoin':obj[6],'role':obj[7],'lastlogin':obj[8]})
        count += 1
    return arr

def getEmail(email):
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM login WHERE email = '{0}'".format(email))
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'userid':obj[0],'namalengkap':obj[1],'email':obj[2],'password':obj[3],'notelp':obj[4],'alamat':obj[5],'tgljoin':obj[6],'role':obj[7],'lastlogin':obj[8]})
        count += 1
    return arr