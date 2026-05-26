A, B, C = map(int, input().split())
if A > B and A > C:
    print("Player A")
elif B > A and B > C:
    print("Player B")
elif C > A and C > B:
    print("Player C")
else:
    print("Tie")