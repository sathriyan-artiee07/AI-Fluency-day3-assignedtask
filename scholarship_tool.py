"""
Single tool for calculating a student's final course fee
after applying a scholarship.
"""


def calculate_final_fee(course_fee: float, scholarship_percent: float) -> str:
    """Calculate final fee after scholarship deduction."""

    try:
        course_fee = float(course_fee)
        scholarship_percent = float(scholarship_percent)

        if course_fee < 0:
            return "Tool error: course fee cannot be negative."

        if scholarship_percent < 0 or scholarship_percent > 100:
            return "Tool error: scholarship must be between 0 and 100 percent."

        discount = course_fee * scholarship_percent / 100
        final_fee = course_fee - discount

        return (
            f"Original fee: Rs. {course_fee:.2f}\n"
            f"Scholarship: {scholarship_percent:.1f}%\n"
            f"Discount: Rs. {discount:.2f}\n"
            f"Final fee: Rs. {final_fee:.2f}"
        )

    except (ValueError, TypeError) as error:
        return f"Tool error: invalid input - {error}"


TOOL_FUNCTIONS = {
    "calculate_final_fee": calculate_final_fee
}


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calculate_final_fee",
            "description": (
                "Calculate the final course fee after applying "
                "a scholarship percentage."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "course_fee": {
                        "type": "number",
                        "description": "Original course fee in rupees."
                    },
                    "scholarship_percent": {
                        "type": "number",
                        "description": "Scholarship percentage."
                    }
                },
                "required": [
                    "course_fee",
                    "scholarship_percent"
                ]
            }
        }
    }
]


if __name__ == "__main__":
    print("Testing scholarship tool:")
    print(calculate_final_fee(30000, 10))
    