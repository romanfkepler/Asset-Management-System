# ASSET MANAGEMENT SYSTEM
# Roman Kepler | Wesley Walling | Emily Owens | Nick Marsh

import tkinter as tk
import sqlite3 as sql
from tkinter import *
from tkinter.ttk import *

class MyGUI:
    def assetsView(self):
        assetsWindow = Toplevel(self.loginWindow)
        assetsWindow.title('Asset Management Database')
        assetsWindow.geometry('300x300')
        

    def usersView(self):
        pass

    # -=-=-=-=- TRY LOGIN -=-=-=-=-
    def tryLogin(self):
        conn = sql.connect('assets.db')
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys = ON")

        tryUsername = str(self.usernameEntry.get())
        tryPassword = str(self.passwordEntry.get())

        cur.execute('SELECT UniqueUsername, Password FROM Users WHERE UniqueUsername == ? AND Password == ?', (tryUsername, tryPassword))
        results = cur.fetchall()
        for row in results:
            print(row)

        conn.commit()
        conn.close()

        if results:
            print("Login successful.")
            tryUsername = None
            tryPassword = None
            self.loginWindow.withdraw()
            self.assetsView()
            return
        else:
            print("Username or password incorrect.")
            tryUsername = None
            tryPassword = None
            return

   


    def __init__(self):

        # connect to database
        conn = sql.connect('assets.db')
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys = ON")

        # -=-=-=-=- TABLES -=-=-=-=-

        # create Assets table
        cur.execute('''CREATE TABLE IF NOT EXISTS Assets(
            AssetID INTEGER PRIMARY KEY NOT NULL, 
            AssetName TEXT,
            Condition TEXT, 
            Available TEXT, 
            Cost REAL, 
            Manufacturer TEXT, 
            Model TEXT, 
            SerialNumber TEXT,
            PurchaseDate INTEGER, 
            Vendor TEXT, 
            Site TEXT,
            FOREIGN KEY(Condition) REFERENCES AssetLog(Condition)
            )
            ''')
        conn.commit()

        # create Asset Log table
        cur.execute('''CREATE TABLE IF NOT EXISTS AssetLog(
            AssetID INTEGER PRIMARY KEY NOT NULL, 
            AssetName TEXT,
            LogDate INTEGER, 
            LogTime INTEGER, 
            Issue TEXT, 
            Condition TEXT,
            FOREIGN KEY(AssetID) REFERENCES Assets(AssetID),
            FOREIGN KEY(AssetName) REFERENCES Assets(AssetName)
            )
            ''')
        conn.commit()

        # create Users table
        cur.execute('''CREATE TABLE IF NOT EXISTS Users(
        UniqueUsername TEXT PRIMARY KEY NOT NULL, 
        FNameLName TEXT,
        Password TEXT, 
        Authority TEXT
        )
        ''')
        conn.commit()

        # insert test entry
        # cur.execute('''INSERT INTO Assets(AssetID, AssetName, Condition, Available, Cost, Manufacturer,
        # Model, SerialNumber, PurchaseDate, Vendor, Site) 
        # VALUES(1, "Test Entry", "Operational", "Checked In", 10000, "Buildin' Boys", "The Wrangler", 
        # "1093S2FF", 01011999, "Facebook Marketplace", "HSV")''')
        # conn.commit()

        # insert test user
        # cur.execute('''INSERT INTO Users(UniqueUsername, FNameLName, Password, Authority)
        # VALUES("JimmyJamboree", "Jimmy Jameson", "1234Froggy97", "Admin")''')
        # conn.commit()

        # trying to look at the table
        cur.execute('SELECT * FROM Assets')
        results = cur.fetchall()

        for row in results:
            print(row)

        cur.execute('SELECT * FROM Users')
        results = cur.fetchall()

        for row in results:
            print(row)
        
        conn.commit()
        conn.close()

        # -=-=-=-=- TKINTER -=-=-=-=-
                
        # main window widget
        self.loginWindow = Tk()
        
        # display title
        self.loginWindow.title('Login Form')

        # create frames
        self.usernameFrame = tk.Frame(self.loginWindow)
        self.passwordFrame = tk.Frame(self.loginWindow)
        self.buttonsFrame = tk.Frame(self.loginWindow)

        # username frame
        self.usernameLabel = tk.Label(self.usernameFrame,
                                      text='Username:')
        self.usernameLabel.pack(side='left', 
                                pady=(5, 0), 
                                padx=(5, 10)
                                )
        self.usernameEntry = tk.Entry(self.usernameFrame)
        self.usernameEntry.pack(side='left')

        # password frame
        self.passwordLabel = tk.Label(self.passwordFrame,
                                      text='Password:')
        self.passwordLabel.pack(side='left', 
                                pady=(5, 0), 
                                padx=(5, 10)
                                )
        self.passwordEntry = tk.Entry(self.passwordFrame)
        self.passwordEntry.pack(side='left')

        # buttons frame
        self.btnLogin = tk.Button(self.buttonsFrame,
                                  text='Log In',
                                  command=self.tryLogin)
        self.btnLogin.pack(side='left',
                           pady=(5, 5),
                           padx=(5, 10)
                           )
        self.btnCancel = tk.Button(self.buttonsFrame,
                                   text='Cancel',
                                   command=self.loginWindow.destroy)
        self.btnCancel.pack(side='left',
                            pady=(5, 5),
                            padx=(5, 10)
                            )

        # pack frames
        self.usernameFrame.pack()
        self.passwordFrame.pack()
        self.buttonsFrame.pack()

        # enter tkinter main loop
        tk.mainloop()



# create instance of MyGUI class
if __name__ == '__main__':
    my_gui = MyGUI()