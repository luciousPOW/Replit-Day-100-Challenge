counter = 0
while True:
    answer = int(input("Enter a number: "))
    print("Adding it up!")
    counter += answer
    print("Current total is", counter)
    addAnother = input("Add another number? Y/N ")
    if addAnother == "no":
     break
print("Bye!")