# ASSET MANAGEMENT SYSTEM
# Roman Kepler | Wesley Walling | Emily Owens | Nick Marsh

import tkinter as tk
import sqlite3 as sql

class MyGUI:
    def __init__(self):

        # connect to database
        conn = sql.connect('assets.db')
        cur = conn.cursor()
                
        # main window widget
        self.main_window = tk.Tk()
        
        # display title
        self.main_window.title('Asset Management System')

        # enter tkinter main loop
        tk.mainloop()

        conn.commit()
        conn.close()

# create instance of MyGUI class
if __name__ == '__main__':
    my_gui = MyGUI()