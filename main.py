#!/usr/bin/env python3
"""
Main entry point for the application
"""

def greet(name: str, mood: str) -> str:
	return f"{name}, du fühlst dich gerade {mood}. Du gehst einen starken Weg 💪"


def main():
	name = input("Wie heißt du? ")
	mood = input("Wie fühlst du dich gerade? ")
	print(greet(name, mood))


if __name__ == "__main__":
	main()
