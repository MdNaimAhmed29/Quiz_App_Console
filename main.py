import json


with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["questions_text"])
    for index, alternative in enumerate (question["alternatives"]):
        print(index+1,"-",alternative)

    choose_answer = int(input("Choose your answer: "))
    question["chosen_answer"] = choose_answer


score = 0
for question in data:

    if question['chosen_answer'] == question['correct_answer']:
        score += 1
        result = "Correct"

    else:
        result = "Incorrect"

    message = f"{result} - Your answer {question['chosen_answer']}," \
              f"{result} - Correct answer {question['correct_answer']}"

    print(message)

print("Your score is:", score, "/" , len(data))