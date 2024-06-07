import string
import getpass

low = up = num = wspace = special = 0
def check_password(password, low=0, up=0, num=0, wspace=0, special=0):
  Strength = 0
  Feedback = ''
  for char in list(password):
    if char in string.ascii_lowercase:
      low+=1
    if char in string.ascii_uppercase:
      up += 1
    elif char in string.digits:
      num += 1
    elif char == ' ':
      wspace += 1
    else:
      special += 1

  # Determine Strength based on character types and minimum requirements
  Strength += 1 if low >= 1 else 0  
  Strength += 1 if up >= 1 else 0  
  Strength += 1 if num >= 1 else 0
  Strength += 1 if wspace >= 1 else 0
  Strength += 1 if special >= 1 else 0

  # Assign Feedback based on Strength Level
  if Strength == 2:
    Feedback = "Very Weak Password"
  elif Strength == 3:
    Feedback = "Good Password"
  elif Strength == 4:
    Feedback = "Very Good Password"
  else:
    Feedback = "Excellent Password"

  return Strength, Feedback

def re_enter(another=False):
  valid = False
  if another :
      choice = input('Do you want to check again ??? (Y/N)')
  else :
      choice = input('Do you want to Check Password ??? (Y/N)')
  while not valid:
    if choice == 'n' :
      return False
    elif choice == 'y' :
      return True
    else:
      print("INVALID TRY AGAIN!")

def main():
  print("WELCOME TO PASSWORD CHECKER")

  while True:
    passw = getpass.getpass("Enter the password : ")
    n = len(passw)
    if n > 8:
      password  = passw
    else :
      print("Enter a Password with more than 8 letters ")
      re_enter()
    strength, feedback = check_password(passw)
    if n > 8:
      print(f"Feedback : {feedback}")
      if strength>1:
        strength_emojis = ['\U00002764' for _ in range(strength)]
        print(*strength_emojis, sep='')  # Print emojis in a single line
      else :
        print('\U0000203C')

    if not re_enter(True):
      break

if __name__ == '__main__':
  main()