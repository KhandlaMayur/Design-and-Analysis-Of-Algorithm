#find minimum number of multiplication
def matrix_chain_multiply(n):
    m = [[0 for _ in range(n)] for _ in range(n)]
    for d in range(1, n):
        for i in range(1, n - d):
            j = i + d
            m[i][j] = float('inf')
            for k in range(i, j):
                temp = m[i][k] + m[k + 1][j] + dn[i - 1] * dn[k] * dn[j]
                
                if temp < m[i][j]:
                    m[i][j] = temp
    return m[1][n - 1]

dn = [3, 5, 2, 3, 4]
n = len(dn)
print("Minimum number of multiplications is:",matrix_chain_multiply(n))
