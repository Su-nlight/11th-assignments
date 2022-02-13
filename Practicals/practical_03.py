def listisequal(list1,list2):
    if list1.sorted() == list2.sorted():
        response=True
    else:
        response=False
    return response
