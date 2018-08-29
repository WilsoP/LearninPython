print("Maths")

number = 1 + 2 * 3 /4.0
print(number)

remainder = 11%3
print remainder

squared = 7**2
cubed = 2**3

print(squared)
print(cubed)

print("")

print("Strings")

helloworld = "hello" + " " + "world"
print(helloworld)


print("")
print("Lists")
evenNumbers = [2,4,6,8]
oddNumbers = [1,3,5,7]

allNumbers = oddNumbers + evenNumbers
print(allNumbers)

numberOrder = []
counter = 1

for y in allNumbers:
    for x in allNumbers:
        if x == counter:
            numberOrder.append(x)
            counter = counter + 1

print(numberOrder)

print([1,2,3]*3)

x = object()
y = object()


xList = [x]*10
yList = [y]*10

bigList = xList + yList

print("X list contains %d objects" % len(xList))
print("Y list contains %d objects" % len(yList))
print("Big List contains %d objets" % len(bigList))

if xList.count(x) == 10 and yList.count(y) == 10:
    print("x list and y list correct size")

if bigList.count(x) == 10 and bigList.count(y) == 10:
        print("Big list correct size")
