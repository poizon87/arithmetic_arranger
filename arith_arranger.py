args = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

def main():
    arithmetic_arranger(args)

def arithmetic_arranger(args):

    first_numbers = ''
    second_numbers = ''
    x = 6
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

        num1 = str(prob[0])
        op = str(prob[1])
        num2 = str(prob[2])

        #for number in prob:
            #dash = max(prob)
        correct1 = f"{num1: >{x}}" + '    '
        correct2 = op +' '+ f"{num2: >4}" + '    '
        #right_align = (f"{num1: >6}\n{op: <} {num2: >4}\n")

        #print(right_align)
        #print(dash)
        #print(correct)

        first_numbers += correct1
        second_numbers += correct2

    print(first_numbers)
    print(second_numbers)

if __name__ == '__main__':
    main()
