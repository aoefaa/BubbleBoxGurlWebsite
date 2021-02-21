from config import app, db 
from datetime import datetime
from app import *
from flask import *

def getCustomers():
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * from login where role='Member' order by userid ASC")
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'userid':obj[0],
                    'namalengkap':obj[1],
                    'email':obj[2],
                    'password':obj[3],
                    'notelp':obj[4],
                    'alamat':obj[5],
                    'tgljoin':obj[6],
                    'role':obj[7],
                    'lastlogin':obj[8]})
        count += 1
    return arr

def getStaff():
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * from login where role='Admin' order by userid ASC")
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'userid':obj[0],
                    'namalengkap':obj[1],
                    'email':obj[2],
                    'password':obj[3],
                    'notelp':obj[4],
                    'alamat':obj[5],
                    'tgljoin':obj[6],
                    'role':obj[7],
                    'lastlogin':obj[8]})
        count += 1
    return arr

def countCustomers():
    arr = []
    cur = db.connection.cursor()
    cur.execute("select count(userid) as jumlahcust from login where role='Member'")
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'jumlahcust':obj[0]})
        count += 1
    return arr

def addUser(namalengkap, email, password, notelp, alamat, role):
    now = datetime.now()
    cur = db.connection.cursor()
    cur.execute("INSERT INTO login (namalengkap, email, password, notelp, alamat, tgljoin, role) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')".format(namalengkap, email, password, notelp, alamat, now, role))
    db.connection.commit()

def is_valid(email, password):
    cur = db.connection.cursor()
    cur.execute("SELECT email, password from login")
    data = cur.fetchall()
    for row in data:
        if row[0] == email and row[1] == password:
            return True
    return False

def getUserByEmail(email):
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * from login where email = '{0}' order by userid".format(email))
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'userid':obj[0],
                    'namalengkap':obj[1],
                    'email':obj[2],
                    'password':obj[3],
                    'notelp':obj[4],
                    'alamat':obj[5],
                    'tgljoin':obj[6],
                    'role':obj[7],
                    'lastlogin':obj[8]})
        count += 1
    return arr

def getLoginDetails():
    if 'email' not in session:
        loggedIn = False
        nama = ''
        userid = ''
        role = ''
    else:
        user = getUserByEmail(session['email'])
        loggedIn = True
        nama = user[0]['namalengkap']
        session['nama'] = nama
        userid = user[0]['userid']
        role = user[0]['role']
        session['role'] = role
    return loggedIn, nama, userid, role