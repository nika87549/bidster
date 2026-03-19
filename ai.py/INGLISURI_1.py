#                                             ნაწილი 1 — Storage System (JSON + Categories + Structure)


import json
import os

# -----------------------------
#   მონაცემების ფაილი
# -----------------------------
DATA_FILE = "english_words_full.json"


# -----------------------------
#   სტანდარტული კატეგორიები
# -----------------------------
DEFAULT_CATEGORIES = [
    "verbs",
    "nouns",
    "adjectives",
    "adverbs",
    "phrases",
    "food",
    "travel",
    "school",
    "business",
    "daily life",
    "emotions",
    "animals",
    "colors",
    "numbers",
    "technology",
    "slang"
]


# -----------------------------
#   მონაცემების ჩატვირთვა
# -----------------------------
def load_data():
    """
    ტვირთავს JSON ფაილს.
    თუ ფაილი არ არსებობს ან გაფუჭებულია — ქმნის ცარიელ სტრუქტურას.
    სტრუქტურა:
    {
        "words": [...],
        "categories": [...]
    }
    """
    if not os.path.exists(DATA_FILE):
        return {
            "words": [],
            "categories": DEFAULT_CATEGORIES.copy()
        }

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

            # თუ რამე აკლია, ვავსებთ
            if "words" not in data:
                data["words"] = []
            if "categories" not in data:
                data["categories"] = DEFAULT_CATEGORIES.copy()

            return data

    except (json.JSONDecodeError, FileNotFoundError):
        return {
            "words": [],
            "categories": DEFAULT_CATEGORIES.copy()
        }


# -----------------------------
#   მონაცემების შენახვა
# -----------------------------
def save_data(data):
    """
    ინახავს მთელ მონაცემთა სტრუქტურას JSON ფაილში.
    """
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# -----------------------------
#   ახალი კატეგორიის დამატება
# -----------------------------
def add_category(data, category_name):
    """
    ამატებს ახალ კატეგორიას.
    მომხმარებელს შეუძლია შექმნას ნებისმიერი კატეგორია.
    """
    category_name = category_name.strip().lower()

    if not category_name:
        return False, "კატეგორიის სახელი ცარიელია."

    if category_name in data["categories"]:
        return False, "ეს კატეგორია უკვე არსებობს."

    data["categories"].append(category_name)
    save_data(data)
    return True, f"კატეგორია '{category_name}' წარმატებით დაემატა."


# -----------------------------
#   სიტყვის დამატება
# -----------------------------
def add_word(data, english, georgian, level, category, example=""):
    """
    ამატებს ახალ სიტყვას მონაცემთა ბაზაში.
    სტრუქტურა:
    {
        "english": "...",
        "georgian": "...",
        "level": "A1",
        "category": "verbs",
        "example": "..."
    }
    """

    word = {
        "english": english.strip(),
        "georgian": georgian.strip(),
        "level": level.strip(),
        "category": category.strip().lower(),
        "example": example.strip()
    }

    data["words"].append(word)
    save_data(data)
    return True


# -----------------------------
#   სიტყვების ფილტრაცია
# -----------------------------
def filter_by_level(data, level):
    return [w for w in data["words"] if w["level"].lower() == level.lower()]


def filter_by_category(data, category):
    return [w for w in data["words"] if w["category"].lower() == category.lower()]


# -----------------------------
#   წინადადების აწყობა
# -----------------------------
def build_sentence_from_indices(data, indices):
    """
    იღებს ინდექსების სიას და აწყობს წინადადებას.
    """
    words = data["words"]
    selected = []

    for idx in indices:
        if 1 <= idx <= len(words):
            selected.append(words[idx - 1]["english"])

    return " ".join(selected)



#                                                                    ნაწილი 2 — Console Menu 
import random

# -----------------------------------------
#   კონსოლური მენიუს ფუნქციები
# -----------------------------------------

def console_add_word(data):
    print("\n--- ახალი სიტყვის დამატება ---")

    english = input("ინგლისური სიტყვა: ").strip()
    if not english:
        print("სიტყვა აუცილებელია.\n")
        return

    georgian = input("ქართული თარგმანი: ").strip()
    if not georgian:
        print("თარგმანი აუცილებელია.\n")
        return

    level = input("დონე (A1, A2, B1...): ").strip() or "A1"

    print("\nარსებული კატეგორიები:")
    for c in data["categories"]:
        print(" -", c)

    category = input("\nაირჩიე კატეგორია ან ჩაწერე ახალი: ").strip().lower()

    # თუ კატეგორია არ არსებობს — ვქმნით
    if category not in data["categories"]:
        ok, msg = add_category(data, category)
        print(msg)

    example = input("მაგალითი წინადადება (არასავალდებულო): ").strip()

    add_word(data, english, georgian, level, category, example)
    print(f"სიტყვა '{english}' წარმატებით დაემატა.\n")


def console_show_all(data):
    print("\n--- ყველა სიტყვა ---")
    if not data["words"]:
        print("სიტყვები ჯერ არ გაქვს.\n")
        return

    for i, w in enumerate(data["words"], start=1):
        print(f"{i}. {w['english']} - {w['georgian']} "
              f"(დონე: {w['level']}, კატეგორია: {w['category']})")
    print()


def console_filter_by_level(data):
    level = input("\nშეიყვანე დონე (A1, A2, B1...): ").strip()
    results = filter_by_level(data, level)

    if not results:
        print("ამ დონის სიტყვები არ მოიძებნა.\n")
        return

    print(f"\n--- {level} დონის სიტყვები ---")
    for i, w in enumerate(results, start=1):
        print(f"{i}. {w['english']} - {w['georgian']}")
    print()


def console_filter_by_category(data):
    print("\nარსებული კატეგორიები:")
    for c in data["categories"]:
        print(" -", c)

    category = input("\nაირჩიე კატეგორია: ").strip().lower()
    results = filter_by_category(data, category)

    if not results:
        print("ამ კატეგორიის სიტყვები არ მოიძებნა.\n")
        return

    print(f"\n--- '{category}' კატეგორიის სიტყვები ---")
    for i, w in enumerate(results, start=1):
        print(f"{i}. {w['english']} - {w['georgian']}")
    print()


def console_build_sentence(data):
    if not data["words"]:
        print("ჯერ სიტყვები დაამატე.\n")
        return

    console_show_all(data)
    raw = input("აირჩიე ნომრები (მაგ: 1 3 4): ").strip()

    try:
        indices = [int(x) for x in raw.split()]
    except ValueError:
        print("ნომრები არასწორია.\n")
        return

    sentence = build_sentence_from_indices(data, indices)
    print("\nშენი წინადადება:")
    print(sentence + "\n")


def normalize_answer(s):
    return " ".join(s.strip().lower().split())


def console_quiz(data):
    if not data["words"]:
        print("ქვიზისთვის ჯერ სიტყვები დაამატე.\n")
        return

    num = min(5, len(data["words"]))
    questions = random.sample(data["words"], num)
    score = 0

    print("\n--- ქვიზი ---")

    for i, w in enumerate(questions, start=1):
        print(f"\nკითხვა {i}/{num}")
        print(f"ინგლისური სიტყვა: {w['english']}")
        ans = input("ქართული თარგმანი: ")

        if normalize_answer(ans) == normalize_answer(w["georgian"]):
            print("სწორია! ✅")
            score += 1
        else:
            print(f"არასწორია. სწორი პასუხი: {w['georgian']}")

    print(f"\nშენი შედეგი: {score}/{num}\n")


# -----------------------------------------
#   მთავარი კონსოლური მენიუ
# -----------------------------------------

def console_menu(data):
    while True:
        print("=== ინგლისური ენის სასწავლი პროგრამა ===")
        print("1) ახალი სიტყვის დამატება")
        print("2) ყველა სიტყვის ჩვენება")
        print("3) სიტყვების ფილტრაცია დონით")
        print("4) სიტყვების ფილტრაცია კატეგორიით")
        print("5) წინადადების აწყობა")
        print("6) ქვიზი (კონსოლი)")
        print("7) ახალი კატეგორიის დამატება")
        print("8) GUI ფანჯარა")
        print("9) გრამატიკის მოდული")
        print("0) გამოსვლა")

        choice = input("აირჩიე (0-9): ").strip()

        if choice == "1":
            console_add_word(data)
        elif choice == "2":
            console_show_all(data)
        elif choice == "3":
            console_filter_by_level(data)
        elif choice == "4":
            console_filter_by_category(data)
        elif choice == "5":
            console_build_sentence(data)
        elif choice == "6":
            console_quiz(data)
        elif choice == "7":
            name = input("შეიყვანე ახალი კატეგორია: ").strip().lower()
            ok, msg = add_category(data, name)
            print(msg + "\n")
        elif choice == "8":
            return "open_gui"   # GUI-ს შემდეგ ნაწილში დავამატებთ
        elif choice == "9":
            return "grammar"    # გრამატიკის მოდული შემდეგ ნაწილში შევა
        elif choice == "0":
            print("ნახვამდის! 👋")
            return "exit"
        else:
            print("არასწორი არჩევანი.\n")
          


#                                                             ნაწილი 3 — Grammar Module

#           -----------------------------------------
#   გრამატიკის მოდული
# -----------------------------------------

def grammar_menu():
    while True:
        print("\n=== გრამატიკის მოდული ===")
        print("1) Present Simple")
        print("2) Past Simple")
        print("3) Future (will)")
        print("4) Modal Verbs")
        print("0) უკან დაბრუნება")

        choice = input("აირჩიე (0-4): ").strip()

        if choice == "1":
            grammar_present_simple()
        elif choice == "2":
            grammar_past_simple()
        elif choice == "3":
            grammar_future()
        elif choice == "4":
            grammar_modal_verbs()
        elif choice == "0":
            return
        else:
            print("არასწორი არჩევანი.\n")


# -----------------------------------------
#   Present Simple
# -----------------------------------------

def grammar_present_simple():
    print("\n--- Present Simple ---")
    print("""
Present Simple გამოიყენება:
- ჩვევები
- ფაქტები
- რუტინა
- მუდმივი სიმართლეები

ფორმულა:
I/You/We/They + verb
He/She/It + verb + s/es

მაგალითები:
- I work every day.
- She plays tennis.
- Water boils at 100°C.
""")

    print("სავარჯიშო:")
    print("თარგმნე ინგლისურად: „ის სწავლობს ყოველდღე“")

    ans = input("პასუხი: ").strip().lower()
    correct = ["she studies every day", "she studies everyday"]

    if ans in correct:
        print("სწორია! ✅\n")
    else:
        print("არასწორია. სწორი პასუხი: She studies every day.\n")


# -----------------------------------------
#   Past Simple
# -----------------------------------------

def grammar_past_simple():
    print("\n--- Past Simple ---")
    print("""
Past Simple გამოიყენება:
- დასრულებული მოქმედებები წარსულში
- კონკრეტული დროით: yesterday, last year, in 2010...

ფორმულა:
Verb + ed (რეგულარული)
Irregular verbs — სპეციალური ფორმა

მაგალითები:
- I visited London last year.
- She went to school yesterday.
""")

    print("სავარჯიშო:")
    print("თარგმნე ინგლისურად: „ის წავიდა სახლში“")

    ans = input("პასუხი: ").strip().lower()
    correct = ["he went home", "she went home"]

    if ans in correct:
        print("სწორია! ✅\n")
    else:
        print("არასწორია. სწორი პასუხი: He went home.\n")


# -----------------------------------------
#   Future (will)
# -----------------------------------------

def grammar_future():
    print("\n--- Future (will) ---")
    print("""
Future Simple გამოიყენება:
- სპონტანური გადაწყვეტილებები
- პროგნოზები
- დაპირებები

ფორმულა:
will + verb

მაგალითები:
- I will call you later.
- It will rain tomorrow.
""")

    print("სავარჯიშო:")
    print("თარგმნე ინგლისურად: „მე დაგირეკავ მოგვიანებით“")

    ans = input("პასუხი: ").strip().lower()
    correct = ["i will call you later"]

    if ans in correct:
        print("სწორია! ✅\n")
    else:
        print("არასწორია. სწორი პასუხი: I will call you later.\n")


# -----------------------------------------
#   Modal Verbs
# -----------------------------------------

def grammar_modal_verbs():
    print("\n--- Modal Verbs ---")
    print("""
მოდალური ზმნები:
can, could, must, should, may, might

გამოიყენება:
- შესაძლებლობა
- ნებართვა
- რჩევა
- აუცილებლობა

მაგალითები:
- I can swim.
- You should study more.
- She must go now.
""")

    print("სავარჯიშო:")
    print("თარგმნე ინგლისურად: „შენ უნდა ისწავლო მეტი“")

    ans = input("პასუხი: ").strip().lower()
    correct = ["you should study more"]

    if ans in correct:
        print("სწორია! ✅\n")
    else:
        print("არასწორია. სწორი პასუხი: You should study more.\n")


#                                                  ნაწილი 4 — Audio Pronunciation (pyttsx3)

# -----------------------------------------
#   აუდიო გამოთქმა (Text-to-Speech)
# -----------------------------------------

import pyttsx3

# pyttsx3 ძრავის ინიციალიზაცია
tts_engine = pyttsx3.init()

# სურვილისამებრ — ხმა ინგლისურად
# (Windows-ზე ჩვეულებრივ 1 ან 2 ხმაა)
voices = tts_engine.getProperty('voices')
for v in voices:
    if "English" in v.name or "en" in v.id.lower():
        tts_engine.setProperty('voice', v.id)
        break


def speak_word(word):
    """
    ხმოვანი წარმოთქმა.
    word — ინგლისური სიტყვა ან წინადადება.
    """
    try:
        tts_engine.say(word)
        tts_engine.runAndWait()
        return True
    except Exception as e:
        print("აუდიო შეცდომა:", e)
        return False


def console_speak_word():
    """
    კონსოლიდან სიტყვის გამოთქმა.
    """
    word = input("ჩაწერე ინგლისური სიტყვა გამოსათქმელად: ").strip()
    if not word:
        print("სიტყვა ცარიელია.\n")
        return

    print(f"გამოთქმა: {word}")
    speak_word(word)
    print()

# # #                                                         ნაწილი 5 — Online Dictionary API (dictionaryapi.dev)

# -----------------------------------------
#   ონლაინ ლექსიკონი (Dictionary API)
# -----------------------------------------

import requests

def fetch_dictionary_data(word):
    """
    იღებს ინგლისური სიტყვის განმარტებას, სინონიმებს და მაგალითებს
    dictionaryapi.dev API-დან.

    აბრუნებს dict სტრუქტურას:
    {
        "word": "...",
        "phonetic": "...",
        "definitions": [...],
        "synonyms": [...],
        "examples": [...]
    }
    """

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return None

        data = response.json()[0]

        result = {
            "word": data.get("word", ""),
            "phonetic": data.get("phonetic", ""),
            "definitions": [],
            "synonyms": [],
            "examples": []
        }

        # Parsing meanings
        meanings = data.get("meanings", [])
        for m in meanings:
            defs = m.get("definitions", [])
            for d in defs:
                if "definition" in d:
                    result["definitions"].append(d["definition"])
                if "example" in d:
                    result["examples"].append(d["example"])
                if "synonyms" in d:
                    result["synonyms"].extend(d["synonyms"])

        # Remove duplicates
        result["synonyms"] = list(set(result["synonyms"]))

        return result

    except Exception as e:
        print("Dictionary API error:", e)
        return None


def console_dictionary_lookup():
    """
    კონსოლური ძიება ონლაინ ლექსიკონში.
    """
    word = input("ჩაწერე ინგლისური სიტყვა: ").strip()
    if not word:
        print("სიტყვა ცარიელია.\n")
        return

    print("მიმდინარეობს ძიება...\n")
    data = fetch_dictionary_data(word)

    if not data:
        print("ინფორმაცია ვერ მოიძებნა.\n")
        return

    print(f"სიტყვა: {data['word']}")
    print(f"ფონეტიკა: {data['phonetic']}\n")

    print("განმარტებები:")
    for d in data["definitions"][:5]:
        print(" -", d)

    if data["synonyms"]:
        print("\nსინონიმები:")
        print(", ".join(data["synonyms"][:10]))

    if data["examples"]:
        print("\nმაგალითები:")
        for ex in data["examples"][:5]:
            print(" -", ex)

    print()

#                                                    ნაწილი 6 — tkinter GUI

# -----------------------------------------
#   tkinter GUI — მთავარი ფანჯარა
# -----------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox

def open_gui(data):
    root = tk.Tk()
    root.title("English Learning Program — GUI")
    root.geometry("900x600")

    app = EnglishGUI(root, data)
    root.mainloop()


class EnglishGUI:
    def __init__(self, root, data):
        self.root = root
        self.data = data
        self.words = data["words"]
        self.categories = data["categories"]

        # -----------------------------
        #   მთავარი ჩარჩოები
        # -----------------------------
        main_frame = tk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # მარცხენა პანელი — კატეგორიები
        left_frame = tk.Frame(main_frame, width=150)
        left_frame.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(left_frame, text="კატეგორიები", font=("Arial", 12, "bold")).pack(pady=5)

        self.category_list = tk.Listbox(left_frame)
        self.category_list.pack(fill=tk.Y, expand=True)

        for c in self.categories:
            self.category_list.insert(tk.END, c)

        self.category_list.bind("<<ListboxSelect>>", self.filter_by_category)

        # -----------------------------
        #   შუა პანელი — სიტყვების სია
        # -----------------------------
        center_frame = tk.Frame(main_frame)
        center_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tk.Label(center_frame, text="სიტყვები", font=("Arial", 12, "bold")).pack(pady=5)

        self.word_list = tk.Listbox(center_frame)
        self.word_list.pack(fill=tk.BOTH, expand=True)

        self.word_list.bind("<<ListboxSelect>>", self.show_word_details)

        self.refresh_word_list()

        # -----------------------------
        #   მარჯვენა პანელი — დეტალები
        # -----------------------------
        right_frame = tk.Frame(main_frame, width=300)
        right_frame.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(right_frame, text="დეტალები", font=("Arial", 12, "bold")).pack(pady=5)

        self.details_text = tk.Text(right_frame, height=15, width=40)
        self.details_text.pack()

        # -----------------------------
        #   ღილაკები — ქვიზი, აუდიო, API
        # -----------------------------
        btn_frame = tk.Frame(right_frame)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="🔊 გამოთქმა", command=self.pronounce_word).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="🌐 Online Definition", command=self.lookup_online).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="🧠 Quiz", command=self.start_quiz).grid(row=1, column=0, columnspan=2, pady=5)

        # -----------------------------
        #   ახალი სიტყვის დამატება
        # -----------------------------
        add_frame = tk.LabelFrame(right_frame, text="ახალი სიტყვის დამატება")
        add_frame.pack(fill=tk.X, pady=10)

        tk.Label(add_frame, text="ინგლისური:").pack(anchor="w")
        self.entry_eng = tk.Entry(add_frame)
        self.entry_eng.pack(fill=tk.X)

        tk.Label(add_frame, text="ქართული:").pack(anchor="w")
        self.entry_geo = tk.Entry(add_frame)
        self.entry_geo.pack(fill=tk.X)

        tk.Label(add_frame, text="დონე (A1, A2...):").pack(anchor="w")
        self.entry_level = tk.Entry(add_frame)
        self.entry_level.pack(fill=tk.X)

        tk.Label(add_frame, text="კატეგორია:").pack(anchor="w")
        self.combo_category = ttk.Combobox(add_frame, values=self.categories)
        self.combo_category.pack(fill=tk.X)

        tk.Label(add_frame, text="მაგალითი:").pack(anchor="w")
        self.entry_example = tk.Entry(add_frame)
        self.entry_example.pack(fill=tk.X)

        tk.Button(add_frame, text="დამატება", command=self.add_new_word).pack(pady=5)

    # -----------------------------------------
    #   Refresh word list
    # -----------------------------------------
    def refresh_word_list(self, filtered=None):
        self.word_list.delete(0, tk.END)
        words = filtered if filtered else self.words
        for w in words:
            self.word_list.insert(tk.END, w["english"])

    # -----------------------------------------
    #   Filter by category
    # -----------------------------------------
    def filter_by_category(self, event):
        if not self.category_list.curselection():
            return

        idx = self.category_list.curselection()[0]
        category = self.categories[idx]

        filtered = [w for w in self.words if w["category"] == category]
        self.refresh_word_list(filtered)

    # -----------------------------------------
    #   Show word details
    # -----------------------------------------
    def show_word_details(self, event):
        if not self.word_list.curselection():
            return

        idx = self.word_list.curselection()[0]
        word = self.words[idx]

        text = (
            f"ინგლისური: {word['english']}\n"
            f"ქართული: {word['georgian']}\n"
            f"დონე: {word['level']}\n"
            f"კატეგორია: {word['category']}\n"
        )

        if word["example"]:
            text += f"\nმაგალითი:\n{word['example']}"

        self.details_text.delete("1.0", tk.END)
        self.details_text.insert(tk.END, text)

    # -----------------------------------------
    #   Add new word
    # -----------------------------------------
    def add_new_word(self):
        eng = self.entry_eng.get().strip()
        geo = self.entry_geo.get().strip()
        level = self.entry_level.get().strip() or "A1"
        category = self.combo_category.get().strip().lower()
        example = self.entry_example.get().strip()

        if not eng or not geo:
            messagebox.showerror("შეცდომა", "ინგლისური და ქართული აუცილებელია.")
            return

        # ახალი კატეგორია?
        if category not in self.categories:
            ok, msg = add_category(self.data, category)
            messagebox.showinfo("კატეგორია", msg)
            self.categories = self.data["categories"]
            self.combo_category["values"] = self.categories
            self.category_list.insert(tk.END, category)

        add_word(self.data, eng, geo, level, category, example)
        self.words = self.data["words"]

        self.refresh_word_list()
        messagebox.showinfo("წარმატება", f"სიტყვა '{eng}' დაემატა.")

    # -----------------------------------------
    #   Pronounce word
    # -----------------------------------------
    def pronounce_word(self):
        if not self.word_list.curselection():
            return

        idx = self.word_list.curselection()[0]
        word = self.words[idx]["english"]
        speak_word(word)

    # -----------------------------------------
    #   Online dictionary lookup
    # -----------------------------------------
    def lookup_online(self):
        if not self.word_list.curselection():
            return

        idx = self.word_list.curselection()[0]
        word = self.words[idx]["english"]

        data = fetch_dictionary_data(word)
        if not data:
            messagebox.showerror("შეცდომა", "ინფორმაცია ვერ მოიძებნა.")
            return

        text = f"სიტყვა: {data['word']}\n\n"

        if data["phonetic"]:
            text += f"ფონეტიკა: {data['phonetic']}\n\n"

        if data["definitions"]:
            text += "განმარტებები:\n"
            for d in data["definitions"][:5]:
                text += f" - {d}\n"

        if data["synonyms"]:
            text += "\nსინონიმები:\n" + ", ".join(data["synonyms"][:10]) + "\n"

        if data["examples"]:
            text += "\nმაგალითები:\n"
            for ex in data["examples"][:5]:
                text += f" - {ex}\n"

        messagebox.showinfo("Dictionary", text)

    # -----------------------------------------
    #   GUI Quiz
    # -----------------------------------------
    def start_quiz(self):
        QuizWindow(self.root, self.words)


# -----------------------------------------
#   Quiz Window
# -----------------------------------------

class QuizWindow:
    def __init__(self, root, words):
        self.words = words
        self.index = 0
        self.score = 0

        self.window = tk.Toplevel(root)
        self.window.title("Quiz")
        self.window.geometry("400x300")

        self.label_word = tk.Label(self.window, text="", font=("Arial", 14))
        self.label_word.pack(pady=20)

        self.entry_answer = tk.Entry(self.window, font=("Arial", 12))
        self.entry_answer.pack()

        tk.Button(self.window, text="პასუხი", command=self.check_answer).pack(pady=10)

        self.label_result = tk.Label(self.window, text="", font=("Arial", 12))
        self.label_result.pack()

        random.shuffle(self.words)
        self.next_question()

    def next_question(self):
        if self.index >= len(self.words):
            self.label_word.config(text=f"ქვიზი დასრულდა!\nქულა: {self.score}/{len(self.words)}")
            return

        self.current = self.words[self.index]
        self.label_word.config(text=f"ინგლისური: {self.current['english']}")
        self.entry_answer.delete(0, tk.END)

    def check_answer(self):
        ans = self.entry_answer.get().strip().lower()
        correct = self.current["georgian"].lower()

        if ans == correct:
            self.score += 1
            self.label_result.config(text="სწორია! ✅", fg="green")
        else:
            self.label_result.config(text=f"არასწორია. სწორი პასუხი: {correct}", fg="red")

        self.index += 1
        self.window.after(1000, self.next_question)


#                                                                     ნაწილი 7 — main() და სრული გაერთიანება

# -----------------------------------------
#   მთავარი გაერთიანება — main()
# -----------------------------------------

def main():
    # ჩატვირთვა JSON-დან
    data = load_data()

    while True:
        action = console_menu(data)

        if action == "exit":
            break

        elif action == "open_gui":
            open_gui(data)

        elif action == "grammar":
            grammar_menu()


# პროგრამის გაშვება
if __name__ == "__main__":
    main()
