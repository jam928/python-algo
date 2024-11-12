
# https://leetcode.com/problems/basic-calculator/description/
# https://leetcode.com/problems/basic-calculator-ii/
class BasicCalculator:
    def calculate_I(self, s: str) -> int:
        # keep track of the sign
        sign = 1

        # use stack while in parentheses
        stack = []

        total_sum = i = 0

        s = s.strip()
        while i < len(s):
            c = s[i]

            match c:
                case c if c.isdigit():
                    num = 0

                    while i < len(s) and s[i].isdigit():
                        num = num * 10 + ord(s[i]) - ord('0')
                        i += 1

                    i -= 1
                    total_sum += num * sign  # accumulate total sum with the current num * sign
                case '+':
                    sign = 1
                case '-':
                    sign = -1
                case '(':
                    stack.append(total_sum)
                    stack.append(sign)

                    # reset sign and sum for the next sum and sign
                    sign = 1
                    total_sum = 0
                case ')':
                    total_sum = total_sum * stack.pop()  # for the sign if 1 or -1
                    total_sum += stack.pop()  # add last recorded total sum
            i += 1

        return total_sum

    def calculate_II(self, s: str) -> int:
        multiply_division = -1
        sign = 1
        prev = total_sum = 0

        i = 0
        s = s.strip()
        while i < len(s):
            c = s[i]
            match c:
                case c if c.isdigit():
                    num = 0
                    while i < len(s) and s[i].isdigit():
                        num = num * 10 + ord(s[i]) - ord('0')
                        i += 1
                    i -= 1

                    match multiply_division:
                        case 0:
                            prev = num * prev
                            multiply_division = -1
                        case 1:
                            prev = prev // num
                            multiply_division = -1
                        case _:  # default case
                            prev = num
                case '*':
                    multiply_division = 0
                case '/':
                    multiply_division = 1
                case '+':
                    total_sum += prev * sign
                    sign = 1
                case '-':
                    total_sum += prev * sign
                    sign = -1
            i += 1

        total_sum += sign * prev
        return total_sum

    # https://leetcode.ca/2018-01-10-772-Basic-Calculator-III/
    def calculate_III(self, s: str) -> int:
        if not s:
            return 0

            # Remove leading and trailing spaces and white spaces.
        s = ''.join(s.split())

        if not s:
            return 0

        op_stack = []
        num_stack = []

        def perform_calculation():
            num2 = num_stack.pop()
            num1 = num_stack.pop()
            op = op_stack.pop()

            if op == '+':
                num_stack.append(num1 + num2)
            elif op == '-':
                num_stack.append(num1 - num2)
            elif op == '*':
                num_stack.append(num1 * num2)
            elif op == '/':
                num_stack.append(num1 // num2)

        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                num_stack.append(num)
            else:
                op = s[i]
                if not op_stack:
                    op_stack.append(op)
                    i += 1
                elif op == '+' or op == '-':
                    while op_stack and op_stack[-1] != '(':
                        perform_calculation()
                    op_stack.append(op)
                    i += 1
                elif op == '*' or op == '/':
                    top = op_stack[-1] if op_stack else None
                    if top in ('*', '/'):
                        perform_calculation()
                    op_stack.append(op)
                    i += 1
                elif op == '(':
                    op_stack.append(op)
                    i += 1
                elif op == ')':
                    while op_stack[-1] != '(':
                        perform_calculation()
                    op_stack.pop()
                    i += 1

        while op_stack:
            perform_calculation()

        return num_stack[-1]

if __name__ == '__main__':
    basic_calculator = BasicCalculator()
    arr = ["3+2*2", " 3/2 ", " 3+5 / 2 "]
    for i in arr:
        print(basic_calculator.calculate_II(i)) # 7,1,5

    print('\n')
    arr2 = ["1 + 1", " 2-1 + 2 ", "(1+(4+5+2)-3)+(6+8)"] # 2, 3, 23
    for i in arr2:
        print(basic_calculator.calculate_I(i))

    arr3 = ["1 + 1", " 6-4 / 2 ", "2*(5+5*2)/3+(6/2+8)", "(2+6* 3+5- (3*14/7+2)*5)+3"] # 2, 4, 21, -12
    for i in arr3:
        print(basic_calculator.calculate_III(i))