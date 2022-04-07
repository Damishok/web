'''
n = int(raw_input())
if n%2==0 and (n in range(2,6) or n>20 ):
    print "Not",
print "Weird"
'''


'''
print("Hello world!")
'''

'''
a = int(input())
b = int(input())
print('{0} \n{1} \n{2}'.format((a + b), (a - b), (a * b)))
'''

'''
n = int(input())
    for i in range(0,n):
        print(i*i)
'''


'''
def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
'''


'''
print(*range(1, int(input())+1), sep='')
'''


'''
n = int(raw_input())
nums = map(int, raw_input().split())	
print sorted(list(set(nums)))[-2]
'''


'''
student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    query_scores = student_marks[query_name]
    print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))
'''


'''
def swap_case(s):
    return s.swapcase()
'''


'''
s = raw_input()
i, c = raw_input().split()
print s[:int(i)] + c + s[int(i)+1:]
'''


'''
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count
'''