import shutil
import os



class TestMaker:
    current_dir = os.getcwd()
    test_path = os.path.join(current_dir, 'Test')
    
    def exist_folder(self):
        '''
        Check Test folder is Exist.
        '''
        if os.path.exists(TestMaker.test_path):
            raise FileExistsError

    def makeinput(self,num):
        '''
        Make inpput testcase file
        '''
        full_path = os.path.join(TestMaker.test_path, 'in')
        if not os.path.exists(full_path):
            os.makedirs(full_path)
        os.chdir(full_path)
        with open('input%d.txt' % (num), 'w') as f:
            pass
        f.close()

    def makeoutput(self,num):
        '''
        Make output testcase file
        '''
        full_path = os.path.join(TestMaker.test_path, 'out')
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
    test=TestMaker()
    try:
        test.exist_folder()
        num = int(input('How many test case do you need? \n'))
        for i in range(1, num+1):
            test.makeinput(i)
            test.makeoutput(i)
        print('Done')
        command=input('Enter to Continue :)')
        if command=='\n':
            exit()
    except FileExistsError:
        print('File or Directory Exist, Do you wanna delete it? [y/n]')
        if input() == 'y':
            shutil.rmtree('Test')
            main()
        else:
            exit()

if __name__ == '__main__':
    main()

# Mohammad YousefiPour - Github.com/myp79
