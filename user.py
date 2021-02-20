from config import app, db 

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