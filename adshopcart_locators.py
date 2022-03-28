from faker import Faker
fake = Faker(locale='en_CA')

# ------------------Advantage Shopping Web App DATA PARAMETERS --------------

app = 'Advantage Shopping'
hmpg_url = 'https://advantageonlineshopping.com/#/'
hmpg_title = 'Advantage Shopping'
register_page_url = 'https://advantageonlineshopping.com/#/register'

username = fake.user_name()
email = fake.email()
password = fake.password()

first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
phonenum = fake.phone_number()

country = fake.current_country()
city = fake.city()
address = fake.street_address()
province = 'BC'  # fake.province() too long, often over 10 char
postal_code = fake.postalcode()
