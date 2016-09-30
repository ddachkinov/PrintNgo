import os
from transliterate import translit

file_list = os.listdir("C:/Python27/Programs/PrintNgo/Files2print")
title_bg = u' \u0421\u041f\u0418\u0421\u042a\u041a \u041d\u0410 \u0414\u041e\u041a\u0423\u041c\u0415\u041d\u0422\u0418 \u0417\u0410 \u041f\u0415\u0427\u0410\u0422\u0415\u041d\u0415 '
choice_bg = u'\u041c\u043e\u043b\u044f, \u0432\u044a\u0432\u0435\u0434\u0435\u0442\u0435 \u043d\u043e\u043c\u0435\u0440\u0430 \u043d\u0430 \u0435\u0434\u0438\u043d \u043e\u0442 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0438\u0442\u0435 \u0437\u0430 \u043f\u0435\u0447\u0430\u0442: '

while True:   
    print (title_bg.center(78, '=')+'\n')
    enum_list = ('\n'.join('{}: {}'.format(*k) for k in enumerate(file_list)))
    print translit(enum_list, "bg")
    print '\n'
    print (choice_bg)
    user_choice = int(raw_input ("# "))
    copie_bg = (u'\u041a\u043e\u043b\u043a\u043e \u043a\u043e\u043f\u0438\u044f \u0436\u0435\u043b\u0430\u0435\u0442\u0435 \u043e\u0442 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442 \u0441 \u043d\u043e\u043c\u0435\u0440 '+str(user_choice)+': ')
    #user_choice = [int(u) for u in user_choice.split(',')]
    current_choice = file_list[user_choice]
    print (copie_bg)
    copies = int(raw_input("# "))

    for i in range(copies):
        current_file = os.startfile("C:/Python27/Programs/PrintNgo/Files2print/"+current_choice, "print")
