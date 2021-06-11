#import module
import random

#defining the function
def game(p,c):

  #Who win?
  if p == c:
    return None

  elif (p=='s') & (c=='w'):
    return True

  elif (p=='w') & (c=='s'):
    return False

  elif (p=='g') & (c=='s'):
    return True

  elif (p=='s') & (c=='g'):
    return False

  elif (p=='w') & (c=='g'):
    return True

  elif (p=='g') & (c=='w'):
    return False

#Heading
print('Enter s for Snake , w for Water , g for Gun')



#Create a random number betwen 1 to 3
r_int = random.randint(1,3)

# Condition to chose Snake,Water,Gun (For computer)
if(r_int == 1):
  c = 'w'

elif(r_int == 2):
  c = 's'

elif(r_int == 3):
  c = 'g'

#Take input from user
p = input('Enter s or g or w:')

#Run function Condition
if p=='s' or p=='w' or p=='g':
  #Call the function
  result = game(p,c)

  #Showing every one's charecter that they chose
  print("You = ",p,"Computer = ",c)

  # Final Winer
  if result == None:
    print("Tie")
  
  elif result == True:
    print("You Win")
  
  elif result == False:
    print("You Lose")
  
else:
  print("Enter a Valid Charecter to Play the Game. Enter s or w or g")
