guess = 0
tries = 0

while guess != 6 and tries < 4:
    guess = int(input("Guess the number: "))
    tries += 1

if tries == 4:
    print('No more chances. The correct number was 6.')
else:
    print("You got it!")

