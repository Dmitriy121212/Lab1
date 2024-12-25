import numpy as np
import matplotlib.pyplot as plt
import math
data = np.genfromtxt("usd_to_uah_rates.csv", delimiter=",", skip_header=1)
dates = np.arange(len(data))
rates = data[:, 1]  # Курс долара
def Stat_characteristics(rates, text):
    num = len(rates)
    ms = np.mean(rates)
    ds = np.var(rates)
    scv = math.sqrt(ds)
    print(f"---------------Статистичні характеристики {text}-----------------------")
    print("Кількість елементів вибірки: ", num)
    print("Математичне очікування: ", ms)
    print("Дисперсія: ", ds)
    print("Середньоквадратичне відхилення: ", scv)
    return
Stat_characteristics(rates, "результатів парсингу")
# ПОбудова моделі
degree = 5
coeffs = np.polyfit(dates, rates, degree)
poly_model = np.poly1d(coeffs)
print("Синтезована математична модель: ")
print(poly_model)
# Передбачення
predicted_rates = poly_model(dates)
Stat_characteristics(predicted_rates, "моделі")
# Графік
plt.figure(figsize=(10, 6))
plt.plot(dates, rates, label="Вихідні дані", color="blue")
plt.plot(dates, predicted_rates, label=f"Поліноміальна модель (ступінь={degree})", color="red")
plt.legend()
plt.xlabel("День")
plt.ylabel("Курс USD/UAH")
plt.show()

errors = rates - predicted_rates
# Гістограма
plt.hist(errors, bins=20, density=True, alpha=0.7, color='blue')
plt.title("Гістограма похибок")
plt.xlabel("Різниця")
plt.ylabel("Частота")
plt.show()
