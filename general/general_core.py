def IntegerChecker(x):
    x=int(x)
    if x<=9:
        x="0"+str(x)
    else:
        x=str(x)
    return x


def CountDays(year,month):
    year_4=int(20+int(year))
    month=int(month)
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        days=31
    elif month==4 or month==6 or month==9 or month==11:
        days=30
    elif month==2:
        if year_4%4==0:
            days=29
        elif year_4%4!=0:
            days=28    
    return str(days)

def Month1to13(month):
    month=int(month)
    if month==13:
        month=1
    else:
        pass
    return month     
