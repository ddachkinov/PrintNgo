import os

file_list = os.listdir("C:/Python27/Programs/PrintNgo/Files2print")
print ("List of available documents to print" '\n')
enum_list = ('\n'.join('{}: {}'.format(*k) for k in enumerate(file_list)))
print(enum_list)

while True:
   try:
      user_choice = int(input('\n' "Documents # you want to print: "))
   except ValueError:
            print("Sorry, that isn't a valid choice")
            continue
   else:
      break
   if user_choice >= 0:
      print (file_list[user_choice])
      #os.startfile("C:/Python27/Programs/PrintNgo/Files2print/doc0.docx", "print")
   else:
      print ("This # does not reffer to a document")

print(file_
