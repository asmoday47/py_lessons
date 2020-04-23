def user_data(user_fname, user_lname, user_birthdate, user_city, user_mail, user_phone):
    return("Имя пользователя: {0}\n"
          "Фамилия пользователя:{1}\n"
          "Дата рождения:{2}\n"
          "Город проживания:{3}\n"
          "Электронная почта:{4}\n"
          "Номер телефона:{5}".format(user_fname, user_lname, user_birthdate, user_city, user_mail, user_phone))


user_fname= str(input("Введите имя"))
user_lname = str(input("Введите фамилию"))
user_birthdate = str(input("Введите дату рождения в формате dd.mm.yyyy"))
user_city = str(input("Введите город проживания"))
user_mail = str(input("Введите адрес электронной почты"))
user_phone = str(input("Введите номер телефона"))

print (user_data(user_fname, user_lname, user_birthdate, user_city, user_mail, user_phone))