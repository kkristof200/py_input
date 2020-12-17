from kinput import input

result, error = input("What's your age?", default=19, type=int)

print(result, error)