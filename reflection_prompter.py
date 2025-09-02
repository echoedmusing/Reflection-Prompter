import random
from datetime import date

def get_prompts():
    """Reads prompts from a 'prompts.txt' file."""
    try:
        with open("prompts.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Error: prompts.txt not found in the same directory.")
        return ["No prompts loaded. Please check prompts.txt."]

def get_daily_prompt(prompts):
    """Generates a consistent daily prompt based on the current date."""
    if not prompts:
        return "No prompts available."
    
    today = date.today()
    # Create a seed for consistent daily prompt selection
    seed_value = today.year * 10000 + today.month * 100 + today.day
    random.seed(seed_value) 
    return random.choice(prompts)

def get_random_prompt(prompts):
    """Generates a random prompt."""
    if not prompts:
        return "No prompts available."
    return random.choice(prompts)

def main():
    print("\n--- Reflection Prompter ---")
    prompts = get_prompts()
    if not prompts:
        print("Cannot generate prompts without prompts.txt.")
        return

    print("1. Get today's reflective prompt.")
    print("2. Get a random reflective prompt.")
    print("---------------------------")

    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == '1':
        print("\nYour daily reflection prompt:")
        print(get_daily_prompt(prompts))
    elif choice == '2':
        print("\nYour random reflection prompt:")
        print(get_random_prompt(prompts))
    else:
        print("Invalid choice. Please enter '1' or '2'.")
    print("\n--- End of Prompter ---")

if __name__ == "__main__":
    main()
