args = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

def main():
    arithmetic_arranger(args)

def arithmetic_arranger(args):

    first_numbers = ''
    second_numbers = ''
    length1 = 0
    dashes = ''

    if len(args) > 5:
        print('Error: Too many problems.')
        return

    for problem in args:
        if '*' in problem or '/' in problem:
            print("Error: operator must be '+' or '-'.")

    for problem in args:
        prob = problem.split()
        length1 = max(len(number) for number in prob)
        for number in prob:
            dash = '-'*(length1 + 2) + '    '
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

        num1 = str(prob[0])
        op = str(prob[1])
        num2 = str(prob[2])

        correct1 = f"{num1: >{length1 + 2}}" + '    '
        correct2 = op + ' ' + f"{num2: >{length1}}" + '    '

        first_numbers += correct1
        second_numbers += correct2
        dashes += dash

    print(first_numbers)
    print(second_numbers)
    print(dashes)

if __name__ == '__main__':
    main()
