# resources only access
# import resources as r
# print(r.institute_name)

 # print(r.greet('ali'))

# import through a function 
# from resources import greet

#greet('ali')





# ab class import ky liya 

# from resources import hccda

# std1=hccda("ali",24,"m",16)

# std1.check_qualified()

from resources import bank_accout as ba


ac1 = ba("Ali", 100001, 2300)

ac2 = ba("ahmed", 100002)

ac1.transfer(300, ac2)

ac2.print_slip()
