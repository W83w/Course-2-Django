from utils import load_random_word


pozitiv = 0
negativ = 0

for i in range(5):
    def main():
        global pozitiv
        global negativ
        main_word = load_random_word()
        print("Ведите слово ")
        user_input = input()
        if main_word.has_subword(user_input):
            pozitiv +=1
            print(f"Слово есть. Угадано {pozitiv}, не угадано {negativ}")
        else:
            negativ += 1
            print(f"Слова нет. Угадано {pozitiv}, не угадано {negativ}")

    main()

