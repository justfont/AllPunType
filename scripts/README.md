# Replace the characters

1. Run `filter.py` to generate the following tables by `reference.json`:
   - `chars_to_replace.json`
   - `check_table.txt`
2. Manually review and select the appropriate pronunciation:
   -  If a character has multiple pronunciations (a.k.a. heteronyms, *破音字*), we need to manually select the most commonly used pronunciation. There are two possible cases:
     1. The most common pronunciation is unrelated to the 12 zodiac animals, in which case it should be skipped during replacement. Generate `chars_to_skip.json` table.
        - `車` (`U+8ECA`) can be pronounced as `ㄔㄜ` and `ㄐㄩ` (similar to `雞`), with the former being more commonly used than the latter. The latter pronunciation is only used in Chinese chess.
        - `佛` (`U+4F5B`) can be pronounced as `ㄈㄛˊ` and `ㄈㄨˊ` (similar to `虎`), with the former being more commonly used than the latter. The latter pronunciation is only used in `仿佛` term.
        - `徵` (`U+5FB5`) can be pronounced as `ㄓㄥˊ` and `ㄓˇ` (similar to `豬`), with the former being more commonly used than the latter. The latter pronunciation is only used in the notation of Chinese Pentatonic Scale (*中國五聲音階*) with *宮、商、角、徵、羽*.
     2. The common pronunciation is related to another zodiac animals, in which case it should be overwritten during replacement. Generate `chars_to_overwrite.json` table.
        - `屬` (`U+5C6C`) can be pronounced as `ㄕㄨˇ` (similar to `鼠`) and `ㄓㄨˇ` (similar to `豬`), with the former being more commonly used than the latter.
        - `朱` (`U+6731`) can be pronounced as `ㄓㄨˊ` (similar to `豬`) and `ㄕˊ` (similar to `鼠`), with the former being more commonly used than the latter. The latter pronunciation is only used in `朱提` as an ancient Han commandery name near Yibin, Sichuan (*四川省宜賓縣*).
3. Consider the Kana (*仮名*) case, including Hirakana (*平仮名*), Katakana (*片仮名*), and glyphs with `.vert` suffix.
   - Generate `chars_to_replace_kana.json` tables.
4. Run `replace.py` in Glyphs.
5. Add `liga`, `calt`, `ss01`, `salt` features as necessary. 
6. Export the instance as the font.

---


# Necessary Features

## Ligature (liga)

```afdko
sub [N n] [E e] [W w] by uni725B;
sub [W w] [H h] [O o] by uni864E; 
sub [T t] [O o] [O o] by uni5154;
sub [T t] [O o] by uni5154;
sub [R r] [O o] [N n] [G g] by uni9F8D;
sub [L l] [O o] [N n] [G g] by uni9F8D;
sub [R r] [O o] [N n] by uni9F8D;
sub [L l] [O o] [N n] by uni9F8D;
sub [S s] [U u] [R r] by uni86C7;
sub [S s] [I i] [R r] by uni86C7;
sub [S s] [E e] [R r] by uni86C7;
sub [Y y] [O o] [U u] [N n] [G g] by uni7F8A;
sub [H h] [O o] by uni7334;
sub [G g] [O o] by uni72D7;
```

# Contextual Alternates (calt)

```afdko
sub uni8AE7 uni9748 uni9644' uni9AD4  by uni9644.ss01;
```

# Stylistic Alternates (salt) & Stylistic Set (ss01)

```afdko
sub uni9644 by uni9644.ss01;
```

