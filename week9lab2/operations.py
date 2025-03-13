from people import Student, Academic

student1 = Student(name="Hary", ID=11, status="domestic",
                   units_completed=["MCD4700", "MCD4701", "MCD4702", "MCD4703"],
                   units_enrolled=["MAGIC105"])

student2 = Student(name="Harmonica", ID=77, status="international",
                   units_completed=["MCD4710", "MCD4720", "MCD4730"],
                   units_enrolled=["MAGIC102"])

student3 = Student(name="Milfoy", ID=84, status="international",
                   units_completed=["COS1101", "COS1102", "COS1103", "COS1104", "COS1008"],
                   units_enrolled=[])

student4 = Student(name="Don", ID=92, status="domestic",
                   units_completed=["MCD4740", "MCD4750"],
                   units_enrolled=["MAGIC102", "MCD4700"])

academic1 = Academic(name="Dumblepork", ID=121, status="domestic",
                     units_taught=["MAGIC101", "MCD4720"])

academic2 = Academic(name="Snake", ID=234, status="international",
                     units_taught=["MAGIC102", "MCD4710"])

print(student1.name, student1.verify_id(), student1.is_enrolled(), student1.is_ready_to_graduate())
print(student2.name, student2.verify_id(), student2.is_enrolled(), student2.is_ready_to_graduate())
print(student3.name, student3.verify_id(), student3.is_enrolled(), student3.is_ready_to_graduate())
print(student4.name, student4.verify_id(), student4.is_enrolled(), student4.is_ready_to_graduate())

print(academic1.name, academic1.verify_id(), academic1.is_teaching("MAGIC101"))
print(academic2.name, academic2.verify_id(), academic2.is_teaching("MAGIC103"))
