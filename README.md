# AI Study Assistant CLI

A command-line study assistant powered by the Gemini API (`gemini-2.5-flash`).
Give it a topic, get a structured study plan, then ask follow-up questions in a
continuing, context-aware conversation.


## How to Run?

1. Clone the repository using git clone.
2. Make sure you have python and all required libraries installed.
3. Make an dot env file as shown in the example file in the repo and add you api key.
4. Open Terminal and run python study_assistant.py

## Prompt Engineering Writeup

**1. What role did you assign in your system prompt, and why did you choose that framing?**

I assigned the role of a "patient, expert tutor." I chose this over a generic
"assistant" framing because tutoring implies a specific behavior pattern: breaking
complex topics into digestible pieces, ordering them from basic to advanced 
, and adjusting explanation depth for a learner who may be new to the
subject. A bare "assistant" role tends to produce less-structured answers,
since it doesn't carry any implicit expectation about teaching clarity.

**2. What format did you specify for the study plan output, and how did you enforce it in the prompt?**

I required a numbered list of 5-7 subtopics, each following the exact pattern
`N. **Subtopic Name** - one sentence `. I enforced this by giving the
literal template directly in the system prompt rather than just describing it in
words, and by explicitly stating that no introduction or conclusion text should
appear before or after the list. Giving the model the exact string pattern to copy
produced far more consistent formatting than describing the format abstractly.

**3. What happens if you remove the system prompt entirely - how does the output change?**

Without the system prompt, `gemini-2.5-flash` still attempts to answer, but the
output does not have any structur: it sometimes adds a Intro and Outro unasked
("Sure, here's a study plan for..."), uses inconsistent formatting (plain paragraphs
in some runs, bullet points in others), and the subtopic count varies unpredictably
between 3 and 10 items depending on phrasing.

- Model used: `gemini-2.5-flash` (free tier, 1,500 requests/day)