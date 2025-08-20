"""
Solves Game 24 - https://en.wikipedia.org/wiki/24_(puzzle)
"""

stack = []


class SolvedException(Exception):
    pass


def solve(arr):
    if len(arr) == 1:
        if arr[0] == 24 or abs(24 - arr[0]) < 0.5:
            raise SolvedException(arr[0], stack)
        return

    for pair in pickPairCombination(arr):
        a, b = pair[0], pair[1]
        for opRes in getOperatedResult(a, b):
            numb2 = arr.copy()
            numb2.remove(a)
            numb2.remove(b)
            numb2.append(opRes[0])
            stack.append((str(a), opRes[1], str(b), str(opRes[0]), 0))
            solve(numb2)
            stack.pop()

        # reversed order
        a, b = pair[1], pair[0]
        for opRes in getOperatedResult(a, b):
            numb2 = arr.copy()
            numb2.remove(a)
            numb2.remove(b)
            numb2.append(opRes[0])
            stack.append((str(a), opRes[1], str(b), str(opRes[0]), 1))
            solve(numb2)
            stack.pop()


def getOperatedResult(a, b):
    for op in ['+', '-', '*', '/']:
        if op == '+':
            app = a + b
        elif op == '-':
            app = a - b
        elif op == '*':
            app = a * b
        elif op == '/':
            if b == 0:
                continue
            app = a / b
        yield app, op


def pickPairCombination(arr):
    for x in range(len(arr)):
        for y in range(len(arr)):
            if y <= x:
                continue
            yield arr[x], arr[y]


def formatSolution(stack):
    if len(stack) == 0:
        return ''
    lastEntry = stack.pop()

    if len(stack) == 0:
        prevEntry = None
    else:
        prevEntry = stack[-1]

    if prevEntry:
        if lastEntry[0] == prevEntry[3]:
            return '(' + formatSolution(stack) + lastEntry[1] + lastEntry[2] + ')'
        else:
            return '(' + lastEntry[0] + lastEntry[1] + formatSolution(stack) + ')'
    else:
        return '(' + lastEntry[0] + lastEntry[1] + lastEntry[2] + ')'


if __name__ == '__main__':
    series = input("Enter number series (separated by comma):")
    numb = [int(x) for x in series.split(",")]
    print("Solve: ", numb)
    try:
        solve(numb)
    except SolvedException as ex:
        print("Solution:", ex.args[1])
        print(formatSolution(ex.args[1]))
