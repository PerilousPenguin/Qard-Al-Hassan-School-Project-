"""Qard Al-Hassan"""
"""Good GUI tips can be found here: https://wiki.python.org/moin/Intro%20to%20programming%20with%20Python%20and%20Tkinter """
from Tkinter import *

import Tkinter as tkinter  #Tkinter as (Remove the commentand place before "tkinter" if python is of an older version)

window = tkinter.Tk() #Allows for a window to be opened

window.title("Qard Al-Hassan"); #Changes the title of the window

window.geometry("350x300"); #Changes the dimensions of the window

#window.wm_iconbitmap("hands.ico"); #Changes the icon of the window

tList = ["$100", "$20, 000", "$22342342", "$1321231", "$123123"] #Contains previous transactions

tListWindow = Listbox(window); #The transaction list within the window

for i in tList:
    tListWindow.insert(0, i) #Takes input from the transaction list and places it into the window.


tListWindow.pack();

window.mainloop();


















"""
def Qard_AlHassan(object):

	logged = False

	def login():
            logged = true
	def sign_up():
            pass
        def borrow():
            if (logged == True):
    		#Open the GUI
            else:
	    	login();
		print str(logged)

	def lend():

		if (logged == True):
                    //Open GUI
                else:
                    login();
Qard_AlHassan(borrow());
"""
