# Своя функция zip
def get_zip(seq1, seq2):
    return [(seq1[i], seq2[i]) for i in range(min(len(seq1), len(seq2)))]

string = 'abcd'
tpl = (10, 20, 30, 40)

zipped = get_zip(string, tpl)
print(zipped)
print("\n".join(str(i) for i in get_zip(string, tpl)))