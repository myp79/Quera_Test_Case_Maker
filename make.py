import shutil
import os

current_dir = os.getcwd()
test_path = os.path.join(current_dir, 'Test')


def makeinput(num):
    '''
    Make inpput testcase file
    '''
    full_path = os.path.join(test_path, 'in')
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    os.chdir(full_path)
    with open('input%d.txt' % (num), 'w') as f:
        pass
    f.close()


def makeoutput(num):
    '''
    Make output testcase file
    '''
    full_path = os.path.join(test_path, 'out')
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    os.chdir(full_path)
    with open('output%d.txt' % (num), 'w') as f:
        pass
    f.close()


def main():
    '''
    This is the main of our program
    '''
    num = int(input('How many test case do you need? \n'))
    try:
        for i in range(1, num+1):
            makeinput(i)
            makeoutput(i)
    except FileExistsError:
        print('File Exist, Do you wanna delete it? [y/n]')
        if input() == 'y':
            shutil.rmtree('Test')
            main()
        else:
            exit()


if __name__ == '__main__':
    main()

# Mohammad YousefiPour - Github.com/myp79
