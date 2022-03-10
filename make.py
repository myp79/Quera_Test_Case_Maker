import shutil
import os
import glob

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


# def makeinput(num, *args):
#     '''
#     Make intput files for testcases. `num` is use for number of files.
#     '''
#     full_path = os.path.join(current_dir, 'in')
#     os.mkdir(full_path)
#     os.chdir('in')
#     print()
#     with open('input%d.txt' % (num), 'w') as f:
#         for items in args:
#             if isinstance(items, list):
#                 f.write('\n')
#                 for item in items:
#                     f.write(item)
#             else:
#                 f.write(items)
#     f.close()


# def makeoutput(num, answer):
#     '''
#     Make output files for testcases. `num` is use for number of files.
#     '''
#     full_path = os.path.join(current_dir, 'out')
#     os.mkdir(full_path)
#     os.chdir(full_path)
#     with open('output%d.txt' % (num), 'w') as f:
#         f.write(answer)
#     f.close()

# def simplify(args: list):
#     '''
#     simplify the input for passing to file
#     '''
#     for i in range(len(args)):
#         if isinstance(args[i], list):
#             args.insert(i, '\n')
#             args[i] = ' '.join(args[i])
#     return ' '.join(args)

# def execute_file(file, args: list):
#     '''
#     Execute your answer/code and test with testcases.
#     '''
#     args = simplify(args)
#     index = file.rfind('.')
#     ext = file[index:]
#     if ext == '.py':
#         command_list = ['python', file]
#         complete = subprocess.run(
#             command_list, input=args, capture_output=True)
#         return complete.stdout.decode()


def get_input():
    '''
    Get input of program for save in input file and execute for output.
    '''
    input_list = []
    while True:
        print('Pass your inputs:')
        input_list.append(input())
        print('Any other input? [y/n]')
        if input() == 'n':
            break
    return input_list


def main():
    '''
    This is the main of our program
    '''
    # print('\n---------Files---------\n')
    # files_list = [i for i in glob.glob(r'*.py') if i != 'make.py']
    # print(files_list)
    # print('\n---------Code---------\n')
    # file = input('Choose your code/answer? \n')
    print('\n---------Test---------\n')
    num = int(input('How many testcases do you need? \n'))
    try:
        for i in range(1, num+1):
            # input_list = get_input()
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
