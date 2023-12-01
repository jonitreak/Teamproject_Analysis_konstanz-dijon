import python_scripts.data_handling.data_handler as dd
import python_scripts.analysis.fourier as ff
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.ticker import MultipleLocator

print("****WELCOME TO FOURIER CLIENT****")
#hardcode path since trouble reading in correct format for now
# TODO dynamic path with user input

file_path = "C:\\Users\\Viktoria Stiem\\Documents\\htwg Konstanz\\2324Wise\\teamprojekt\\code\\Teamproject_Analysis\\src\\data\\daten.csv"
# file_path= input("Which Data-file would you like to upload? File must be csv")
# if dd.validade_path(file_path):
#     print("File accepted")
# else:
#     print("File not accepted")
#     quit()

#load data
user_data = dd.loaData(file_path)
columns = dd.get_column_names(user_data)
i = 0;

# column selection
print("Which column would you like to analyse?")
for column in columns:
    print(i+1 , ".: " , columns[i])
    i = i+1;
print("666.: EXIT")
column_valid = False
while(column_valid == False):
    global selected_column_index
    selected_column = input("Please select column number: ")
    column_valid = selected_column.isnumeric()
    if(selected_column == "666"):
        quit()
    if(column_valid == False):
        print("To choose a Column Number please enter a numeric characters only")

selected_column_index = int(selected_column)-1
column_name = columns[selected_column_index]

# Get user input for the date range
# start_date = input('Enter the start date (YYYY-MM-DD): ')
# end_date = input('Enter the end date (YYYY-MM-DD): ')
# start_date = "2021-02-01T00:00:00.0000000Z"
# end_date = "2021-02-15T00:00:00.0000000Z"


# # ff.visualize_fourier_analysis(user_data, column_name, start_date, end_date)
timestamps = pd.to_datetime(user_data['timestamp'])

# # Convert start and end dates to datetime64[ns]
# # start_date = np.datetime64(start_date)
# # end_date = np.datetime64(end_date)
    
# # Filter data based on the specified date range
# mask = (timestamps >= start_date) & (timestamps <= end_date)
column_values = user_data[column_name]
# timestamps = timestamps[mask]


##plotting

y_min = min(column_values)
y_max = max(column_values)
y_delta = 1

# Plot the data
plt.plot(timestamps, column_values, color='b')
plt.title('Temperature Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Temperature (°C)')

# Set y-axis limits and delta
# plt.ylim(y_min, y_max)
# # y_major_locator = MultipleLocator(y_delta)
# # plt.gca().yaxis.set_major_locator(y_major_locator)

# # Show the plot
plt.grid(True)
plt.show()


# for value in column_values:
#     print(value)


# for values in timestamps:
#     print(values)

# print(timestamps[1])
# for i in range(len(timestamps)):
#     print(timestamps[i])
    
print(timestamps[1])