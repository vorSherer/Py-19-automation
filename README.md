# Lab 19 - Automation with Python

### *Author: Thomas Sherer*, 2020-08-01

---

## Description
### Feature Tasks and Requirements
- Given a document __`potential-contacts`__, find and collect all email addresses and phone numbers.
- Phone numbers may be in various formats; 
    - __(xxx) yyy-zzzz__, __yyy-zzzz__, __xxx-yyy-zzzz__, etc.
    - phone numbers with missing area code should presume __206__
    - phone numbers should be __stored in xxx-yyy-zzzz format__. <br>
- Once emails and phone numbers are found they should be stored in two separate documents.
    - The '__*phone_numbers.txt*__' and '__*emails.txt*__' files will be verified by an automated system, so make sure to match the naming/formatting requirements exactly.
- The information should be sorted in ascending order.
- Duplicate entries are not allowed.
 <br>

---

My code is [here](./automation/automation.py) <br>

---

### Collaborations and Attributions

__Merry Cimakasky__ helped with text file imports.

__Leo Kukhorev__ helped with regex.

.gitignore content courtesy of https://www.toptal.com/developers/gitignore/api/python

__Automate the Boring Stuff with Python__ helped with [email extraction regex code](https://automatetheboringstuff.com/chapter7/)

---

<!-- Submission PR: NN -->
