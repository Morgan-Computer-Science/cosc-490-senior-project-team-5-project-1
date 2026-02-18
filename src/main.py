def main():
    print("Morgan CS Advising Assistant Prototype")
    print("Type 'exit' to quit")

    knowledge = [
        "COSC 112 requires COSC 111",
        "Freshman recommended courses include COSC 111 and MATH 141",
        "Tutoring lab available for CS students",
        "Advising office provides course planning support"
    ]

    while True:
        question = input("You: ").lower()
        if question == "exit":
            break

        found = False
        for line in knowledge:
            if any(word in line.lower() for word in question.split()):
                print("Answer:", line)
                found = True

        if not found:
            print("No match found yet.")

if __name__ == "__main__":
    main()

