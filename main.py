# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def choices ():
    print("enter 1 for phase voltage ")
    print("enter 0 for exit ")
def phase_V(voltage):
    offset=-882.35
    gain=0.43
    voltage=voltage/0.7071
    v = (voltage-offset)/gain
    return v


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        choices()
        n = int(input("Enter your choice or 0 for exit "))
        Res = []
        if n == 0:
            break
        numvalues = int(input("Enter number of values you need "))
        if numvalues == 0:
            break

        if n == 1:
            for i in range(numvalues):
                phaseAv = float(input(f"Enter value  {i + 1}: "))
                Res.append(phase_V(phaseAv))

            print(Res)


