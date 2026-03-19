#   ამ ამოცანების მზგავსი ამოცანები მომიმზადე 10 დონიანი ამოცანები სადაც დონე 1 არის მარტივი,
#   ხოლო 10 დონე არის რთული, თითო დონეში  10 ამოცანა შენ ჯერ კოდი არ დამიწერო მე დავწერ და მერე
#   შენ შეამოწმე განმიმარტე ყველაფერი და ყოველ ჯერზე დასაწყისში შემახსენე დონე და ამოცანის ნომერი და ერთ
#   ჯერზე ერთ ამოცანაზე მეტი არ მაცჩვენო რომ დავწერ და კოდს შემიმოწმებ მერე შემდეგი მაჩვენე და ასე ბოლომდე ბოლო დონის ბოლო ამოცანამდე



# 1
# user = ("hello world")
# print (user)

# 2
# user = input("ra gqvia?")
# user2 = (f"gamarjoba {user} sasiamovnoa sheni gacnoba")
# print (user2)

# 3
# user = input("dawere winadadeba:")
# user2 = len(user)
# print (user2)

# 4
# user = int(input("pirveli ricxvi:"))
# user2 = int(input("meore ricxvi:"))
# u3= user + user2
# u4= user - user2
# u5= user * user2
# u6= user / user2
# print(f"{user}+{user2}={u3}\n"
#       f"{user}-{user2}={u4}\n"
#       f"{user}*{user2}={u5}\n"
#       f"{user}/{user2}={u6}")

# 5
# user = input("dawere citata: ")
# user2 = input("vin aris am citatis avtori? ")
# print(f"{user2} ambobda '{user}'")

#5
# def main():
#     quote = input("დაწერე ციტატა: ").strip()
#     author = input("ვინ არის ამ ციტატის ავტორი? ").strip()
#     if quote and author:
#         print(f"{author} ამბობდა '{quote}'")
#     else:
#         print("ციტატა ან ავტორი არ უნდა იყოს ცარიელი.")

# main()


# 6
# user = input("mitxari sheni sayvareli gamonatqvami: ").lower()
# print(user)

#6
# def main():
#     user = input("შეიყვანე შენი საყვარელი გამონათვათი: ").lower().strip()
#     if user:
#         print(f"შენ დაწერე: {user}")
#     else:
#         print("შეყვანა ცარიელია!")

# main()


# 7
# user =input("dawere teqsti: ").replace(" ","...")
# print (user)

#7
# def main():
#     user = input("დაეწერეთ ტექსტი: ")
#     modified = user.replace(" ", "...")
#     print(modified)

# main()


# 8
# user = input("dawer rac ginda:").replace(":)","🙂").replace(":(","🙁")
# print(user)


#8
# def main():
#     user = input("დაეწერეთ ტექსტი: ")
#     user = user.replace(":)", "🙂").replace(":(", "🙁")
#     print(user)

# main()


# 9
# def main():
#     c = 300_000_000  # სინათლის სიჩქარე მეტრ/წმ-ში
#     m = float(input("შეიყვანეთ მასა კილოგრამებში: "))
#     E = m * c**2
#     print(f"გამოთვლილი ენერგია E = {E:.2e} ჯოული")

# main()


# 10
# c= int(input("dawere gradusi celsiusi: "))
# user=(c * 9/5 + 32)
# print(f"{c} gradusi celsiusi aris {user} farengeiti")


#10
# def main():
#     c = int(input("შეიყვანეთ ტემპერატურა ცელსიუსში: "))
#     f = c * 9 / 5 + 32
#     print(f"{c} გრადუსი ცელსიუსში არის {f:.1f} გრადუსი ფარენგეითში.")

# main()


# 13
# user = int(input("mitxari sheni asaki: "))
# user2= int(input("mitxari sapensio asaki: "))
# user3= user - user2
# print(f"shen pensiaze gaxval {user3} weliwadshi")


#13
# def main():
#     current_age = int(input("შეიყვანე შენი ასაკი: "))
#     pension_age = int(input("შეიყვანე საპენსიო ასაკი: "))

#     years_left = pension_age - current_age

#     if years_left > 0:
#         print(f"შენ საპენსიო ასაკამდე დარჩა {years_left} წელი.")
#     elif years_left == 0:
#         print("გილოცავ, ახლა შეგიძლია წასვლა საპენსიო ასაკში!")
#     else:
#         print(f"პენსიაზე გასული ხარ უკვე {-years_left} წლით.")

# main()


# 14
# user = int(input("mitxari ramdenia sigrdze futebshi: "))
# user2 = int(input("mitxari ramdenia sigane futebshi: "))
# u1 = user * 0.09290304
# u2 = user2 * 0.09290304
# u3 = user * user2
# u4 = u1 * u2
# print(f"otaxis fartobi futebshi aris:{u3}\n"
#       f"otaxis fartobi metrkvadratshi aris:{u4}")


# 15
# u1 = int(input("mitxari adamianebis raodenoba: "))
# u2 = int(input("mitxari ramdeni pizza gaqvs: "))
# u3 = int (input("mitxari tito pizza ramdeni navheria: "))
# u4 = u3 * u2
# u5 = u4 // u1
# u6 = u4 % u1
# print(f"tqven gaqvt {u4} nacheri pizza\n"
#       f"tito adamians ergeba {u5} nacheri\n"
#       f"darchenili nachrebis raodenoba aris {u6}")
#  def main():
#     # უსაფრთხოდ ვიღებთ თანხასა და პროცენტს, ვალიდაციით
#     dollars = get_valid_dollar_input("How much was the meal? ")
#     percent = get_valid_percent_input("What percentage would you like to tip? ")

#     tip = dollars * percent
#     print(f"Leave ${tip:.2f}")

#16
# def get_valid_dollar_input(prompt):
#     while True:
#         try:
#             d = input(prompt).strip()
#             return float(d.replace("$", ""))
#         except ValueError:
#             print("❌ Please enter a valid amount, like $50.00")


# def get_valid_percent_input(prompt):
#     while True:
#         try:
#             p = input(prompt).strip()
#             return float(p.replace("%", "")) / 100
#         except ValueError:
#             print("❌ Please enter a valid percent, like 10%")


# main()

#22
# def main():
#     text = input("Enter your text: ").strip().lower()

#     if text.startswith("hello"):
#         print("$0")
#     elif text.startswith("h"):
#         print("$20")
#     else:
#         print("$100")

# main()

#21
# def main():
#     # მომხმარებლის მიერ შეყვანილი თანხა და პროცენტი გარდაიქმნება რიცხვებად
#     dollars = dollars_to_float(input("How much was the meal? "))  # მაგ: $50.00
#     percent = percent_to_float(input("What percentage would you like to tip? "))  # მაგ: 10%

#     # გამოთვლე პროცენტი
#     tip = dollars * percent

#     # დაბეჭდე შედეგი 2 ათწილადი სიმბოლოთი
#     print(f"Leave ${tip:.2f}")


# def dollars_to_float(d):
#     # $ ნიშნის მოცილება და გარდაქმნა float ტიპში
#     return float(d.replace("$", ""))


# def percent_to_float(p):
#     # % ნიშნის მოცილება და გარდაქმნა ათწილადში, მაგ: 10% → 0.10
#     return float(p.replace("%", "")) / 100


# main()

#23
# def main():
#     user = (input("add text: ")).strip().lower()
#     if "please" in user:
#         print("polite:$0")
#     elif "sorry" in user:
#         print("Apology noted: $10")
#     else:
#         print("woow $100")
# main()

#24
# def main():
#     # პროცენტის შეყვანა
#     percent_str = input("ჩააწერე რამდენ პროცენტს მისცემდით? (მაგ: 15%): ")
#     percent = float(percent_str.replace("%", ""))

#     # კომენტარი
#     comment = input("გთხოვთ დაწეროთ კომენტარი მომსახურებაზე: ").strip().lower()

#     # ზრდილობიანობის შემოწმება
#     polite = "please" in comment or "thank you" in comment or "sorry" in comment

#     # შეფასება
#     if polite and percent > 15:
#         print("Great customer! Reward level: Gold")
#     elif polite and 10 <= percent <= 15:
#         print("Polite and Fair: Reward level: Silver")
#     else:
#         print("Needs improvement: Reward level: Bronze")

# main()


# u1 = int(input("mitxari adamianebis raodenoba: "))
# u2 = int(input("mitxari ramdeni pizza gaqvs: "))
# u3 = int (input("mitxari tito pizza ramdeni navheria: "))
# u4 = u3 * u2
# u5 = u4 // u1
# u6 = u4 % u1
# print(f"tqven gaqvt {u4} nacheri pizza\n"
#       f"tito adamians ergeba {u5} nacheri\n"
#       f"darchenili nachrebis raodenoba aris {u6}")

#23
# def main():
#     user = input("რა არის სიცოცხლის მნიშვნელობა? ").strip().lower()
#     if user == "42":
#         print("yes")
#     elif user == "forty two":
#         print("yes")
#     elif user == "forty-two":
#         print("yes")
#     else:
#         print("no")
#     # if user == "42" or user == "forty two" or user == "forty-two":
#     #     print("yes")
#     # else:
#     #     print("no")

# main()


#24
# def get_mime_type(filename):
#     # გაფართოება და შესაბამისი MIME ტიპი
#     mime_types = {
#         'html': 'text/html',
#         'htm': 'text/html',
#         'jpg': 'image/jpeg',
#         'jpeg': 'image/jpeg',
#         'png': 'image/png',
#         'gif': 'image/gif',
#         'css': 'text/css',
#         'csv': 'text/csv',
#         'txt': 'text/plain',
#         'pdf': 'application/pdf',
#         'json': 'application/json',
#         'js': 'application/javascript',
#         'mp3': 'audio/mpeg',
#         'mp4': 'video/mp4',
#         'mpeg': 'video/mpeg',
#         'webm': 'video/webm',
#         'webp': 'image/webp',
#         'svg': 'image/svg+xml',
#         'zip': 'application/zip',
#         'xml': 'application/xml'
#     }

#     # ამოღება გაფართოების
#     if '.' in filename:
#         ext = filename.rsplit('.', 1)[1].lower()
#         mime_type = mime_types.get(ext)
#         if mime_type:
#             return f"ფაილის ტიპია: {mime_type}"
#         else:
#             return "ფაილის ტიპი უცნობია."
#     else:
#         return "ფაილს არ აქვს გაფართოება."


# # მომხმარებლის შეყვანა
# filename = input("შეიყვანეთ ფაილის სახელი (მაგ. cat.jpeg): ")
# result = get_mime_type(filename)
# print(result)


#25
# მომხმარებლის შეყვანა
# expression = input("შეიყვანეთ მათემატიკური გამოთვლა (მაგ. 25 - 15): ")

# try:
#     # გამოთვლა
#     result = eval(expression)
#     print(f"შედეგი არის: {result}")
# except Exception as e:
#     print("შეცდომა მოხდა გამოთვლისას. გთხოვთ, შეიყვანოთ სწორი მათემატიკური გამოსახულება.")


#26
# def main():
#     time_str = input("What time is it? ")
#     time = convert(time_str)

#     if 7.0 <= time <= 8.0:
#         print("breakfast time")
#     elif 12.0 <= time <= 13.0:
#         print("lunch time")
#     elif 18.0 <= time <= 19.0:
#         print("dinner time")
#     # სხვა შემთხვევაში არაფერი არ იბეჭდება


# def convert(time):
#     hours, minutes = time.split(":")
#     return int(hours) + int(minutes) / 60


# if __name__ == "__main__":
#     main()


#27
# import re

# def is_camel_case(s: str) -> bool:
#     """
#     ვამოწმებთ, არის თუ არა სტრინგი camelCase ფორმატში:
#     - იწყება პატარა ასოთი
#     - შეიცავს მინიმუმ ერთ დიდ ასოს (ანუ მინიმუმ ორი სიტყვაა შეერთებული)
#     - არ შეიცავს "_", "-", სივრცეებს
#     """
#     return bool(re.fullmatch(r'[a-z]+(?:[A-Z][a-z0-9]*)+', s))

# def camel_to_snake(s: str) -> str:
#     """
#     camelCase -> snake_case გარდაქმნა.
#     თუ s არ არის camelCase, ვაბრუნებთ s-ს უცვლელად.
#     """
#     if not is_camel_case(s):
#         return s
#     # თითო დიდ ასოს წინ ვამატებთ ქვედა ტირეს და ვაქცევთ პატარა ასოდ
#     snake = re.sub(r'([A-Z])', r'_\1', s).lower()
#     return snake

# def main():
#     text = input("შეიყვანეთ ტექსტი camelCase ფორმატში: ").strip()
#     print(camel_to_snake(text))

# if __name__ == "__main__":
#     main()

#28
# def get_valid_coin() -> int:
#     """
#     კითხულობს მონეტას მომხმარებლისგან.
#     აბრუნებს მხოლოდ 5, 10 ან 25-ს.
#     სხვა შემთხვევაში ისევ ეკითხება.
#     """
#     while True:
#         try:
#             coin = int(input("Insert Coin: "))
#             if coin in [5, 10, 25, 50]:
#                 return coin
#             else:
#                 print("Invalid coin. Please insert 5, 10, or 25.")
#         except ValueError:
#             print("Invalid input. Please insert a number.")

# def coke_machine():
#     price = 50
#     amount_due = price

#     while amount_due > 0:
#         print(f"Amount Due: {amount_due}")
#         coin = get_valid_coin()
#         amount_due -= coin

#     change = abs(amount_due)   # თუ ზედმეტი გადაიხადა
#     print(f"Change Owed: {change}")


# def main():
#     coke_machine()


# if __name__ == "__main__":
#     main()

#29
# def remove_vowels(text: str) -> str:
#     vowels = "aeiouAEIOUაეიოუ"  # ქართულიც და ინგლისურიც
#     result = "".join(ch for ch in text if ch not in vowels)
#     return result

# def main():
#     user_input = input("შეიყვანეთ ტექსტი: ")
#     print("ხმოვნების გარეშე:", remove_vowels(user_input))

# if __name__ == "__main__":
#     main()

#30
# import string

# def check_length(text: str) -> bool:
#     return 2 <= len(text) <= 6

# def check_first_two_letters(text: str) -> bool:
#     return len(text) >= 2 and text[0].isalpha() and text[1].isalpha()

# def check_no_punctuation(text: str) -> bool:
#     return not any(ch in string.punctuation for ch in text)

# def check_numbers(text: str) -> bool:
#     digits = [ch for ch in text if ch.isdigit()]
#     if not digits:
#         return True  # საერთოდ არ არის ციფრები
#     # პირველი ციფრი ნულზე არ იწყება
#     if '0' == digits[0]:
#         return False
#     # ციფრის შემდეგ აღარ უნდა იყოს ასობგერა
#     first_digit_index = min(i for i, ch in enumerate(text) if ch.isdigit())
#     after_digits = text[first_digit_index:]
#     return after_digits.isdigit()

# def is_valid(text: str) -> bool:
#     return (check_length(text)
#             and check_first_two_letters(text)
#             and check_no_punctuation(text)
#             and check_numbers(text))

# def main():
#     user_input = input("Enter text: ")
#     if is_valid(user_input):
#         print("Valid")
#     else:
#         print("Invalid")

# if __name__ == "__main__":
#     main()

#31
# import unicodedata
# import string

# def is_punctuation(ch: str) -> bool:
#     """უბრალოდ შემოწმება — თუ სიმბოლო იუნიკოდში პუნქტუაციის კატეგორიას მიეკუთვნება."""
#     return unicodedata.category(ch).startswith("P") or ch in string.punctuation

# def check_length(text: str):
#     if 2 <= len(text) <= 6:
#         return True, None
#     return False, "ტექსტის სიგრძე უნდა იყოს მინიმუმ 2 და მაქსიმუმ 6 სიმბოლო"

# def check_first_two_letters(text: str):
#     if len(text) >= 2 and text[0].isalpha() and text[1].isalpha():
#         return True, None
#     return False, "პირველი ორი სიმბოლო აუცილებლად უნდა იყოს ასო"

# def check_no_punctuation(text: str):
#     for ch in text:
#         if is_punctuation(ch):
#             return False, "ტექსტი არ უნდა შეიცავდეს პუნქტუაციის ნიშნებს"
#     return True, None

# def check_numbers(text: str):
#     """
#     წესები:
#     - თუ ტექსტში ციფრები არაა, ყველაფერი კარგი
#     - თუ არის ციფრი: პირველი ციფრი არ უნდა იყოს '0'
#     - თუ გამოჩნდა ციფრი, მის შემდეგ ტექსტში არ უნდა იყოს ასო (ასე კი ვეწინააღმდეგებით 'ციფრის მერე არ უნდა იყოს ასობგერა')
#     """
#     # პირველი ციფრის ინდექსი (თუ არის)
#     first_digit_idx = next((i for i, ch in enumerate(text) if ch.isdigit()), None)
#     if first_digit_idx is None:
#         return True, None

#     # პირველი ციფრი არ უნდა იყოს '0'
#     if text[first_digit_idx] == '0':
#         return False, "პირველი ციფრი არ უნდა იყოს 0"

#     # ციფრის შემდეგ არ უნდა იყოს ასობგერა
#     after = text[first_digit_idx:]
#     for ch in after:
#         if ch.isalpha():
#             return False, "ციფრის შემდეგ არ შეიძლება ასობგერა"
#         # თუ არის სხვა (არა ციფრი და არა ასო) — ამას დაფიქსირებს check_no_punctuation,
#         # მაგრამ აქაც ვფრთხილობთ და ვაჩვენებთ შესაბამის მესიჯს
#         if not ch.isdigit():
#             return False, "ციფრის შემდეგ არ შეიძლება სხვა სიმბოლო (მაგ. ხაზი, ცარიელი აღნიშვნა და სხვ.)"

#     return True, None

# def validate(text: str):
#     """გარბენინებს ყველა შემოწმებას და აგროვებს შეცდომებს."""
#     checks = [
#         check_length,
#         check_first_two_letters,
#         check_no_punctuation,
#         check_numbers
#     ]
#     errors = []
#     for chk in checks:
#         ok, reason = chk(text)
#         if not ok and reason:
#             # ერთი და იგივეს გამო რამდენიმე ჩინებული შედეგისთვის არ დავიმატოთ დუპლიკატი
#             if reason not in errors:
#                 errors.append(reason)
#     return len(errors) == 0, errors

# def main():
#     text = input("Enter text: ")
#     valid, errors = validate(text)
#     if valid:
#         print("Valid")
#     else:
#         print("Invalid")
#         for e in errors:
#             print("-", e)

# if __name__ == "__main__":
#     main()

#32
# def main():
#     # ხილის სახელები და კალორიები (100 გრამზე, მაგალითად)
#     fruits = {
#         "apple": 52,
#         "banana": 89,
#         "orange": 47,
#         "pear": 57,
#         "grape": 69,
#         "kiwi": 61,
#         "peach": 39,
#         "plum": 46,
#         "cherry": 50,
#         "melon": 36,
#         "watermelon": 30,
#         "pineapple": 50,
#         "strawberry": 33
#     }

#     user_input = input("Enter fruit name: ").strip().lower()

#     if user_input in fruits:
#         print(f"{fruits[user_input]} kcal")

# if __name__ == "__main__":
#     main()