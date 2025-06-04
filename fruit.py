import random

class fruit:
    def __init__(self):
        self.fruits = {'apple':'red', 'banana': 'yellow', 'mango':'orange', 'watermelon':'green'}

    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            print('Wat is the color of {}'.format(fruit))
            Uans = input()

            if Uans.lower() == color:
                print('Correct')
            else:
                print('Wrong')
            option = int(
                input('Enter 0 if you want play again or press 1 if not: '))
                
            
            if option == 1:
                break
            elif option == 0:
                continue


print('Welcome to fruit quiz')
fr = fruit()
fr.quiz()