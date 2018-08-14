print("Hello World!")

x = 0
if x == 1:
    print("x = 1")
if x != 1:
    print("x don't = 1")

print("")

print("int")
myint = 7
print(myint)

print("")

print("float")
myfloat = 7.9
print(myfloat)
myfloat = float(7.5)
print(myfloat)

print("")

print("string")
mystring1 = 'hello'
print(mystring1)
mystring2 = "world"
print(mystring2)
mystring = mystring1 + " " + mystring2
print(mystring)
mystring = "SSSS'A"
print(mystring)
stringA, stringB = "gryff","dogg"
gdog = stringA + " " + stringB
print(stringA," ",stringB)
print(gdog)
a,b = 3,4
print(a,b)
print a,b
print a + b

print""
print"Excersize"
eString = "hello"
eFloat = 10.0
eInt = 20

if eString == "hello":
    print("String: %s" % eString)
if isinstance(eFloat, float) and eFloat == 10.0:
    print("Float : %f" % eFloat)
if isinstance(eInt, int) and eInt == 20:
    print("Int : %d" % eInt)
