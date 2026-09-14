def add(x,y):
    """Adds two numbers."""
    return x+y

def subtract(x,y):
    """Subtracts two numbers."""
    return x-y

def multiply(x,y):
    """Multiplies two numbers."""
    return x*y

def divide(x,y):
    """Divides two numbers, handles ZeroDivisionError."""
    try:
        #Attempt to divide the numbers
        result=x/y
        return result
    except ZeroDivisionError:
        #Handle the case where the user tries to divide by zero
        return "Error: Division by zero is not defined."

def get_number(number):
    """Gets a valid number from the user."""
    while True:
        try:
            #Attempt to convert user input to an integer
            num=int(input(number))
            return num
        except ValueError:
            #Handle the case where input is not a number (e.g., text)
            print("Invalid input. Please enter a valid number.")

def main():
    """Main function to run the calculator loop."""
    print("-------------MENU--------------")
    print("Welcome to the Basic Calculator!")
    print("Operations are Displayed Below: ")
    print("1.Add (+)")
    print("2.Subtract (-)")
    print("3.Multiply (*)")
    print("4.Divide (/)")

    while True:
        #Prompt user to choose an operation
        choice=input("\nEnter operation (1/2/3/4 or q/Q to quit): ")

        #Check if the user wants to quit
        if choice.lower()=='q':
            print("Exiting calculator. Goodbye!")
            break

        #Check if the chosen operation is valid
        if choice in ('1','2','3','4'):
            #Get numbers from the user
            num1=get_number("Enter first number: ")
            num2=get_number("Enter second number: ")

            #Perform the selected operation and display the result
            if choice=='1':
                print("Result:",num1,"+",num2,"=",add(num1,num2))
            elif choice=='2':
                print("Result:",num1,"-",num2,"=",subtract(num1,num2))
            elif choice=='3':
                print("Result:",num1,"*",num2,"=",multiply(num1,num2))
            elif choice=='4':
            #Convert both number from integer to float when operation is division
                NUM1=float(num1)
                NUM2=float(num2)
                print("Result:",num1,"/",num2,"=",divide(NUM1,NUM2))
        else:
            #Handle invalid menu choices
            print("Invalid Input. Please select a valid operation from the menu. You can quit as well.")

if __name__ == "__main__":
    main()
