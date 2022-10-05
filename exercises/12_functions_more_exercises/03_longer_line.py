from math import floor, sqrt


def line_len_largest(a1, b1, a2, b2, c1, d1, c2, d2):
    len_line_a = sqrt((a1 - a2) ** 2 + (b1 - b2) ** 2)
    len_line_b = sqrt((c1 - c2) ** 2 + (d1 - d2) ** 2)
    if len_line_a >= len_line_b:
        return f"({floor(a1)}, {floor(b1)})({floor(a2)}, {floor(b2)})" if abs(a1 + b1) <= abs(a2 + b2) \
          else f"({floor(a2)}, {floor(b2)})({floor(a1)}, {floor(b1)})"
    else:
        return f"({floor(c1)}, {floor(d1)})({floor(c2)}, {floor(d2)})" if abs(c1 + d1) <= abs(c2 + d2) \
          else f"({floor(c2)}, {floor(d2)})({floor(c1)}, {floor(d1)})"


w1, w2, x1, x2 = float(input()), float(input()), \
                 float(input()), float(input())
y1, y2, z1, z2 = float(input()), float(input()), \
                 float(input()), float(input())

print(line_len_largest(w1, w2, x1, x2, y1, y2, z1, z2))
