# Malcolm Keniston
#Prog Purpose: This program finds the cost of movie tickets
#Price for one ticket: $10.99
#Sales tax rate: 5.5%

import datetime

###############  define global variables  ###############################
# define tax rates and prices
sales_tax_rate = 0.055
pr_ticket = 10.99

# define global variables
num_tickets = 0
subtotal = 0
sales_tax = 0
total = 0


###############  define program functions  ##################################### 
def main():
    more_tickets = True
    while more_tickets:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to order again (Y or N)? ")
        if yesno == 'N' or yesno == 'n':
            more_tickets = False
            print('Thank you for your order. Goodbye!')

def get_user_data():
    global num_tickets
    num_tickets = int(input("Enter the number of tickets: "))   

def perform_calculations():
    global subtotal, sales_tax, total
    subtotal = num_tickets * pr_ticket
    sales_tax = subtotal * sales_tax_rate
    total = subtotal + sales_tax

def display_results():
    print('-----------------------------')
    print('**** CINEMA HOUSE MOVIES ****')
    print('-Your neighborhood movie house-')
    print('-----------------------------')
    print('Tickets     $' + str(subtotal))
    print('Sales Tax   $' + str(sales_tax))
    print('Total       $' + str(total))
    print('-----------------------------')
    print(str(datetime.datetime.now()))

###############  call main function  ########################################## 
main()