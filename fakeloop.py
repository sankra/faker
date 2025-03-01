#importing Faker Module from faker package
from faker import Faker

fake = Faker()

for i in range(10):
    message = {
        'name' : fake.name(),
        'address' : fake.address(),
        'phone' : fake.phone_number()    
    }
    print(message)
