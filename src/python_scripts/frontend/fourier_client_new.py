import data_handling.data_handler as dd
import analysis.fourier as ff

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
column_name = column[selected_column_index]

# Get user input for the date range
start_date = input('Enter the start date (YYYY-MM-DD): ')
end_date = input('Enter the end date (YYYY-MM-DD): ')

ff.visualize_fourier_analysis(user_data , column_name, start_date, end_date)

# # time_series needed for fourier
# user_time_series = dd.get_time_series(user_data, columns[selected_column_index])

# # get window_size
# size_valid = False

# while(size_valid == False):
#     global window_size
#     window_size = input("Select window_size: (must be numeric, enter 666 to quit)")
#     size_valid = window_size.isnumeric()
#     if(selected_column == "666"):
#         quit()
#     if(column_valid == False):
#         print("To choose a window size please enter a numeric characters only")

# window_size = int(window_size)

# # intervall hard code TODO dynamic user input

# intervall = 15*60.0
# #smooth signal
# smoothed_signal = ff.smooth_signal(user_time_series, window_size)

# #
# ff.fourier_plot(smoothed_signal, intervall)
