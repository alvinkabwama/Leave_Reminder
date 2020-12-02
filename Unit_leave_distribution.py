import pandas as pd
import os


#GETTING THE CURRENT DIRECTORY
current_directory = os.getcwd()

#GETTING THE FILE PATH 
file_path = os.path.join(current_directory, 'Leave_reminder_web', 'csv_files', 'Leave_file.csv')

#print(file_path)
#READING THE CSV FILE
leave_df = pd.read_csv(file_path)

#GETTING THE PEOPLE AND DATES ONLY
unit_and_date_df = leave_df.iloc[:,[4,5,6,7,8,9,10,11,12,13,14,15,16]]

#FILLING THE NAN CELLS WITH EMPTY
unit_and_date_df = unit_and_date_df.fillna('Empty')

#GETTING A LIST OF COLUMN NAMES
column_list = list(unit_and_date_df.columns.values)


month_counter = 12

#GETTING THE NUMBER OF PEOPLE
people_counter = unit_and_date_df.shape[0]

#CREATING A DATA FRAME WITH EMPTY ROWS AND COLUMN
final_df = pd.DataFrame(columns = column_list[1:], index = ['DQU', 'DMU', 'Benefits', 'Customer_service'])


for month in range(month_counter):
    
    DMU_count = 0
    DQU_count = 0
    Benefits_count = 0
    Customer_service_count = 0
    
    for person in range(people_counter):
        
        if unit_and_date_df.iloc[person, 0] == 'DQU' and unit_and_date_df.iloc[person, month+1] != 'Empty':
            DQU_count += 1
            
        if unit_and_date_df.iloc[person, 0] == 'DQU' and unit_and_date_df.iloc[person, month+1] != 'Empty':
            DMU_count += 1
            
        if unit_and_date_df.iloc[person, 0] == 'Benefits' and unit_and_date_df.iloc[person, month+1] != 'Empty':
            Benefits_count += 1
            
        if unit_and_date_df.iloc[person, 0] == 'Customer_service' and unit_and_date_df.iloc[person, month+1] != 'Empty':
            Customer_service_count += 1
            
    
    final_df.iloc[0, month] = DQU_count
    final_df.iloc[1, month] = DMU_count
    final_df.iloc[2, month] = Benefits_count
    final_df.iloc[3, month] = Customer_service_count

path = os.getcwd()
print (path)

finalpath = os.path.join(path, 'Unit_leave_distribution.csv')  
final_df.to_csv(finalpath, index=True)


