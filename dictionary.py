students = {
    "s1":{ "name":"ranu", "surname":"patidar", "address":"jeeran"},
    "s2":{ "name":"tanvi", "surname":"ptdr", "address":"manasa"},
    "s3":{ "name":"ravina", "surname":"shrma", "address":"mds"},
    "s4":{ "name":"sanju", "surname":"rathore", "address":"nmh"},
}

#print(f"Hello {students["s1"]["name"]} patidar from jeeran")

for student in students:
    print(f"Hello {students[student]["name"]} {students[student]["surname"]} From {students[student]["address"]}")