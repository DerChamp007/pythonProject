def remove_and_add_numbers(input_string):
    numbers_sum = 0
    result_string = ""

    for char in input_string:
        if char.isnumeric():
            numbers_sum += int(char)
        else:
            result_string += char

    return numbers_sum, result_string

input_string = input("Gib einen String ein: ")
total_sum, result = remove_and_add_numbers(input_string)
print("Ergebnis der Addition der Zahlen:", total_sum)
print("String ohne Zahlen:", result)
