# From Prompt to Action: LLM With and Without an External Tool

## 1. Scenario

For this task, I selected a college scholarship fee calculation scenario.

The scenario is based on a student who wants to understand scholarships and calculate the final course fee after applying a scholarship percentage.

The single external tool used in this project is called `calculate_final_fee`. It accepts the original course fee and scholarship percentage and returns the original fee, discount amount, and final fee.

This scenario was selected because some questions can be answered using the language model's general knowledge, while a numerical calculation can be handled more reliably by an external function.

---

## 2. What is a Large Language Model?

A Large Language Model (LLM) is an AI system trained on large amounts of text to understand and generate natural-language responses.

In this scenario, the plain LLM was able to answer questions such as:

> What is a scholarship?

It also answered:

> What is the purpose of a college scholarship?

These questions do not require access to an external system or a special calculation tool.

However, when the user asks for an exact calculation, relying only on generated text is less desirable because the model is generating the mathematical reasoning rather than obtaining the result from a dedicated calculation function.

In my experiment, the no-tool model answered:

> 10% of Rs. 30,000 is Rs. 3,000.

The answer was correct. However, the purpose of the experiment is to show that a tool can perform the operation explicitly and return a deterministic result.

---

## 3. What is an Agent?

An AI agent is an LLM-based system that can interact with tools or external resources to complete a task.

A normal chat response can generate an answer directly from the model.

An agent can take an additional action when required.

In my scenario, the plain LLM answered the scholarship questions directly.

The tool-enabled version behaved differently for the calculation question. It recognized that the question could be handled using the `calculate_final_fee` tool, generated a tool call, received the calculation result, and then produced the final response.

Therefore, the main difference in this experiment is not simply the quality of the language response. The important difference is that the tool-enabled system can perform an external operation before producing its final answer.

---

## 4. What is a Tool?

A tool is an external function that an LLM can request when it needs an operation that is better handled by a program.

The tool created for this project is:

`calculate_final_fee(course_fee, scholarship_percent)`

The tool receives:

- `course_fee` - the original course fee
- `scholarship_percent` - the scholarship percentage

It calculates the discount and final fee.

For example:

```text
course_fee = 30000
scholarship_percent = 10