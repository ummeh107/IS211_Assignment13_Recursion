
def main():

    print("--Fibonnaci--")
    number = int(input("Enter Number : "))

    for i in range(number):
        result = fibonnaci(i)
    print(result)

    print("--GCD--")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(gcd(a,b))


    print("--Compare String--")
    s1 = input("Enter first string :")
    s2 = input("Enter second string :")
    print(comapreTo(s1, s2))


def fibonnaci(number):
    if number <= 1:
        return number
    else:    
        return fibonnaci(number-1) + fibonnaci(number-2)


def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)    


def comapreTo(s1, s2):
    if s1 == s2:
        return 0
    elif (len(s1) == 1 and len(s2) > 1):
        return  -ord(s2[0])
    elif (len(s1) > 1 and len(s2) == 1):
        return  ord(s1[0]) 
    elif ord(s1[0]) > ord(s2[0]):
        return ord(s1[0])
    elif ord(s1[0]) < ord(s2[0]):
        return -ord(s2[0])
    else:
        return comapreTo(s1[1:], s2[1:])    



if __name__ == "__main__":
    main()

    