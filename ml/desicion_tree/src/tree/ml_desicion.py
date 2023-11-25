import pandas as pd
import matplotlib.pyplot as plt
# Создание примера данных (замените этот блок своими данными)
data = {'Category': ['A', 'B', 'C', 'D'],
        'Values1': [10, 24, 18, 30],
        'Values2': [15, 20, 25, 12]}

df = pd.DataFrame(data)

# Создание двух графиков на одной картинке
ax = df.plot.bar(x='Category', y=['Values1', 'Values2'], rot=0)

# Настройки для улучшения внешнего вида
ax.set_title('Графики Values1 и Values2')
ax.set_xlabel('Category')
ax.set_ylabel('Values')

# Показать график
plt.show()
