# calculator.py

print("🔢 Welcome to the Smart Calculator")

# Loop to keep the calculator running
while True:
    command = input("😊 Type your calculation (or type 'exit'): ").lower()

    if command == "exit":
        print("👋 Sayonaara!")
        break

    # Breaking the sentence into word
    words = command.split()

    # Extract numbers from the text
    numbers = [int(word) for word in words if word.isdigit()]

    if "add" in command:
        result = sum(numbers)

    elif "subtract" in command:
        if "from" in command and len(numbers) == 2:
            result = numbers[1] - numbers[0]
        else:
            result = numbers[0] - numbers[1]

    elif "multiply" in command:
        result = numbers[0] * numbers[1]

    elif "divide" in command:
        try:
            result = numbers[0] / numbers[1]
        except ZeroDivisionError:
            result = "💀 sorry mathematician I cannot divide any number by zero"

    else:
        result = "😭 Sorry I dont understand that operation"

    print("✅Result :", result)
