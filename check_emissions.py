import pandas as pd

dataset = pd.read_excel('dataset.xlsx')
print("Исходный набор данных:")
dataset.info()

print("\nНабор данных после удаления повторяющихся строк:")
dataset = dataset.drop_duplicates()
dataset.info()

print()
for column in dataset.columns:
    print(str(column) + ": " + "Мин. значение - " + str(dataset[column].min()) + ". Макс. значение - " + str(dataset[column].max()))


###
# Нулевые или пропущенные значения отсутствуют. 
# Повторяющиеся строки отсутствуют. 
# Выбросов не было замечено (максимально возможное значение стрессоусточивости 140). 
# ЛПР - от до 5 приемлемый уровень в зависимости от возраста, если больше то возрастает риск ИБС.
###