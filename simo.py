# Матрица:
# from sympy import Matrix

# A = Matrix([[1, 2], [3, 4]])
# B = Matrix([[5, 6], [7, 8]])

# # Произведение матриц
# result_matrix = A * B
# print("Произведение матриц:", result_matrix)

# # Обратная матрица
# inverse_matrix = A.inv()
# print("Обратная матрица:", inverse_matrix)




# Дифференцирование и интегрирование:
# from sympy import symbols, diff, integrate, sin

# x = symbols('x')  # Определение символа x

# # Производная
# derivative = diff(x**2 + 3*x, x)
# print("Производная:", derivative)

# # Интеграл
# integral_result = integrate(sin(x), x)
# print("Интеграл:", integral_result)



# Символьные переменные и выражения:
# from sympy import symbols, Eq, solve

# x, y = symbols('x y')
# expr = x + 2*y
# print("Выражение:", expr)

# equation = Eq(expr, 10)
# solution = solve(equation, (x, y))
# print("Решение:", solution)




# Решения уравнения:
# from sympy import symbols, solve

# x = symbols('x')
# equation = x**2 - 4
# solutions = solve(equation, x)

# print("Решения уравнения:", solutions)



# Линейная алгебра:
# from sympy import Matrix, Eq, symbols, solve

# x, y = symbols('x y')  # Определение символов

# A = Matrix([[1, 2], [3, 4]])
# B = Matrix([5, 6])

# # Создание системы линейных уравнений
# system = Eq(A * Matrix([x, y]), B)

# # Решение системы:
# solution = solve(system, (x, y))

# print("Решение системы:", solution)


# Графики и визуализация:
# from sympy import symbols, plot

# x = symbols('x')
# p = plot(x**2, (x, -5, 5), show=False)
# p.show()
