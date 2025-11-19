# ASSET MANAGEMENT SYSTEM
# Roman Kepler | Wesley Walling | Emily Owens | Nick Marsh

import tkinter as tk
import sqlite3 as sql

class MyGUI:
    def __init__(self):

        # connect to database
        conn = sql.connect('assets.db')
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys = ON")

        # -=-=-=-=- TABLES -=-=-=-=-=-

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

        # trying to look at the table
        cur.execute('SELECT * FROM Assets')
        results = cur.fetchall()

        for row in results:
            print(row)
        
        conn.commit()
        conn.close()
                
        # main window widget
        self.main_window = tk.Tk()
        
        # display title
        self.main_window.title('Asset Management System')

        # enter tkinter main loop
        tk.mainloop()



# create instance of MyGUI class
if __name__ == '__main__':
    my_gui = MyGUI()