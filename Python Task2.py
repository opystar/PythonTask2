#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

status= True
user_details =[]

usernumber = 1

while status:
    
#get user details#
    
    first_name = input('Please enter your first name: ')
    first_two = first_name [0:2]
    last_name = input('Please enter your last name: ')
    last_two = last_name [-2:]
    email = input('Please enter your e-mail address: ')

    details = [first_name, last_name, email]

#generate random password(letters and numbers)#
    #use this code to generate random characters: 
        #characters = string.ascii_letters
        #length = 5
        #random+characters = ''.join(randomchoice(characters)for i in range(length))
    rand_str = '{:05d}'.format(random.randrange (1,99999))
    random_password = '{}{}{}'.format(first_two,last_two,rand_str)
    
    print (f"This is your password: {random_password}")

    
    satisfied= input('Are you satisfied with this password? Yes/No: ')
    
    satisfied_loop = True

    while satisfied_loop:
        if satisfied== 'Yes':
            confirm_password= input('Please confirm your password again: ')

            details.append(random_password)

            user_details.append(details)

            satisfied_loop = False

        else:
            choice_password =''
            choice_password = input('Please enter your desired password which must be at least 7 characters in length: ')
            
            pass_length= True

            while pass_length:
                if len(choice_password) < 7:
                    print("Invalid password; password must be a minimum of 7 characters.")
                    break
                else:
                    confirm_password= input('Please confirm your password again: ')

                    if confirm_password != choice_password:
                        print("This is not the password you entered earlier. Please check again")

                    else:
                        details.append(choice_password)

                        user_details.append(details)

                        pass_length = False

                        satisfied_loop = False
        
    new_user= input('Would you like to enter a new user? Yes or No: ')

    if (new_user == 'No'):
        print(user_details)
        status = False
        
    else:
        status = True
    
usernumber +=1

    


# In[ ]:




