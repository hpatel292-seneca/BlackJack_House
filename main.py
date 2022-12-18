import random

cards = [1, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def show_info():
  print(f"Your cards are {user}")
  print(f"computer 1st card is [{computer[0]}]")

def get_random_card():
  return random.choice(cards)

def sum(player):
  return_value = 0
  for i in player:
    return_value += i

  return return_value  

def check_result(user, computer):
  user_sum = sum(user)
  computer_sum = sum(computer)
  if computer_sum > 21:
    if user_sum > 21:
      print("It's a draw")
      return
    else:
      print("User win")
      return
  elif user_sum > 21:
    print("User busted!\n computer Win")
  elif user_sum == computer_sum:
    print("it's a draw")
    return
  elif user_sum > computer_sum:
    print("User Win")
    return
  else:
    print("Computer Win")

    

user = []
computer = []

user.append(get_random_card());
user.append(get_random_card());
computer.append(get_random_card());
computer.append(get_random_card());

done = True
while done:
  show_info()
  next = input("type 'y' for another card or 'n' for check?  ").lower()
  if next == 'n':
    while sum(computer) >= 17:
      computer.append(get_random_card());
    print(f"User cards {user}")
    print(f"Computer cards {computer}")
    check_result(user, computer)  
    done = False
  else:
    user.append(get_random_card());

    if sum(user) >= 21:
      print(f"User cards {user}")
      print(f"Computer cards {computer}")
      check_result(user, computer)
      done = False
    