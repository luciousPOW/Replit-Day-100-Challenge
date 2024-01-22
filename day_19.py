loan = 100
interest = 0.02

for i in range(10):
    loan += (loan * interest)
    print('Day:', i+1, 'is', round(loan,2))
print('Total interest at the end of 10 days: ', round(loan, 2))