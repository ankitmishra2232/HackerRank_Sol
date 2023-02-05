# https://www.hackerrank.com/challenges/drawing-book/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

n=9
p=9
def pageCount(n, p):
    d = n - p
    d += int(p % 2 and not n % 2)
    print(min(p//2, d//2))

pageCount(n, p)

# https://www.hackerrank.com/challenges/counting-valleys/problem?h_r=next-challenge&h_v=zen

a=['U','D','D','U','U','D','U','U']

count = 0 #in a plain
valley_count = 0
prev = 0
flag = False

for i in a:
    if i == "D":
        count -= 1
        if flag:
            if count == 0 and prev < 0:
                valley_count += 1
    
    elif i == "U":
        count += 1
        if flag:
            if count == 0 and prev < 0:
                valley_count += 1
    

    prev = count
    flag = True
print(valley_count)


#https://www.hackerrank.com/challenges/electronics-shop/problem

b=6
key= [40,50,60]
drives=[5,8,12]
out=[]

for i in range(len(key)):
    for j in range(len(drives)):
        sum = key[i]+drives[j]
        result = b-sum
        if result >= 0:
            out.append(sum)
if out ==[]:
    print('-1')
else:
    print(max(out))
    
# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

x=1
y=3
z=2

catA = abs(x - z)
catB = abs(y - z)
if catA < catB:
    print('Cat A') 
elif catB < catA:
    print('Cat B')
else:
    print('Mouse C')