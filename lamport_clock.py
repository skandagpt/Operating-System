def display(P):
    for i in range(len(P)):
        print(f'P{i+1} -->', end = ' ')
        for j in range(len(P[i])):
            print('---',P[i][j],'---', end = '')
        print('\n')
        
P = [[],[], []]
n1, n2, n3 = map(int, input('Enter no of event in each process : ').split())

for i in range(1, n1+1):
    P[0].append(i)
    
for i in range(1, n2+1):
    P[1].append(i)
    
for i in range(1, n3+1):
    P[2].append(i)
    
display(P)
comm = int(input('Enter no of communication lines : '))
count = 0

while count < comm:
    sent, sentevent = map(int, input('Enter sending process and event number : ').split())
    recv, recvenent = map(int, input('Enter recieving process and event number : ').split())
    
    print(f'Process P{sent}({sentevent}) --->  P{recv}({recvenent})')
    
    if recvenent > 1:
        P[recv-1][recvenent-1] = max(P[recv-1][recvenent-2] + 1, P[sent-1][sentevent-1] + 1)
    else:
        P[recv-1][recvenent-1] = P[sent-1][sentevent-1] + 1
    for i in range(recvenent,len(P[recv-1])):
        P[recv-1][i] = max(P[recv-1][i-1] + 1, P[recv-1][i])
    display(P)
    count += 1