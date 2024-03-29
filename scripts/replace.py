import json

with open('chars_to_replace.json', 'r') as read_file:
    replace_chars = json.load(read_file)

with open('chars_to_skip.json', 'r') as read_file:
    skip_chars = json.load(read_file)
    skip_chars = [char.upper() for char in skip_chars]

with open('chars_to_overwrite.json', 'r') as read_file:
    overwrite_chars = json.load(read_file)

with open('chars_to_replace_kana.json', 'r') as read_file:
    kana_chars = json.load(read_file)

count = 1

Glyphs.font.disableUpdateInterface()

# Replace chars based on chars_to_replace.json (basic)
for from_char, to_char in replace_chars.items():
    if from_char.upper() in skip_chars:
        Glyphs.font.glyphs[from_char].color = 1  # marked orange color
        continue
    if Glyphs.font.glyphs[from_char]:
        Glyphs.font.glyphs[from_char].layers[0].width = Glyphs.font.glyphs[to_char].layers[0].width
        Glyphs.font.glyphs[from_char].layers[0].shapes = Glyphs.font.glyphs[to_char].layers[0].shapes
        Glyphs.font.glyphs[from_char].color = 0  # marked red color
        print(f"{count}. {from_char} -> {to_char}")
        count += 1

# Replace chars based on chars_to_overwrite.json (overwrite if char is heteronyms, select the general one)
for from_char, to_char in overwrite_chars.items():
    if from_char.upper() in skip_chars:
        Glyphs.font.glyphs[from_char].color = 1  # marked orange color
        continue
    if Glyphs.font.glyphs[from_char]:
        Glyphs.font.glyphs[from_char].layers[0].width = Glyphs.font.glyphs[to_char].layers[0].width
        Glyphs.font.glyphs[from_char].layers[0].shapes = Glyphs.font.glyphs[to_char].layers[0].shapes
        Glyphs.font.glyphs[from_char].color = 2  # marked brown color
        print(f"*{count}. {from_char} -> {to_char}")
        count += 1

# Replace chars based on chars_to_replace_kana.json (include hirakana, katakana, and vert-kana)
for from_char, to_char in kana_chars.items():
    if from_char.upper() in skip_chars:
        Glyphs.font.glyphs[from_char].color = 1  # marked orange color
        continue
    if Glyphs.font.glyphs[from_char]:
        Glyphs.font.glyphs[from_char].layers[0].width = Glyphs.font.glyphs[to_char].layers[0].width
        Glyphs.font.glyphs[from_char].layers[0].shapes = Glyphs.font.glyphs[to_char].layers[0].shapes
        Glyphs.font.glyphs[from_char].color = 3  # marked yellow color
        print(f"^{count}. {from_char} -> {to_char}")
        count += 1

Glyphs.font.enableUpdateInterface()
