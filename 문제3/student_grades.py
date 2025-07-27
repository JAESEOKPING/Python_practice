# student_grades.py

dict_list = {'김철수': 85,'이영희': 92,'박민수': 78,'최수진':95}

for key,value in dict_list.items():
    print(f'{key}: {value}점')

scores = list(dict_list.values()) 
average = sum(scores) / len(scores)  

print(f"평균 점수: {average:.1f}")

