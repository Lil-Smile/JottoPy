import random

__author__ = 'Smile'
list_of_word = ["песок", "крона", "корма", "конец", "злоба", "петух", "капот", "кроль", "залог", "жилет", "место", "хорёк", "ложка"]


def play():
    continue_flag = True
    while continue_flag is True:
        the_word = list_of_word[random.randint(0, len(list_of_word)-1)]
        flag = True
        print("Я загадал новое слово!")
        while flag is True:
            input_str = input("Ваш вариант:")
            checked = check_word(input_str, the_word)
            if checked is True:
                win()
                flag = False
            elif checked == "q":
                continue_flag = False
                flag = False
            else:
                try_again(checked)


def win():
    print("Вы угадали!")


def try_again(right_letters):
    print("Совпадающих букв ", right_letters, "попробуйте еще")


def check_word(word, the_word):
    count = 0
    if word == the_word:
        return True
    elif word == "q":
        return "q"
    else:
        for item in word:
            for letter in the_word:
                if item == letter:
                    count += 1
                    break
        return count


print("Добрый вечер! Давай сыграем в игру. \nЯ загадал слово, вы - откадывайте.\nДля выхода введите q")

play()

