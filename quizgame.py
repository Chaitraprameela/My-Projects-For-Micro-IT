def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
            "answer": "A"
        },
        {
            "question": "What is 5 + 7?",
            "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
            "answer": "C"
        }
    ]

    score = 0

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.")

    print(f"\n🎉 You got {score} out of {len(questions)} correct!")

run_quiz()
