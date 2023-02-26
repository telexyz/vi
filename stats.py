def scan_docs(filename, maxx=None):
    texts = open(filename).read().split("\n")[:-1]
    max_len = 0;  min_len = 99999999;  total = 0
    max_para = 0; min_para = 99999999; total_para = 0
    max_tk = 0;   min_tk = 99999999;   total_tk = 0

    if maxx is None: maxx = len(texts)
    for i in range(maxx):
        text = texts[i]
        n = len(text)
        # if n < 10: print(text);
        if n > max_len: max_len = n
        if n < min_len: min_len = n
        total += n

        para_n = text.count('\\n') + 1
        if para_n > max_para: max_para = para_n
        if para_n < min_para: min_para = para_n
        total_para += para_n
        
        # if 3379 == max_para: print(text); assert False

        tk_n = text.count(' ') + para_n
        if tk_n > max_tk: max_tk = tk_n
        if tk_n < min_tk: min_tk = tk_n
        total_tk += tk_n
    print(f"""\n>>>Found {maxx} documents in {filename}:
Characters: max {max_len}, min {min_len}, avg {total // maxx}.
Est Tokens: max {max_tk}, min {min_tk}, avg {total_tk // maxx}.
Paragraphs: max {max_para}, min {min_para}, avg {total_para // maxx}.
""")

prefixs = [
    # "vi_meta_part_1",
    "all"
]

for prefix in prefixs:
    scan_docs(f"{prefix}.utf8")
