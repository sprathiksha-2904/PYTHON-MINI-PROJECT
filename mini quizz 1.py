questions = [
    {
        "question": "1. Which language are we using?",
        "options": ["A. Java", "B. Python", "C. C++", "D. HTML"],
        "answer": "B"
    },
    {
        "question": "2. Which keyword displays output in Python?",
        "options": ["A. show()", "B. display()", "C. print()", "D. output()"],
        "answer": "C"
    },
    {
        "question": "3. Which data type stores whole numbers?",
        "options": ["A. int", "B. str", "C. list", "D. bool"],
        "answer": "A"
    },
    {
        "question": "4. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. <!--", "D. **"],
        "answer": "B"
    },
    {
        "question": "5. Which function gets input from a user?",
        "options": ["A. print()", "B. type()", "C. input()", "D. range()"],
        "answer": "C"
    }
]

score = 0

print("================================")
print("      PYTHON QUIZ APPLICATION")
print("================================")
print("Choose A, B, C, or D.\n")

for q in questions:
    print(q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Your answer: ").strip().upper()

    if user_answer == q["answer"]:
        print("Correct answer!\n")
        score += 1
    else:
        print("Wrong answer!")
        print("Correct answer:", q["answer"], "\n")

print("================================")
print("           QUIZ RESULT")
print("================================")
print("Your score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Excellent performance!")
elif percentage >= 50:
    print("Good effort! Keep practising.")
else:
    print("Keep learning and try again!")

print("Thank you for playing!")