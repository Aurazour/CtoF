# I got tired of having to constantly look up a converter so I made a project I can simply have on hand
# This is no different from having a search tab open


def convertFtoC(val):
    result = (val - 32) * (5/9)
    print("Converting fahrenheit to celsius")
    return result

def convertCtoF(val):
    result = val * (9/5) + 32
    print("Converting celsius to fahrenheit")
    return result


if __name__ == '__main__':
    #set these to the value you want to convert
    cel = 25
    fa = 65
    #result = convertCtoF(cel)
    result = convertFtoC(fa)
    print(result)
