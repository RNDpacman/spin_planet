import planet
import time

def clear_screen():
    '''
    Clears the screen
    '''
    print('\033[2J')

def move_cursor(right=0, left=0, up=0, down=0):
    '''
    Moves the cursor in a given direction
    '''
    if up: print(f'\u001b[{up}A')
    elif down: print(f'\u001b[{right}B')
    elif right: print(f'\u001b[{right}C')
    elif left: print(f'\u001b[{left}D')

def print_colored(color: str, string: str, **kargs):
    '''
    Prints color text
    Colors: black, red, green, yellow, blue, dark blue, white, purple
    '''
    colors = {'black': '30',
              'red': '31',
              'green': '32',
              'yellow': '33',
              'dark blue': '34',
              'purple': '35',
              'blue': '36',
              'white': '37',
              'reset': '0'
             }

    print(f'\u001b[{colors[color]}m', **kargs)
    print(string, **kargs)
    print(f"\u001b[{colors['reset']}m", **kargs)


def main():

    color = 'yellow'
    wait_str =  'Getting information from satellites '
    clear_screen()
    print('\n', wait_str, end='', sep='')

    for i in range(15):
        time.sleep(0.25)
        print('.', end='', flush=True)

    for frame in planet.frames:
        clear_screen()
        print_colored(color, frame, end='')
        time.sleep(1)
        move_cursor(up=26)
    else:
        clear_screen()
        print('THE END')

if __name__ == '__main__':
    main()
