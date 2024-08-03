def cal():
    
    print("This is a Calendar Softwore\n") # nav cal
    yy = int(input("Year : ")) # input of year
    mm = int(input("Month : ")) # input of month
    import calendar #calendar import
    print(calendar.month(yy, mm)) # output calendar
    
while True:
    cal()