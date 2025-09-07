from faker import Faker 
 
fake = Faker() 
 
for i in range(20): 
    print(fake.country()) 