def lone_sum(a, b, c):
  return c if (a == b and a!=c) else a if (b == c and b!=a) else b if (a == c and a!=b) else 0 if a==b==c else a + b + c
