morse_dict = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D",
    ".": "E", "..-.": "F", "--.": "G", "....": "H",
    "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
    "--": "M", "-.": "N", "---": "O", ".--.": "P",
    "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
    "-.--": "Y", "--..": "Z"
}# dictionary for storing morse code and alphabets and numbers

def morse_to_text(morse):
    words = morse.split(" / ") #this will split the para into words
    decoded_words = [] #empty string being created

    for word in words:
        letters = word.split()
        decoded_word = ""

        for letter in letters:
            decoded_word += morse_dict.get(letter, "?")

        decoded_words.append(decoded_word)

    return " ".join(decoded_words)


