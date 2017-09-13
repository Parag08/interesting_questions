import sys
import os
import tty,termios
import time
import random

done = 25
score = 0
width = 30
height = 30
path = '    '
car = 'II'
level = '@'*((width-len(path))/2) + path +  '@'*((width-len(path))/2)
initialdesign = (level + '\n') * height


class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def clear():
    os.system( 'clear' )

def designBoard(width,heigth,pos):
    global score
    global  initialdesign
    score = score + 1
    choice = ['right','left']
    levels = initialdesign.split('\n')
    baselevel = levels[heigth-2]
    baselevel = baselevel[0:pos] + car + baselevel[pos+len(car):]
    del levels[heigth-1]
    del levels[heigth-2]
    move = random.choice(choice)
    level = levels[0]
    print('score:',score)
    if move == 'right' and levels[0][-1] != path[0]:
        level = '@' + level[0:-1]
    elif  move == 'right' and levels[0][-1] == path[0]:
        level =  level[1:] + '@'
    elif move == 'left' and  levels[0][0] != path[0]:
        level =  level[1:] + '@'
    elif move == 'left' and  levels[0][0] == path[0]:
        level = '@' + level[0:-1]
    else:
        level = level
    levels.insert(0,level)
    levels.insert(-1,baselevel)
    string = '\n'.join(levels)
    initialdesign = string
    print(string)


def draw(pos):
    levels = initialdesign.split('\n')
    safeArea = levels[-2].replace('I',' ').find(' ')
    print('pos',pos,'safeArea',safeArea,'string:',levels[-2],safeArea + len(path))
    if pos < safeArea:
        return False
    elif pos > safeArea + len(path) -2:
        return False
    else:
        designBoard(width,height,pos)
        return True


def userinput():
    inkey = _Getch()


def play():
    inkey = _Getch()
    pos = width/2
    starttime=time.time()
    while True:
        k=inkey()
        if k=='\x1b[A':
            print "increasing speed up"
        elif k=='\x1b[B':
            print "decreasing speed down"
        elif k=='\x1b[C':
            print "turning right"
            pos  =  pos + 1
        elif k=='\x1b[D':
            print "turning left"
            pos = pos - 1
        else:
            print "not an arrow key!"
            break
        clear()
        result = draw(pos)
        if not result:
            print("game over\n","score:",score)
            break

if __name__ ==  '__main__':
    print("hi")
    play()
