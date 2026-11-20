
def summarization_prompt(topic):
    return f"Summarize the following topic in simple words: {topic}"


def email_prompt(subject):
    return f"Write a professional email about: {subject}"


def coding_prompt(problem):
    return f"Explain and solve this coding problem step by step: {problem}"


def research_prompt(topic):
    return f"Provide a structured overview of: {topic}"


if __name__ == "__main__":
    print(summarization_prompt("Generative AI"))
    print(email_prompt("Internship application"))
    print(coding_prompt("Find the largest number in a list"))
    print(research_prompt("Prompt Engineering"))
