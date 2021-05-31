import random
import os
import json
import time

clear = lambda: os.system('cls')

def data(funct,key,value):
    directory = 'records.json'
    with open(directory, 'r') as file:
        if funct == 'load':
            r = json.loads(file.read())
            return str(r[key])
        elif funct == 'save':
            w = json.load(file)
            w[str(key)] = int(value)
            with open(directory, 'w') as file:
                json.dump(w, file, indent=2)
        else:
            print("ERROR PLEASE REEBOT THE CODE")

def run():
    clear()
    replay = True
    while replay == True:
        print('Randon Number is generating...')
        time.sleep(2)
        clear()
        print('Lets go')
        time.sleep(1)
        clear()
        random_number = random.randint(1, 100)
        record = int(data('load','record','nn'))
        print("The record is: " + str(record))
        time.sleep(1)
        print("The last Attempt is: " + str(data('load','last','nn')))
        time.sleep(1.25)
        selected_number = int(input('Select a number from 1 and 100: '))
        time.sleep(0.5)
        counter = 1
        while selected_number != random_number:
            time.sleep(0.5)
            if selected_number < random_number:
                print('Look for a bigger number')
                counter +=1
            else:
                print('Look for a smaller number')
                counter +=1
            time.sleep(0.5)
            selected_number = int(input('Select other number: ')) 
        time.sleep(0.5)
        if counter == 1:
            print("Congratulations you won in the first attempt")
        else:
            print('You won in ' + str(counter) + ' attempts!')
        data('save','last',counter)
        if counter < record:
            data('save','record',counter)
            pass
        data('save','last',counter)
        print('Do you want play again? (y/n)')
        choise = input()
        if choise == 'n':
            replay = False
        elif choise != 'n' and choise != 'y':
            print('System Error 378 (The player is Stupid)')
            replay = False
        else:
            time.sleep(2)
            clear()
    clear()
    time.sleep(2)
    print('Thank you so much a-for-to playing my game!')
    time.sleep(2)
    clear()
        
        
if __name__ == '__main__':
    run()  
