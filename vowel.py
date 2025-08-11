from collections import Counter
text = input("Enter a paragraph: ").lower()

for ch in [",", ".", "!", "?", ";", ":"]:
    text = text.replace(ch, "")

words = text.split()

total_words = len(words)

word_freq = Counter(words)

top_3 = word_freq.most_common(3)

vowels = "aeiou"
vowel_count = sum(1 for ch in text if ch in vowels)

print("\nTotal number of words:", total_words)
print("\nFrequency of each word:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")

print("\nTop 3 most frequent words:")
for word, freq in top_3:
    print(f"{word}: {freq}")

print("\nTotal number of vowels:", vowel_count)