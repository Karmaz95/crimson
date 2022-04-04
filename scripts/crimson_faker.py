# Created by KARMAZ95
#
###
# Generate random persons data.
# Serves as a template for testing APIs.
###

from faker import Faker
from datetime import datetime

def generate_person(username,email):
    fake = Faker("pl_PL")
    first_name = fake.first_name()
    last_name = fake.last_name()
    identity_card_number = fake.identity_card_number()
    nip = fake.nip()
    date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=90)
    pesel=fake.pesel(date_of_birth)
    iban=fake.iban()

    date_of_birth=date_of_birth.strftime("%Y-%m-%d")
    i=0
    while(i < 10):
        phone_number=fake.phone_number()
        if phone_number[0:3] == "+48":
            phone_number=(phone_number[4:]).replace(" ","")
        phone_number=phone_number.replace(" ","")
        i+=1;
    return username+","+email+","+first_name+","+last_name+","+identity_card_number+","+nip+","+date_of_birth+","+pesel+","+phone_number+","+iban


def make_persons_list():
    j=0
    persons=[]
    while(j < 10000):
        username="kmazurek"+str(j)
        email="kmazurek+"+str(j)
        persons.append(generate_person(username,email))
        j+=1;
    
    return persons

def save_array_to_csv(array,file_name):
    with open(file_name,"w+") as f:
        data = f.read()
        f.write("username,email,first_name,last_name,identity_card_number,nip,date_of_birth,pesel,phone_number,iban\n")
        for el in array:
            f.write(el+"\n")


array = make_persons_list()
save_array_to_csv(array,"10k_persons_wordlists.csv")
