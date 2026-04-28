#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from robodoc.crew import Robodoc

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    print("\n=== RoboDoc Symptom Checker ===")
    print("Type 'quit' to exit\n")

    while True:
        symptoms = input("Enter your symptoms: ")

        if symptoms.lower() == "quit":
            break

        inputs = {
            "symptoms": symptoms
        }

        try:
            
            result = Robodoc().crew().kickoff(inputs=inputs)
            print("\nPossible Diagnosis:")
            print(result)
            print("\n---------------------------\n")

        except Exception as e:
            print(f"Error: {e}")

#Note: Ollama must be running before the crew can run(ollama list).
