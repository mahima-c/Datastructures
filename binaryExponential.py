# bit exponent function
# application----matrix power-----linear recurrance----transpormation



class Matrix:
    def __init__(self,no,n):
        self.n=n
        self.mat=[[no]*n]*n

def matMul(A,B):
    # c=Matrix(0,2)
    # n=c.n
    c=[[0 for j in range(2)] for _ in range(2)]
    for row in range(2):
        for col in range(2):
            here=0
            for k in range(2):
                here+=(A[row][k]*B[k][col])
            c[row][col]=here
    return c

# matrix_identity=Matrix(1,2)
matrix_identity=[[1,0],[0,1]]

class Power:#log(n)
    def power(self,a,n):#o(logn)
        if n==0:
            return 1
        b=self.power(a,n//2)
        if n%2==0:
            return b*b

        return a*b*b

    def power_it(self,a,n):#s(1)
        ans=1
        while n>0:
            if n%2==1:
                # odd no
                ans=ans*a
            b=b>>1
            a=a*a
        return ans
    # power of matrix
    def matrixPow(self,A,n):
        if n==0:
            return matrix_identity
        # as a**0 is equal to identity matrix
        x=self.matrixPow(A,n//2)
        if n%2==0:
            return matMul(x,x)
        else:
            return matMul(matMul(x,x),A)

    def getFibSeries(self,n):
        fib=[[1,1],[1,0]]
        ans=self.matrixPow(fib,n)[1]
        return sum(ans)




A=[[1,2],[1,0]]
n=2
s=Power()
print(matMul(A,A))
print(Power().matrixPow(A,n))
for i in range(1,10):
    print(s.getFibSeries(i))




            

