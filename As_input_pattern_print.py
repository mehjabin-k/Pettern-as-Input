play="y"
i=0
while play=='y' or play=='Y':
    n=int(input("Please a number : "))
    b=n
    while True:
        bol=int(input("Please enter a value between 0 or 1 : "))
        if bol==0 or bol==1:
            bool(bol)
            break
        else:
            print("Wrong!!!... You'r enter wrong input.\n")
            print("Please re-Enter\n")
        i=i+1

    def true_condi(f1,f2):
        """This is applicable only for True condition and print as *"""

        '''if(bol==True):
            b=n
            c=1
            while (n>0 or b>0):
                #b=n
                while b-a and b>0:
                    print("*",end="")
                    c=c+1
                a+1
                b=b-1
    '''

        '''if(bol==True):
            i = 0
            row = 1
            a = 1
            while f1>0:
                while row>0:
                    print("*")
                    row=row-1
                print("\n")
                f1=f1-1
                a=a+1
                row=a'''
        f1=f2-1
        for i in range(0,f2):
            for j in range(0,i+1):
                print("*",end=" ")
            print("\r")

    def false_condi(f1,f2):
        """This function is only applicable for Fasle Condition.."""

        f1=f2-1
        for i in range(0,f2):
            for j in range(0,f2-i):
                print("*",end=" ")
            print("\r")

    if bol==True:
        true_condi(b, n)
    else:
        false_condi(b,n)
    play=input("Do you want to Re- Run then please enter Y or N : ")
