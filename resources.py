institute_name="CS Technologies"
course_name='AI'
def greet(name):
    print('Welcome',name)
    print("You are at",institute_name,'in',course_name,'class')



class hccda:

    def __init__(self,name,age,gender,max_edu):
        self.name =name
        self.age = age
        self.gender = gender
        self.max_edu=max_edu

    def check_qualified(self):
        if(self.age>18 and self.age<40):
            if(self.max_edu >= 16):
                print('You Are Eligible For this Course')
            else:
                print("Sorry!! We Need 16 Year Of Education For Enrollment")
        else:
            print("Sorry You Age Is Not Good Fit For This Course")



## oop master class

class bank_accout:

    # class attribute
    bank_name="CS Banking System"
    t_fee=20


# constructor 
    def __init__(self,title,acc_num,balance=0):
        self.title=title
        self.acc_num=acc_num
        self.__balance=balance

    def deposite(self,amount):
        if(amount>0):
           self.__balance +=amount
           print("Deposite Success")
        else:
            print("Please Enter Legal Amount")
    
    def withdraw(self,amount):
        if(self,__balance+self.t_fee>amount):
            self.__balance-=amount
            self.__transaction_fee()
            print("Withdraw Success")
        else:
            print('Please Enter Valid Amount')
            self.print_slip()

    def __transaction_fee(self):
        self.__balance-=self.t_fee

    def print_slip(self):
        print('-'*40)
        print(f"Hello{self.title} This is {self.bank_name}")
        print('-'*40)
        print("Your Account Number is ",self.acc_num)
        print('Your Balance is ',self.__balance)
        print('-'*40)

    
    def transfer(self,amount,receiver):
        if(self.__balance+self.t_fee>amount):
            self.__balance -=amount
            self.__transaction_fee()
            receiver.__balance +=amount
            print('Transaction Success')
        else:
            print('Invaild Amouunt')
            self.print_slip()


    @classmethod
    def update_t_fee(cls,amount):
        cls.t_fee=amount
        print('Updated To',amount)
    @staticmethod
    def greet():
        print("Hello This is a Static Method")


    # destructor
    def __del__(self):
        print("Your Account Have Been Deleted Successfully")


    def __str__(self):
        return f"your account balance is {self.__balance}"




    
