from python_scripts.data_handling import data_handler as dd
import python_scripts.analysis.fourier as ff

def main():
    print("****WELCOME TO FOURIER CLIENT****")

    # Load data
    user_data = dd.loaData()
    columns = dd.get_column_names(user_data)
    
    # Column selection
    print("Which column would you like to analyse?")
    for i, column in enumerate(columns):
        print(f"{i+1} .: {column}")
    
    print("0.: EXIT")
    column_valid = False
    while not column_valid:
        selected_column = input("Please select column number: ")
        if selected_column == "0":
            quit()
        column_valid = selected_column.isnumeric()
        if not column_valid:
            print("To choose a column number please enter numeric characters only")

    selected_column_index = int(selected_column) - 1
    column_name = columns[selected_column_index]

    # Get user input for the date range
    # Uncomment these lines if you want to take user input for dates
    # start_date = input('Enter the start date (YYYY-MM-DD): ')
    # end_date = input('Enter the end date (YYYY-MM-DD): ')
    start_date = "2021-06-01"
    end_date = "2021-06-10"

    ff.do_fourier(user_data, column_name, start_date, end_date)

if __name__ == "__main__":
    main()
