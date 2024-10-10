#Open the file.
myfile=open('numbers.txt','r')

#Read and display the file's contents.
for line in myfile:
    number=int(line)
    print(number)

# Close the file.
myfile.close()

#Write a program that ask the user for the name of a file.
def display_first_five_lines():
    file_name = input("Enter the name of the file: ")#asking for the name of the file

    try:
        with open(file_name) as file:
            for i in range(5):#the range only to display the first five 
                line = file.readline()
                if not line:
                    break
                print(line, end='')
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")

if __name__ == "__main__":
    display_first_five_lines()

#Write a program that ask the user for the name of a file. 
#The program should display the contents of the file with each line preceded with a line number folled by a colon.
def display_file_with_line_numbers():
    file_name = input("Enter the name of the file: ")

    try:
        with open(file_name) as file:
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number}: {line}", end='') 
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    display_file_with_line_numbers()


#Write a program that displays the number of names that are stored in the file.
def count_names_in_file():
    file_name = 'names.txt'

    try:
        with open(file_name) as file:
            # Count the number of names (lines) in the file
            name_count = sum(1 for line in file)
        
        print(f"Number of names in '{file_name}': {name_count}")
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    count_names_in_file()


#Using numbers.txt write a program that reads all of the numbers stored in the file and calculates their total.
def calculate_total_from_file():
    file_name = 'numbers.txt'

    try:
        with open(file_name) as file:
            total = sum(int(line.strip()) for line in file if line.strip().isdigit())
        
        print(f"The total of the numbers in '{file_name}' is: {total}")
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
    except ValueError:
        print("The file contains non-integer values.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculate_total_from_file()

