def mark_spot(n):

    if isinstance(n, int) and n > 0 and n % 2 != 0:
        string = ""
        # Forward loop
        for row in range(0, n, 2):
            leading_spaces = row * " " + "X"
            if row + 1 == n:
                trailing_spaces = "\n"
            else:
                trailing_spaces = (2 * n - 3 - 2 * row) * " " + "X\n"
            string += leading_spaces + trailing_spaces

        # Backward loop
        for row in range(n - 3, -1, -2):
            leading_spaces = row * " " + "X"
            trailing_spaces = (2 * n - 3 - 2 * row) * " " + "X\n"

            string += leading_spaces + trailing_spaces

        return string
    else:
        return "?"


print(mark_spot(11))
