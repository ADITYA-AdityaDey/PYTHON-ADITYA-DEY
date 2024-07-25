def print_pascals_triangle(n):
    def generate_pascals_triangle():
        triangle = [[1]]
        for _ in range(1, n):
            row = [1]
            for j in range(1, len(triangle[-1])):
                row.append(triangle[-1][j - 1] + triangle[-1][j])
            row.append(1)
            triangle.append(row)
        return triangle

    def print_triangle(triangle):
        max_width = len(str(triangle[-1][len(triangle[-1]) // 2])) * 2  # calculate max width for formatting
        for row in triangle:
            row_str = ' '.join(map(lambda x: f"{x:>{max_width}}", row))
            print(row_str.center(len(row_str) + max_width))

    pascals_triangle = generate_pascals_triangle()
    print_triangle(pascals_triangle)

# Example usage:
n_rows = 7
print_pascals_triangle(n_rows)

