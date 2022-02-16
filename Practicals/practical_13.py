def highest(diction):
    if type(diction)==dict:
        temp=sorted(diction.values())
        high1=temp[-1]
        high2=temp[-2]
        return high1,high2
    else:
        raise TypeError
#provide dictionary to this function
