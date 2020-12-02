import pandas as pd
import re
import datetime
import emailsend
import os


#GETTING THE CURRENT DIRECTORY
current_directory = os.getcwd()

#GETTING THE FILE PATH 
file_path = os.path.join(current_directory, 'Leave_reminder_web', 'csv_files', 'Leave_file.csv')

print(file_path)
#READING THE CSV FILE
leave_df = pd.read_csv(file_path)

#GETTING THE PEOPLE AND DATES ONLY
people_and_date_df = leave_df.iloc[:,[0,5,6,7,8,9,10,11,12,13,14,15,16]]

#FILLING THE NAN CELLS WITH EMPTY
people_and_date_df = people_and_date_df.fillna('Empty')

#GETTING A LIST OF COLUMN NAMES
column_list = list(people_and_date_df.columns.values)

month_counter = 12

#GETTING THE NUMBER OF PEOPLE
people_counter = people_and_date_df.shape[0]



#ITERATING THROUGH THE PEOPLE AND THEIR LEAVE DATES
for person in range(people_counter):
      
    for month in range(month_counter):
        
        daystring = ''
        
        #GETING THE DATES THAT ARE NOT EMPTY
        if people_and_date_df.iloc[person, month+1] != 'Empty':
            
            try:
                daystring = people_and_date_df.iloc[person, month+1]
                
                #SUBSTRINGING AND ONLY GETTING THE NUMBERS IN THE DATE
                daystring  = re.sub('[^0-9]', '', daystring[0:3])
                
                #CHECKING IF THE DAY LENGTH IS GREATER THAN 1 TO KNOW WHEN TO ADD A ZERO OR NOT 
                if len(daystring) == 1:
                    daystring = '0'+ daystring
                    
                #GETTING THE MONTH AND YEAR FROM THE LIST OF MONTHS 
                month_year_string = str(column_list[month+1])
                
                #REPLACING THE - WITH A /
                month_year_string = re.sub('-','/', month_year_string)
                
                #ADDING UP THE STRING TO MAKE THE FINAL DATE STRING FOR THE DATE TIME OBJECT
                datestring = daystring + '/' + month_year_string
                print(datestring)
                            
                #TURNING THE LEAVE DATE INTO A DATE TIME OBJECT
                leave_date = datetime.datetime.strptime(datestring, '%d/%b/%y')
                
                #GETTING TODAY'S DATE 
                today = datetime.datetime.now()
                
                #CALCULATING THE NUMBER OF DAYS BETWEEN THE DATES
                delta = leave_date - today
                           
                #EXTRACTING THE INFO ABOUT THE EMPLOYEE AND THEIR SUPERVISOR
                employee = str(leave_df.iloc[person, 0])
                employee_email = str(leave_df.iloc[person, 1])  
                supervisor = str(leave_df.iloc[person, 2])  
                supervisor_email = str(leave_df.iloc[person, 3])
                         
                #SEVEN DAY REMINDER USE 6 DAYS INSTEAD OF 7
                if delta.days == 6:
                    print('Leave')
                    emailsend.sevendayreminderemail(employee, supervisor, employee_email, supervisor_email, datestring)
                            
                #TWO DAY REMINDER USE 1 DAY INSTEAD OF 2 
                if delta.days == 1:
                    print('Leave')
                    emailsend.twodayreminderemail(employee, supervisor, employee_email, supervisor_email, datestring)
                    
                    
                print(delta.days)
                
            except:
                print('Leave date has an issue')
            
            #print(leave_date_object)
            
            
            
            
    
    