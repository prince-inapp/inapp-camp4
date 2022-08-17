import os

# phone book 
def displayOptions():
    print('''
    1. List all contacts
    2. Add new contact
    3. Delete contact
    4. Search contact by name
    5. Search contact by number
    6. Exit
    ''')

phone_book = dict()


print(os.getcwd())
current_path = os.getcwd()+'\File Handling\Contacts'
if(os.path.exists(current_path)):
    os.chdir(current_path)
    if(os.path.exists(current_path+'\contact.txt')):
        pass
    else:
        f = open('contact.txt','w')
        f.close()
else:
    os.makedirs(current_path)
    os.chdir(current_path)
    f = open('contact.txt','w')
    f.close()
print(os.getcwd())



while(True):
    displayOptions()
    option = int(input("Enter option :"))
    match option:
        case 1:
            f = open('contact.txt','r')
            temp = f.readlines()
            names = []
            '''List all Contacts'''
            for name in temp:
                names.append(name.split(':')[0])
            names = sorted(names)
            for name in names:
                print(name)
            f.close()
        case 2:
            '''Add a new contact'''
            name = input("Enter name :")
            phone_number = input("Enter phone number :")
            #phone_book[name] = phone_number
            
            f = open('contact.txt','a')
            f.write(name+':'+phone_number+'\n')
            print("Contact {} : {} added to phone book".format(name,phone_number))
            f.close()

        case 3:
            '''Delete a contact'''
            name = input("enter name to delete :")
            #  if(name in phone_book.keys()):
            #     del phone_book[name]
            #     print("contact {} deleted!...".format(name))
            # else:
            #     print("No names found!...") 
            f = open('contact.txt','r')
            content = f.readlines()
            f.close()
            
            found_contact = False
            for line in content:
                if(line.split(':')[0] == name):
                    content.remove(line)
                    found_contact = True
                    break
            if(found_contact):
                f = open('contact.txt','w')
                #print(content)
                f.writelines(content)
                print("contact {} deleted!...".format(name))
            else:
                print("No names found!...")
            f.close()
            

        case 4:
            '''seach by contact by name'''
            name = input("Enter name to search: ")
        #    if name in phone_book.keys():
        #         print("{}-{}".format(name,phone_book[name]))
        #     else:
        #         print("no contacts found") 
            f = open('contact.txt','r')
            content = f.readlines()
            f.close()
            found_contact = False
            for line in content:
                if(line.split(':')[0] == name):
                    name = line.split(':')[0]
                    number = line.split(':')[1]
                    print("{}-{}".format(name,number))
                    found_contact = True
                    break
            if(not found_contact):
                print("No contacts found")
        case 5:
            '''search by number'''
            number = input("Enter phone number:")
            # numbers = list(phone_book.values())
            # #print(numbers)
            # if(number in numbers):
            #     pos = numbers.index(number)
            #     names = list(phone_book.keys())
            #     print("Name :",names[pos])
            # else:
            #     print("number not found!")
            f = open('contact.txt','r')
            content = f.readlines()
            f.close()
            found_contact = False
            for line in content:
                temp_number = line.split(':')[1].strip('\n')
                if(temp_number == number):
                    name = line.split(':')[0]
                    number = line.split(':')[1].strip('\n')
                    print("{}-{}".format(name,number))
                    found_contact = True
                    break
            if(not found_contact):
                print("No contacts found")
            
        case 6:
            if(not f.closed):
                f.close()
            print("Program Exited!")
            break
