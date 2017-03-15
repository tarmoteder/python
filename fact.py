
def fact():
    count=1
    factoriaal = input("Sisesta täisarv: ")
    if factoriaal.isdigit():
        facto = int(factoriaal)
        if facto > 0:
            result =1
            while(count<=facto):
                result = count * result
                count +=1
            print(result)     
        else:
            print ("Number ei tohi olla väiksem, kui 0.")
            fact()
    else:
        print("Nadikael, täisarvu küsiti")
        fact()
        
    

fact()