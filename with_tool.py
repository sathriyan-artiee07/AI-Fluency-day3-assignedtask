"""
Day 3 Assigned Task
LLM with one external scholarship calculation tool.
"""

import json

from config import client, MODEL
from scholarship_tool import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = """
You are a college fee assistant.

You can answer general questions directly.

When a question requires calculating a scholarship-adjusted
course fee, use the calculate_final_fee tool.

Do not guess the calculated result when the tool can calculate it.

After receiving the tool result, explain the answer clearly.
"""


def ask_with_tool(question):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=TOOLS,
        temperature=0
    )

    message = response.choices[0].message

    # No tool required
    if not message.tool_calls:
        return {
            "tool_called": False,
            "tool_name": None,
            "tool_arguments": None,
            "tool_result": None,
            "answer": message.content
        }

    # Record the tool call
    tool_call = message.tool_calls[0]

    tool_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)

    print("\nTool call:")
    print("Tool:", tool_name)
    print("Arguments:", arguments)

    # Run the tool
    function = TOOL_FUNCTIONS.get(tool_name)

    if function is None:
        tool_result = f"Unknown tool: {tool_name}"
    else:
        tool_result = function(**arguments)

    print("Tool result:")
    print(tool_result)

    # Give the tool result back to the model
    messages.append({
        "role": "assistant",
        "content": message.content or "",
        "tool_calls": [
            {
                "id": tool_call.id,
                "type": "function",
                "function": {
                    "name": tool_name,
                    "arguments": tool_call.function.arguments
                }
            }
        ]
    })

    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": str(tool_result)
    })

    final_response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0
    )

    final_answer = final_response.choices[0].message.content

    return {
        "tool_called": True,
        "tool_name": tool_name,
        "tool_arguments": arguments,
        "tool_result": tool_result,
        "answer": final_answer
    }


if __name__ == "__main__":

    questions = [
        "What is a scholarship?",
        "A course costs Rs. 30000. Calculate the final fee after a 10% scholarship.",
        "Why do colleges provide scholarships?"
    ]

    print("=" * 60)
    print("LLM WITH ONE TOOL")
    print("=" * 60)

    for question in questions:

        print("\n" + "-" * 60)
        print("Q:", question)

        result = ask_with_tool(question)

        print("\nFinal answer:")
        print(result["answer"])