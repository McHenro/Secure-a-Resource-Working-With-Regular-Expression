from auth import authenticate
#importing time and extracting the day, month, year and the time
import time
current_date = time.strftime("%a, %d %b %Y")      
current_time = time.strftime("%I:%M:%S")



def resource_deco(email='example@email.com', password='example123'):
      def another_deco(func):
            user = authenticate(email, password)
            #wrapper of my decorator 
            def wrapper():
                  if user:
                        func()
                        if user['role'] == 'superadmin' or user['role'] == 'admin':
                              outcome = f"{user['first_name']} {user['last_name']}\n{func()}"
                              with open("access_granted.txt", "a") as file_handle:
                                file_handle.write(f"\n{user['role']}  {user['first_name']} {user['last_name']} viewed company resources on {current_date } at {current_time }")
                              return outcome
                        
                        elif user['role'] == 'engineer' or user['role'] == 'marketer' or user['role']  == 'staff':
                               with open("access_denied.txt", "a") as file_handle:
                                file_handle.write(f"\n{user['role']}  {user['first_name']} {user['last_name']} tried to view the company resources on {current_date } at {current_time }")
                               outcome2 = (f"{user['first_name']} {user['last_name']}\nYou are not allowed to view this resource")
                               return outcome2
                             
                  else:
                        return "Only staff can access this resource"                    
            return wrapper
      return another_deco      


