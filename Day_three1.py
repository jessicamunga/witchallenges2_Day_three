def mylist(listA):
    evens=list()
    odds=list()
    chars=str()
    mydict=dict()

    for i in listA:
        if isinstance(i,int) or isinstance(i,float):
            if i%2==0:
                evens.append(i)
                mydict["evens"]=sorted(evens)
            
            else:
                odds.append(i)
                mydict["odds"]=sorted (odds)
                
        elif isinstance(i,str):
            chars+=i
            mydict["chars"]=sorted(chars)
            
        else:
            return ("invalid input")
    return mydict    
print(mylist([2,0,6,5,1,7,'z','a']))











