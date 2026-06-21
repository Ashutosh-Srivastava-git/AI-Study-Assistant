import google.generativeai as genai
import os
import sys
from dotenv import load_dotenv

def create_model():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction=(
            "You are a patient, expert tutor who specializes in breaking down any "
            "academic or technical subject into a clear, beginner-friendly study plan. "
            "When the user gives you a topic, respond ONLY with a numbered list of 5 to 7 subtopics, "
            "ordered from foundational to advanced. Each item MUST follow this exact format: "
            "1. **Subtopic Name** - one concise sentence describing what it covers. "
            "Do not add an introduction, conclusion, or any text before or after the numbered list "
            "when presenting a study plan. "
            "When the user asks a follow-up question about any subtopic, answer directly and concisely "
            "in plain text (no forced list format required), staying strictly within the context of the "
            "topic already being studied. "
            "Do not go off-topic into unrelated subjects even if the user's question drifts -"
            " gently bring the conversation back to the study topic."
        ),
    )
    return model
 
 
def print_summary(topic_studied, question_count):
    print("\n  SESSION SUMMARY")
    print(f"  Topic studied      : {topic_studied if topic_studied else 'None'}")
    print(f"  Follow-up questions: {question_count}")
    print("Goodbye! Keep studying.")
 
 
def main():
    model = create_model()
    chat = model.start_chat(history=[])
    print(" AI STUDY ASSISTANT")
    print(" Type a topic to get a study plan.")
 
    topic_studied = None
    question_count = 0
 
    first_input = input("\nEnter a topic you want to study: ").strip()
    if first_input.lower() in ("quit", "exit"):
        print_summary(topic_studied, question_count)
        return
 
    topic_studied = first_input
 
    try:
        response = chat.send_message(first_input)
        print("\n" + response.text)
    except Exception as e:
        print(f"\n[Error contacting Gemini API: {e}]")
        return
 
    while True:
        user_input = input("\nAsk a follow-up question (or 'quit'/'exit'): ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit"):
            print_summary(topic_studied, question_count)
            break
        try:
            response = chat.send_message(user_input)
            print("\n" + response.text)
            question_count += 1
        except Exception as e:
            print(f"\n[Error contacting Gemini API: {e}]")
 
 
if __name__ == "__main__":
    main()
