# def recursion():
#     num = int(input())
#     b = 1
#     a = 1
#     if num == 0:
#         print(1)
#     else:    
#         for i in range(num):
#             a = a*b
#             b += 1
#         print(a)

# recursion()

counting = 0
def apple(x,a,b,c):
    global counting
    # counting +=1
    if x == 1:
        counting +=1
        print(f"{a} - {c}")
    else:
        apple(x-1,a,c,b)
        apple(1,a,b,c)
        apple(x-1,b,a,c )

result = apple(4,"a","b","c")
print(counting)

