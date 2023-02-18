- https://github.com/ChenghaoMou/text-dedup

# Deduplicating Training Data Makes Language Models Better
- https://arxiv.org/pdf/2107.06499.pdf
- https://github.com/google-research/deduplicate-text-datasets

## 4 Methods for Identifying Duplicates

Cách đơn giản nhất là exact string match, tuy nhiên chưa đủ. 2 cách nữa là:

- Đầu tiên dùng suffix array để loại bỏ duplicated substrings từ dataset nếu chúng xuất hiện nguyên văn trong nhiều hơn một mẫu.

- Tiếp theo dùng MinHash, rất hiệu quả để estimate n-gram simlilarity giữa 2 cặp mẫu trong corpus, để loại bỏ toàn bộ các mẫu từ dataset néu chúng có n-gram overlap cao với bất cứ mẫu nào khác.

Ta coi dataset D = `{x_i}_{i=1}^N` là một tập của các mẫu x_i. Và các mẫu đó là một chuỗi các tokens:
`x_i = [ x_i^1, x_i^2, ...m, s_i^{s_i} ]`

### 4.1 Exact Substring Duplication
