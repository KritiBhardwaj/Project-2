import json

quiz_questions = {}

with open("data/quiz.json") as json_file:
    data = json.load(json_file)


# print(data["quiz"]["One"])
# print(type(data["quiz"]["One"]))

# for quesNum, question in data["quiz"].items():
#     print(f"{quesNum}: {question}")
#     print()

#quiz - dict
#question details - dict
#question - string
#options - list
#answer - string

# for key, value in data.items():
#     for k1, v1 in value.items():
#         print(f"Question {k1}: {v1['question']}")
#         for option in v1['options']:
#             print(f"      {option}")

for quiz, details in data.items():
    print(details)
    print()
    for quesNum, content in details.items():
        print()
        print(f"Question {quesNum} : {content['question']}")
        for option in content["options"]:
            print(f"      {option}")
        print(f"Answer {quesNum} : {content['answer']}")

    print()

    



    

