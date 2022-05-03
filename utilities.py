# -*- coding: utf-8 -*-
"""
Brittany Fleury and Lauren Jamison
"""
import tkinter as tk
import pandas as pd
import tkinter.font as font
import matplotlib.pyplot as plt
import matplotlib as mlp





#functions


    

#function reads csv file and counts the amount of members that joined in each month

def joinmonth(data):
     
     #create data frame and then get counts of data frame
     df = pd.DataFrame(data,columns=['Month_Name_of_Joining'])
     join_month = df["Month_Name_of_Joining"].value_counts()
     
    
    
     
     #getting the values from the Month_Name_of_Joining column in the dataframe
     #then getting the keys directly from the dataframe
     Counts = join_month.values
     Months= list(join_month.keys())
    
     #plotting the figure and determining the size
     fig = plt.figure(figsize = (9, 5))
     
     #creating a bar chart and creating appropriate labels
     plt.bar(Months, Counts, color ='blue',
            width = 0.4)
     plt.xlabel("Months")
     plt.ylabel("Number of Members Joined")
     plt.title("Most Popular Months that members join")
     plt.xticks(rotation = 35)
     
     #saving figure as an image so we can display it on our canvas later
     fig.savefig('joingraph.jpg')
     #returning the top month that members join the gyms
     return Months[0]
  
#function that puts the ages of members in the midwest into 4 different categories and displays the sum of the counts


def agebymidwest(data):
    #reading file and creating a dataframe with the columns region and age from Records.csv
    
    df= pd.DataFrame(data, columns=['Region', 'Age'])
    
    #filtering dataframe by different age categories
    df_filtered = df.query('Age < 30')
    df_filtered2= df.query('Age >=30 & Age<40')
    df_filtered3= df.query('Age >=40 & Age <50')
    df_filtered4= df.query('Age >=50 & Age <60')
    
    #filtering the dataframe again and only getting the count of the ages from the midwest
    #then summing up the counts of each age range 
    agesunder30= df.query('Region == "Midwest" & Age<30').value_counts().sum()
    agesbetween30and39= df.query('Region== "Midwest" & Age >=30 & Age<40').value_counts().sum()
    agesbetween40and49= df.query('Region== "Midwest" & Age >=40 & Age <50').value_counts().sum()
    ages50andup= df.query('Region== "Midwest" & Age >=50 & Age <60').value_counts().sum()
    
    
    #create dictionary and keys in order to make a figure
    data1= {'Ages Under 30': agesunder30, 'Ages Between 30 and 39': agesbetween30and39, 
            'Ages Between 40 and 49': agesbetween40and49, 'Ages 50 and Up': ages50andup}
   #new dataframe
    df = pd.DataFrame(data1, columns = ['Age'])
    
    #getting keys of dictionary and the values of the filtering variables
    Ages = data1.keys()
    Counts = data1.values()
    
    
    #creating figure and setting its size
    fig = plt.figure(figsize = (9, 5))
    
    #creating bar chart and labels
    plt.bar(Ages, Counts, color ='maroon',
            width = 0.4)
    

    
    plt.xlabel("Age Category")
    plt.ylabel("Count of People in Age Category")
    plt.title("Midwest Age Counts")
    fig.savefig('MidwestAges.jpg')
    plt.show()
    

   
#function that filters the ages of members in the northeast and summing the counts   
def agebynortheast(data):
    #reading file and creating a dataframe with the columns region and age from Records.csv
    
    df= pd.DataFrame(data, columns=['Region', 'Age'])
    
    #filtering dataframe by different age categories
    df_filtered = df.query('Age < 30')
    df_filtered2= df.query('Age >=30 & Age<40')
    df_filtered3= df.query('Age >=40 & Age <50')
    df_filtered4= df.query('Age >=50 & Age <60')
    
     #filtering the dataframe again and only getting the count of the ages from the northeast
    #then summing up the counts of each age range 
    agesunder30= df.query('Region == "Northeast" & Age<30').value_counts().sum()
    agesbetween30and39= df.query('Region== "Northeast" & Age >=30 & Age<40').value_counts().sum()
    agesbetween40and49= df.query('Region== "Northeast" & Age >=40 & Age <50').value_counts().sum()
    ages50andup= df.query('Region== "Northeast" & Age >=50 & Age <60').value_counts().sum()
    
     #create dictionary and keys in order to make a figure
    data1= {'Ages Under 30': agesunder30, 'Ages Between 30 and 39': agesbetween30and39, 
            'Ages Between 40 and 49': agesbetween40and49, 'Ages 50 and Up': ages50andup}
    #new dataframe
    df = pd.DataFrame(data1, columns = ['Age'])
    
     #getting keys of dictionary and the values of the filtering variables
    Ages = data1.keys()
    Counts = data1.values()
    
    
  #creating figure and setting its size
    fig = plt.figure(figsize = (9, 5))
   
    #creating bar chart
    plt.bar(Ages, Counts, color ='green',
            width = 0.4)
    plt.xlabel("Age Category")
    plt.ylabel("Count of People in Age Category")
    plt.title("Northeast Age Counts")
    fig.savefig('NortheastAges.jpg')
    plt.show()
    

   
#function that filters ages of members in the south, and then summing the counts
def agebysouth(data):
    
    df= pd.DataFrame(data, columns=['Region', 'Age'])
    
    df_filtered = df.query('Age < 30')
    df_filtered2= df.query('Age >=30 & Age<40')
    df_filtered3= df.query('Age >=40 & Age <50')
    df_filtered4= df.query('Age >=50 & Age <60')
    
    agesunder30= df.query('Region == "South" & Age<30').value_counts().sum()
    agesbetween30and39= df.query('Region== "South" & Age >=30 & Age<40').value_counts().sum()
    agesbetween40and49= df.query('Region== "South" & Age >=40 & Age <50').value_counts().sum()
    ages50andup= df.query('Region== "South" & Age >=50 & Age <60').value_counts().sum()
    
    data1= {'Ages Under 30': agesunder30, 'Ages Between 30 and 39': agesbetween30and39, 
            'Ages Between 40 and 49': agesbetween40and49, 'Ages 50 and Up': ages50andup}
    df = pd.DataFrame(data1, columns = ['Age'])
    
    Ages = data1.keys()
    Counts = data1.values()
    
    

    fig = plt.figure(figsize = (9, 5))
   
    #creating bar chart
    plt.bar(Ages, Counts, color ='orange',
            width = 0.4)
    plt.xlabel("Age Category")
    plt.ylabel("Count of People in Age Category")
    plt.title("South Age Counts")
    fig.savefig('SouthAges.jpg')
   
    plt.show()
    

#function that filters out the ages of members from the West into specific age categories. Then taking the sum of the counts
def agebywest(data):
    
    df= pd.DataFrame(data, columns=['Region', 'Age'])
    
    df_filtered = df.query('Age < 30')
    df_filtered2= df.query('Age >=30 & Age<40')
    df_filtered3= df.query('Age >=40 & Age <50')
    df_filtered4= df.query('Age >=50 & Age <60')
    
    agesunder30= df.query('Region == "West" & Age<30').value_counts().sum()
    agesbetween30and39= df.query('Region== "West" & Age >=30 & Age<40').value_counts().sum()
    agesbetween40and49= df.query('Region== "West" & Age >=40 & Age <50').value_counts().sum()
    ages50andup= df.query('Region== "West" & Age >=50 & Age <60').value_counts().sum()
    
    
    data1= {'Ages Under 30': agesunder30, 'Ages Between 30 and 39': agesbetween30and39, 
            'Ages Between 40 and 49': agesbetween40and49, 'Ages 50 and Up': ages50andup}
    df = pd.DataFrame(data1, columns = ['Age'])
    
    Ages = data1.keys()
    Counts = data1.values()
    

    fig = plt.figure(figsize = (9, 5))
   
    #creating bar chart
    plt.bar(Ages, Counts, color ='purple',
            width = 0.4)
    
    plt.xlabel("Age Category")
    plt.ylabel("Count of People in Age Category")
    plt.title("West Age Counts")
    fig.savefig('WestAges.jpg')
    plt.show()
    


#function that calculates the locations with the most members
def states(data):
     
     #dataframe
     df = pd.DataFrame(data,columns=['State'])
     
     
     #calculating the counts of the dataframe and then retriving the top 5 states
     df1= df['State'].value_counts()[:5]
     
     #getting the value of the count calculation and the keys from the dataframe
     Counts = df1.values
     States= list(df1.keys())
     
     fig = plt.figure(figsize = (9, 5))
   
    #creating bar chart and labels
     plt.bar(States, Counts, color ='red',
            width = 0.4)
     
     plt.xlabel("States")
     plt.ylabel("Count of Current Members in Each State")
     plt.title("Most Popular States")
     fig.savefig('PopularStates.jpg')
     plt.show()
     #returning the top states
     return States[0]

    
    

                  




