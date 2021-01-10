score = 0


sol_1_1 =  ('Владимир Шаталов')
sol_2_1 =  ('Юрий Гагарин')
sol_3_1 =  ('Тарас Шевченко')
sol_4_1 =  ('Іван Франко')

sol_1_2 =  ('Ткач')
sol_2_2 =  ('Гагарин')
sol_3_2 =  ('Шевченко')
sol_4_2 =  ('Тёркин')

sol_1_3 =  ('до первой звезды')
sol_2_3 =  ('до десятой звезды')
sol_3_3 =  ('до червртой звезды')
sol_4_3 =  ('до второй звезды')

sol_1_4 =  ('лев')
sol_2_4 =  ('рибы')
sol_3_4 =  ('змея')
sol_4_4 =  ('рак')


print(sol_1_1)
print(sol_2_1)
print(sol_3_1)
print(sol_4_1)

first_g = str(input("Какой советский космонавт получил первую космическую почту? "))


if first_g == sol_1_1:
    print('правельний ответ')
    score += 100
    print('у вас', score, 'очков')
else:
    print('не правильний ответ')
    print('у вас', score, 'очков')





print(sol_1_2)
print(sol_2_2)
print(sol_3_2)
print(sol_4_2)

second_g = str(input("Какую фамилию носил главный герой поэмы А. Твардовского? "))




if second_g == sol_4_2:
    print('правельний ответ')
    score += 100
    print('у вас', score, 'очков')
else:
    print('не правильний ответ')
    print('у вас', score, 'очков')




print(sol_1_3)
print(sol_2_3)
print(sol_3_3)
print(sol_4_3)

tr_g = str(input("До какого события продолжается рождественский пост? "))


if tr_g == sol_1_3:
    print('правельний ответ')
    score += 100
    print('у вас', score, 'очков')
else:
    print('не правильний ответ')
    print('у вас', score, 'очков')



print(sol_1_4)
print(sol_2_4)
print(sol_3_4)
print(sol_4_4)

fo_g = str(input("Какой знак восточного гороскопа следует за знаком Дракона? "))




if fo_g == sol_3_4:
    print('правельний ответ')
    score += 100
    print('у вас', score, 'очков')
else:
    print('не правильний ответ')
    print('у вас', score, 'очков')
