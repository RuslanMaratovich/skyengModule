if __name__ == "__main__":
    command =""
    while command != "10":
        print("Доступные действия")
        print("10 - выйти")

        command = input("Выберите действие: ")

        if command == "10":
            print('До свидания.')
        else:
            print("Действие не распознано. Попробуйте еще раз")
