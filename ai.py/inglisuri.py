# import json
# import os
# import random
# import tkinter as tk
# from tkinter import messagebox

# # -----------------------------
# # კონფიგურაცია და მონაცემების ფაილი
# # -----------------------------

# DATA_FILE = "english_words.json"


# # -----------------------------
# # დამხმარე ფუნქციები ფაილთან მუშაობისთვის
# # -----------------------------

# def load_words():
#     """ჩატვირთავს სიტყვებს JSON ფაილიდან."""
#     if not os.path.exists(DATA_FILE):
#         return []
#     try:
#         with open(DATA_FILE, "r", encoding="utf-8") as f:
#             data = json.load(f)
#             return data if isinstance(data, list) else []
#     except (json.JSONDecodeError, FileNotFoundError):
#         return []


# def save_words(words):
#     """შეინახავს სიტყვებს JSON ფაილში."""
#     with open(DATA_FILE, "w", encoding="utf-8") as f:
#         json.dump(words, f, ensure_ascii=False, indent=2)


# # -----------------------------
# # კონსოლური ფუნქციები
# # -----------------------------

# def add_word(words):
#     """ახალი ინგლისური სიტყვის დამატება."""
#     print("\n--- ახალი სიტყვის დამატება ---")
#     eng = input("ინგლისური სიტყვა: ").strip()
#     if not eng:
#         print("სიტყვა აუცილებელია.\n")
#         return

#     geo = input("თარგმანი ქართულად: ").strip()
#     if not geo:
#         print("თარგმანი აუცილებელია.\n")
#         return

#     level = input("დონე (A1, A2, B1...): ").strip() or "A1"
#     example = input("მაგალითი წინადადება (არასავალდებულო): ").strip()

#     word = {"english": eng, "georgian": geo, "level": level, "example": example}
#     words.append(word)
#     save_words(words)
#     print(f"სიტყვა '{eng}' წარმატებით დაემატა.\n")


# def show_all_words(words):
#     """ყველა სიტყვის ჩვენება."""
#     print("\n--- ყველა სიტყვა ---")
#     if not words:
#         print("სიტყვები ჯერ არ გაქვს.\n")
#         return

#     for i, w in enumerate(words, start=1):
#         print(f"{i}. {w['english']} - {w['georgian']} (დონე: {w['level']})")
#     print()


# def show_words_by_level(words):
#     """სიტყვების ფილტრაცია დონით."""
#     level = input("\nშეიყვანე დონე (A1, A2, B1...): ").strip()
#     filtered = [w for w in words if w["level"].lower() == level.lower()]

#     if not filtered:
#         print("ამ დონის სიტყვები არ მოიძებნა.\n")
#         return

#     print(f"\n--- {level} დონის სიტყვები ---")
#     for i, w in enumerate(filtered, start=1):
#         print(f"{i}. {w['english']} - {w['georgian']}")
#     print()


# def build_sentence(words):
#     """სიტყვებისგან წინადადების აწყობა."""
#     if not words:
#         print("ჯერ სიტყვები დაამატე.\n")
#         return

#     show_all_words(words)
#     choice = input("აირჩიე ნომრები (მაგ: 1 3 4): ").strip()

#     try:
#         indices = [int(x) for x in choice.split()]
#     except ValueError:
#         print("ნომრები არასწორია.\n")
#         return

#     selected = []
#     for idx in indices:
#         if 1 <= idx <= len(words):
#             selected.append(words[idx - 1]["english"])

#     if not selected:
#         print("არც ერთი სწორი სიტყვა არ შეირჩა.\n")
#         return

#     print("\nშენი წინადადება:")
#     print(" ".join(selected) + "\n")


# def normalize(s):
#     return " ".join(s.strip().lower().split())


# def quiz_console(words):
#     """კონსოლური ქვიზი."""
#     if not words:
#         print("ქვიზისთვის სიტყვები დაამატე.\n")
#         return

#     num = min(5, len(words))
#     questions = random.sample(words, num)
#     score = 0

#     for i, w in enumerate(questions, start=1):
#         print(f"\nკითხვა {i}/{num}")
#         print(f"ინგლისური სიტყვა: {w['english']}")
#         ans = input("ქართული თარგმანი: ")

#         if normalize(ans) == normalize(w["georgian"]):
#             print("სწორია! ✅")
#             score += 1
#         else:
#             print(f"არასწორია. სწორი პასუხი: {w['georgian']}")

#     print(f"\nშენი შედეგი: {score}/{num}\n")


# # -----------------------------
# # tkinter GUI
# # -----------------------------

# class EnglishGUI:
#     def __init__(self, root, words):
#         self.root = root
#         self.root.title("ინგლისური ენის სასწავლი პროგრამა")
#         self.words = words

#         frame = tk.Frame(root, padx=10, pady=10)
#         frame.pack(fill=tk.BOTH, expand=True)

#         # მარცხენა სია
#         left = tk.Frame(frame)
#         left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#         tk.Label(left, text="ინგლისური სიტყვები:").pack(anchor="w")
#         self.listbox = tk.Listbox(left, width=30)
#         self.listbox.pack(fill=tk.BOTH, expand=True)

#         for w in words:
#             self.listbox.insert(tk.END, w["english"])

#         self.listbox.bind("<<ListboxSelect>>", self.show_info)

#         # მარჯვენა მხარე
#         right = tk.Frame(frame)
#         right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

#         tk.Label(right, text="ინფორმაცია სიტყვაზე:").pack(anchor="w")
#         self.info = tk.Text(right, height=6, width=40)
#         self.info.pack(fill=tk.X)
#         self.info.config(state=tk.DISABLED)

#         tk.Label(right, text="--- ქვიზი ---").pack(pady=5)

#         self.quiz_label = tk.Label(right, text="დააჭირე 'დაწყება'-ს")
#         self.quiz_label.pack(anchor="w")

#         self.answer = tk.Entry(right, width=30)
#         self.answer.pack(anchor="w", pady=5)

#         btns = tk.Frame(right)
#         btns.pack(anchor="w")

#         tk.Button(btns, text="დაწყება", command=self.start_quiz).pack(side=tk.LEFT, padx=2)
#         self.submit = tk.Button(btns, text="პასუხი", command=self.check_answer, state=tk.DISABLED)
#         self.submit.pack(side=tk.LEFT, padx=2)

#         self.quiz_pool = []
#         self.current = None

#     def show_info(self, event):
#         if not self.listbox.curselection():
#             return
#         idx = self.listbox.curselection()[0]
#         w = self.words[idx]

#         text = (
#             f"ინგლისური: {w['english']}\n"
#             f"ქართული: {w['georgian']}\n"
#             f"დონე: {w['level']}\n"
#         )
#         if w["example"]:
#             text += f"მაგალითი: {w['example']}\n"

#         self.info.config(state=tk.NORMAL)
#         self.info.delete("1.0", tk.END)
#         self.info.insert(tk.END, text)
#         self.info.config(state=tk.DISABLED)

#     def start_quiz(self):
#         if not self.words:
#             messagebox.showinfo("ქვიზი", "ჯერ სიტყვები დაამატე.")
#             return

#         self.quiz_pool = random.sample(self.words, len(self.words))
#         self.submit.config(state=tk.NORMAL)
#         self.next_word()

#     def next_word(self):
#         if not self.quiz_pool:
#             self.quiz_label.config(text="ქვიზი დასრულდა!")
#             self.submit.config(state=tk.DISABLED)
#             return

#         self.current = self.quiz_pool.pop()
#         self.quiz_label.config(text=f"ინგლისური სიტყვა: {self.current['english']}")
#         self.answer.delete(0, tk.END)

#     def check_answer(self):
#         if not self.current:
#             return

#         user = self.answer.get()
#         correct = self.current["georgian"]

#         if normalize(user) == normalize(correct):
#             messagebox.showinfo("შედეგი", "სწორია! ✅")
#         else:
#             messagebox.showinfo("შედეგი", f"არასწორია.\nსწორი პასუხი: {correct}")

#         self.next_word()


# def open_gui(words):
#     root = tk.Tk()
#     EnglishGUI(root, words)
#     root.mainloop()


# # -----------------------------
# # მთავარი მენიუ
# # -----------------------------

# def main():
#     words = load_words()

#     while True:
#         print("=== ინგლისური ენის სასწავლი პროგრამა ===")
#         print("1) ახალი სიტყვის დამატება")
#         print("2) ყველა სიტყვის ჩვენება")
#         print("3) სიტყვების ფილტრაცია დონით")
#         print("4) წინადადების აწყობა")
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
#             open_gui(words)
#         elif choice == "7":
#             print("ნახვამდის! 👋")
#             break
#         else:
#             print("არასწორი არჩევანი.\n")


# if __name__ == "__main__":
#     main()




