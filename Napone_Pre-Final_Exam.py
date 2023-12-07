def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

# Get user input for the range
start = int(input("Enter starting number (non-negative): "))

# Loop until user enters a valid end number or 0
while True:
  end = int(input("Enter ending number (greater than or equal to start): "))

  # Check for invalid start number
  if start < 0:
    print("Enter a non-negative number.")
    continue

  # Check for termination condition
  elif end == 0:
    print("Program terminated.")
    break

  # Check for invalid end number
  elif end < start:
    print("Enter a number greater than or equal to start.")
    continue

  else:
    break

# Print prime numbers within the range
if end != 0:
  print(f"Prime numbers between {start} and {end}:")
  for num in range(start, end + 1):
    if is_prime(num):
      print(num)
