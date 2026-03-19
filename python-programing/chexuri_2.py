# სიტყვების დამატება
# სიტყვების შენახვა ფაილში
# ტესტი და ქულები
# ყოველდღიური პრაქტიკა
# წინადადებების გენერაცია ნასწავლი სიტყვებით

# import json
# import random

# FILE = "czech_dictionary.json"

# # ლექსიკონის ჩატვირთვა
# try:
#     with open(FILE, "r", encoding="utf-8") as f:
#         dictionary = json.load(f)
# except:
#     dictionary = {}

# score = 0


# def save():
#     with open(FILE, "w", encoding="utf-8") as f:
#         json.dump(dictionary, f, ensure_ascii=False, indent=4)


# def show_words():
#     if not dictionary:
#         print("ლექსიკონი ცარიელია")
#         return

#     print("\nნასწავლი სიტყვები:")
#     for cz, ge in dictionary.items():
#         print(f"{cz} - {ge}")


# def add_word():
#     cz = input("ჩეხური სიტყვა: ")
#     ge = input("ქართული მნიშვნელობა: ")

#     dictionary[cz] = ge
#     save()

#     print("✅ სიტყვა დაემატა")


# def quiz():
#     global score

#     if not dictionary:
#         print("ჯერ სიტყვები არ არის")
#         return

#     cz = random.choice(list(dictionary.keys()))
#     answer = input(f"\nრას ნიშნავს '{cz}' ქართულად? ")

#     if answer.lower() == dictionary[cz].lower():
#         print("✅ სწორია!")
#         score += 1
#     else:
#         print("❌ არასწორია")
#         print("სწორი პასუხია:", dictionary[cz])


# def sentence_builder():
#     if len(dictionary) < 3:
#         print("მინიმუმ 3 სიტყვა უნდა იცოდე")
#         return

#     words = random.sample(list(dictionary.keys()), 3)

#     print("\nშეადგინე წინადადება ამ სიტყვებით:")
#     print(", ".join(words))

#     sentence = input("შენი წინადადება: ")

#     print("👍 კარგი პრაქტიკა!")


# while True:

#     print("\n====================")
#     print("🇨🇿 Czech Learning App")
#     print("====================")
#     print("1 - სიტყვების ნახვა")
#     print("2 - ახალი სიტყვის დამატება")
#     print("3 - ტესტი")
#     print("4 - წინადადების აწყობა")
#     print("5 - ქულების ნახვა")
#     print("6 - გამოსვლა")

#     choice = input("აირჩიე: ")

#     if choice == "1":
#         show_words()

#     elif choice == "2":
#         add_word()

#     elif choice == "3":
#         quiz()

#     elif choice == "4":
#         sentence_builder()

#     elif choice == "5":
#         print("🏆 შენი ქულებია:", score)

#     elif choice == "6":
#         print("ნახვამდის 👋")
#         break

#     else:
#         print("არასწორი არჩევანი")