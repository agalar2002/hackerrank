n = int(input())
if 1 <= n <= 100:
    if n % 2 == 1:
        print('Weird')
    if n % 2 == 0:
        if 2 <= n < 5:
            print('Not Weird')
        elif 6 <= n <= 20:
            print('Weird')
        else:
            print('Not Weird')
