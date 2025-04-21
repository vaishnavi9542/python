def elections(N, A):
    if N == 1:
        return A[0]
    vote = {}
    for i in A:
        if i in vote:
            vote[i] += 1
        else:
            vote[i] = 1
    max_votes = 0
    winner = -1
    tie = False
    for j in vote:
        if vote[j] > max_votes:
            max_votes = vote[j]
            winner = j
            tie = False
        elif vote[j] == max_votes:
            tie = True
    return -1 if tie else winner

N = int(input())
A = list(map(int, input().split()))
print(elections(N,A))
