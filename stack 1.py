#stack 
stack=[]
choice=='y'
while choice==y:
    print('1.push')
    print('2.pop')
    print('3.display elements in a stack')
    choice=int(input('enter your choice'))
    if choice==1:
        a=int(input('enter element to push'))
        stack.append(a)
    elif choice==2:
        if stack==[]:
            print('stack is emptyunderflow')
    else:
        print('delete element is',stack.pop())
    elif: choice==3:
        print('stack')
    else:
        print('wrong input')
    choice=input('do you want to continue (y/n)')
    