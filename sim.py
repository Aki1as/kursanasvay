from sympy import Matrix, symbols, Eq, solve

x, y = symbols('x y')

A = Matrix([[1, 2], [3, 4]])
B = Matrix([5, 6])

система = Eq(A * Matrix([x, y]), B)
решение = solve(система, (x, y))

print(решение)
