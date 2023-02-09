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
    

# https://www.hackerrank.com/challenges/magic-square-forming/problem?isFullScreen=false

squares = [
    [[8, 1, 6], [3, 5, 7], [4, 9, 2]], 
    [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
    [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
    [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
    [[4, 9, 2], [3, 5, 7], [8, 1, 6]], 
    [[8, 3, 4], [1, 5, 9], [6, 7, 2]], 
    [[6, 1, 8], [7, 5, 3], [2, 9, 4]], 
    [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
]

def formingMagicSquare(s):
    costs=[]
    for q in squares:
        cost=0
        for i in range(3):
            for j in range(3):
                cost+=abs(q[i][j]-s[i][j])
        costs.append(cost)
    print(min(costs)) 
    
    
    
    


 # https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
 
a=[4,6,5,3,3,1]
a.sort()
maxLen = 1
for i in range(len(a)):
    maxElement = a[i]
    minElement = a[i]
    
    for j in range(i+1, len(a)):
        maxElement = max(maxElement, a[j])
        minElement = min(minElement, a[j])
        if ((maxElement - minElement) <=1):
            current_lenght = j - i + 1
            maxLen = max(maxLen, current_lenght)
print(maxLen)


# https://www.hackerrank.com/challenges/the-hurdle-race/problem?isFullScreen=true
k=5
height=[1,2,5,5,8,6]

ans = max(height) - k    
if ans < 0:
    print('0')
else:
    print(ans)


# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

def designerPdfViewer(h, word):
    a=[]
    b=[]
    for i in word:
        a.append(ord(i)-97)
    for j in a:
        b.append(int(h[j]))
    return max(b)*len(a)


