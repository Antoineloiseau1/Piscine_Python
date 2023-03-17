def	all_thing_is_obj(object: any) -> int:
	types = {list: "List", tuple: "Tuple", dict : "Dict", set : "Set", str: "Str"}
	for i in types:
		if i is type(object):
			if (i is str):
				print(object, "is in the kitchen", type(object))
			else:
				print(types[i], ": ", type(object))
			return 42
	print("Type not found")
	return 42