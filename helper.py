from faker import Faker

faker = Faker()

def generate_email():
    email = faker.email()
    return email

