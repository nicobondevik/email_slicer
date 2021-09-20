'''
email-slicer
The program asks for the email-adress, and stores it in a csv file called sliced_emails. 
The usernames and domains will be seperated.
'''

import csv

f = open('sliced_emails.csv', 'w', encoding='UTF8')

writer = csv.writer(f)  # create csv writer
writer.writerow(['username', 'domain'])

email = input('email (enter when done): ')
while email != '':
    email = email.split('@')
    writer.writerow(email)
    email = input('email (enter when done): ')
f.close()

print('bye.')