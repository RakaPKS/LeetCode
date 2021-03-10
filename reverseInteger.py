def reverse(x: int) -> int:
        inputHead, *inputString = str(x)
        if inputHead == "-":
            outputInt =int("-" + "".join(str(a) for a in inputString)[::-1])
            return outputInt if checkInt(outputInt) else 0
        else:
            outputInt = int (str(x)[::-1])
            return outputInt if checkInt(outputInt) else 0

def checkInt(x:int) -> bool:
    return x > -2**31 and x<2**31-1
        