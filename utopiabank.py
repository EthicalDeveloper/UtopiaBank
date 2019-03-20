from tkinter import *
import time




#new seperate window functions. These code is just a front end for the deposit, withdraw, and balance functions

def deposit_window():
    time.sleep(1)
    dwindow = Toplevel(root)
    dwindow.title('Deposit')
    dwindow.geometry("470x300")
    dwindow.resizable(0,0)
    dlabel=Label(dwindow,text='Deposit Amount',width=40)
    dlabel.grid(row=2,column=1,padx=10,pady=10)
    dlabel.config(font=("Courier", 15))

    dentry=Entry(dwindow)
    dentry.grid(row=3,column=1,padx=10,pady=10)

    dmath=Button(dwindow,text='Deposit',height=3,width=10)
    dmath.grid(row=4,column=1,padx=10,pady=10)













def withdraw_window():
    time.sleep(1)
    wwindow = Toplevel(root)
    wwindow.title('Withdraw')
    wwindow.geometry("470x300")
    wlabel = Label(wwindow, text='Withdraw Amount', width=40)
    wlabel.grid(row=2, column=1, padx=10, pady=10)
    wlabel.config(font=("Courier", 15))
    wentry=Entry(wwindow)
    wentry.grid(row=3,column=1,padx=10,pady=10)
    wmath=Button(wwindow,text='Withdraw',height=3,width=10,command=balance_window)
    wmath.grid(row=4,column=1,padx=10,pady=10)




def balance_window():
    time.sleep(1)
    bwindow = Toplevel(root)
    bwindow.title('Balance')
    bwindow.geometry("470x300")
    blabel = Label(bwindow, text='Your Current Balance', width=40)
    blabel.grid(row=2, column=1, padx=10, pady=10)
    blabel.config(font=("Courier", 15))

    blistbox = Listbox(bwindow)
    blistbox.grid(row=3, column=1, padx=10, pady=10)
    





# deposit windows function. it deposits the money to the balance

















root=Tk()


root.title("Bank Of Utopia")

root.geometry("900x350")
root.resizable(0,0)


#label

welcome=Label(root,text='Welcome to',width=20)
welcome.grid(row=2,column=0)
welcome.config(font=("Courier", 44))

welcome1=Label(root,text='Bank Of Utopia',width=20)
welcome1.grid(row=3,column=0)
welcome1.config(font=("Courier", 44))




#Buttons of tkinter

Dbutton=Button(root,text='Deposit',height='3',width='20',command=deposit_window)
Dbutton.grid(row=1,column=3,padx=10,pady=10)


Wbutton=Button(root,text='Withdraw',height='3',width='20',command=withdraw_window)
Wbutton.grid(row=2,column=3,padx=10,pady=10)

Sbutton=Button(root,text='Balance',height='3',width='20',command=balance_window)
Sbutton.grid(row=3,column=3,padx=10,pady=10)

Ebutton=Button(root,text='Exit',height='3',width='20',command=exit)
Ebutton.grid(row=4,column=3,padx=10,pady=10)












root.mainloop()
