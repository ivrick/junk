from time import perf_counter

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def shift_string(string: str) -> str:
    start_time = perf_counter()
    stack = [letter for letter in string]
    stack = stack[::-1]
    if stack[0] != 'Z':
        stack[0] = ALPHABET[(ALPHABET.index(stack[0]) + 1) % 26]
        return ''.join(stack[::-1]) + f' <= {((perf_counter() - start_time) * 1000).__round__(4)} ms'
    for index, item in enumerate(stack):
        try:
            if stack[index] == 'Z' and stack[index + 1] == 'Z':
                stack[index] = 'A'
                continue
            elif stack[index] == 'Z' and stack[index + 1] != 'Z':
                stack[index] = 'A'
                stack[index + 1] = ALPHABET[(ALPHABET.index(stack[index + 1]) + 1) % 26]
        except IndexError:
            stack[index] = 'A'
            stack.append('A')

    return ''.join(stack[::-1]) + f' <= {((perf_counter() - start_time) * 1000).__round__(4)} ms'


while True:
    global_start_time = perf_counter()
    string = input('Enter a string or press Enter to finish: ')
    if string == '':
        print(f'Total runtime: {((perf_counter() - global_start_time) * 1000).__round__(4)} ms')
        break
    print(shift_string(string))