test_list = [{"id" : 1, "data" : "test data 1"},
			{"id" : 2, "data" : "test data 2"},
			{"id" : 3, "data" : "test data 3"}]

print ("The original list is : " + str(test_list))


for i in range(len(test_list)):
	if test_list[i]['id'] == 2:
		del test_list[i]
		break

print ("List after deletion of dictionary : " + str(test_list))