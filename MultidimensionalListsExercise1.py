n = int(input())

matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split(", ")])

primary = []
secondary = []
for idx in range(n):
    primary.append(matrix[idx][idx])
    secondary.append(matrix[idx][n - 1 - idx])

print(f"Primary diagonal: {', '.join([str(x) for x in primary])}, Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}, Sum: {sum(secondary)}")


