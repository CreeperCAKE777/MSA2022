import os.path

def get_file_name():
    while True:
        #prompt user to enter file name
        user_input = input("Please enter a file name: ")
        #make sure user entered a value. Re prompt if not
        if user_input == "":
            print("ERROR: please enter a value.\n")
            continue
        elif not os.path.exists(user_input):
            print("ERROR: File does not exist.\n")
            continue
        else:
            break
    #else return the value
    return user_input

#Function to load numbers from file into list
#Parameters: file name
#returns a list of numbers
def load_numbers_list(file_name):
    numbers_list = []
    #open the file
    file = open(file_name, "r")
    #read file line by line
    for number in file:
        #convert to int and append numbers to a list
        numbers_list.append(int(number))
    #return the list
    return numbers_list

def calculate_median_value(numbers_list):
    #sort the list
    numbers_list.sort()
    #determine if the list has an even or odd number of items using the len() function
    if (len(numbers_list) % 2 == 0):
        is_even = True
    else:
        is_even = False
    #if even find the two middle values and calculate the average of the two
    if is_even:
        index_1 = int(len(numbers_list) / 2)
        print(index_1)
        index_2 = index_1 - 1
        print(index_2)
        median_value = (numbers_list[index_1] + numbers_list[index_2]) / 2
    #if odd, return the middle value
    else:
        index = int((len(numbers_list) - 1) / 2)
        median_value = numbers_list[index]
 
    return median_value

def determine_modal_value(numbers_list):
    #create a dictionary to store list vaules and frequencies
    modal_values = {}
    list_of_modal_values = []
    #Loop through list.
    for number in numbers_list:
    #   If the number is in the dictionary then add 1 to its value
    #   If number not in dictionary then insert as key in dict with value 1
        if number in modal_values:
            modal_values[number] += 1
        else:
            modal_values[number] = 1
    #Determine the largest value in the dictionary
    list_values = modal_values.values()
    max_value = max(list_values)
    #Append those keys with the largest values to a list
    for key in modal_values:
        if modal_values[key] == max_value:
            list_of_modal_values.append(key)
    #Return list of modal value(s)
    return list_of_modal_values
    
def calculate_sum(numbers_list):
    total = 0
    for number in numbers_list:
        total += number
    return total

def print_output(name_of_file, list_sum, num_items, list_avg, max_val, min_val, num_range, median_val, modal_val):
    print("\nProgram Statistics\n-------------------")
    print(f"Filename: {name_of_file}")
    print(f"Sum: {list_sum}")
    print(f"Count: {num_items}")
    print(f"Average: {list_avg:.2f}")
    print(f"Maximum: {max_val}")
    print(f"Minimum: {min_val}")
    print(f"Range: {num_range}")
    print(f"Median: {median_val}")
    print(f"Mode: {modal_val}")
    return

def process_data(file_name, list_of_numbers):
    median_value = calculate_median_value(list_of_numbers)
    modal_values = determine_modal_value(list_of_numbers)
    num_items = len(list_of_numbers)
    sum_of_list = calculate_sum(list_of_numbers)
    average = sum_of_list / num_items
    max_value = max(list_of_numbers)
    min_value = min(list_of_numbers)
    range_of_values = max_value - min_value
    print_output(file_name, sum_of_list, num_items, average, max_value, min_value, range_of_values, median_value, modal_values)
    return


def main():
    while True:
        #ask user to enter filename and open that file
        file_name = get_file_name()
        
        #load number from file into a list
        list_of_numbers = load_numbers_list(file_name)

        #check the length of the list to determine how to process the data
        if len(list_of_numbers) == 0:
            print("File was empty!")
        elif len(list_of_numbers) == 1:
            print_output(file_name, list_of_numbers[0], 1, list_of_numbers[0], list_of_numbers[0], 
            list_of_numbers[0], 0, list_of_numbers[0], list_of_numbers[0])
        else:
            process_data(file_name, list_of_numbers)

        #Ask user if they want to perform another calculation. If not, end program.
        do_again = input("\nWould you like to perform another calculation? Press 'Y' or 'y' to continue: ")
        if do_again.upper() != "Y":
            print("Goodbye :-)")
            break
main()