first_name = input("First name: ")
last_name = input("Last name: ")
birth_day = int(input("Enter your birth day: "))
birth_month = input("Enter your birth month: ")
birth_year = input("Enter your birth year: ")
age = 2022 - int(birth_year)

print("Hello I am " + first_name, last_name +
      ".", "I am birth", birth_day, birth_month, birth_year + ".", "I am age", age, "years old.")
