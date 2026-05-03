name = input("What is your cat's name? ")
age = int(input("How old is your cat? "))

print(f"Hello, owner of {name}")

if age < 5:
    print("Your cat is under 5 years old.")
else:
    print("Your cat is over 5 years old.")

print(f"Next year your cat will be {age + 1}")
