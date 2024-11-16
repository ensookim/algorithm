people = int(input())
seat = input()
cupholder = seat.count('S') + seat.count('L') //2 +1
maxpeople = min(people,cupholder)
print(maxpeople)

