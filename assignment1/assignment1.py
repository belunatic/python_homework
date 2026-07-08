# task1
def hello():
    return "Hello!"

# task2
def greet(name):
    return "Hello, " + name + "!"

# task3
def calc(num1, num2, operation="multiply"):

    if  type(num1) == str or  type(num2) == str:
        return f"You can't {operation} those values!"
    try:
        num1 = float(num1)
        num2 = float(num2)
        if operation == "multiply":
            return num1 * num2
        elif operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "divide":
            return num1 / num2
        elif operation == "modulo":
            return num1 % num2
        elif operation == "power":
            return num1 ** num2
        elif operation == "int_divide":
            return num1 // num2
    except ZeroDivisionError:
        return "You can't divide by 0!"
    

#task 4
def data_type_conversion(value, target_type):
    try:
        if target_type == "int":
            return int(value)
        elif target_type == "float":
            return float(value)
        elif target_type == "str":
            return str(value)
        else:
            return "Invalid target type."
    except ValueError:
        return f"You can't convert {value} into a {target_type}."
    

#task 5
def grade(*scores):
    try:
        average = sum(scores) / len(scores)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."

#task 6
def repeat(string, count):
    try:
        count = int(count)
        new_string = ""
        for _ in range(count):
            new_string += string
        return new_string
    except ValueError:
        return "Count must be an integer."

#task 7
def student_scores(score, **students):
    if not students:
        return "No students provided."
    
    if score == "mean":
        total_score = 0
        for value in students.values():
            total_score += value
        return total_score / len(students)
    elif score == "best":
        best_student = ''
        current_value = 0
        for key, value in students.items():
            if value > current_value:
                current_value = value
                best_student = key
        return best_student
    else:
        return "Invalid score requested."
    
#task 8
def titleize(string):
    words = string.split()
    little_words = ["a", "on", "an", "the", "of", "and", "is","in"]
    titleized_words = []
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word.lower() not in little_words:
            titleized_words.append(word.capitalize())
        else:
            titleized_words.append(word.lower())
    return ' '.join(titleized_words)

#task 9
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

#task 10
def pig_latin(sentence):
    words = sentence.split()
    pig_latin_words = []
    vowels = "aeiou"
    for word in words:
        if word[0] in vowels:
            pig_latin_words.append(word + "ay")
        else:
            consonant_cluster = ""
            for i,letter in enumerate(word):
                if letter not in vowels:
                    consonant_cluster += letter
                    if letter == "q" and  word[i + 1] == "u":
                        consonant_cluster += word[i + 1]
                        break
                else:
                    break
            pig_latin_word = word[len(consonant_cluster):] + consonant_cluster + "ay"
            pig_latin_words.append(pig_latin_word)
    return ' '.join(pig_latin_words)

print(pig_latin("the quick brown fox"))
print(pig_latin("square"))