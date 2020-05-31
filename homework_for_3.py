school_marks = [
    {'school_class': '1a', 'indiv_marks': [4,5,4,5,4,5,5,4]},
    {'school_class': '2a', 'indiv_marks': [5,4,2,5,2,2]},
    {'school_class': '3a', 'indiv_marks': [1,2,4,3,2]},
]

def averaging(marks):
    average = round(sum(marks['indiv_marks'])/len(marks['indiv_marks']),1)
    return str(average)

for marks in school_marks:
    class_number = str(marks['school_class'])
    av_class_mark = averaging(marks)
    print(f'Средняя оценка ' + class_number + ' класса: ' + av_class_mark)

sum_of_all_marks = 0
count_of_all_marks = 0
for marks in school_marks:
    sum_of_marks = sum(marks['indiv_marks'])
    count_of_marks = len(marks['indiv_marks'])
    sum_of_all_marks += sum_of_marks
    count_of_all_marks += count_of_marks
    average_school_mark = round(sum_of_all_marks/count_of_all_marks,1)

print(f'Средняя оценка в школе: ' + str(average_school_mark))
