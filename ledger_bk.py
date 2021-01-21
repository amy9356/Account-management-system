#please
#PLEASE
import sqlite3
def create():#테이블 생성
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS account(account_num TEXT PRIMARY KEY, name TEXT, password TEXT, money INTEGER)")
    #account테이블 생성, account_num이 기본키
    con.commit()
    con.close()
def viewall():
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM account")
    rows = cur.fetchall()
    con.close()
    return rows

# def search(name="",user="",password="",category=""):
#     con = sqlite3.connect("aledger.db")
#     cur = con.cursor()
#     cur.execute("SELECT * FROM account WHERE name=? OR user=? OR password=? OR category=?",(name,user,password,category))
#     rows = cur.fetchall()
#     con.close()
#     return rows
def add(account_num, name, password, money):#데이터 추가
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("INSERT INTO account VALUES(?,?,?,?)",(account_num, name, password, money))
    #매개변수로 들어온 값을 DB에 저장
    con.commit()
    con.close()
# def update(id,name,user,password,category,cdate):
#     con = sqlite3.connect("aledger.db")
#     cur = con.cursor()
#     cur.execute("UPDATE account SET name=?,user=?,password=?,category=?,cdate=? WHERE id=?",(name,user,password,category,cdate,id))
#     con.commit()
#     con.close()
def delete(account_num):#데이터 삭제
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("DELETE FROM account WHERE account_num=?",(account_num,))
    #매개변수로 들어온 값을 가진 데이터 삭제
    con.commit()
    con.close()
create()
#print(search(category="social"))
