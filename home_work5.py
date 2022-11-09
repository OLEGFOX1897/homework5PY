# Task 1 Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# import random
# from my_functions import inp_num
# remains=59
# first_name=input('Введите имя первого игрока: ')
# second_name=input('Введите имя компьютера: ')
# rnd=random.randint(0,1)
# if rnd==1:
#     list_rnd=[first_name,second_name]
# else:
#     list_rnd=[second_name,first_name]
# print(f'По результатам жеребьевки первым берет коньфеты игром под именем <{list_rnd[0]}>. Всего конфет {remains}')
# count=1
# while remains>0:
#     if count//2==count/2:
#         print(f'Игрок <{list_rnd[1]}> в {count} ход берет конфет = ')
#         delta=inp_num(1)
#     else: 
#         print(f'Игрок <{list_rnd[0]}> в {count} ход берет конфет = ')
#         delta=random.randint(0,30) # сделан диапазон не от 1 до 28, чтобы компьютер тоже мог ошибаться
#         print(delta)
#     if delta<=28 and delta>0 and remains>=delta:
#         remains=remains-delta
#         count=count+1
#         print(f'Остаток коньфет: {remains}')
#     else: print("Повторите ввод снова. Можно взять от 1 до 28 конфет и не больше остатка.")
# if count//2!=count/2:
#     print(f'Победил игрок <{list_rnd[1]}>')    
# else: print(f'Победил игрок <{list_rnd[0]}>')


# Task 2  Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# file = 'task2inp.txt' # информация для сжатия должна быть представленна любыми символами, кроме цифр
# data=open(file, 'r', encoding='utf-8')
# line=data.readline()
# data.close()
# print(f'Ваш исходный текст записан в файле <task2inp.txt> и представляет собой: {line}')
# print('Данный алгоритм не работает с цифрами')


# def rle_encode(data): # модуль сжатия
#     encoding = ''
#     prev_char = ''
#     count = 1
#     if not data: return ''
#     for char in data:
#         if char != prev_char:
#             if prev_char!='':
#                 encoding += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     else:
#         encoding += str(count) + prev_char
#         return encoding
# encod=rle_encode(line)
# print(f'Текст упакован и записан в фаил <task2out.txt> и представляет собой: {encod}')

# data=open('task2out.txt', 'w',encoding='utf-8')
# data.write(encod)
# data.close

# def rle_dencode(encode): #модуль раскодирования
#     if not encode: return 
#     char = ''
#     digit=''
#     decode=''
#     for char in encode:
#         if char.isdigit()==1:
#             digit+=char
#         else:
#             decode+=char*int(digit)
#             digit=''
#     return decode
# decod=rle_dencode(encod)
# print(f'Распакованный текст записан в фаил <taskout2.txt> и представляет собой: {decod}. ')



# data=open('task2out2.txt', 'w',encoding='utf-8')
# data.write(decod)
# data.close

# Task 3 Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.

# ex_text='Вот такой абвгдшный пример с абвгдшными и вбаащщными словами'
# word=''
# line_text=[]
# ex_text=ex_text+' '
# for char in ex_text:
#     if char!=' ':
#         word+=char
#     else:
#         if 'абв' not in word:
#             line_text.append(word)
#         word=''
# print(' '.join(line_text))




