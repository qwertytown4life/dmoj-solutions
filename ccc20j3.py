XQ = 0
YQ = 0
amount_of_coords = int(input())

XQ, YQ = map(int, input().split(','))

biggestX = XQ
biggestY = YQ
smallestX = XQ
smallestY = YQ

while amount_of_coords != 1:
    XQ, YQ = map(int, input().split(','))

    if XQ < smallestX:
        smallestX = XQ
    else:
        smallestX = smallestX

    if YQ < smallestY:
        smallestY = YQ
    else: smallestY = smallestY


    if XQ > biggestX:
        biggestX = XQ
    else:
        biggestX = biggestX

    if YQ > biggestY:
        biggestY = YQ
    else:
        biggestY = biggestY

    amount_of_coords -= 1
print(f"{smallestX - 1},{smallestY - 1}")
print(f"{biggestX + 1},{biggestY + 1}")
