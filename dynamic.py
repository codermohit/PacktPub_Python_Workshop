stored_results = {}
def sum_to_n(n):
    result = 0
    for i in reversed(range(n)):
        result += i + 1
    stored_results[n] = result
    print(result)

stored_results = {}
def sum_to_n(n):
    result = 0
    for i in reversed(range(n)):
        if i + 1 in stored_results:
            print('Stopping sum at %s because we have previously computed it' % str(i + 1))
            result += stored_results[i + 1]
            break
        else:
            result += i + 1
    stored_results[n] = result
    print(result)

sum_to_n(5)
sum_to_n(6)
