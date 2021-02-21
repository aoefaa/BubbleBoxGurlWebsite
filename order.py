from config import app, db 
from datetime import datetime

def countOrders():
    arr = []
    cur = db.connection.cursor()
    cur.execute("select count(idcart) as jumlahorder from cart where status not like 'Selesai' and status not like 'Canceled'")
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'jumlahorder':obj[0]})
        count += 1
    return arr

def countTransaction():
    arr = []
    cur = db.connection.cursor()
    cur.execute("select count(orderid) as jumlahtrans from konfirmasi")
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'jumlahtrans':obj[0]})
        count += 1
    return arr

def getCartById(user_id):
    arr = []
    cur = db.connection.cursor()
    cur.execute("select * from cart where userid={0} and status='Cart'".format(user_id))
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'idcart':obj[0],
                    'orderid':obj[1],
                    'userid':obj[2],
                    'tglorder':obj[3],
                    'status':obj[4]})
        count += 1
    return arr

def getCartByOrderId(orderid):
    arr = []
    cur = db.connection.cursor()
    cur.execute("select * from cart where orderid='{0}' and status='Cart'".format(orderid))
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'idcart':obj[0],
                    'orderid':obj[1],
                    'userid':obj[2],
                    'tglorder':obj[3],
                    'status':obj[4]})
        count += 1
    return arr

def countCartByOrderId(order_id):
    arr = []
    cur = db.connection.cursor()
    cur.execute("select count(detailid) as jumlahtrans from detailorder where orderid='{0}'".format(order_id))
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'count':obj[0]})
        count += 1
    return arr

def countCartByUserId(userid):
    arr = []
    cur = db.connection.cursor()
    cur.execute("select count(detailid) as jumlahtrans from detailorder where userid='{0}'".format(userid))
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'count':obj[0]})
        count += 1
    return arr

def getCartByUserId(userid):
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * from detailorder d, produk p where d.userid='{0}' and d.idproduk=p.idproduk order by d.userid ASC".format(userid))
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'detailid':obj[0],
                    'orderid':obj[1],
                    'idproduk':obj[2],
                    'userid':obj[3],
                    'qty':obj[4],
                    'idproduk':obj[5],
                    'idkategori':obj[6],
                    'namaproduk':obj[7],
                    'gambar':obj[8],
                    'deskripsi':obj[9],
                    'rate':obj[10],
                    'hargabefore':obj[11],
                    'hargaafter':obj[12],
                    'tgldibuat':obj[13]})
        count += 1
    return arr

def tambahKeranjang(idproduk, userid):
    orderid = datetime.now()
    now = datetime.now()
    cur = db.connection.cursor()
    defaultStatus = 'Cart'
    cur.execute("INSERT INTO cart (orderid, userid, tglorder, status) VALUES ('{0}', {1}, '{2}', '{3}')".format(orderid, userid, now, defaultStatus))
    db.connection.commit()
    isAdd = True
    if isAdd:
        cur = db.connection.cursor()
        cur.execute("INSERT INTO detailorder (orderid, idproduk, userid, qty) VALUES ('{0}', '{1}', {2}, {3})".format(orderid, idproduk, userid, '1'))
        db.connection.commit()

def cekBarang(idproduk, orderid):
    arr = []
    cur = db.connection.cursor()
    cur.execute("select * from detailorder where idproduk='{0}' and orderid='{1}'".format(idproduk, orderid))
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'detailid':obj[0],
                    'orderid':obj[1],
                    'idproduk':obj[2],
                    'userid':obj[3],
                    'qty':obj[4]})
        count += 1
    return arr

def updateBarang(idproduk, orderid, qty):
    cur = db.connection.cursor()
    jumlah = qty + 1
    cur.execute("update detailorder set qty={0} where orderid='{1}' and idproduk={2}".format(jumlah, orderid, idproduk))
    db.connection.commit()

def updateJumlahBarang(idproduk, orderid, qty):
    cur = db.connection.cursor()
    cur.execute("update detailorder set qty={0} where orderid='{1}' and idproduk={2}".format(qty, orderid, idproduk))
    db.connection.commit()

def deleteBarang(idproduk, orderid):
    cur = db.connection.cursor()
    cur.execute("delete from detailorder where idproduk='{0}' and orderid='{1}'".format(idproduk, orderid))
    db.connection.commit()

def updateCheckout(orderid):
    cur = db.connection.cursor()
    cur.execute("update cart set status='Payment' where orderid='{0}'".format(orderid))
    db.connection.commit()