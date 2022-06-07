args = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

def main():
    arithmetic_arranger(args)

def arithmetic_arranger(args):


    if len(args) > 5:
        print('Error: Too many problems.')
        return

    for problem in args:
        if '*' in problem or '/' in problem:
            print("Error: operator must be '+' or '-'.")

    for problem in args:
        prob = problem.split()
        
        for number in prob:
            if len(number) > 4:
                print("Error: Numbers cannot be more than four digits.")
                return

        for digit in prob[0]:
            if digit.isdigit() == False:
                print('Error: Numbers must only contain digits.')
                return
        for digit in prob[2]:
            if digit.isdigit() == False:
                print('Error: Numbers must only contain digits.')
                return

        num1 = int(prob[0])
        op = prob[1]
        num2 = int(prob[2])

        print(f'{num1}\n{op} {num2}') #for some reason if a number is too long it will print the previous numbers
                            #then it will print the error message, why is this?

if __name__ == '__main__':
    main()

