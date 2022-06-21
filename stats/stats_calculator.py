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


def main():
    #ask user to enter filename and open that file
    file_name = get_file_name()
    
    #load number from file into a list
    list_of_numbers = load_numbers_list(file_name)

    print(list_of_numbers)


main()