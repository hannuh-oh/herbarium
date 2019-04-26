import database



print('hello!')
# asks user for info, will later store it in database

def main():
    done = True
    x = 0
    while not done:
        x += 1
        if x > 4:
            done = True
    print(x, done)
    return done


if __name__ == '__main__':
    main()
else:
    print( "Hey I am in commandline.py and __name__ is ", __name__)



