prompt = "Enter your age: "

while True:
    try:
        age_input = input(prompt)
        age = int(age_input)
    except EOFError:
        print("EOF Error. Please enter your age.")
    except ValueError:
        print("Value Error. Please enter only integers.")
    except KeyboardInterrupt:
        print("Keyboard Interrupt. Please enter your age.")
    else:
        break

print(age)
