# Mấu chốt

- Làm thế nào để có metrics đánh giá "độ tốt" của văn bản?
  - Để có thể chọn văn bản từ tốt tới xấu cho đến một độ lớn nhất định thì dừng lại
  - Để khi huấn luyện chọn ra một tỉ lệ nhất định các văn bản tốt huấn luyện trước?

- Làm thế nào để lọc ra văn bản vừa "tốt" vừa "đa dạng" từ nhiều nguồn?
  - Cân bằng về số lượng tokens giữa các categories?

- - -

# Cần có hệ thống quản lý dữ liệu văn bản

- Crawl dữ liệu nên đi theo từng website và có bộ parser riêng cho web đó để lọc nội dung chuẩn ngay từ đầu, tránh bị lẫn sạn. Có APIs để cung cấp json/xml cho apps càng tốt.

- Crawl dữ liệu như bot của search engine, quản lý văn bản như quản lý search engine quản lý cơ sở dữ liệu

- Các bài toán quản trị meta data của văn bản:
  - Đánh số thứ tự (id)
  - Độ dài văn bản (theo chars, tokens, paragraphs ...)
  - Full text search indexing
  - n-gram indexing (2,3-gram)
  - MinHash (để dedup)
  - Lưu nguồn văn bản (url)
  - Lĩnh vực (domains) và phân loại (categories)
  - Thời gian cập nhật

- Các truy vấn trên CSDL văn bản:
  - Tìm cho tôi 1000 văn bản có độ dài ngắn nhất
  - Tìm cho tôi các văn bản có chủ đề "văn hóa"
  - Thống kê số lượng văn bản theo từng chủ đề


- - -

TODOs

- [x] Lọc [OSCAR vi](https://huggingface.co/datasets/oscar-corpus/OSCAR-2201/tree/main/compressed/vi_meta) (99GB, lọc từ cc)
  - Mỗi doc là 1 string của trường `content` trong file `.jsonl`
  - Vẫn còn nhiễu `... 10PHUT Combo 2 của sách 10PHUT Combo 3 của sách 10PHUTCombo của sách 1200 Combo 2 của sách 1200 Combo 3 ..`, cần train classifier ở để lọc quảng cáo hoặc lọc cảm tính theo tỉ lệ uniq syllables / độ dài doc
  - Còn code nhúng `ông Trịnh...\nAugust 3, 2017\n'); var formated_str = arr_splits[i].replace(/\\surl\\(\\'(?!data\\:)/gi, function regex_function(str)` lẫn trong nội dung doc
  - Còn những từ rất dài `KôngIcelandIndonesiaIranIraqIrelandIsraelJamaicaJerseyJordanKazakhstanKenyaKiribatiKuwaitKyrgyzstanLatviaLebanonLesothoLiberiaLibyaLiechtensteinLithuaniaLuxembourgLàoLãnh`
  - Đã lọc các docs quá ngắn < 800 tokens và các docs có hàm lượng tiếng Việt thấp
  - Sample extracted text https://huggingface.co/datasets/tiendung/vi500/blob/main/00112131415061718191.txt.7z
  - Sample pre-processing https://huggingface.co/datasets/tiendung/vi500/blob/main/00112131415061718191.utf8.7z

- [x] Thống kê dữ liệu OSCAR vi, bao nhiêu docs, thể loại, độ dài ngắn, số lượng âm tiết / doc, độ phủ tiếng Việt ...
  - Lấy mẫu 1/10 dữ liệu, lọc ra được khoảng 5G text, và thống kê:
    - Found 956_751 documents,
    - Characters: max 6_160_173, min 1, avg 4475.
    - Est Tokens: max 153_393, min 1, avg 946.
    - Paragraphs: max 5370, min 1, avg 42.
  - Xem thống kê chi tiết trên 10GB [tại đây](https://github.com/telexyz/vi/tree/main/symato/oscar-vi-10gb-stats)

- [x] Văn bản pháp luật https://huggingface.co/datasets/th1nhng0/vietnamese_legal_corpus (6G raw text)
  - https://huggingface.co/datasets/tiendung/vi500/blob/main/thinh-laws.utf8.7z

- [x] Wikipedia
  - https://huggingface.co/datasets/bigscience-data/roots_vi_wikipedia (257MB)
    - Found 129_608 documents in roots-wikipedia-vi.parquet:
      - Characters: max 202_906, min 196, avg 2873.
      - Est Tokens: max 45855, min 22, avg 622.
      - Paragraphs: max 801, min 3, avg 16.
  - https://huggingface.co/datasets/tiendung/vi500/blob/main/roots-wikipedia-vi.utf8.7z


- [x] Tin tức https://huggingface.co/datasets/truongpdd/vietnews-dataset (~70GB đã dedup)


- [ ] Các dữ liệu sắp xuất bản
  - Lọc `vi` từ https://github.com/CarperAI/pilev2 (chuẩn bị public)
  - Lọc `vi` từ https://github.com/EleutherAI/polyglot#polyglot-east-asian-wip (chuẩn bị public)


- - -

__Tokenization và chuẩn bị huấn luyện__

- [x] Lọc một phần dữ liệu để train tokenizer

- [ ] Hợp nhất 1-gram, 2-gram từ `lawpedia-5gb` và `oscar-vi-5gb`

- [ ] Chọn top `04-alphmark_freqs`, `05-alph0m0t_freqs` từ `lawpedia-5gb` và `oscar-vi-10gb`

- [ ] Build symato based trên lowercase syllables, so sánh hiệu năng (khả năng nén) với sentencepiece

- [ ] Tokenize dữ liệu và lưu dưới định dạng binidx


- - -

RESEARCH

- [ ] Chọn dữ liệu tương đồng với 1 tập dữ liệu đã có
  - [ ] Dùng [dsir](https://github.com/p-lambda/dsir) để lọc news có liên quan tới pháp luật

- [ ] Loại bỏ dữ liệu kém
  - [ ] lọc theo tỉ lệ âm tiết, chất lượng âm tiết ...
    - Điều chỉnh code của `engine`
  - [x] Các thuật toán dedup
    - [x] minhash
    - [x] SuffixArray Substring
    - [ ] Áp dụng minhash, suffix-array vào âm tiết TV (sau khi đã đánh số = u16)
  - Tham khảo
    - https://github.com/CarperAI/pilev2/tree/main/pile/processing/dedup
    - https://github.com/CarperAI/squeakily

- [ ] Cân bằng giữa các loại dữ liệu
  - [ ] Xem https://stanford-cs324.github.io/winter2022/lectures/data
  - [ ] Xem [unimax](./docs/unimax.md)

- [ ] Chọn dữ liệu tốt để huấn luyện trước (cách lấy mẫu khôn ngoan)
  - [ ] Cramming paper
  - [ ] Check [quality of dataset using kenlm](https://github.com/huggingface/olm-datasets/blob/main/pipeline_scripts/common_crawl/apply_bigscience_filters.py)

- - -

# Kịch bản tiền xử lý dữ liệu
> Cramming paper có nhiều ý tưởng tốt cho limited computing power.

- https://github.com/JonasGeiping/cramming/tree/main/cramming/data
- https://github.com/bigscience-workshop/data-preparation
- https://github.com/bigscience-workshop/data_tooling
![](https://raw.githubusercontent.com/bigscience-workshop/data-preparation/main/roots_pipeline.png)

# Công cụ mạnh để xử lý ngữ liệu lớn
- https://github.com/telexyz/engine phân tách âm tiết tiếng Việt và thống kê dữ liệu
- https://github.com/kpu/kenlm n-gram language model nhanh nhất, python binding
- https://github.com/facebookresearch/fastText word embedding & text classifier

# Cần cào thêm
- [ ] Sách
  - Chưa có nguồn

- [ ] Văn bản chính quy
  - Mới được 6G văn bản luật, cần crawl thêm ...

- [ ] Khác (cần crawl thêm nguồn dữ liệu lớn và đa dạng này)
  - Bình luận trên các trang báo chí
  - Diễn đàn
  - Mạng xã hội
  - Public chat room
  - ...

- - -

- [x] cc-100 [vi](https://data.statmt.org/cc-100/vi.txt.xz) (166G, 1 file text, xxxx-2020, mỗi doc là 1 line?)
  - Bỏ qua vì chưa được lọc. Dùng OSCAR.

- [x] Truyện, thơ (1.1GB chưa nén, thơ OK + lowercases, truyện bị lẫn news)
  - Không nhiều, thơ thì ngắn, truyện không đặc sắc, có thể bỏ qua
  - https://huggingface.co/datasets/truongpdd/vietnamese_story (480MB)
  - https://huggingface.co/datasets/truongpdd/vietnamese_poetry_story (538MB)
  - https://huggingface.co/datasets/bigscience-data/roots_vi_vietnamese_poetry (57MB)
  - https://huggingface.co/datasets/truongpdd/vietnamese_poetry (64MB)
  - https://huggingface.co/datasets/truongpdd/luc-bat (33MB)
