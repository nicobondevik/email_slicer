def slice(emails_path):
    import csv

    # open specified file in read mode
    emails = open(emails_path, "r")

    # open file in write mode
    f = open('sliced.csv', 'w', encoding='UTF8')

    # create csv writer and write header
    writer = csv.writer(f)
    header = ['username', 'domain']
    writer.writerow(header)

    # loops forever
    while True:

        # get email
        email = emails.read().splitlines()

        # if no email entered, close the file and break the loop
        if email == '':
            f.close()
            break

        # split email at @ sign
        email = email.split('@')
        print(f'{email}')

        #write email to csv-file
        writer.writerow(email)

    # close the file
    f.close()

# run the function
slice('emails.txt')