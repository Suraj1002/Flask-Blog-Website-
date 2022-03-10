import pymysql as p
def getConnection():
    return p.connect(host='localhost',user='root',password='',database='flaskdemo')
    
def addStudent(t):
    db=getConnection()
    sql='insert into registertable (uname,password,city,email) values(%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def selectAllStudent():
    db=getConnection()
    sql='select * from registertable'
    cr=db.cursor()
    cr.execute(sql)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist

def selectStudentById(id):
    db=getConnection()
    sql='select * from registertable where id=%s'
    cr=db.cursor()
    cr.execute(sql,id)
    elist=cr.fetchall()
    db.commit()
    db.close()
    return elist[0]

def updateStudent(t):
    db=getConnection()
    sql='update registertable set uname=%s,password=%s,city=%s,email=%s where id=%s'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def deleteStudent(id):
    db=getConnection()
    sql='delete from registertable where id=%s'
    cr=db.cursor()
    cr.execute(sql,id)
    db.commit()
    db.close()