n = int(input())
answer = []
for i in range(n+1):
    if i != 0:
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(f"{i}")

print(answer)