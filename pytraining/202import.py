# # style 1
# from modules.my_module import addStuff

# if __name__ == "__main__":
#     print (addStuff(1,2))


# # style 2
# from modules import my_module

# if __name__ == "__main__":
#     print (my_module.addStuff(2,3))


# # style 3
# import modules.my_module as m

# if __name__ == "__main__":
#     print (m.addStuff(3,5))


from modules import sanitize as s

name = "mr tushar mathur"
print(s.cleanup(name))
