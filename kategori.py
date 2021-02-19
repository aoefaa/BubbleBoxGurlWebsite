from flask import jsonify
from config import app, db

def getCategories():
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM kategori")
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'idkategori':obj[0],'namakategori':obj[1],'tgldibuat':obj[2]})
        count += 1
    return arr

def getCategory(id_kategori):
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM kategori WHERE idkategori = '{0}'".format(id_kategori))
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'idkategori':obj[0],'namakategori':obj[1],'tgldibuat':obj[2]})
        count += 1
    return arr