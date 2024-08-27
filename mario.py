# Prompt the user for the height of the pyramid
while True:
    try:
        height = int(input("Height: "))
        if 1 <= height <= 8:
            break
    except ValueError:
        continue

# Build the half-pyramid
for i in range(1, height + 1):
    print(" " * (height - i) + "#" * i)
