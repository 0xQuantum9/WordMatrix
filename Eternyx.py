import itertools
import sys

def get_items(prompt_text):
    print(f"\n[+] {prompt_text}")
    print("    (Press Enter on an empty line to finish)")
    items = []
    while True:
        value = input(f"    {len(items) + 1}> ").strip()
        if not value:
            break
        items.append(value)
    return items

def expand_word_cases(word):
    cases = {word, word.lower(), word.upper(), word.capitalize()}
    if len(word) <= 5:
        for p in itertools.product(*[(char.lower(), char.upper()) for char in word]):
            cases.add("".join(p))
    return list(cases)

def generate_brute_force(words, numbers, dates, symbols, max_depth=4):

    expanded_words = []
    for w in words:
        expanded_words.extend(expand_word_cases(w))

    digits = set("".join(numbers + dates))
    
    pool = set(expanded_words + numbers + dates + symbols + list(digits))
    
    if not pool:
        return

    for length in range(1, max_depth + 1):
        for combo in itertools.product(pool, repeat=length):
            result = "".join(combo)
            yield result

def main():
    print("=" * 60)
    print("       ULTIMATE BRUTE-FORCE COMBINATION GENERATOR V3")
    print("=" * 60)

    words = get_items("Enter words (e.g., adam):")
    numbers = get_items("Enter numbers (e.g., 2, 0, 20):")
    dates = get_items("Enter dates (e.g., 1995, 2026):")
    symbols = get_items("Enter symbols (e.g., @, #, !):")

    print("\n" + "-" * 60)
    print("Set maximum combination depth.")
    print("Note: Depth 3-4 covers most patterns like 'adamadam20' or '00adam'.")
    depth_input = input("Enter max depth [Default: 3]: ").strip()
    max_depth = int(depth_input) if depth_input.isdigit() else 3

    print("\n[+] Generating all absolute possibilities... Please wait.\n")

    count = 0
    with open("output.txt", "w", encoding="utf-8") as file:
        for result in generate_brute_force(words, numbers, dates, symbols, max_depth):
            file.write(result + "\n")
            count += 1
            if count % 200000 == 0:
                print(f"    Generated {count:,} combinations...")

    print("=" * 60)
    print(f"[SUCCESS] Total combinations generated: {count:,}")
    print("[SUCCESS] Saved to: output.txt")
    print("=" * 60)

if __name__ == "__main__":
    main()