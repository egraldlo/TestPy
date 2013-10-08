'''
Created on 2013-9-24

@author: casa
'''

print 'hello'
running = True;

while running:
    guess=int(raw_input('enter a integer'))
    if guess == 2:
        print 'ok'
    elif guess == 4:
        continue
    else:
        break
    for i in range(1, guess):
        print 'ok'
    else:
        print 'the loop is over'
print 'done'

def sayhello():
    print 'hello def'

sayhello()

def printmax(x,y):
    if x > y:
        print 'x>y'
    else:
        print 'x<y'

printmax(3, 4)

x = 9
y = 8
printmax(x, y)

def say(message, times=1):
    print message * times

say('hello')
print '-----------------'
say('hello',5)

def printmin(x, y=1):
    if x > y:
        print 'x>y'
    else:
        print 'x<y'
printmin(x=2, y=3)
printmin(x=6, y=3)
printmin(x=3)
