list1 = [0] * 3
time = [5, 4, 10]
cost = [1500, 1000, 3000]
inputTime = int(input("Enter the  time: "))
king = []  
ans = []  
def findMax(ind, currentTime, profit, l):
    if ind == len(time):
          
        if currentTime != 0:

            for i in range(len(cost)):
                if l[i] != 0:
                    profit += currentTime * cost[i] *l[i]
            
        ans.append(profit)
        king.append(l.copy())
        return
    
    if currentTime - time[ind] >= 0:
        if l:
            for i in range(len(cost)):
                if l[i] != 0:
                    profit += time[ind] * cost[i] * l[i]
        l[ind] += 1
        findMax(ind, currentTime - time[ind], profit, l)
        l[ind] -= 1
        if l:
            for i in range(len(cost)):
                if l[i] != 0:
                    profit -= time[ind] * cost[i] * l[i]
    findMax(ind+1, currentTime, profit, l)

findMax(0, inputTime, 0, list1) 
maximum = max(ans)

maxi = []
original = []
for i in range(len(ans)):
    if ans[i] == maximum:
        maxi.append(i)

for i in maxi:  
    original.append(king[i])

o = [{'T': i[0], 'P': i[1], 'C': i[2]} for i in original]
print(f'Profit : {maximum}')
for i in o:
    print(i)



    
