#Simple account management system suitable for windows operationg system
# Copyright 2017 by Martial Himanshu.  All rights reserved.
# Distributed under the MPL license.  See LICENSE.txt for details.

from tkinter import *
import ledger_bk
import datetime # datetime 정보 가져옴
import random # random 정보 가져옴
window = Tk()
window.title("Account Ledger")

def rand_accnum() : # 랜덤한 계좌번호를 문자열로 생성해서 리턴 하는 함수
    accnum_list = []
    acc_num = ""

    for i in range(16) :
        accnum_list.append(random.randint(0, 9))#0부터 9사이로 된 숫자가 랜덤으로 입력 
    accnum_list[6] = '-'#7번째 자리에 '-'입력
    accnum_list[9] = '-'#10번째 자리에 '-'입력

    for j in range(16):
        acc_num += str(accnum_list[j])#acc_num에 str로 하나씩 저장
    return acc_num

def view_command():
    lb.delete(0,END)
    for row in ledger_bk.viewall():
        lb.insert(END,row)

# def search_command():
#     lb.delete(0,END)
#     for row in ledger_bk.search(name=name.get(),user=user.get(),password=password.get(),category=category.get()):
#         lb.insert(END,row)

def add_command():
    # 정보 입력 시 빈칸이 있으면 에러 발생하고 저장 x
    if name.get() == "" or password.get() == "" or money.get() == "" :
        msgbox.showerror("에러", "정보 칸을 모두 입력해주세요!")#에러 발생
        return -1

    acc_number = rand_accnum()
    ledger_bk.add(acc_number, name.get(), password.get(), money.get())#ledger_bk파일에 있는 add()함수 이용
    lb.delete(0,END) #0항목부터 END까지 삭제
    lb.insert(END,"이름 : " + name.get(),"계좌번호 : " + acc_number, "패스워드 : " + "*" * len(password.get()),"계좌잔고 : " + money.get(), "계좌 개설 시간 : " + datetime.datetime.now().strftime('%Y년 %m월 %d일 %H시 %M분 %S초'))
    #lb에 ledger_bk파일에 있는 add()함수에서 받아온 정보와 계좌번호, 그리고 계좌를 생성한 시간을 화면에 출력


def get_selected_row(event):
    try:
        global selected_tuple
        index=lb.curselection()[0]
        selected_tuple = lb.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        # e2.delete(0,END)
        # e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        # e5.delete(0,END)
        # e5.insert(END,selected_tuple[5])
    except IndexError:
        pass

# def update_command():
#     ledger_bk.update(selected_tuple[0],name.get(),user.get(),password.get(),category.get(),cdate.get())
#     view_command()

def delete_command():
    ledger_bk.delete(selected_tuple[0])
    view_command()
    #lb.delete(END,get_selected_row.selected_tuple)
def clear_command():
    lb.delete(0,END)
    e1.delete(0,END)
    # e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    # e5.delete(0,END)

l1 = Label(window,text="성명")
l1.grid(row=0,column=0,columnspan=2)
# l2 = Label(window,text="Username/Email")
# l2.grid(row=1,column=0,columnspan=2)
l3 = Label(window,text="비밀번호")
l3.grid(row=2,column=0,columnspan=2)
l4 = Label(window,text="금액")
l4.grid(row=3,column=0,columnspan=2)
# l5 = Label(window,text="Date")
# l5.grid(row=4,column=0,columnspan=2)

name=StringVar()
e1 = Entry(window,textvariable=name,width=50)
e1.grid(row=0,column=0,columnspan=10)

# user=StringVar()
# e2 = Entry(window,textvariable=user,width=50)
# e2.grid(row=1,column=0,columnspan=10)

password=StringVar()
e3 = Entry(window,textvariable=password,width=50)
e3.grid(row=2,column=0,columnspan=10)

money=StringVar()
e4 = Entry(window,textvariable=money,width=50)
e4.grid(row=3,column=0,columnspan=10)

# cdate=StringVar()
# e5 = Entry(window,textvariable=cdate,width=50)
# e5.grid(row=4,column=0,columnspan=10)

b1 = Button(window,text="계좌생성",width=12,command=add_command)
b1.grid(row=5,column=0)

# b2 = Button(window,text="Update",width=12,command=update_command)
# b2.grid(row=5,column=1)

# b3 = Button(window,text="Search",width=12,command=search_command)
# b3.grid(row=5,column=2)

b4 = Button(window,text="View All",width=12,command=view_command)
b4.grid(row=5,column=3)

b5 = Button(window,text="Delete",width=12,command=delete_command)
b5.grid(row=5,column=4)

b6 = Button(window,text="나가기",width=12,command=window.destroy)
b6.grid(row=5,column=5)

b7 = Button(window,text="초기화",width=12,command=clear_command)
b7.grid(row=0,column=5)

lb=Listbox(window,height=20,width=94)
lb.grid(row=6,column=0,columnspan=6)

sb=Scrollbar(window)
sb.grid(row=6,column=6,rowspan=6)

lb.configure(yscrollcommand=sb.set)
sb.configure(command=lb.yview)

lb.bind('<<ListboxSelect>>',get_selected_row)
window.mainloop()
