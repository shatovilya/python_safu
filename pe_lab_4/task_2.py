import pandas as pd

## Автоматическое созданеи структуры Dataframe через библиотеку Pandas
data = pd.read_csv(filepath_or_buffer ="students.csv", sep = ';')

## 2.1 Выведите информацию о студентах, отсортировав их по фамилии

print(data.sort_values(['ФИО']))

## 2.2 Выведите информацию о студентах, в возрасте старше 22 лет.
greater_than = data[data['Возраст'] > 22]

print(greater_than)