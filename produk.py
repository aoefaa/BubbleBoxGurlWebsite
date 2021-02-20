from flask import jsonify
from config import app, db 

def getProducts():
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM produk order by idproduk ASC")
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'idproduk':obj[0],'idkategori':obj[1],'namaproduk':obj[2],'gambar':obj[3],'deskripsi':obj[4],'rate':obj[5],'hargabefore':obj[6],'hargaafter':obj[7],'tgldibuat':obj[8]})
        count += 1
    return arr

def getProductById(id_produk):
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM produk where idproduk = '{0}'".format(id_produk))
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'idproduk':obj[0],'idkategori':obj[1],'namaproduk':obj[2],'gambar':obj[3],'deskripsi':obj[4],'rate':obj[5],'hargabefore':obj[6],'hargaafter':obj[7],'tgldibuat':obj[8]})
        count += 1
    return arr

def getProductByCategory(id_kategori):
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM produk where idkategori = '{0}'".format(id_kategori))
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'idproduk':obj[0],'idkategori':obj[1],'namaproduk':obj[2],'gambar':obj[3],'deskripsi':obj[4],'rate':obj[5],'hargabefore':obj[6],'hargaafter':obj[7],'tgldibuat':obj[8]})
        count += 1
    return arr

def searchProduct(namaproduk):
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM produk WHERE namaproduk LIKE '{0}' or deskripsi LIKE '{1}'".format(namaproduk, namaproduk))
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'idproduk':obj[0],'idkategori':obj[1],'namaproduk':obj[2],'gambar':obj[3],'deskripsi':obj[4],'rate':obj[5],'hargabefore':obj[6],'hargaafter':obj[7],'tgldibuat':obj[8]})
        count += 1
    return arr

def getOrders():
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * from cart c, login l, detailorder d, produk p where c.userid=l.userid and c.orderid=d.orderid and p.idproduk=d.idproduk order by idcart ASC")
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'idcart':obj[0],
                    'orderid':obj[1],
                    'userid':obj[2],
                    'tglorder':obj[3],
                    'status':obj[4],
                    'userid':obj[5],
                    'namalengkap':obj[6],
                    'email':obj[7],
                    'password':obj[8],
                    'notelp':obj[9],
                    'alamat':obj[10],
                    'tgljoin':obj[11],
                    'role':obj[12],
                    'lastlogin':obj[13],
                    'detailid':obj[14],
                    'orderid':obj[15],
                    'idproduk':obj[16],
                    'qty':obj[17],
                    'idproduk':obj[18],
                    'idkategori':obj[19],
                    'namaproduk':obj[20],
                    'gambar':obj[21],
                    'deskripsi':obj[22],
                    'rate':obj[23],
                    'hargabefore':obj[24],
                    'hargaafter':obj[25],
                    'tgldibuat':obj[26]})
        count += 1
    return arr

def getOrder(orderid):
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * from cart c, login l, detailorder d, produk p where c.userid=l.userid and c.orderid=d.orderid and p.idproduk=d.idproduk and c.orderid = '{0}' order by idcart ASC".format(orderid))
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'idcart':obj[0],
                    'orderid':obj[1],
                    'userid':obj[2],
                    'tglorder':obj[3],
                    'status':obj[4],
                    'userid':obj[5],
                    'namalengkap':obj[6],
                    'email':obj[7],
                    'password':obj[8],
                    'notelp':obj[9],
                    'alamat':obj[10],
                    'tgljoin':obj[11],
                    'role':obj[12],
                    'lastlogin':obj[13],
                    'detailid':obj[14],
                    'orderid':obj[15],
                    'idproduk':obj[16],
                    'qty':obj[17],
                    'idproduk':obj[18],
                    'idkategori':obj[19],
                    'namaproduk':obj[20],
                    'gambar':obj[21],
                    'deskripsi':obj[22],
                    'rate':obj[23],
                    'hargabefore':obj[24],
                    'hargaafter':obj[25],
                    'tgldibuat':obj[26]})
        count += 1
    return arr

def getConfirmation(orderid):
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * from konfirmasi WHERE orderid = '{0}'".format(orderid))
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'idkonfirmasi':obj[0],
                    'orderid':obj[1],
                    'userid':obj[2],
                    'payment':obj[3],
                    'namarekening':obj[4],
                    'tglbayar':obj[5],
                    'tglsubmit':obj[6]})
        count += 1
    return arr

def getProductByIdCategory():
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * from kategori k, produk p where k.idkategori=p.idkategori order by idproduk ASC")
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'idkategori':obj[0],
                    'namakategori':obj[1],
                    'tgldibuat':obj[2],
                    'idproduk':obj[3],
                    'idkategori':obj[4],
                    'namaproduk':obj[5],
                    'gambar':obj[6],
                    'deskripsi':obj[7],
                    'rate':obj[8],
                    'hargabefore':obj[9],
                    'hargaafter':obj[10]})
        count += 1
    return arr
# def addProduct(idkategori, namaproduk, gambar, deskripsi, rate, hargabefore, hargaafter, tgldibuat):

def addProduct(gambar):
    cur = db.connection.cursor()
    cur.execute("INSERT INTO produk (gambar) VALUES ('{0}')".format(gambar))
    # cur.execute("INSERT INTO produk (idkategori, namaproduk, gambar, deskripsi, rate, hargabefore, hargaafter, tgldibuat) VALUES ({0}, '{1}', '{2}', '{3}', {4}, {5}, {6}, '{7}')".format(idkategori, namaproduk, gambar, deskripsi, rate, hargabefore, hargaafter, tgldibuat))
    db.connection.commit()