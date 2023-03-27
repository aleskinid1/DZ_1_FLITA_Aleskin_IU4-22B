from time import sleep
first = []
second = []
a=1
while a != 0:
    print('You have 4 moves: ')
    
    print('1. Input')
    
    print('2. Output')

    print('3. Addition')
    
    print('4. Deleting')
    
    move = input('What move you prefer? If you want to stop, print "Stop". ')


    if move == 'Stop':
        a-=1
   
   
    elif move == 'Input':
        que = input('Choose multitude (first or second): ')
        if que == 'first':
            first.clear()
            b=1
            while b !=0 :
                pr = (input('Input: '))
                if pr == '0':
                    b-=1
                else :
                    if pr not in first:
                       first.append(pr) 
                    else:
                        print('Such element is already in', que)
                                              
        elif que == 'second':
            second.clear()
            b=1
            while b !=0 :
                pr = (input('Input: '))
                if pr == '0':
                    b-=1
                else :
                    if pr not in second:
                       first.append(pr) 
                    else:
                        print('Such element is already in', que)
        else: 
            print('invalid multitude')
            sleep(3)
    

    elif move == 'Output':
        que = input('Choose multitude (first or second): ')
        if que == 'first':
            print(first)
            sleep(3)
        elif que == 'second':
            print(second)
            sleep(3)
        else: 
            print('invalid multitude')
            sleep(3)


    elif move == 'Addition':
        que = input('Choose multitude (first or second): ')
        if que == 'first':
            pr = (input('Input: '))
            if pr not in first:
                first.append(pr) 
            else:
                print('Such element is already in', que)
        elif que == 'second':
            pr = (input('Input: '))
            if pr not in first:
                second.append(pr) 
            else:
                print('Such element is already in', que)
        else: 
            print('invalid multitude')
            sleep(3)

    
    elif move == 'Deleting':
        print('You can delete specific element or clear multitude')
        if input('Choose multitude (first or second): ') == 'first':
            if input('Clear/Delete: ') == 'Clear':
                first.clear()
            elif input('Clear/Delete: ') == 'Delete':
                try:
                    first.remove(input('what element do you want to delete: '))
                except ValueError:
                    print('There is not such element. Try later.')
                    sleep(3)
            else:
                print('invalid instruction')
                sleep(3)
        
        
        elif input('Choose multitude (first or second): ') == 'second':
            if input('Clear/Delete: ') == 'Clear':
                second.clear()
            elif input('Clear/Delete: ') == 'Delete':
                try:
                    second.remove(input('what element do you want to delete: '))
                except ValueError:
                    print('There is not such element. Try later.')
                    sleep(3)
            else:
                print('invalid instruction')
                sleep(3)





