def lcm(a,b):
    lcm=0;
    big=a
    if a>b:
        big=b
    while(big<=a*b):
        if big%a==0 and big%b==0:
            lcm=big
            return lcm
        big+=1

def hcf(a,b):
    hcf=0;
    small=a
    if a>b:
        small=b
    while(small>=1):
        if a%small==0 and b%small==0:
            hcf=small
            return hcf
        small-=1
        
cond=True
a,b,res=0,0,''
while cond:
    que=input('Ask your question : ')
    lst=que.split(sep=' ')
    try:
        if lst.index('hello')+1:
            res='Hello Sir/Mam, Welcome to Smart Calculator'
    except:
        pass
    try:
        if lst.index('hyy')+1:
            res='Hyy Sir/Mam, Welcome to Smart Calculator'
    except:
        pass
    try:
        if lst.index('end')+1:
            res='Thankyou for Using'
            cond=False
    except:
        pass
    try:
        if lst.index('off')+1:
            res='Thankyou for Using'
            cond=False
    except:
        pass
    try:
        if lst.index('close')+1:
            res='Thankyou for Using'
            cond=False
    except:
        pass
    try:
        if lst.index('quit')+1:
            res='Thankyou for Using'
            cond=False
    except:
        pass
    try:
        if lst.index('exit')+1:
            res='Thankyou for Using'
            cond=False
    except:
        pass
    for i in lst:
        try:
            if a==0:
                a=int(i)
            elif b==0:
                b=int(i)
        except:
            pass
    try:
        if lst.index('add')+1:
            res=a+b
    except:
        pass
    try:
        if lst.index('+')+1:
            res=a+b
    except:
        pass
    try:
        if lst.index('plus')+1:
            res=a+b
    except:
        pass
    try:
        if lst.index('addition')+1:
            res=a+b
    except:
        pass
    try:
        if lst.index('sum')+1:
            res=a+b
    except:
        pass
    try:
        if lst.index('subtract')+1:
            res=a-b
    except:
        pass
    try:
        if lst.index('-')+1:
            res=a-b
    except:
        pass
    try:
        if lst.index('subtraction')+1:
            res=a-b
    except:
        pass
    try:
        if lst.index('difference')+1:
            res=a-b
    except:
        pass
    try:
        if lst.index('minus')+1:
            res=a-b
    except:
        pass
    try:
        if lst.index('divide')+1:
            res=a/b
    except:
        pass
    try:
        if lst.index('/')+1:
            res=a/b
    except:
        pass
    try:
        if lst.index('by')+1:
            res=a/b
    except:
        pass
    try:
        if lst.index('division')+1:
            res=a/b
    except:
        pass
    try:
        if lst.index('multiply')+1:
            res=a*b
    except:
        pass
    try:
        if lst.index('into')+1:
            res=a*b
    except:
        pass
    try:
        if lst.index('*')+1:
            res=a*b
    except:
        pass
    try:
        if lst.index('product')+1:
            res=a*b
    except:
        pass
    try:
        if lst.index('multiplication')+1:
            res=a*b
    except:
        pass
    try:
        if lst.index('power')+1:
            res=a**b
    except:
        pass
    try:
        if lst.index('raise')+1:
            res=a**b
    except:
        pass
    try:
        if lst.index('raised')+1:
            res=a**b
    except:
        pass
    try:
        if lst.index('^')+1:
            res=a**b
    except:
        pass
    try:
        if lst.index('lcm')+1:
            res=lcm(a,b)
    except:
        pass
    try:
        if lst.index('hcf')+1:
            res=hcf(a,b)
    except:
        pass
    if res=='':
        print('Sorry I don\'t understand')
    print(res)
    a,b,res=0,0,''
input()
