# Wordle Tools for NYT Wordle: Analyze Start word and Check Results
from tkinter import *

window = Tk()

logo = Label(
    window,
    text="Wordle Tools", 
    font=('impact',40,'bold'),
    fg='#ffffff',
    bg='#121213'
)
day_label = Label(
    window, 
    text="Select Wordle Day", 
    font=('arial',20),
    fg='#ffffff',
    bg='#121213'
)
logo.pack()
day_label.pack()

user_day_var = StringVar()
day_entered = Entry(window,textvariable = user_day_var, font = ('arial', 10), bd=0)
day_entered.pack()

guess_label = Label(
    window,
    text="Enter your guess",
    font=('arial', 20),
    fg='#ffffff',
    bg='#121213'
)
guess_label.pack()

word_var = StringVar()
word_entered = Entry(window,textvariable = word_var, font = ('arial', 10), bd=0)
word_entered.pack()


window.geometry("420x420")   
window.title("Wordle.tools")       
window.config(background="#121213")       

def best_guess(word_guessed, valid_words, day_correct, user_day):

    is_prev = False

    guess_percent = 0
    com_ct = 0
    num_cor = 0
    num_placed = 0

    COMMON_LETTERS = 'earotlisnc'
    word_correct = valid_words[day_correct]

    prev_solutions = []

    for i in range(len(valid_words)):
        if (i < user_day):
            prev_solutions.append(valid_words[i])

    for i in range(len(word_guessed)):
        for j in range(len(COMMON_LETTERS)):
            if (word_guessed[i]==COMMON_LETTERS[j]):
                com_ct += 1
    for char, word in zip(word_guessed, word_correct):
        if (word in word_correct and word in char):
            num_placed += 1
        elif (word in word_correct):
            num_cor += 1

            
    guess_percent = com_ct + (num_cor * 5) + (num_placed * 20)

    for i in range(len(prev_solutions)):
        if (word_guessed == prev_solutions[i]):
            is_prev = True

    if (is_prev):
        guess_percent = guess_percent - 50

    if (guess_percent > 100 or user_day == day_correct):
        guess_percent = 100
    elif (guess_percent < 0):
        guess_percent = 0

    return guess_percent

def run_analysis():
    word = str(word_entered.get())
    user_day = int(day_entered.get())
    valid_words = [
    'cigar',
    'rebut',
    'sissy',
    ]
    word_valid = False
    while word_valid == False:
        for i in range(len(valid_words)):
            if word == valid_words[i]:
                day_correct = i
                print('word is valid')
                print('Word entered:',valid_words[i])
                print('Correct Day',day_correct)
                word_valid = True

    if day_correct == user_day:
        print('word is correct')
    else:
        print('word is incorrect')

    guess_score = best_guess(word, valid_words, day_correct, user_day)

    print('Your guess score is: '+str(guess_score)+'%')

run = Button(window, text = 'Enter', font = ('arial'), command = run_analysis)
run.pack()

window.mainloop()
