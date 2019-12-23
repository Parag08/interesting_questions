n = int(input())


if (n%10 == 6) and (int(n/10)%2 == 0):
    print(((n-n%10)/2)/10 + 1)
elif (n%10 == 9) and (int(n/10)%2 == 0):
    print(((n-n%10)/2)/10 + 1)
elif (n%10 == 5) and (int(n/10)%2 ==1):
    print(((n -n%10)/2)/10 + 2 - 0.5)
elif (n%10 == 0) and (int(n/10)%2 == 0):
    print(((n - n%10)/2)/10)
else:
    print("NONE")
