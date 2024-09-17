from datetime import datetime
from calendar import monthrange

x = datetime.now().year #текущий год
y = int(input("Введите номер месяца ")) #месяц

days = monthrange(x, y)[1]
print("В месяце", days, "дней")
