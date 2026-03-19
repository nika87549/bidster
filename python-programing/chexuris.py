# 1) ჩეხური სიტყვების შენახვა
# 2) ახალი სიტყვის დამატება
# 3) სიტყვების ჩვენება
# 4) ნასწავლი სიტყვებისგან წინადადების აწყობა
# 5) მონაცემების ფაილში შენახვა, რომ შემდეგ გაშვებისას არ დაიკარგოს

# import json
# import random

# file_name = "dictionary.json"

# # ფაილიდან ჩატვირთვა
# try:
#     with open(file_name, "r", encoding="utf-8") as file:
#         dictionary = json.load(file)
# except:
#     dictionary = {}

# def save_dictionary():
#     with open(file_name, "w", encoding="utf-8") as file:
#         json.dump(dictionary, file, ensure_ascii=False, indent=4)

# while True:
#     print("\n--- ჩემი ჩეხური ლექსიკონი ---")
#     print("1 - ყველა სიტყვის ნახვა")
#     print("2 - ახალი სიტყვის დამატება")
#     print("3 - სიტყვების გამოკითხვა")
#     print("4 - წინადადების აწყობა")
#     print("5 - გამოსვლა")

#     choice = input("აირჩიე: ")

#     if choice == "1":
#         if not dictionary:
#             print("ლექსიკონი ცარიელია")
#         else:
#             for cz, ge in dictionary.items():
#                 print(f"{cz} - {ge}")

#     elif choice == "2":
#         czech = input("ჩეხურად როგორ არის სიტყვა?: ")
#         georgian = input("ქართული მნიშვნელობა?: ")

#         dictionary[czech] = georgian
#         save_dictionary()

#         print("სიტყვა დაემატა ლექსიკონს")

#     elif choice == "3":
#         if not dictionary:
#             print("ჯერ სიტყვები არ არის")
#         else:
#             cz = random.choice(list(dictionary.keys()))
#             answer = input(f"რას ნიშნავს '{cz}' ქართულად? ")

#             if answer.lower() == dictionary[cz].lower():
#                 print("სწორია!")
#             else:
#                 print("არასწორია. სწორი პასუხია:", dictionary[cz])

#     elif choice == "4":
#         if len(dictionary) < 3:
#             print("წინადადებისთვის მინიმუმ 3 სიტყვა გჭირდება")
#         else:
#             words = random.sample(list(dictionary.keys()), 3)
#             print("შეადგინე წინადადება ამ სიტყვებით:")
#             print(", ".join(words))
#             sentence = input("შენი წინადადება: ")
#             print("კარგია! წინადადება ჩაიწერა.")

#     elif choice == "5":
#         print("პროგრამა დასრულდა")
#         break

#     else:
#         print("არასწორი არჩევანი")