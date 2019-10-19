from Question import Question

question_prompts = [
    "what color are ur skin?\n A) Pink\n B) Red\n C) Purple\n\n",
    "bla bla bla?\n A) Ponk\n B) Rdd\n C) Pdrple\n\n"
]
question = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b")
]
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got" + str(score) + "/" + str(len(questions)) + " correct")
run_test(question)
