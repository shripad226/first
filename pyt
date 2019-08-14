sub1=int(input("enter sub1 marks"))
sub2=int(input("enter sub2 marks"))
sub3=int(input("enter sub3 marks"))
sub4=int(input("enter sub4 marks"))
sub5=int(input("enter sub5 marks"))
T=sub1+sub2+sub3+sub4+sub5
P=T/500*100
if P>=75:
        print("O grade")
else: 
    if P<=75 and P>=65:
                      print("A grade")
    else:
        if P<=60 and P>=45:
                          print("B grade")
        else:
            if P<=45 and P>=35:
                              print("C grade")
            else:
                if P<35:
                       print("fail")
