#
#       Daniel Warren
#       Python version: 3.9
#
#       Task:
#       Find PI to the Nth Digit - Enter a number and have the program generate PI up to that
#       many decimal places. Keep a limit to how far the program will go.
#

def main():  

    #loop while num not valid
    valid = False
    while(not valid):

        # try/catch for input validation
        try:
            # get input num & set num max
            pi = int(input("Enter the number of decimals to calculate pi to: "))
            limit = 2000

            # check num valid
            if (pi <= limit and pi > 0):
                pi = calcPi(pi)
                
                # print pi to user's num choice 
                i = 0
                for i in pi:
                    print(i, end='')
                valid = True

            # check num not valid
            elif (pi > limit or pi <= 0):
                print("Please enter a VALID and WHOLE number below 2000.")
                valid = False
        except:
            print("Please enter a VALID and WHOLE number below 2000.")
            valid = False

# use leibniz-formula to calc
def calcPi(num):  
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

    dec = num
    i = 0

    # first pass sets single digit value and function iterates through adding
    # the next value in the sequence each time
    while i != dec + 1:
            if 4 * q + r - t < n * t:
                    yield n
                    if i == 0:
                            yield '.'
                    if dec == i:
                            print('')
                            break
                    i += 1
                    nr = 10 * (r - n * t)
                    n = ((10 * (3 * q + r)) // t) - 10 * n
                    q *= 10
                    r = nr
            else:
                    nr = (2 * q + r) * l
                    nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
                    q *= k
                    t *= l
                    l += 2
                    k += 1
                    n = nn
                    r = nr

if __name__ == '__main__':
    main()
