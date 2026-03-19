# import json
# import os

# DATA_FILE = "czech_words.json"


# def load_words():
#     """ჩატვირთავს სიტყვებს ფაილიდან, თუ არსებობს."""
#     if not os.path.exists(DATA_FILE):
#         return []
#     try:
#         with open(DATA_FILE, "r", encoding="utf-8") as f:
#             return json.load(f)
#     except (json.JSONDecodeError, FileNotFoundError):
#         return []


# def save_words(words):
#     """შეინახავს სიტყვებს ფაილში."""
#     with open(DATA_FILE, "w", encoding="utf-8") as f:
#         json.dump(words, f, ensure_ascii=False, indent=2)


# def add_word(words):
#     """ახალი ჩეხური სიტყვის დამატება."""
#     czech = input("ჩაწერე ჩეხური სიტყვა: ").strip()
#     if not czech:
#         print("ცარიელი სიტყვა ვერ დაემატება.")
#         return

#     georgian = input("ჩაწერე თარგმანი (ქართულად): ").strip()
#     if not georgian:
#         print("თარგმანი აუცილებელია.")
#         return

#     word = {"czech": czech, "georgian": georgian}
#     words.append(word)
#     save_words(words)
#     print(f"სიტყვა '{czech}' წარმატებით დაემატა.")


# def show_words(words):
#     """ყველა შენახული სიტყვის ჩვენება."""
#     if not words:
#         print("ჯერ არც ერთი სიტყვა არ გაქვს შენახული.")
#         return

#     print("\nშენახული ჩეხური სიტყვები:")
#     for i, w in enumerate(words, start=1):
#         print(f"{i}. {w['czech']}  -  {w['georgian']}")
#     print()


# def build_sentence(words):
#     """ნასწავლი სიტყვებისგან წინადადების აწყობა."""
#     if not words:
#         print("ჯერ სიტყვები უნდა დაამატო, რომ წინადადება ააწყო.")
#         return

#     print("\nაირჩიე სიტყვები წინადადებისთვის (ნომრებით).")
#     show_words(words)
#     print("მაგალითად: 1 3 4")
#     choice = input("შეიყვანე ნომრები სივრცით გამოყოფილი: ").strip()

#     if not choice:
#         print("არაფერი შეგიყვანია.")
#         return

#     try:
#         indices = [int(x) for x in choice.split()]
#     except ValueError:
#         print("ნომრები უნდა იყოს მთელი რიცხვები.")
#         return

#     selected = []
#     for idx in indices:
#         if 1 <= idx <= len(words):
#             selected.append(words[idx - 1]["czech"])
#         else:
#             print(f"ნომერი {idx} არასწორია, გამოტოვებულია.")

#     if not selected:
#         print("არც ერთი სწორი სიტყვა არ შეირჩა.")
#         return

#     sentence = " ".join(selected)
#     print("\nშენი ჩეხური წინადადება:")
#     print(sentence)
#     print()


# def main():
#     words = load_words()

#     while True:
#         print("=== ჩეხური ენის სასწავლი პროგრამა ===")
#         print("1) ახალი სიტყვის დამატება")
#         print("2) სიტყვების ჩვენება")
#         print("3) ნასწავლი სიტყვებისგან წინადადების აწყობა")
#         print("4) გამოსვლა")
#         choice = input("აირჩიე მოქმედება (1-4): ").strip()

#         if choice == "1":
#             add_word(words)
#         elif choice == "2":
#             show_words(words)
#         elif choice == "3":
#             build_sentence(words)
#         elif choice == "4":
#             print("ნახვამდის! 👋")
#             break
#         else:
#             print("არასწორი არჩევანი, სცადე თავიდან.\n")


# if __name__ == "__main__":
#     main()





# ფანჯრიანი პროგრამა

# import json
# import os
# import random
# import tkinter as tk
# from tkinter import messagebox

# # -----------------------------
# # კონფიგურაცია და მონაცემების ფაილი
# # -----------------------------

# DATA_FILE = "czech_words_extended.json"


# # -----------------------------
# # დამხმარე ფუნქციები ფაილთან მუშაობისთვის
# # -----------------------------

# def load_words():
#     """
#     ჩატვირთავს სიტყვებს JSON ფაილიდან.
#     თუ ფაილი არ არსებობს ან გაფუჭებულია, აბრუნებს ცარიელ სიას.
#     """
#     if not os.path.exists(DATA_FILE):
#         return []

#     try:
#         with open(DATA_FILE, "r", encoding="utf-8") as f:
#             data = json.load(f)
#             if isinstance(data, list):
#                 return data
#             return []
#     except (json.JSONDecodeError, FileNotFoundError):
#         return []


# def save_words(words):
#     """
#     შეინახავს სიტყვების სიას JSON ფაილში.
#     """
#     with open(DATA_FILE, "w", encoding="utf-8") as f:
#         json.dump(words, f, ensure_ascii=False, indent=2)


# # -----------------------------
# # კონსოლური ფუნქციები
# # -----------------------------

# def add_word(words):
#     """
#     ახალი სიტყვის დამატება:
#     ჩეხური, ქართული თარგმანი, დონე (A1, A2...) და სურვილისამებრ მაგალითი.
#     """
#     print("\n--- ახალი სიტყვის დამატება ---")
#     czech = input("ჩეხური სიტყვა: ").strip()
#     if not czech:
#         print("ჩეხური სიტყვა აუცილებელია.\n")
#         return

#     georgian = input("თარგმანი ქართულად: ").strip()
#     if not georgian:
#         print("თარგმანი აუცილებელია.\n")
#         return

#     level = input("დონე (მაგ: A1, A2, B1...): ").strip()
#     if not level:
#         level = "A1"  # ნაგულისხმევი დონე

#     example = input("მაგალითი წინადადება (არასავალდებულო): ").strip()

#     word = {
#         "czech": czech,
#         "georgian": georgian,
#         "level": level,
#         "example": example
#     }
#     words.append(word)
#     save_words(words)
#     print(f"სიტყვა '{czech}' წარმატებით დაემატა.\n")


# def show_all_words(words):
#     """
#     ყველა სიტყვის ჩვენება.
#     """
#     print("\n--- ყველა სიტყვა ---")
#     if not words:
#         print("ჯერ სიტყვები არ გაქვს შენახული.\n")
#         return

#     for i, w in enumerate(words, start=1):
#         print(f"{i}. {w['czech']} - {w['georgian']} (დონე: {w.get('level', 'უცნობი')})")
#     print()


# def show_words_by_level(words):
#     """
#     სიტყვების ფილტრაცია დონით (A1, A2...).
#     """
#     print("\n--- სიტყვები დონით ---")
#     if not words:
#         print("ჯერ სიტყვები არ გაქვს შენახული.\n")
#         return

#     level = input("შეიყვანე დონე (მაგ: A1, A2, B1...): ").strip()
#     if not level:
#         print("დონე არ არის შეყვანილი.\n")
#         return

#     filtered = [w for w in words if w.get("level", "").lower() == level.lower()]

#     if not filtered:
#         print(f"დონის '{level}' სიტყვები ვერ მოიძებნა.\n")
#         return

#     for i, w in enumerate(filtered, start=1):
#         print(f"{i}. {w['czech']} - {w['georgian']} (დონე: {w.get('level', 'უცნობი')})")
#     print()


# def build_sentence(words):
#     """
#     ნასწავლი სიტყვებისგან წინადადების აწყობა ინდექსების მიხედვით.
#     """
#     print("\n--- წინადადების აწყობა ---")
#     if not words:
#         print("ჯერ სიტყვები უნდა დაამატო.\n")
#         return

#     show_all_words(words)
#     print("აირჩიე სიტყვების ნომრები სივრცით გამოყოფილი (მაგ: 1 3 4):")
#     choice = input("ნომრები: ").strip()

#     if not choice:
#         print("არაფერი შეგიყვანია.\n")
#         return

#     try:
#         indices = [int(x) for x in choice.split()]
#     except ValueError:
#         print("ნომრები უნდა იყოს მთელი რიცხვები.\n")
#         return

#     selected = []
#     for idx in indices:
#         if 1 <= idx <= len(words):
#             selected.append(words[idx - 1]["czech"])
#         else:
#             print(f"ნომერი {idx} არასწორია, გამოტოვებულია.")

#     if not selected:
#         print("არც ერთი სწორი სიტყვა არ შეირჩა.\n")
#         return

#     sentence = " ".join(selected)
#     print("\nშენი ჩეხური წინადადება:")
#     print(sentence + "\n")


# def normalize_answer(s):
#     """
#     პასუხის ნორმალიზაცია შედარებისთვის:
#     პატარა ასოები და ზედმეტი სივრცეების მოცილება.
#     """
#     return " ".join(s.strip().lower().split())


# def quiz_console(words):
#     """
#     კონსოლური ქვიზი:
#     შემთხვევითი ჩეხური სიტყვა -> მომხმარებელი წერს ქართულ თარგმანს.
#     ბოლოს აჩვენებს ქულას.
#     """
#     print("\n--- ქვიზი (კონსოლი) ---")
#     if not words:
#         print("ქვიზისთვის ჯერ სიტყვები უნდა დაამატო.\n")
#         return

#     num_questions = min(5, len(words))
#     questions = random.sample(words, num_questions)

#     score = 0
#     for i, w in enumerate(questions, start=1):
#         print(f"\nკითხვა {i}/{num_questions}")
#         print(f"ჩეხური სიტყვა: {w['czech']}")
#         answer = input("შეიყვანე თარგმანი ქართულად: ")

#         if normalize_answer(answer) == normalize_answer(w["georgian"]):
#             print("სწორია! ✅")
#             score += 1
#         else:
#             print(f"არასწორია. სწორი პასუხი: {w['georgian']}")

#     print(f"\nშენი შედეგი: {score} / {num_questions}\n")


# # -----------------------------
# # tkinter GUI
# # -----------------------------

# class CzechGUI:
#     """
#     მარტივი GUI ჩეხური სიტყვების სანახავად და პატარა ქვიზისთვის.
#     """

#     def __init__(self, root, words):
#         self.root = root
#         self.root.title("ჩეხური ენის პროგრამა - GUI")
#         self.words = words

#         # მთავარი ჩარჩო
#         frame = tk.Frame(root, padx=10, pady=10)
#         frame.pack(fill=tk.BOTH, expand=True)

#         # მარცხენა მხარეს - სიტყვების სია
#         left_frame = tk.Frame(frame)
#         left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#         tk.Label(left_frame, text="ჩეხური სიტყვები:").pack(anchor="w")
#         self.listbox = tk.Listbox(left_frame, width=30)
#         self.listbox.pack(fill=tk.BOTH, expand=True)

#         # სიტყვების ჩატვირთვა listbox-ში
#         for w in self.words:
#             self.listbox.insert(tk.END, w["czech"])

#         self.listbox.bind("<<ListboxSelect>>", self.on_select)

#         # მარჯვენა მხარეს - დეტალები და ქვიზი
#         right_frame = tk.Frame(frame)
#         right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

#         tk.Label(right_frame, text="ინფორმაცია სიტყვაზე:").pack(anchor="w")

#         self.info_text = tk.Text(right_frame, height=6, width=40)
#         self.info_text.pack(fill=tk.X)
#         self.info_text.config(state=tk.DISABLED)

#         # ქვიზის ნაწილი
#         separator = tk.Label(right_frame, text="--- ქვიზი GUI-ში ---")
#         separator.pack(pady=5)

#         self.quiz_word_label = tk.Label(right_frame, text="დააჭირე 'დაწყება'-ს ქვიზისთვის")
#         self.quiz_word_label.pack(anchor="w")

#         self.answer_entry = tk.Entry(right_frame, width=30)
#         self.answer_entry.pack(anchor="w", pady=5)

#         quiz_buttons_frame = tk.Frame(right_frame)
#         quiz_buttons_frame.pack(anchor="w")

#         self.start_quiz_button = tk.Button(quiz_buttons_frame, text="დაწყება", command=self.start_quiz)
#         self.start_quiz_button.pack(side=tk.LEFT, padx=2)

#         self.submit_button = tk.Button(quiz_buttons_frame, text="პასუხი", command=self.check_answer, state=tk.DISABLED)
#         self.submit_button.pack(side=tk.LEFT, padx=2)

#         self.current_quiz_word = None
#         self.quiz_pool = []

#     def on_select(self, event):
#         """
#         როცა listbox-ში სიტყვას ავირჩევთ, ვაჩვენოთ მისი თარგმანი და დონე.
#         """
#         if not self.listbox.curselection():
#             return
#         index = self.listbox.curselection()[0]
#         word = self.words[index]

#         info = (
#             f"ჩეხური: {word['czech']}\n"
#             f"ქართული: {word['georgian']}\n"
#             f"დონე: {word.get('level', 'უცნობი')}\n"
#         )
#         if word.get("example"):
#             info += f"მაგალითი: {word['example']}\n"

#         self.info_text.config(state=tk.NORMAL)
#         self.info_text.delete("1.0", tk.END)
#         self.info_text.insert(tk.END, info)
#         self.info_text.config(state=tk.DISABLED)

#     def start_quiz(self):
#         """
#         GUI ქვიზის დაწყება: ვამზადებთ შემთხვევით სიტყვებს.
#         """
#         if not self.words:
#             messagebox.showinfo("ქვიზი", "ჯერ სიტყვები უნდა დაამატო.")
#             return

#         self.quiz_pool = random.sample(self.words, len(self.words))
#         self.next_quiz_word()
#         self.submit_button.config(state=tk.NORMAL)

#     def next_quiz_word(self):
#         """
#         შემდეგი სიტყვის ჩვენება ქვიზში.
#         """
#         if not self.quiz_pool:
#             self.current_quiz_word = None
#             self.quiz_word_label.config(text="ქვიზი დასრულდა!")
#             self.submit_button.config(state=tk.DISABLED)
#             return

#         self.current_quiz_word = self.quiz_pool.pop()
#         self.quiz_word_label.config(text=f"ჩეხური სიტყვა: {self.current_quiz_word['czech']}")
#         self.answer_entry.delete(0, tk.END)

#     def check_answer(self):
#         """
#         GUI ქვიზის პასუხის შემოწმება.
#         """
#         if not self.current_quiz_word:
#             return

#         user_answer = self.answer_entry.get()
#         correct = self.current_quiz_word["georgian"]

#         if normalize_answer(user_answer) == normalize_answer(correct):
#             messagebox.showinfo("შედეგი", "სწორია! ✅")
#         else:
#             messagebox.showinfo("შედეგი", f"არასწორია.\nსწორი პასუხი: {correct}")

#         self.next_quiz_word()


# def open_gui(words):
#     """
#     tkinter GUI ფანჯრის გახსნა.
#     """
#     root = tk.Tk()
#     app = CzechGUI(root, words)
#     root.mainloop()


# # -----------------------------
# # მთავარი მენიუ (კონსოლი)
# # -----------------------------

# def main():
#     words = load_words()

#     while True:
#         print("=== ჩეხური ენის სასწავლი პროგრამა ===")
#         print("1) ახალი სიტყვის დამატება")
#         print("2) ყველა სიტყვის ჩვენება")
#         print("3) სიტყვების ჩვენება დონით (A1, A2...)")
#         print("4) წინადადების აწყობა ნასწავლი სიტყვებით")
#         print("5) ქვიზი (კონსოლი)")
#         print("6) GUI ფანჯარა")
#         print("7) გამოსვლა")
#         choice = input("აირჩიე (1-7): ").strip()

#         if choice == "1":
#             add_word(words)
#         elif choice == "2":
#             show_all_words(words)
#         elif choice == "3":
#             show_words_by_level(words)
#         elif choice == "4":
#             build_sentence(words)
#         elif choice == "5":
#             quiz_console(words)
#         elif choice == "6":
#             print("იხსნება GUI ფანჯარა...\n")
#             open_gui(words)
#         elif choice == "7":
#             print("ნახვამდის! 👋")
#             break
#         else:
#             print("არასწორი არჩევანი, სცადე თავიდან.\n")


# if __name__ == "__main__":
#     main()

