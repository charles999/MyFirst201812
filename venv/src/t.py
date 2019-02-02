
variable1 = "hello world";
print(variable1)


def  xxxfff(num1,num2):
    return num1 + num2

numbers = [11, 22, 33, 100, 200, 300]


def numberfind(numbers, target):
    i = len(numbers)
    for x in (0,i - 1):
        for y in (0,i-1):
            if x != y :
                count = numbers[x] + numbers[y]
                if(count == target):
                    return [x,y]



#print(len(numbers))

#x = input(" input a number")

#print("the number been input is []", x)


def  addBinary(a,b):
    return bin(a + b)[2:]

print(addBinary(1,2))



