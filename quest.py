# import customtkinter as ctk
# from tkinter import messagebox
#
# # Настройка темы
# ctk.set_appearance_mode("light")
# ctk.set_default_color_theme("blue")
#
# QUESTIONS = [
#     {
#         "question": "Вопрос 1: Какой у нас общий любимый напиток на перерыве?",
#         "answer": "кофе"  # Ответ в нижнем регистре для упрощения сравнения
#     },
#     {
#         "question": "Вопрос 2: В каком месяце у тебя день рождения? (укажи название, например: 'март')",
#         "answer": "ноябрь"
#     },
#     {
#         "question": "Вопрос 3: Как зовут нашего общего коллегу, который всегда носит красные кроссовки?",
#         "answer": "алексей"
#     }
# ]
#
# class QuestApp(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#         self.title("🎁 Мини-квест: Найди крем для рук!")
#         self.geometry("500x300")
#         self.resizable(False, False)
#         self.current_question = 0
#         self.setup_ui()
#
#     def setup_ui(self):
#         self.label = ctk.CTkLabel(
#             self,
#             text=QUESTIONS[self.current_question]["question"],
#             font=("Arial", 16),
#             wraplength=450,
#             justify="center"
#         )
#         self.label.pack(pady=30)
#
#         self.entry = ctk.CTkEntry(self, width=300, font=("Arial", 14))
#         self.entry.pack(pady=10)
#         self.entry.bind("<Return>", self.check_answer)  # Enter для подтверждения
#
#         self.button = ctk.CTkButton(
#             self,
#             text="Проверить ответ",
#             command=self.check_answer,
#             font=("Arial", 14)
#         )
#         self.button.pack(pady=20)
#
#     def check_answer(self, event=None):
#         user_answer = self.entry.get().strip().lower()
#         correct_answer = QUESTIONS[self.current_question]["answer"]
#
#         if user_answer == correct_answer:
#             self.current_question += 1
#             if self.current_question < len(QUESTIONS):
#                 # Следующий вопрос
#                 self.label.configure(text=QUESTIONS[self.current_question]["question"])
#                 self.entry.delete(0, "end")
#             else:
#                 # Конец квеста
#                 self.show_success()
#         else:
#             messagebox.showerror("Неверно!", "Попробуй ещё раз 😊")
#
#     def show_success(self):
#         # Очистка интерфейса
#         for widget in self.winfo_children():
#             widget.destroy()
#
#         success_label = ctk.CTkLabel(
#             self,
#             text="🎉 Поздравляю! Ты прошёл квест!",
#             font=("Arial", 18, "bold")
#         )
#         success_label.pack(pady=30)
#
#         message = ctk.CTkLabel(
#             self,
#             text="Твой подарок — крем для рук —\nлежит в верхнем ящике моего стола.\nНаслаждайся заботой о коже! 💆‍♀️✨",
#             font=("Arial", 14),
#             justify="center",
#             wraplength=450
#         )
#         message.pack(pady=20)
#
#         close_button = ctk.CTkButton(
#             self,
#             text="Закрыть",
#             command=self.destroy,
#             font=("Arial", 14)
#         )
#         close_button.pack(pady=20)
#
# if __name__ == "__main__":
#     app = QuestApp()
#     app.mainloop()

import tkinter as tk
from tkinter import messagebox
import sys
import os

# Настройка цветов для красивого интерфейса
COLORS = {
    "bg": "#2b2b2b",
    "fg": "#ffffff",
    "accent": "#FF6B9D",
    "accent_hover": "#E55A8A",
    "success": "#50C878",
    "progress": "#3B8ED0",
    "gold": "#FFD700"
}


class QuestApp:
    def __init__(self):
        self.current_question = 0
        self.questions = [
            {
                "question": "🎯 ВОПРОС 1/3\n\nБез чего не может работать ни программист, ни повар,\nЧто защищает от холода и ветра,\nИ бывает лечебным, увлажняющим, а иногда и кремовым?",
                "answers": ["Голова", "Руки", "Ноги", "Сердце"],
                "correct": 1,
                "hint": "Подсказка: именно ими ты печатаешь этот текст 🤔"
            },
            {
                "question": "🎯 ВОПРОС 2/3\n\nНе в саду, а в тюбике или баночке,\nПачули, лаванда или ваниль…\nУгадай, что это может быть?",
                "answers": ["Цветок", "Аромат", "Еда", "Напиток"],
                "correct": 1,
                "hint": "Подсказка: почувствуй запах кофе на кухне ☕"
            },
            {
                "question": "🎯 ВОПРОС 3/3\n\nФинальная загвоздка! Вспомни, что говорят:\n'Сухие…' – жалоба, которую часто слышат в офисах.\nЧто мажут, чтобы вернуть мягкость и нежность?",
                "answers": ["Хлеб", "Кожа", "Волосы", "Обувь"],
                "correct": 1,
                "hint": "Подсказка: ищи там, где хранят заботу о себе 💫"
            }
        ]

        self.setup_ui()

    def setup_ui(self):
        self.root = tk.Tk()
        self.root.title("🎁 Тайный Квест для Коллеги")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        self.root.configure(bg=COLORS["bg"])

        # Центрирование окна
        self.center_window()

        # Главный фрейм
        self.main_frame = tk.Frame(self.root, bg=COLORS["bg"])
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Заголовок
        self.title_label = tk.Label(
            self.main_frame,
            text="🎁 ТАЙНЫЙ КВЕСТ 🎁",
            font=("Arial", 24, "bold"),
            fg=COLORS["gold"],
            bg=COLORS["bg"]
        )
        self.title_label.pack(pady=20)

        # Текст приветствия
        self.welcome_text = tk.Label(
            self.main_frame,
            text="Привет! Ты нашёл секретную программу!\n\nОтветь на 3 вопроса, чтобы узнать,\nгде спрятан твой подарок! 💝",
            font=("Arial", 16),
            fg=COLORS["fg"],
            bg=COLORS["bg"],
            justify="center"
        )
        self.welcome_text.pack(pady=10)

        # Кнопка начала
        self.start_button = tk.Button(
            self.main_frame,
            text="НАЧАТЬ КВЕСТ!",
            command=self.start_quest,
            font=("Arial", 16, "bold"),
            bg=COLORS["accent"],
            fg="white",
            activebackground=COLORS["accent_hover"],
            activeforeground="white",
            height=2,
            width=20,
            cursor="hand2",
            relief="flat",
            bd=0
        )
        self.start_button.pack(pady=20)

        # Прогресс бар (имитация)
        self.progress_frame = tk.Frame(self.main_frame, bg=COLORS["bg"])
        self.progress_frame.pack(pady=10, fill="x", padx=50)

        self.progress_canvas = tk.Canvas(self.progress_frame, height=20, bg=COLORS["bg"], highlightthickness=0)
        self.progress_canvas.pack(fill="x")
        self.progress_bar = self.progress_canvas.create_rectangle(0, 0, 0, 20, fill=COLORS["progress"], outline="")

        # Текст вопроса
        self.question_label = tk.Label(
            self.main_frame,
            text="",
            font=("Arial", 14),
            fg=COLORS["fg"],
            bg=COLORS["bg"],
            wraplength=500,
            justify="center"
        )

        # Фрейм для кнопок ответов
        self.answers_frame = tk.Frame(self.main_frame, bg=COLORS["bg"])

        # Кнопка подсказки
        self.hint_button = tk.Button(
            self.main_frame,
            text="💡 Подсказка",
            command=self.show_hint,
            font=("Arial", 12),
            bg=COLORS["bg"],
            fg=COLORS["fg"],
            activebackground=COLORS["bg"],
            activeforeground=COLORS["fg"],
            relief="flat",
            bd=1,
            cursor="hand2"
        )

    def center_window(self):
        """Центрирует окно на экране"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def start_quest(self):
        self.start_button.pack_forget()
        self.welcome_text.pack_forget()

        self.question_label.pack(pady=20)
        self.answers_frame.pack(pady=10, fill="both", expand=True)
        self.hint_button.pack(pady=10)

        self.show_question()

    def show_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.configure(text=question_data["question"])

            # Очищаем старые кнопки
            for widget in self.answers_frame.winfo_children():
                widget.destroy()

            # Создаем новые кнопки ответов
            for i, answer in enumerate(question_data["answers"]):
                btn = tk.Button(
                    self.answers_frame,
                    text=answer,
                    command=lambda idx=i: self.check_answer(idx),
                    font=("Arial", 14),
                    height=2,
                    width=20,
                    bg="#3B8ED0",
                    fg="white",
                    activebackground="#36719F",
                    activeforeground="white",
                    cursor="hand2",
                    relief="flat",
                    bd=0
                )
                btn.pack(pady=5, fill="x", padx=10)

            # Обновляем прогресс
            progress_width = (self.current_question / len(self.questions)) * 500
            self.progress_canvas.coords(self.progress_bar, 0, 0, progress_width, 20)

    def check_answer(self, answer_index):
        question_data = self.questions[self.current_question]

        if answer_index == question_data["correct"]:
            self.current_question += 1

            if self.current_question < len(self.questions):
                messagebox.showinfo("✅ Правильно!", "Отлично! Переходим к следующему вопросу!")
                self.show_question()
            else:
                self.show_final()
        else:
            messagebox.showerror("❌ Неправильно", "Попробуй еще раз! Может, подсказка поможет?")

    def show_hint(self):
        question_data = self.questions[self.current_question]
        messagebox.showinfo("💡 Подсказка", question_data["hint"])

    def show_final(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Финальное сообщение
        final_text = """🎉 ПОЗДРАВЛЯЮ! Ты прошел квест! 🎉

Твой подарок ждет тебя там, где хранят заботу о руках 💝

Ищи крем для рук в ящике с надписью:
'Для того, чьи руки творят добро и магию каждый день'

Спасибо за твой труд! 💫

P.S. Надеюсь, тебе понравился这个小 квест! 😊"""

        final_label = tk.Label(
            self.main_frame,
            text=final_text,
            font=("Arial", 14),
            fg=COLORS["fg"],
            bg=COLORS["bg"],
            justify="center",
            wraplength=500
        )
        final_label.pack(pady=30, padx=20)

        # Кнопка выхода
        exit_btn = tk.Button(
            self.main_frame,
            text="Закрыть программу",
            command=self.root.destroy,
            font=("Arial", 14, "bold"),
            bg=COLORS["success"],
            fg="white",
            activebackground="#40A060",
            activeforeground="white",
            height=2,
            width=20,
            cursor="hand2",
            relief="flat",
            bd=0
        )
        exit_btn.pack(pady=20)

        # Полный прогресс
        self.progress_canvas.coords(self.progress_bar, 0, 0, 500, 20)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = QuestApp()
    app.run()