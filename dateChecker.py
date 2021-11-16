import datetime

class Date:
    def __init__(self, dd, mm, yy):
        self.dd = dd
        self.mm = mm
        self.yy = yy
        self.__checkDate()

    def __checkDate(self):
        isValid = True
        try:
            datetime.datetime(self.yy, self.mm, self.dd)
        except ValueError:
            isValid = False

        if isValid:
            print("Input Date is valid: ", self.dd, "/" ,self.mm, "/", self.yy)
        else:
            print("Input Date is invalid")

# try:
#     date = input("Enter date, Month and Year in the following format [dd.mm.yy]: ")
#     dd = int(date.split('.')[0])
#     mm = int(date.split('.')[1])
#     yy = int(date.split('.')[2])
# except ValueError:
#     print("Invalid date format entered")
# d = Date(dd,mm,yy)
        
# Find Age



