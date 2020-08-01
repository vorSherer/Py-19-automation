from faker import Faker
import shutil

faux_data = Faker('en_US')

content = ''

for _ in range(25):
    content += faux_data.paragraph()
    content += f" {faux_data.email()} "
    content += f" {faux_data.zipcode()} " 
    content += faux_data.paragraph()
    content += f" {faux_data.phone_number()} "
    content += faux_data.paragraph()
    content += f" {faux_data.zipcode()} " 

# print(dir(faux_data))
# print(content)
with open("./assets/sample.txt", "w+") as file:
    file.write(content)


