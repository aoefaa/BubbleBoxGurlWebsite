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
    cur.execute("select * from cart where userid='{0}' and status='Cart'".format(user_id))
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

def getCartByOrderId(order_id):
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * from detailorder d, produk p where orderid='{0}' and d.idproduk=p.idproduk order by d.idproduk ASC".format(order_id))
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'detailid':obj[0],
                    'orderid':obj[1],
                    'idproduk':obj[2],
                    'qty':obj[3],
                    'idproduk':obj[4],
                    'idkategori':obj[5],
                    'namaproduk':obj[6],
                    'gambar':obj[7],
                    'deskripsi':obj[8],
                    'rate':obj[9],
                    'hargabefore':obj[10],
                    'hargaafter':obj[11],
                    'tgldibuat':obj[12]})
        count += 1
    return arr

def tambahKeranjang(idproduk, userid):
    orderid = datetime.now()
    now = datetime.now()
    cur = db.connection.cursor()
    defaultStatus = 'Cart'
    cur.execute("INSERT INTO cart (orderid, userid, tglorder) VALUES ('{0}', {1}, '{2}', '{3}')".format(orderid, userid, now, defaultStatus))
    db.connection.commit()
    # isAdd = True
    # if isAdd:
    #     cur = db.connection.cursor()
    #     cur.execute("INSERT INTO cart (orderid, idproduk, qty) VALUES ('{0}', {1}, {2})".format(orderid, idproduk, '1'))
    #     db.connection.commit()