import random

rules = {
    "hello": ["there", "alex", "world"],
    "there": ["alex", "friend"],
    "alex": ["how", "is"],
    "how": ["are"],
    "are": ["you"],
    "you": ["today"]
}

text = input("Prompt: ").lower()
words = text.split()

for i in range(10):
    last = words[-1]

    if last in rules:
        next_word = random.choice(rules[last])
    else:
        next_word = random.choice(list(rules.keys()))

    words.append(next_word)
    print(" ".join(words))
