list1=["c=","c-","dz=","d-","lj","nj","s=","z="]
str1=input()
count=0

for i in range(len(str1)):
    if str1[i]=='=' or str1[i]=='-':
        if str1[i-1]=='c' or str1[i-1]=='d' or str1[i-1]=='s':
            count+=0
        elif str1[i-1]=='z':
            if (i>1 and str1[i-2]=='d'):
                count-=1
            else:
                count+=0
    elif str1[i]=='j':
        if (i>0 and str1[i-1]=='l') or (i>0 and str1[i-1]=='n'):
            count+=0
        else:
            count+=1
    else:
        count+=1


print(count)
        