# GUI_application
Gym Member Application made with Python in Computational Thinking.

## Table of Contents
* [General Info](#general-information)
* [Business Problem](#business-problem)
* [Development Process](#development-process)
* [Functions](#functions)
* [Project Status](#project-status)

## General Information
The purpose of this project was to create a GUI application to inform a gym what areas and age ranges they can expand to. We used python to filter and display a large data set.



## Business Problem
A gym is planning on expanding its business. They want to increase their marketing efforts and potentially opening a new branch somewhere. The gym is unsure of what their target market is and where they should continue expansion. The gym's management and marketing team need a data analysis of the current members to see how they should market the existing gyms and to see the potential trends in the current members. 


## Development Process
- Used a csv file with over 500 rows of gym member's data
- Use tkinter to set up GUI
- Added buttons, labels, dropdown menu, listbox and entries
- Added functions to that would filter out the dataset, calculate total members, display age ranges, etc.


## Functions
- Joinmonth() function​
    - Creates a dataframe out of input
    - Found counts of each month​
    - Got values and keys directly from the dataframe​
    - Created bar plot and saved as jpg​
    - PURPOSE: to calculate and visualize the top months that people join

- Agebymidwest() function​
    - Function that puts the ages of members in the Midwest into 4 different categories and displays the sum of the counts​
    - Created a dataframe and filtered it into age categories and only count the members in the Midwest​
    - Calculated the sum in each age range​
    - Created a dictionary with values and keys ​
    - Created a bar chart and saved as jpg​
    - PURPOSE: determine the appropriate age range to target ​

- ​Agebynortheast() function​
    - Same functionality as last function except filters specifically for the Northeast​
    - PURPOSE: determine the appropriate age range to target ​

- Agebysouth() function​
    - Same functionality as last function except filters specifically for the south​
    - PURPOSE: determine the appropriate age range to target 

- Agebywest() function​
    - Same functionality as last function except filters specifically for the west​
    - PURPOSE: determine the appropriate age range to target 


- States() function​
    - Create a dataframe and calculate the counts of each of the states​
    - Return top 5 states​
    - Values and keys from dataframe​
    - Plot bar chart ​
    - PURPOSE: visualize the top 5 states and determine what states gym should expand/advertise to

- Loads() function​
    - Loads data from input (Records.csv) into the program​
    - Error handle if user does not put in correct file name then "File Not Found" message displays​

- Loadstategraph()​
    - Calls the joinmonth function and displays the generated graph onto the canvas​
    - Error handling if user clicks the button first then error message "Please load the file first."​
    - Else: calls state function and places the generated graph onto the canvas

- Loadstategraph()​
    - Calls the states function and loads the saved graph generated and displays it onto canvas

- Dropdowncontroller() function​
    - PURPOSE: whatever option is selected in the drop down menu, this function calls the correct function and loads/displays the correct graph​
    - Error handling: if user selects a region before loading the csv file, then "Please load the file first." Error message displays in the listbox​
    - Error handling 2: if user does not select an option and clicks select, then "Invalid option selected" is displayed​
    - If/elif/else statements to determine what function to call and display according to what region is clicked​
    - PURPOSE: gym can see what target market is according to each region


## Project Status
Project is: complete


