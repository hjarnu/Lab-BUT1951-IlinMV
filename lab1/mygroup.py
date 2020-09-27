from statistics import mean
groupmates = [
{
"name": "Максим",
"surname": "Ильин",
"exams": ["Информатика", "ЭЭиС", "Web"],
"marks": [4, 3, 5]
},
{
"name": "Илья",
"surname": "Максимов",
"exams": ["История", "АиГ", "КТП"],
"marks": [3, 4, 3]
},
{
"name": "Иван",
"surname": "Петров",
"exams": ["Математика", "КГ", "Английский язык"],
"marks": [3, 3, 4]
},
{
"name": "Петр",
"surname": "Иванов",
"exams": ["Электротехника", "IoT", "Физика"],
"marks": [4, 4, 4]
},
{
"name": "Кирилл",
"surname": "Смирнов",
"exams": ["Философия", "ИС", "КТП"],
"marks": [5, 5, 5]
}
]
def filter(students):
    print(u"Имя".ljust(10), u"Фамилия".ljust(10), u"Экзамены".ljust(40), u"Оценки".ljust(10))
    for student in students:
            mark = student['marks']
            avg = mean(mark)
            if avg >= x:
                print(student["name"].ljust(10), student["surname"].ljust(10), str(student["exams"]).ljust(40), str(student["marks"]).ljust(10))
x = float(input('Введите средний балл для фильтрации: '))
filter(groupmates);