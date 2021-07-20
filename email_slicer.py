'''
TODO:
Split email at @
Assign first part to username list/csv
Assign last part to domain list/csv
'''

import csv

def slice(email):
    #initiate variables and write header
    username = ('')
    domain = ('')
    at = False
    header = ['username', 'domain']
    # open file in write mode
    f = open('sliced.csv', 'w', encoding='UTF8')
    # create csv writer and write header
    writer = csv.writer(f)
    writer.writerow(header)
    #iterates through characters of email
    for x in email:
        #write email[x] to csv if letter is not @
        if x != '@':
            # at only true when @ encountered
            if at == False:
                username += (f'{x}')
            if at == True:
                domain += (f'{x}')
        elif x == '@':
        #set at to True if @ is encountered
            at = True
            print('@ sign found')
            pass

    data = (f'{username} {domain}')
    writer.writerow(data)

    f.close()

def main():
    for i in range(0,9):
        email = input('Email: ')
        slice(email)
main()