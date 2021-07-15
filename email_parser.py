# import pattern for regex
import re
def email_parser(email):
# checking  if the constraints from the README.md file are met 
    pattern = re.compile(r"([a-z][a-z0-9+]+[+]?[a-z]@[^0-9][a-z0-9]+\.com$)")
    check = pattern.findall(email)
    if check:
    # finding the position of "@", doing some slicing and converting to dictionary
        position = email.index('@')
        prefix = email[:position]
        sufix = email[position+1:]
        parsed_output= {'username': prefix, 'domain': sufix}    
        return parsed_output
    else:
        return None
print(email_parser("sunday4f@gmail.com"))



        




                  
            
