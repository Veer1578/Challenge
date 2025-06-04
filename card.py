class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word + ' ('+self.meaning+') '

flash = []
print('Welcome to flashcard app')

while(True):
    word = input('Enter title for flashcard: ')
    meaning = input('Enter its definition: ')
    flash.append(flashcard(word, meaning))
    option = int(input('Enter 0 if you want to add another flashcard or press 1 if not: '))
    if option == 1:
        break
    elif option == 0:
        continue

print('Your flashcards')
for i in flash:
    print('-', i)
