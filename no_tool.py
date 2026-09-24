"""
Day 3 Assigned Task
Plain LLM test without any external tool.
"""

from config import client, MODEL


def ask_without_tool(question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful college assistant. "
                    "Answer the student's question using only "
                    "your existing knowledge. You do not have "
                    "access to external tools."
                )
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    questions = [
        "What is a scholarship?",
        "A course costs Rs. 30000. What is 10% of Rs. 30000?",
        "What is the purpose of a college scholarship?"
    ]

    print("=" * 60)
    print("PLAIN LLM - NO TOOL")
    print("=" * 60)

    for question in questions:
        print("\nQ:", question)

        answer = ask_without_tool(question)

        print("A:", answer)