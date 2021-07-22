#7. Given a signed 32-bit integer x, return x with its digits reversed. If reversing it causes it to go out of range [-2^31, 2^31-1] return 0

def reverse(x: int) -> int:
    r = 0
    sign = 1
    if x > pow(2,31)-1 or x < -1*pow(2,31):
        return 0
    if x < 0:
        sign = -1
        x *= -1
    while x > 0:
        r *= 10
        r += x%10
        x //= 10
    return r * sign

print(reverse(100))
print(reverse(12345))
print(reverse(-123))
