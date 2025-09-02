def longest_common_substring(s1, s2):
    n = len(s1)
    m = len(s2)
    l = [[0 for i in range(n+1)] for j in range(m+1)]   

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[j-1] == s2[i-1]:                     
                l[i][j] = 1 + l[i-1][j-1]
            else:
                l[i][j] = max(l[i][j-1], l[i-1][j])     

    return l[m][n]                                      

s1 = str(input("Enter the String s1: "))                   
s2 = str(input("Enter the String s2: "))

print("Longest common substring is", longest_common_substring(s1, s2))
