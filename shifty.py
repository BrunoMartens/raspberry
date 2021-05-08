def setShiftRegister(value):
    print(value)
    print("-------------------------------")
    pinValues = [1,2,4,8,16,32,64,128]
    for x in range(8):
        print(pinValues[x])
        print(pinValues[x] == value & pinValues[x])

for i in range(255):
    setShiftRegister(i)


