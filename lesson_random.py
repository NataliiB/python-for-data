import random

comp_choice = random.randint(0,10)
n_count = 0
while n_count < 3:
    try:
      user_choice = int(input("Enter a integer"))
    except ValueError:
      print("Uncorrect number")
      continue
    else:
      print("I remembered your number")
    finally:
      n_count += 1
      print(f"{user_choice}")
    if comp_choice > user_choice:
        print("Make the number bigger")
    elif comp_choice == user_choice:
        print("Congatulations!You guessed it")
        break
    else:
        print("Make the number smaller")
    print("Try again!")