def charFrequency(sentence):
    # Inicializace slovníku pro ukládání frekvence znaků
    char_count = {}

    # Procházení řetězce a počítání frekvence znaků
    for char in sentence:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Seřazení slovníku podle frekvence sestupně
    sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

    return sorted_char_count


# Testování funkce
if __name__ == "__main__":
    sentence = "Šel za mnou jeden Řek, a ten mi řek, abych mu řek, kolik je v Řecku řeckých řek. A já mu řek, že nejsem řek, abych mu řek, kolik je v Řecku řeckých řek,"
    char_frequencies = charFrequency(sentence)

    print("Věta:", sentence)
    print("Četnost výskytu písmen:")
    print("-" * 23)
    for char, count in char_frequencies:
        print(f"('{char}', {count}),")
    print("-" * 23)
