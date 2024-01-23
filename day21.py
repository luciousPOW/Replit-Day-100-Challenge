# lives = 3
# while True:
#     user_input = int(input('1 x 7: '))
#     if user_input == 7:
#         print('Good!')
        
#     else:
#         lives -= 1
#         break
#     user_input = int(input('2 x 7: '))
#     if user_input == 14:
#         print('Keep it up!')
        
#     else:
#         lives -= 1
#         break
        
#     print(f'You scored {lives} out of 2')
    
print('Welcome to Quiz Game!')
print()

fact_family = int(input('Name your multiples: '))
print()
counter = 0
for i in range(1,11):
    correct_answer = i * fact_family
    print(i, 'x', fact_family)
    answer = int(input('> '))
    if answer == correct_answer:
        print('You got it right!')
        counter += 1
    else:
        print("That's not correct. It should have been", correct_answer)
        
    if counter == 10:
        print('Wow! A perfect score!')
    else:
        print(f"You got {counter} out of 10 correct.")
