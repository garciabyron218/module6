# Byron Garcia
# 2/25/24
# program will figure out PI

def leibniz_formula(terms):
    approx_pi = 0
    for n in range(terms):
        term = (-1) ** n / (2 * n + 1)
        approx_pi += 4 * term
    return approx_pi

terms = 10000
approximation = leibniz_formula(terms)


# Print the result
print("Approximation of pi using Leibniz formula:", approximation)
