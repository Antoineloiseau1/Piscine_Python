def NULL_not_found(object: any) -> int:
	if (type(object) is float and object != object):
		print("Cheese:", "nan", type(object))
		return 0
	null_types = {int: ["Zero:", 0], bool: ["Fake:", False], type(None): ["Nothing:", None], str: ["Empty:", ""]}
	for i in null_types:
		if(i is type(object) and (null_types[i][1] == object)):
				print(null_types[i][0], null_types[i][1], type(object))	
				return (0)
	print("Type not found")
	return 1