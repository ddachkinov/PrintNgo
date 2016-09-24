import os

file_list = os.listdir("C:/Python27/Programs/PrintNgo/Files2print")
print ("List of available documents to print" '\n')

enum_list = ('\n'.join('{}: {}'.format(*k) for k in enumerate(file_list)))
print(enum_list)

user_choice = input('\n' "Documents # you want to print: ")
copies = input("How many copies would you like from each: ")

current_choice = file_list[user_choice]
current_file = os.startfile("C:/Python27/Programs/PrintNgo/Files2print/"+current_choice, "print")

