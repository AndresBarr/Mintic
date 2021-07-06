info = [int(input()),input().split(' 89')]
print('True'if all (list(map(lambda x:x>0,list(map(int,info[1])))))
and any(list(map(lambda x: x[0]==x[1]
or x[0]=='5',list(zip(info[1],list(map(lambda x:x[-1:(len(x)+1)*-1:-1],info[1]))))))) 
else 'False' )