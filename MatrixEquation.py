print ("Solving Ax = b")
n = input("Enter size of matrix A")
A = list()
for i in range(n):
    A.append(list())
for i in A:
    for j in range(n):
        i.append(input())
print ("now enter values of b")
b = list()
for i in range(n):
    b.append(input())

print ("matrix afzoode is : ")

j =0
for i in A:
        i.append(b[j])
        j+=1
        print (i)
j=0
i=0
while j < n:
    i = j
    while i < n:
        if (A[i])[j] != 0:
            A[i] , A[j] = A[j] , A[i]
            print ("how u doin ? : ",(A[j]),A[i])
            break
        i+=1
    i=j+1
    while i < n:
        if (A[i])[j] != 0:
            reduce = float(float((A[i])[j])/(float((A[j])[j])))
            m=0
            while m <= n:
                A[i][m] -= reduce*(A[j])[m]
                m+=1
        i+=1
    j+=1
j=n-1
while j>=0:
    if (A[j])[j] != 1 and (A[j])[j] != 0:
        m=j+1
        while m <=n:
            A[j][m] =float (float (A[j][m]) /float (A[j][j]))
            m+=1
        A[j][j] = 1
    j-=1

print (A)
j=n-2
while j>=0:
    if (A[j])[j+1] != 0 and (A[j+1][j+1]) != 0:
        m=j+1
        reduce = float (A[j][j+1]) /float (A[j+1][j+1])
        while m <=n:
            A[j][m] -=float ( reduce* float (A[j+1][m]))
            m+=1
    j-=1
print (A)
answerNum = 1

answer = list()
if A[n-1][n-1] == 0:
    if A[n-1][n] != 0:
        answerNum = 0
    else:
        answerNum = 2
if answerNum == 0:
    print ("doesn't have answer!")
elif answerNum == 1:
    j=0
    while j<n:
        answer.append(A[j][n])
        j+=1
else:
    j=0
    while j<n:
        i=j+1
        answer.append("")
        if A[j][j] == 0:
            answer[j]+= "x" + str(j+1)
            j+=1
            continue
        while i<n:
            answer[j] +="(" +str(-A[j][i])+"x"+str(i+1) + ")+"
            i+=1
        answer[j] += str(A[j][n])
        j+=1
print ("answer : ",answer)