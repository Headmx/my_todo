print ('Записная приветствует Вас')
notebook = {1:'Milk', 2:'Bread', 3:'Coffee', 4:'Sausage', 5: 'Salt', 6:'Fish'}
step = 0
while step:
    step = input ('Ваше действие: \n1. Просмотреть список. \n2. добавить задачу \n3. удалить задачу. \n4. редактировать задачу. \n5. отметить задачу. \n0. ВЫЙТИ \n:')
    if step == '1':
        for key, value in notebook.items():
            print (key,value) 
    elif step == '0':
        print ('Спасибо, до свидания!')
        break       
    elif step == '2':
        for step in '2':
            add_key = int(input('присвойте номер записи:'))
            if add_key in notebook:
                print ('такой номер уже есть, выберите другой!')
                continue
            else:
                add_value= input('введите запись:')
                notebook[add_key] = add_value
                for key, value in notebook.items():
                    print (key,value)
    elif step == '3':
        del_elem = int(input(' введите номер задачи: '))
        long_note = int(len(notebook))
        if del_elem in notebook.keys():
            del notebook[del_elem]
            for key, value in notebook.items():
                print (key,value)
        else:
            print ('Нет такого элемента! попробуйте снова')
    elif step == '4':
        change_value = int(input('введите номер записи:'))
        notebook[change_value] = input('Введите новое значение:')
    elif step == '5':
        end_value = int(input('введите номер записи:'))
        notebook[end_value] = '++  ' + notebook.get(end_value)
        for key, value in notebook.items():
                print (key,value)
    else:
        print ('НЕТ такого значения попробуйте еще раз!')

