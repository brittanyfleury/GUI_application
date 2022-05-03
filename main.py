# -*- coding: utf-8 -*-
"""
Brittany Fleury
"""
#imports
import tkinter as tk
import pandas as pd
import tkinter.font as font
import PIL.ImageTk
from tkinter import *
from utilities import *

#created a class so we can instantiate multiple objects.

class AllTkinterWidgets(Frame):

    def __init__(self, master):

        


#designing the GUI
        height= 1500
        width= 1500

        # container variable for data
        #create canvas
        canvas= tk.Canvas(root, height= height, width= width)
        canvas.pack()
        
        # full frame
        frame=tk.Frame(root, bg= '#a2d7db')
        frame.place(relwidth=1, relheight= 1, relx=0.01, rely=0.01)

        
        framegymlookup= tk.Frame(root, bg='#a2d7db')
        framegymlookup.place(relwidth=0.5, relheight=0.07)
        
        #spacing labels in order for GUI to look symmetricial and professional
        self.data = NONE
         
        Label5=tk.Label(framegymlookup,text="                                                        ", bg="#a2d7db")
        Label5.grid(row=1, column=15)

        label= tk.Label(framegymlookup, text= "Gym Members' Information", bg='#a2d7db')
        label.grid(row=1, column=20)
        myFont = font.Font(size=20)
        label['font'] = myFont

        Frame3=tk.Frame(root, bg='#a2d7db')
        Frame3.place(relwidth=0.7, relheight= 0.1, relx= 0.09, rely= 0.1)

        #file/data entry, 
        label2= tk.Label(Frame3, text= "File: ", bg="#a2d7db")
        label2.grid(row=3, column=9)

        label6= tk.Label(Frame3, text="         ", bg="#a2d7db")
        label6.grid(row=3, column=11 )

        entry= tk.Entry(Frame3, width=50)
        entry.grid(row=3, column= 10)

        Button2=tk.Button(Frame3, text='Load', command= lambda: loads())
        Button2.grid(row=3, column=12 )


    #listbox creation
        LS1 = Listbox(Frame3, width = 50, height = 4, bg='white')
        LS1.grid(row = 4, column = 10)






        #Buttons for funtions/data 
        Frame4= tk.Frame(root, bg= '#a2d7db')
        Frame4.place(relwidth=0.7, relheight=0.5, relx= 0, rely=0.2)

        label8= tk.Label(Frame4, text="  ", bg="#a2d7db")
        label8.grid(row=13, column=11 )

        Label7= tk.Label(Frame4, text= "Click to see the most popular months of joining      ", bg= '#a2d7db')
        Label7.grid(row=14, column=9)

        MonthsButton= tk.Button(Frame4, text= "Top Months", command= lambda:loadgraph())
        MonthsButton.grid(row=14, column=10)


        StatesLabel=tk.Label(Frame4, text="Click to see our gym's top states", bg='#a2d7db')
        StatesLabel.grid(row=16, column=9)

        StatesButton=tk.Button(Frame4, text= "Top States", command= lambda: loadstategraph())
        StatesButton.grid(row= 16, column=10)

        label8= tk.Label(Frame4, text="  ", bg="#a2d7db")
        label8.grid(row=15, column=11 )

        #creating a drop down menu in order to select different areas we want to display
        self.clicked= StringVar()
        self.clicked.set("Midwest")
        drop= OptionMenu(Frame4,self.clicked, "Midwest", "Northeast", "South", "West")
        drop.grid(row=18, column=10)

        
        AgeLabel=tk.Label(Frame4, text="Ages by Region", bg='#a2d7db')
        AgeLabel.grid(row=18, column= 9)



        selectbutton= tk.Button(Frame4, text="Select", command=lambda: dropdowncontroller())
        selectbutton.grid(row=18, column=15)
#spacing labels in order for buttons to be symmetrical and neat
        label8= tk.Label(Frame4, text="  ", bg="#a2d7db")
        label8.grid(row=17, column=11 )

        label8= tk.Label(Frame4, text="  ", bg="#a2d7db")
        label8.grid(row=29, column=11 )


       

#creating canvas
        self.canvasframe= tk.Canvas(root, bg= 'white')
        self.canvasframe.place(relwidth=0.7, relheight= 1, relx=0.5, rely=0.01)



#functions
        #loads the csv file (Records.csv) into the app
        def loads():
       
            try: 
                Fileentry = entry.get()
                self.data = pd.read_csv(Fileentry)
                LS1.insert(0,"Loaded csv file") 
            except:
                #Error handling!!
                    LS1.insert(0, "File Not Found")
                    
                    
        #calls the joinmonth function and displays the generated graph onto the canvas
        def loadgraph():
            #error handling if data is not loading
            if self.data is NONE:
                LS1.insert(0,"Please load the file first.")
            else:
            
            
        
                Month=joinmonth(self.data)
                self.img = PIL.ImageTk.PhotoImage(file='joingraph.jpg')
                #clears the canvas
                if self.canvasframe is not NONE:
                    self.canvasframe.destroy()
                #creating canvas
                self.canvasframe = Canvas( bg = "Black")
                self.canvasframe.place(relwidth=0.7, relheight= 1, relx=0.5, rely=0.01)
                self.canvasframe.create_image((0,0), image=self.img, anchor = NW)
                LS1.insert(0, Month+" is the most popular month to join the gym.")
            
            
         # calls the states function and loads the saved graph from function and displays it onto canvas   
        def loadstategraph():
              #error handling if data is not loading
            if self.data is NONE:
                LS1.insert(0,"Please load the file first.")
            else:
            
            
                State=states(self.data)
                self.img = PIL.ImageTk.PhotoImage(file='PopularStates.jpg')
                if self.canvasframe is not NONE:
                    self.canvasframe.destroy()
                self.canvasframe = Canvas( bg = "Black")
                self.canvasframe.place(relwidth=0.7, relheight= 1, relx=0.5, rely=0.01)
                self.canvasframe.create_image((0,0), image=self.img, anchor = NW)
                LS1.insert(0, State+" is the most popular location.")

        #function where whatever option in the drop down menu is clicked,
        #then the appropriate function will be called and the appropriate graph will display
        
        def dropdowncontroller():
            #used "if"/"else" statement to display the right function/graph when the appropraite option is clicked
             #error handling if data is not loading
            if self.data is NONE:
                LS1.insert(0,"Please load the file first.")
            else:
            
           
                if self.clicked.get() == "Midwest":
                    agebymidwest(self.data)
                    self.img = PIL.ImageTk.PhotoImage(file='MidwestAges.jpg')
                    if self.canvasframe is not NONE:
                        self.canvasframe.destroy()
                    self.canvasframe = Canvas( bg = "Black")
                    self.canvasframe.place(relwidth=0.7, relheight= 1, relx=0.5, rely=0.01)
                    self.canvasframe.create_image((0,0), image=self.img, anchor = NW)
                elif self.clicked.get() =="Northeast":
                    agebynortheast(self.data)
                    self.img = PIL.ImageTk.PhotoImage(file='NortheastAges.jpg')
                    if self.canvasframe is not NONE:
                        self.canvasframe.destroy()
                    self.canvasframe = Canvas( bg = "Black")
                    self.canvasframe.place(relwidth=0.7, relheight= 1, relx=0.5, rely=0.01)
                    self.canvasframe.create_image((0,0), image=self.img, anchor = NW)
                elif self.clicked.get() == "South":
                    agebysouth(self.data)
                    self.img = PIL.ImageTk.PhotoImage(file='SouthAges.jpg')
                    if self.canvasframe is not NONE:
                        self.canvasframe.destroy()
                    self.canvasframe = Canvas( bg = "Black")
                    self.canvasframe.place(relwidth=0.7, relheight= 1, relx=0.5, rely=0.01)
                    self.canvasframe.create_image((0,0), image=self.img, anchor = NW)
                elif self.clicked.get() == "West":
                    agebywest(self.data)
                    self.img = PIL.ImageTk.PhotoImage(file='WestAges.jpg')
                    if self.canvasframe is not NONE:
                        self.canvasframe.destroy()
                    self.canvasframe = Canvas( bg = "Black")
                    self.canvasframe.place(relwidth=0.7, relheight= 1, relx=0.5, rely=0.01)
                    self.canvasframe.create_image((0,0), image=self.img, anchor = NW)
                else:
                    #another instance of error handling
                    LS1.insert(0,"Invalid Option Selected")
            
       
            
# main--setup tkinter object, instantiate AllTkinterWidgets class and display root
root= tk.Tk()
app = AllTkinterWidgets(root)
root.mainloop()





