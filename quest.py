
import tkinter as tk
from tkinter import messagebox

# Настройка цветов для красивого интерфейса
COLORS = {
    "bg": "#765d69",
    "fg": "#fcd0ba",
    "accent": "#8fb9ab",
    "accent_hover": "#E55A8A",
    "success": "#50C878",
    "gold": "#fefad4"
}


class QuestApp:
    def __init__(self):
        self.current_question = 0
        self.questions = [
            {
                "question": "🎯 ВОПРОС 1/7\n\n«Что уходит быстрее всего, когда мы погружены в задачу?»",
                "answers": ["Кофе", "Батарея", "Время", "Интернет"],
                "correct": 2,
                "hint": "Подсказка: Кажется, только сел за работу — а уже обед!"
            },
            {
                "question": "🎯 ВОПРОС 2/7\n\nЧто все обещают написать 'потом', но 'потом' никогда не наступает?",
                "answers": ["Документация к коду", "Завещание", "Письмо Деду Морозу", "Роман"],
                "correct": 0,
                "hint": "Подсказка: Самая популярная фраза: 'и так все понятно'"
            },
            {
                "question": "🎯 ВОПРОС 3/7\n\nЧто наступает внезапно, как налоговая проверка, и так же не радует?",
                "answers": ["Июльская жара", "День рождение тещи", "Понедельник"],
                "correct": 2,
                "hint": "Подсказка:  Утро этого дня - это как холодный душ без предупреждения"
            },
            {
                "question": "🎯 ВОПРОС 4/7\n\nЧто пахнет так соблазнительно, что может остановить работу всего отдела?",
                "answers": ["Новые духи коллеги", "Еда в микроволновке", "Деньги", "Новые ароматизированные маркеры"],
                "correct": 1,
                "hint": "Подсказка:  Особенно когда кто-то разогревает рыбу"
            },
            {
                "question": "🎯 ВОПРОС 5/7\n\nЧто появляется внезапно, как призрак, и заставляет всех работать в 3 раза быстрее?",
                "answers": ["Уборщица", "Вдохновение", "Внезапный дедлайн", "Офисный кот"],
                "correct": 2,
                "hint": "Подсказка:  Чаще всего возникает в пятницу"
            },
            {
                "question": "🎯 ВОПРОС 6/7\n\nЧто в офисном кабинете имеет 'окна', но не является стеклянным?",
                "answers": ["Аквариум", "Микроволновка", "Окно", "Картина", "Монитор"],
                "correct": 4,
                "hint": "Подсказка:  На него мы смотрим больше всего в течение дня"
            },
            {
                "question": "🎯 ФИНАЛЬНЫЙ ВОПРОС\n\nКакая фамилия у директора АВАНТИСА???(чур на корп.сайт не заходить)",
                "answers": ["Сайфутинов", "Сайфудинов", "Сайфутдинов", "Сайфетдинов", "Сафутдинов"],
                "correct": 2,
                "hint": "Подсказка: ну тут без меня, прости"
            }
        ]

        self.setup_ui()

    def setup_ui(self):
        self.root = tk.Tk()
        self.root.title("🎁 Тайный Квест для Анастасии")
        self.root.geometry("700x700")
        self.root.resizable(False, False)
        self.root.configure(bg=COLORS["bg"])
        #
        # # Центрирование окна
        # self.center_window()
        # Простое центрирование без сложной логики
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 700) // 2
        y = (screen_height - 700) // 2
        self.root.geometry(f"700x700+{x}+{y}")

        # Главный фрейм
        self.main_frame = tk.Frame(self.root, bg=COLORS["bg"])
        self.main_frame.pack(fill="both", expand=True)

        #Заголовок
        # self.title_label = tk.Label(
        #     self.main_frame,
        #     text="ТАЙНЫЙ КВЕСТ",
        #     font=("Segoe Print", 24, "bold"),
        #     fg=COLORS["gold"],
        #     bg=COLORS["bg"],
        #
        # )
        # self.title_label.pack(pady=20, anchor="center")

        # Текст приветствия
        self.welcome_frame = tk.Frame(self.main_frame, bg=COLORS["bg"])
        self.welcome_frame.pack(expand=True)
        self.welcome_text = tk.Label(
            self.welcome_frame,
            text="Привет Анастасия, на связи твой Тайный Санта!\nГоворят ты любишь сюрпризы?\n\nОтветь на 7 вопросов, чтобы узнать, где спрятан твой подарок! 💝",
            font=("Segoe Print", 16),
            fg=COLORS["fg"],
            bg=COLORS["bg"],
            justify="center",
            wraplength=600
        )
        self.welcome_text.pack(pady=(30, 30))

        # Кнопка начала
        self.start_button = tk.Button(
            self.welcome_frame,
            text="НАЧАТЬ КВЕСТ!",
            command=self.start_quest,
            font=("Segoe Print", 16, "bold"),
            bg=COLORS["accent"],
            fg="white",
            activebackground='#40A060',
            activeforeground="white",
            height=2,
            width=20,
            cursor="hand2",
            relief="flat",
            bd=0
        )
        self.start_button.pack(pady=20)

        # Текст вопроса
        self.question_label = tk.Label(
            self.main_frame,
            text="",
            font=("Segoe Print", 14),
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
            font=("Segoe Print", 12),
            bg=COLORS["bg"],
            fg='#f1828d',
            activebackground=COLORS["bg"],
            activeforeground=COLORS["fg"],
            relief="flat",
            bd=0,
            highlightbackground="#f1828d",
            highlightcolor="#f1828d",
            highlightthickness=1,
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
        self.welcome_frame.pack_forget()
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
                    font=("Segoe Print", 14),
                    height=1,
                    width=30,
                    bg="#8fb9a8",
                    fg="#fefad4",
                    activebackground="#36719F",
                    activeforeground="#f1828d",
                    cursor="hand2",
                    relief="flat",
                    bd=0
                )
                btn.pack(pady=5, padx=10)


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

        # ✅ Заголовок — отдельно, по центру, оранжевый
        title_label = tk.Label(
            self.main_frame,
            text="ПОЗДРАВЛЯЮ АНАСТАСИЯ!!!",
            font=("Segoe Print", 16, "bold"),
            fg="orange",
            bg=COLORS["bg"]
        )
        title_label.pack(pady=(30, 10), anchor="center")

        # ✅ Основной текст — белый, по центру
        message_label = tk.Label(
            self.main_frame,
            text=(
                "Ты ответила на все вопросы!\n\n"
                "Твой подарок ждёт тебя у того, кто отправил тебе этот файлик \n\n"
                "P.S. Надеюсь, тебе понравился квест! "
            ),
            font=("Segoe Print", 14),
            fg=COLORS["fg"],
            bg=COLORS["bg"],
            justify="center",
            wraplength=500
        )
        message_label.pack(pady=10, padx=20)

        # Кнопка выхода
        exit_btn = tk.Button(
            self.main_frame,
            text="Закрыть программу",
            command=self.root.destroy,
            font=("Segoe Print", 14, "bold"),
            bg='#8fb9a8',
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

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = QuestApp()
    app.run()
