import customtkinter as ctk
from dotenv import load_dotenv
from weather import get_weather

load_dotenv()

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Погода")
app.geometry("800x600")


title_label = ctk.CTkLabel(
    app,
    text="Погода",
    font=ctk.CTkFont(size=24, weight="bold"),
)
title_label.pack(pady=20, expand=True)

entry = ctk.CTkEntry(
    app,
    placeholder_text="Введите название города",
    width=200,
    height=40,
    border_width=0,
    corner_radius=10,
    font=ctk.CTkFont(size=16),
)
entry.pack(pady=10, expand=True)

# Создаём result_label ЗАРАНЕЕ — пустым
result_label = ctk.CTkLabel(
    app,
    text="",
    font=ctk.CTkFont(size=22),
    justify="left",
)
result_label.pack(pady=20, expand=True)

# Функция объявлена ДО кнопки
def on_search():
    city = entry.get()

    if not city:
        result_label.configure(text="Введите название города!")
        return

    # Блокируем кнопку пока идёт запрос
    button.configure(state="disabled", text="Загрузка...")

    result = get_weather(city)

    if result is None:
        result_label.configure(text="Город не найден 😕")
    else:
        text = (
            f"Город: {result['city']}\n"
            f"Температура: {result['temp']}°C\n"
            f"Ощущается как: {result['feels_like']}°C\n"
            f"Влажность: {result['humidity']}%\n"
            f"Описание: {result['description']}"
        )
        result_label.configure(text=text)

    # Разблокируем кнопку после запроса
    button.configure(state="normal", text="Получить погоду")

# Кнопка создаётся ПОСЛЕ функции
button = ctk.CTkButton(
    app,
    text="Получить погоду",
    width=200,
    height=40,
    border_width=0,
    corner_radius=10,
    font=ctk.CTkFont(size=16),
    command=on_search,
)
button.pack(pady=10, expand=True)

app.mainloop()