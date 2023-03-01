def hcf(a, b):
  if a == 0:
    return b
  if b == 0:
    return a
  return hcf(b, a % b)

a = int(input("a: "))
b = int(input("b: "))
hcf_result = hcf(a,b)
print(f"HCF of {a} and {b} is {hcf_result}")
