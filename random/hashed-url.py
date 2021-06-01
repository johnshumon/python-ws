""" Example function to generate  hashed url"""
import json
import hashlib


def generate_url(payload):
    key = "hrsoirtg4iidIWJ4d3DFWK653SdsFDSD"
    username = "lvsbrokers"
    base_url = "https://test-5b.ks-295ferr.com/EADI"
    token = hashlib.sha1(
        "".join([key, json.dumps(payload)]).encode("utf-8")
    ).hexdigest()

    return "/".join([base_url, username, token, ""])


payload = {
    "action": "APPLY",
    "firstName": "John",
    "lastName": "Smith",
    "clientAddress": "Test 3 K 4",
    "clientPostcode": "12345",
    "clientCity": "Karkkila",
    "country": "Finland",
    "emailAddress": "test@test.com",
    "website": "www.test.com",
    "personal_id": "123456-1234",
    "bankAccount": "FI09 1330 3000 1415 75",
    "birthDate": "1965-05-11",
    "loanAmount": "20000",
    "loanPurpose": "Working capital",
    "groupName": "Test company",
    "entityType": "Other",
    "business_id": "123456789",
    "mobilePhone1": "0440000000",
    "businessAddress": "Test 3 K 4",
    "postcode": "54321",
    "city": "Karkkila",
    "industryType": "Other",
    "yrsBusiness": "5",
    "consentDirectMarketing": "No",
    "revenue": "150000",
}

URL = generate_url(payload)
print("url: ", URL)
