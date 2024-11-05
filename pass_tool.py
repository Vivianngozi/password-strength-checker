from zxcvbn import zxcvbn

password = input("Enter a password: ")
result = zxcvbn(password)

print(f"Password Strength Score {result['score']} / 4")
print(f"Estimated Crack Time: {result['crack_times_display']['offline_slow_hashing_1e4_per_second']}")
print("Feedback:", result['feedback']['suggestions'])