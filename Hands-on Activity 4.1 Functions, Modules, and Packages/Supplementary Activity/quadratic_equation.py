import math

def solve_quadratic(a, b, c):
    d = b*b - 4*a*c

    if d >= 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        answer = "Roots: " + str(x1) + " and " + str(x2)
    else:
        answer = "No real roots"

    # write to file
    file = open("output.txt", "w")
    file.write("a=" + str(a) + ", b=" + str(b) + ", c=" + str(c) + "\n")
    file.write(answer)
    file.close()

    return answer


# This is the test
print(solve_quadratic(1,-2, 1))