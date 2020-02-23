#Q1


# a=int(input('Enter a Length:- '))
# b=a*2.54
# if(a>0):
#   print('Result:'+str(b))
# else:
#   print('Incorrect Value')



#Q2

# import random
# a=input("Enter the  guess number:-  ")
# computer=random.randint(0,11)
# if a==computer:
#     print("Your Guess is Correct"+"Computer Number is:- " +str(computer))
# else:
#     print("Try Again"+"Computer Number is:- "+str(computer))


#Q3

import random
while(True):
 num1 = random.randint(1,10)
 num2 = random.randint(1,10)
 guess =int(input("What is " + str(num1) + "x" + str(num2) + ":- "))
 if guess==num1*num2:
     print("Correct")
 else:
     print("Wrong")
     print("Correct Answer is:- "+str(num1*num2))
print("Correct Anawer")



#Q4
#
#
#
#
#
