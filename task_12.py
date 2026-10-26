text = input("Введите текст: ")
words = text.split()

print(f"Всего слов: {len(words)}")

counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

most_common = ""
max_count = 0
for word, count in counts.items():
    if count > max_count:
        max_count = count
        most_common = word

 
print(f"Самое частое слово: {most_common} ({max_count} раз)")

longest = max(words, key=len)
shortest = min(words, key=len)
print(f"Самое длинное: {longest}")
print(f"Самое короткое: {shortest}")

filtered = [w for w in words if len(w) >= 3]
print(f"\nВсего слов (без коротких): {len(filtered)}")
print(f"Самое длинное (без коротких): {max(filtered, key=len)}")