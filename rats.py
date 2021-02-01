import numpy as np


def f(n, k):
    # Loop to iterate over all rats and point what is the perfect start
    for i in range(n):
        print(i)
        # Array of mouses
        rats = np.array([i for i in range(n)])
        number_of_rats = n

        # First mouse is the ith iteration
        first_mouse = i
        counter = first_mouse

        # If white mouse is dead, end the loop
        while rats[0] == 0:
            if len(rats) == 1 and rats[0] == 0:
                print(f"\nRat found!\nConfiguration: f({n},{k})\nRat number: {first_mouse} after the white one (clockwise)")
                exit(0)

            elif len(rats) == 1 and rats[0] != 0:
                print("Leave")
                break

            counter += k-1
            rats = np.delete(rats, counter % number_of_rats)
            counter = counter % number_of_rats
            number_of_rats -= 1
            print(rats)


print("Function f(n,k)")
n = int(input("Select n: "))
k = int(input("Select k: "))
f(n, k)
