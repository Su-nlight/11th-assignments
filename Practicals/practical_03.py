def listisequal(list1,list2):
    list1=sorted(list1) 
    list2=sorted(list2) 
    if list1 == list2:
        response=True
    else:
        response=False
    return response
