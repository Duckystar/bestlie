groupmates = [
    {
        "name": "Андрей",
        "surname": "Ким",
        "exams": ["АиГ", "Вышмат", "ИНО"],
        "marks": [5,4,5]
    },
    {
         "name": "Юра",
        "surname": "Пискунов",
        "exams": ["ИНО", "Философия", "Введ"],
        "marks": [5,4,4]
    },
    {
        "name": "Екатерина",
        "surname": "Миролюбова",
        "exams": ["Введ", "История", "ИиКГ"],
        "marks": [5,5,5]
    },
    {
        "name": "Дима",
        "surname": "Емельянов",
        "exams": ["Физика", "АиГ", "Философия"],
        "marks": [3,4,4]
    },
    {
        "name": "Никита",
        "surname": "Смирнов",
        "exams": ["Физкультура", "Вышмат", "Физика"],
        "marks": [3,3,3]
    }
    ]
x=float(input("\nВведите среднее значение оценки "))
def sorting(students, a):
    for studen in students:
        n = 0
        sum = 0
        for i in studen['marks']:
            sum = sum + i
            n = n + 1
        if sum/n >=a:
            print(studen['name'])
    
sorting(groupmates, x)
