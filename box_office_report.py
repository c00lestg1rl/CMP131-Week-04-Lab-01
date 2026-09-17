# Samantha Vasquez 
# CMP131-Week-04-Lab-01
# Sept. 17, 2026

# Program 1
# Program Description: A movie theater charges different ticket prices for adults and children.

# Use the following ticket prices:

# Adult ticket: $10.00
# Child ticket: $6.00
# The theater does not keep all the money collected from ticket sales. The theater keeps 20% of the gross box office revenue. The remaining 80% is paid to the movie distributor.

# Create a Python program that asks the user for the movie title and the number of adult and child tickets sold.

# The program must calculate and display a complete box office report.


# Part 1 
movie_title= input('What is the movie name?')
adult_tickets= int(input('How many adult tickets were sold?'))
child_tickets= int(input('How many child tickets were sold?'))

# Part 2
adult_price= 10.00
child_price= 6.00
revenue_adults= adult_tickets * adult_price
revenue_child= child_tickets * child_price
gross_box= revenue_adults + revenue_child
amount_kept= gross_box * 0.20
amount_paid= gross_box * 0.80

print(f'***Movie Sales Report***')
print('Movie name:', movie_title)
print('Adult tickets sold:', adult_tickets)
print('Child tickets sold:', child_tickets)
print(f'***Movie Financials***')
print(f'Revenue from adult tickets: ${revenue_adults:.2f}')
print(f'Revenue from child tickets: ${revenue_child:.2f}')
print(f'Gross box office revenue: ${gross_box:.2f}')
print(f'Amount kept by the theater: ${amount_kept:.2f}')
print(f'Amount paid to movie distributor: ${amount_paid:.2f}')