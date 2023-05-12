# Escape Sequence	“Escaped” Interpretation
# \a	ASCII Bell (BEL) character
# \b	ASCII Backspace (BS) character
# \f	ASCII Formfeed (FF) character
# \n	ASCII Linefeed (LF) character
# \N{<name>}	Character from Unicode database with given <name>
# \r	ASCII Carriage Return (CR) character
# \t	ASCII Horizontal Tab (TAB) character
# \uxxxx	Unicode character with 16-bit hex value xxxx
# \Uxxxxxxxx	Unicode character with 32-bit hex value xxxxxxxx
# \v	ASCII Vertical Tab (VT) character
# \ooo	Character with octal value ooo
# \xhh	Character with hex value hh
# Examples:
print("Yes!!!!")
print("'\\t --> Horizontal <TAB> a character, a\\tb':  a\tb  = a    b")
print("'\\ooo --> Character with octal value ooo, a\\141\\142\\143': a\141\142\143  = aabc")
print("'\\xhh --> Character with hex value hh, a\\x61\\x62\\x63\\x64 ': a\x61\x62\x63\x64  = aabcd")
print("'\\n -->	ASCII Linefeed (LF) character a\\nb (and then in a new line 'b')': a\nb = a \nb")
print("'\\uxxxx	--> Unicode character with 16-bit hex value xxxx, \\u2192 ': \u2192  = -->")
print("'\\N{<name>} -->	Character from Unicode database with given <name>, \\N{rightwards arrow}'\
: \N{rightwards arrow} = --> ")
print("'\\a -->	ASCII Bell (BEL) character, \\a': \a ")
print("'\\b --> ASCII Backspace (BS) character, \\b': \b ")
print("'\\f -->	ASCII Formfeed (FF) character, \\f': \f ")
print("'\\r -->	ASCII Carriage Return (CR) character, \\r': aaa\r bbb")
print("'\\v -->	ASCII Vertical Tab (VT) character, aaa\\v bcd': aaa\v b\v c\v d\v \vz")


# Raw Strings:
# a raw string literal is preceded by 'r' or 'R', which specifies that the escap sequences in the \
# associated string are not translated. the backslash character is left in the string literal:
print("\\n new line 'foo\\nbar': displays foo and bar in two lines: foo\nbar")
print(r" r'xxx': do not translate the escape sequence started with \: foo\nbar ")
print("foo\\bar")
print(R"foo\\bar")
