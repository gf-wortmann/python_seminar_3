

from curses.ascii import isdigit


def IntCheckedInput (message:str) :
    while True:
        res = input(f'{message}: ')
        if res.isdigit():
            return int(res)
        print('Enter digits only, please!')

def IntCheckedInputLtd (message:str, max:int) :
    while True:
        res = input(f'{message}: ')
        if res.isdigit():
            if int(res)<int(max):
                return int(res)
            else:
                print(f'number must be less than {max}')
        else:
            print('Enter digits only, please!')        

def OneOrZero(messge:str):
    while True:
        res = input(f'{messge}: ')
        if res == '1' or res == '0':
            return res
        print('Enter "1" or "0", please')
