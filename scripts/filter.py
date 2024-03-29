import json
import csv


def char_to_unicode(char):
    return hex(ord(char))[2:]


def dict_to_csv(dictionary, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for key, values in dictionary.items():
            row = [key] + values
            writer.writerow(row)


with open('Dictionary_full.json', 'r') as read_file:
    data_dict = json.load(read_file)

with open('reference.json', 'r') as read_file:
    replace_chars_dict = json.load(read_file)

print(f'Length of Dictionary: {len(data_dict)}')

res = {}
check_table = {}

for char, char_details in data_dict.items():
    if char_details['pronunciation_mandarin_zhuyin']:
        zhuyin_list = char_details['pronunciation_mandarin_zhuyin']
        is_heteronyms = True if len(zhuyin_list) > 1 else False
        for zhuyin in zhuyin_list:
            for replace_char, candidates in replace_chars_dict.items():
                if zhuyin in candidates:
                    replace_char_hex = char_to_unicode(replace_char)
                    res[char_details['unicode_hex']] = replace_char_hex
                    check_table[char_details['text']] = [
                        replace_char, zhuyin, char_details['unicode_hex'], is_heteronyms
                    ]

print(f'Number of replaced character: {len(res)}')

with open('chars_to_replace.json', 'w') as file:
    json.dump(res, file)

dict_to_csv(check_table, 'check_table.csv')
