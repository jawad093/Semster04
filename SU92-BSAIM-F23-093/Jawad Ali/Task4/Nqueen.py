def N_Queen(N):
    n_queen = [[0] * (1 << N) for _ in range(N + 1)]
    n_queen[0][0] = 1  

    for row in range(N):
        for mask in range(1 << N): 
            if n_queen[row][mask] == 0:
                continue
            for col in range(N):
                if mask & (1 << col) == 0: 
                    new_mask = mask | (1 << col)
                    n_queen[row + 1][new_mask] += n_queen[row][mask]

    return sum(n_queen[N])  
N = int(input("Enter N for N-Queen: "))
print("Total Solutions:", N_Queen(N))
