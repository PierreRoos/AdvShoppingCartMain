from faker import Faker
fake = Faker(locale='en_CA')

# ------------------Advantage Shopping Web App DATA PARAMETERS --------------

app = 'Advantage Shopping'
hmpg_url = 'https://advantageonlineshopping.com/#/'
hmpg_title = 'Advantage Shopping'
register_page_url = 'https://advantageonlineshopping.com/#/register'

username = fake.user_name()#[0:15] limit characters
email = fake.email()
password = fake.password()

first_name = fake.first_name()#[0:15] limit characters
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
phonenum = fake.phone_number()

country = fake.current_country()
city = fake.city()
address = fake.street_address()
province = fake.province_abbr()
postal_code = fake.postalcode()

subject = fake.sentence(100)
