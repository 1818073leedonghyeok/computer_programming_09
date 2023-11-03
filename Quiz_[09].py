height = int(input("크리스마스 트리의 높이를 설정하세요: "))
for i in range(height):
    for j in range(height - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()
