def main():
    # Get user inputs
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")

    # Create the story
    story = f"Today I saw a {adjective} {noun} that {verb} {adverb}."

    # Print the story
    print("\nHere is your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    main()