from config import app, db 

def getPayment():
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * from pembayaran order by no ASC")
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'no':obj[0],'metode':obj[1],'norek':obj[2],'logo':obj[3],'an':obj[4]})
        count += 1
    return arr