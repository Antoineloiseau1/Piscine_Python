ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#modify list
ft_list[1] = "World"

#modify tuple
tmp = list(ft_tuple)
tmp[1] = "France"
ft_tuple = tuple(tmp)

#modify set
ft_set.remove("tutu!")
ft_set.add("Nice")

#modify dictionary
#ft_dict.update({"Hello": "42Nice"})
ft_dict["Hello"] = "42Nice"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)