class Customer:
    def __init__(self, contact_data):
        self.contact_data = contact_data

    # def contact_manager(self):
    #     self.name = input("please add name: ")
    #     self.phone = input("please add phone: ")
    #     self.email = input("please add email: ")

    def add_custom(self,name,phone,email):
        with open(self.contact_data, mode="a+") as file:
            file.write(f"{name}, {phone}, {email}\n")

    def list_customers(self):
        with open(self.contact_data, mode="r") as file:
            print(file.read())

    def looking_for(self,name):
        # result = input("please enter looking for name: ")
        # choose_line = int(input("Please choose a number line: "))
        with open(self.contact_data, mode="r") as file:
            list_line = file.readlines()
#            צריך להפוך את אייטם לרשימה ואז למצוא את המיקום הראשון שזה "שם" וכך למצוא
        for item in list_line:
            item1 = item.split(",")
            if name in item:
                print("yess")
            print("item = " ,item1[2])

            # for line in file:
            #     if result == line[:2]:
            #        print("ho")
            #     else:
            #        print("ho no")
    def set_info(self, name ,phone, email):
        line_num = int(input("please enter line to set: "))
        with open(self.contact_data, mode="r") as file:
            list_line = file.readlines()
            for i in list_line:
                print(i)
        with open(self.contact_data, mode="w+") as file:
            list_line[line_num-1] = file.write(f"{name}, {phone}, {email}")
# list_line[line_num-1].writh(f"{name}, {phone}, {email}")

#

# customer_name = "my_file.txt"
customer1 = Customer("my_file.txt")
# contact_manager = ContactManager("contact_list.txt”)
# customer1.contact_manager()
# customer1.add_custom("noam","055-4499332","noam@gmail.com")

# customer1.list_customers()
# customer1.looking_for("noam")
customer1.set_info("moshe", "055-342-2432", "email.deo@gmail.com")
# contact_manager.read_contact_list()
# contact manager.search contact(“John”)
# contact_manager.update_infromation(“John”,”555-1111”,”Jhon@walla.com”)