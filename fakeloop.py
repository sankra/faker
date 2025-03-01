#importing Faker Module from faker package
from faker import Faker

fake = Faker()

#below is the loop that generates multiples fake messages in a loop.
for i in range(10):
    message = {
        'name' : fake.name(),
        'address' : fake.address(),
        'phone' : fake.phone_number()    
    }
    print(message)
