from tkinter import *
from sqlite3 import dbapi2 as sqlite
from PIL import ImageTk, Image

c=sqlite.connect("grocery.sqlite")
l=c.cursor()
WinStat = ''


def stock():
    
    application.destroy()
    
    c.close()
    
    import stockdetails
    a = stockdetails.stock()
    
    open_win()

def dailyincome():
    
    application.destroy()
    
    c.close()
    
    import billingdetails
    a = billingdetails.dailyincome()
    
    open_win()    
    
def billingitems():
    
    application.destroy()
    
    c.close()
    
    import billingdetails
    a = billingdetails.billingitems()
    
    open_win()
    
def delstock():
    
    application.destroy()
    c.close()
    
    import stockdetails
    a = stockdetails.deletestock()
    
    open_win()
    
def updatestock():
    
    application.destroy()
    c.close()
    
    import stockdetails
    a = stockdetails.updatestock()
    
    open_win()    

def open_win(): 
    global application, WinStat
    WinStat='application'
    application=Tk()
    application.title("GROCERY STORE")
    application.geometry("800x600")
    menu_bar = Menu(application)
    stock_menu = Menu(menu_bar,tearoff=0)
    expiry_menu = Menu(menu_bar,tearoff=0)
    billing_menu = Menu(menu_bar,tearoff=0)
    stock_menu.add_command(label="Add Items", command=stock)
    stock_menu.add_command(label="Delete Items", command=delstock)
    stock_menu.add_command(label="Update Items", command=updatestock)
    billing_menu.add_command(label="Sell", command=billingitems)   
    menu_bar.add_cascade(label="Stock Maintainance", menu=stock_menu)
    menu_bar.add_cascade(label="Sell", menu=billing_menu)
    application.config(menu=menu_bar)        
    application.mainloop()

    
open_win()