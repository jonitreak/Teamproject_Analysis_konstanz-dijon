import python_scripts.data_handling.data_handler as dd
import python_scripts.analysis.fourier as ff
from matplotlib import pyplot as plt

print("****WELCOME TO FOURIER CLIENT****")


#load data
user_data = dd.loaData()
columns = dd.get_column_names(user_data)
i = 0;

# column selection
print("Which column would you like to analyse?")
for column in columns:
    print(i+1 , ".: " , columns[i])
    i = i+1;
print("0.: EXIT")
column_valid = False
while(column_valid == False):
    global selected_column_index
    selected_column = input("Please select column number: ")
    column_valid = selected_column.isnumeric()
    if(selected_column == "0"):
        quit()
    if(column_valid == False):
        print("To choose a Column Number please enter a numeric characters only")

selected_column_index = int(selected_column)-1
column_name = columns[selected_column_index]

# Get user input for the date range
start_date = input('Enter the start date (YYYY-MM-DD): ')
end_date = input('Enter the end date (YYYY-MM-DD): ')
# start_date = "2021-02-01"
# end_date = "2021-02-15"


ff.do_fourier(user_data, column_name, start_date, end_date)
