def steps(number):
    if number<1 or number-round(number)>0: 
        return print("error")
    else:
        if number % 2 == 0 : 
            number= number/2 
        elif number==1: 
            number=number
        else: 
            number=3*number+1
        print(str(number))
        if number==1: 
            return  1
        else: 
            return steps(number)