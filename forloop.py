class feature():
    id : 0
    name = str
    details = str

feature1 = feature()
feature1.name = 'uche'
feature1.details = 'Very Reliable'

feature2 = feature()
feature2.name = 'Alex'
feature2.details = 'Very Affordable'

feature3 = feature()
feature3.name = 'Daniel'
feature3.details = 'Confused about him'

variable = [feature1, feature2, feature3]

dict = {'varkey': variable}

for i in variable:
    print("Hello world")

print(variable[0])