print("Enter Markes Obtained in 5 subjects:")

mark1=int(input())
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())

sum=mark1+mark2+mark3+mark4+mark5
avg=sum/5

if avg>=91 and avg<=100:
    print("Your Grade is A1")

elif avg>=81 and avg<=91:
    print("Your Grade is A2")

elif avg>=71 and avg<=81:
    print("Your Grade is B1")

elif avg>=61 and avg<=81:
    print("Your Grade is B2")

elif avg>=51 and avg<=61:
    print("Your Grade is C1")

elif avg>=41 and avg<=51:
    print("Your Grade is C2")

elif avg>=33 and avg<=41:
    print("Your Grade is D1")

elif avg>=21 and avg<=33:
    print("Your Grade is D2")

elif avg>=11 and avg<=21:
    print("Your Grade is E1")

elif avg>=0 and avg<=11:
    print("Your Grade is E2")

else:
    print("Invalid Input!")