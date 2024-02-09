def parse_molecule(formula):
    molecules_names = {}
    formula = list(formula)
    for item in formula:
        if not item.isdigit() and item.isalpha():
            molecules_names[item] = formula.count(item)
            print(molecules_names)

    for i, item in enumerate(formula):
        if item.isdigit():
            molecules_names[formula[i - 1]] = molecules_names[formula[i - 1]] * int(
                item
            )

    return molecules_names


formula = "H2O"
formula_1 = "Mg(OH)2"
parse_molecule(formula)
print()
parse_molecule(formula_1)

"""
1. Wysuzkaj jednego z charakterysycznych znaków -> )]} lub num
2. Jeżeli znajdziesz nawias, sprawdź czy kolejny znak to nawias ]} bądź liczba 
3. Je\zeli znajdziesz } to suzkaj liczby
4. 
"""
