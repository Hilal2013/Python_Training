import json
json_file=open(r'C:\Users\hilal\PycharmProjects\Python_Bootcamp\day04\files\Test.json')
dictionary=json.load(json_file)
print(dictionary)

#{'name': 'John Doe', 'age': 43, 'address':
# {'street': '10 Downing Street', 'city': 'London'}, 'phones': ['+44 1234567', '+44 2345678']}
print(type(dictionary))#<class 'dict'>

for x in dict(dictionary).keys():
    print(x)

json_file.close()

print('------------ Write Json file----------------------')


students = {
    'A01': {
        'name': 'James',
        'gender': 'Male',
        'gpa': 3.5,
        'subjects': ['Math', 'Physics']
    },

    'A02': {
        'name': 'Hazel',
        'gender': 'Female',
        'gpa': 3.8,
        'subjects': ['Biology', 'Programming']
    },

    'A03': {
        'name': 'Yulia',
        'gender': 'Female',
        'gpa': 4,
        'subjects': ['Chemistry', 'Programming']
    }
}

jason_file = open('files/Test2.json', 'w')

json_object = json.dumps(students, indent=3)   # converting dictionary object to json object

jason_file.write(json_object)