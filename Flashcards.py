import random
import os

FILE = "cards.txt"

def load_cards():
    if not os.path.exists(FILE):
        print("cards.txt not found. Create it with 'question | answer' per line.")
        return []
    
    cards = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            if "|" in line:
                q, a = line.strip().split("|", 1)
                cards.append((q.strip(), a.strip()))
    return cards

def quiz(cards):
    random.shuffle(cards)
    score = 0
    
    for i, (q, a) in enumerate(cards, 1):
        print(f"\nQ{i}: {q}")
        user = input("Your answer: ").strip()
        
        if user.lower() == a.lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Correct answer: {a}")
    
    print(f"\nFinal Score: {score}/{len(cards)}")

def main():
    cards = load_cards()
    if cards:
        quiz(cards)

if __name__ == "__main__":
    main()
