import numpy as np
import random
import os

class Password:
    def __init__(self, Favorite_word, symbols_count_in_procent="35%", num_count_in_procent="15%", Favorite_word_non_capital_procent="25%", Favorite_word_capital_procent="25%", randomize_letters=True):
        if randomize_letters:
            self.choise                         = ['symbols', 'numbers', 'Favorite_word_non_capital', 'Favorite_word_capital']
        else:
            self.choise                         = ['symbols', 'numbers']
        self.numbers                            = '1234567890'
        self.symbols                            = '!@#$%^&*()-=_+\\|:;"\'{[}]<>,./?~`'
        self.Favorite_word                      = Favorite_word
        self.Favorite_word_non_capital          = self.Favorite_word.lower()
        self.Favorite_word_capital              = self.Favorite_word.upper()
        self.len                                = len(Favorite_word)
        self.symbols_count                      = int(round((float(symbols_count_in_procent[:-1])*self.len)/100))
        self.num_count                          = int(round((float(num_count_in_procent[:-1])*self.len)/100))
        self.generated_password                 = ''
        self.expected_symbols_count             = 0
        self.expected_num_count                 = 0
        self.randomize_letters                  = randomize_letters
        self.letter_choise                      = ['Favorite_word_non_capital', 'Favorite_word_capital']
        
        self.symbols_count_in_procent           = symbols_count_in_procent
        self.num_count_in_procent               = num_count_in_procent
        self.Favorite_word_non_capital_procent  = Favorite_word_non_capital_procent
        self.Favorite_word_capital_procent      = Favorite_word_capital_procent
        self.p = [float(self.symbols_count_in_procent[:-1])/100, float(self.num_count_in_procent[:-1])/100, float(self.Favorite_word_non_capital_procent[:-1])/100, float(self.Favorite_word_capital_procent[:-1])/100]
        
    def createPassword(self):
        idx = 0
        prob_dict = {'symbols_count_in_procent': 1, 'num_count_in_procent': 2, 'Favorite_word_non_capital_procent': 3, 'Favorite_word_capital_procent': 4}
        while idx < self.len:
            using = np.random.choice(np.arange(1, 5), p=self.p)
            if using == prob_dict['Favorite_word_non_capital_procent']:
                self.generated_password += self.Favorite_word_non_capital[idx]
            if using == prob_dict['Favorite_word_capital_procent']:
                self.generated_password += self.Favorite_word_capital[idx]
            if using == prob_dict['num_count_in_procent']:
                if self.num_count != self.expected_num_count:
                    self.generated_password += random.choice(self.numbers)
                    self.expected_num_count += 1
            if using == prob_dict['symbols_count_in_procent']:
                if self.symbols_count != self.expected_symbols_count:
                    self.generated_password += random.choice(self.symbols)
                    self.expected_symbols_count += 1
            if self.randomize_letters == False:
                self.generated_password += self.Favorite_word[idx]
            else:
                pass
            
            idx += 1
        return self.generated_password
    

    def __str__(self):
        if self.len > 8:
            if self.Favorite_word.isalpha():
                return f'{self.createPassword()}'
            else:
                return f'{None}'
        else:
            return f'{None}'
        



Favorite_word = 'IWantToCreateNewProgrammingLanguageInPython'

i = 1
password = Password(Favorite_word, '35%', '15%', '25%', '25%', randomize_letters=True)
pass_ = str(password)

try:
    print("Your generated Password is: "+pass_)
    dir = input("Where do you want to save your password? (enter directory)\n> ")
    if os.path.isdir(dir + f'passwords'):
        i += 1
    while os.path.isdir(dir + f'passwords ({i})'):
        i += 1
    if i > 1:
        os.mkdir(dir + f'passwords ({i})')
        dir += f'passwords ({i})\\'
    elif i == 1:
        os.mkdir(dir + f'passwords')
        dir += f'passwords\\'
    B = input("Whould you like to use your email address\n[1] yes\n[2] no\n>")
    
    if B == '1':
        email = input("enter your email address\n>")
        doc = f'email: {email}\n'+'password: '+pass_
        i = 1
        if os.path.exists(dir + f'password.txt'):
            i += 1
        while os.path.exists(dir + f'password ({i}).txt'):
            i += 1
        if i > 1:
            file = open(dir + f'password ({i}).txt', 'x')
            with open(dir + f'password ({i}).txt', 'w') as f:
                f.write(doc)
        elif i == 1:
            file = open(dir + f'password.txt', 'x')
            with open(dir + f'password.txt', 'w') as f:
                f.write(doc)
        
    elif B == '2':
        doc = 'password: '+pass_
        file = open(dir+'password.txt', 'x')
        with open(dir+'password.txt', 'w') as f:
            f.write(doc)
    else:
        print('I don\'t understand redebug the program')

    
        
except ValueError as v:
    if str(v) == 'probabilities do not sum to 1':
        print('make sure that all of your procents equal to 100%')