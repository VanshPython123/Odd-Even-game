import random
print(f'Rules')
even_odd=str.lower(input(f'Enter odd or even to start the game:'))
num=int(input(f'Enter the number:'))
if num>10 :
    print('Number should be below or equal to 10')
    exit()
elif num<1:
    print('Number should not be below 1')
    exit()
opt=random.choice(range(1,10))
sum=num+opt
print(f'I choosed {opt} and you choosed {num}\n The sum is {sum} \n \n')
if even_odd=='odd' and sum%2!=0:
    print('You won! I lose')
elif even_odd=='even' and  sum%2==0:
    print('You won! I lose')
elif even_odd=='odd' and sum%2==0:
    print('I won! You lose ')
elif even_odd=='even' and sum%2!=0:
    print('I won! You lose')
