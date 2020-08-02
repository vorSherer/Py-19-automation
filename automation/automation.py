import re

def gold_pan(file):
    phone_data = []
    email_data = []

    phone_re = r'(\(?\d{3}\)?[-\.\s]?\d{3}[-\.\s]?\d{4})(x\d+)?'

    email_re = re.compile(r'''(
        [a-zA-Z0-9.%+-]+    # username
        @                   # separator
        [a-zA-Z0-9.-]+      # domain name (mail server)
        (\.[a-zA-Z]{2,4})   # top-level domain
        )''', re.VERBOSE)

        # ALT EMAIL CODE:  \w+[\.-_\+]?(\w+)?@\w+([\.-_]\w+)?\.\w+

    with open(file, "r") as f:
        notes = f.read()

    numbers = re.findall(phone_re, notes)
    for phone in numbers:
        masked_phone = phone[0] + phone[1]
        masked_phone = [char for char in masked_phone if char.isnumeric() or char == "x"]
        masked_phone.insert(3, "-")
        masked_phone.insert(7, "-")
        masked_phone = ''.join(masked_phone)
        phone_data.append(masked_phone + "\n")
    
    phone_data = sorted(set(phone_data))
    with open("assets/phone_numbers.txt", "w+") as file:
        file.writelines(phone_data)

    for groups in email_re.findall(notes):
        email_data.append(groups[0] + "\n")
        email_data = sorted(set(email_data))
    with open("assets/emails.txt", "w") as file:
        file.writelines(email_data)

    print("Done.")






if __name__ == "__main__":
    # gold_pan("assets/sample1.txt")
    # gold_pan("assets/sample2.txt")
    # gold_pan("assets/sample.txt")
    gold_pan("assets/potential-contacts.txt")
