import random

class FlashCard:
    def __init__(self):
        self.fruits = {
            'apple': 'red',
            'banana': 'yellow',
            'grapes': 'green',
            'orange': 'orange'
        }

    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            ans = input(f'What is the color of {fruit} ?')
            if ans.lower() == color:
                print('Correct Answer!!')
            else:
                print('Wrong Answer!!')

            option = int(input("enter 0 , if you want to play again : "))
            if (option):
                break

print("Welcome to the quiz")
fc = FlashCard()
fc.quiz()