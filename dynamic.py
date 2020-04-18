import time #Importing time module to calculate time taken to execute the code
stored_results = {}
def sum_to_n(n):
    result = 0
    for i in reversed(range(n)):
        result += i + 1
    stored_results[n] = result
    print(result)

stored_results = {}
def sum_to_n(n):
    start_time= time.perf_counter() #It notes the tiem at the start of execution
    result = 0
    for i in reversed(range(n)):
        if i + 1 in stored_results:
            print('Stopping sum at %s because we have previously computed it' % str(i + 1))
            result += stored_results[i + 1]
            break
        else:
            result += i + 1
    stored_results[n] = result
    #Writinng code to find the time taken by subrating it from time at the end
    print(time.perf_counter() - start_time, "seconds")
    print(result)

sum_to_n(5)
