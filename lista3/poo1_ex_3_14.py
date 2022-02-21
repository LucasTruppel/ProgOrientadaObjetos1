while True:
    N = int(input())
    if N == 0:
        break
    quadrados = int(N*(N+1)*(2*N+1)/6)
    print(quadrados)
