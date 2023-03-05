# Huấn luyện mô hình ngôn ngữ trên máy trạm DGX 4 GPU A100 160G vram trong 7 ngày (04-10/03/2023)

## Chuẩn bị huấn luyện và các thử nghiệm
- [x] Chuẩn bị 6GB dữ liệu laws để thử nghiệm với mô hình 1.2 tỉ params

- [x] Quản lý [lấy mẫu huấn luyện](./sampling/README.md)
  - [x] Lấy mẫu theo chiều xuôi sao cho mỗi token đc train 1 lần với bigdata
  - [x] Thêm khoảng trượt data_shift để thay đổi cửa sổ lấy mẫu ở lần huấn luyện lặp lại tiếp theo

- [x] Tokenize dữ liệu và lưu dưới định dạng binidx theo kịch bản lấy mẫu
  - [x] Tknz theo symato_2944 (~5g filtered text = ~2 tỉ tokens)
  - [x] Tknz theo symato_16k  (~5g filtered text = ~1 tỉ tokens) 
    - Khả năng nén tương đương sentencepiece_16k (nhỉnh hơn 1 chút) và tập trung nén âm tiết
    - _!!! Lưu ý prompt đầu vào có thể làm tknz bi_grams khác trình tự so với lúc train làm giảm độ chính xác !!!_
  
- [x] Huấn luyện mô hình với dữ liệu laws:
  - [x] symato_2944 3 lượt:
    - [x] Lấy mẫu ngẫu nhiên
    - [x] Cách lấy mẫu mới đảm bảo mỗi token được huấn luyện 1 lần

  - [x] symato_16k 3 lượt:
      - [x] Mỗi mẫu huấn luyện 1 lần data_shift = 0
      - [x] Mỗi mẫu huấn luyện 1 lần data_shift = 170
      - [x] Mỗi mẫu huấn luyện 1 lần data_shift = 340

`>> I'M HERE <<`

  - [ ] sentencepiece_16k 3 lượt:
      - [ ] Mỗi mẫu huấn luyện 1 lần data_shift = 0
      - [ ] Mỗi mẫu huấn luyện 1 lần data_shift = 170
      - [ ] Mỗi mẫu huấn luyện 1 lần data_shift = 340

  - [ ] Huấn luyện một mô hình kết hợp cả 2 cách tknz => Thử nghiệm mới hoàn toàn!
    - Dùng symato_16k làm based, turn off fill-in-the-middle mode
    - [ ] Viết code trộn 2 loại dữ liệu tknz theo 2 cách khác nhau
    - [ ] Mỗi mẫu huấn luyện 1 lần data_shift = 0
    - [ ] Mỗi mẫu huấn luyện 1 lần data_shift = 170
    - [ ] Mỗi mẫu huấn luyện 1 lần data_shift = 340

## Huấn luyện mô hình 2.5 tỉ tham số trên ~13 tỉ tokens
- [x] Chuẩn bị dữ liệu huấn luyện với news, lọc theo chất lượng tokens và độ dài ngắn của văn bản
  - [x] Tknz dữ liệu với symato_16k
  - [x] Kịch bản huấn luyện mỗi token 2 rounds
  - [ ] `shortnews_000_079_symato_16k_text_document` train trước với cxt512 bs24
  - [ ] `news_030_137_symato_16k_text_document` train sau với cxt768 bs16
  - [x] Chuẩn bị dữ liệu tương tác
  - [+] Fine-tune với dữ liệu tương tác (~7GB) nếu còn thời gian (optional)
  - [+] Test perlexity với `truongnews-000-009` (làm sau)

```
TOTAL:
>>> documents 12734754
>>> tokens 13371714096

    news_010_029_laws_symato_16k_text_document
>>> documents 694327
>>> tokens 2117570773
>>> portion 0.1583619

    news_030_137_symato_16k_text_document
>>> documents 2867110
>>> tokens 5282778588
>>> portion 0.3950711

    shortnews_000_079_symato_16k_text_document
>>> documents 9173317
>>> tokens 5971364735
>>> portion 0.4465668
```

- - -

## Cần tìm thêm
- [ ] Văn bản chính quy
  - Đã có 6G văn bản luật từ Thịnh

- [ ] Tương tác đa chiều (lớn, đa dạng, giàu thông tin, dễ làm ứng dụng)
  - Bình luận trên các trang báo chí
  - Diễn đàn
  - Mạng xã hội
  - Public chat room
  - ...

- [ ] Sách
  - Chưa có nguồn


- - -


# Mấu chốt

- Làm thế nào để có metrics đánh giá "độ tốt" của văn bản?
  - Để có thể chọn văn bản từ tốt tới xấu cho đến một độ lớn nhất định thì dừng lại
  - Để khi huấn luyện chọn ra một tỉ lệ nhất định các văn bản tốt huấn luyện trước?

- Làm thế nào để lọc ra văn bản vừa "tốt" vừa "đa dạng" từ nhiều nguồn?
  - Cân bằng về số lượng tokens giữa các categories?


## Cần có hệ thống quản lý dữ liệu văn bản

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

## Công cụ mạnh để xử lý ngữ liệu lớn
- https://github.com/telexyz/engine phân tách âm tiết tiếng Việt và thống kê dữ liệu
- https://github.com/kpu/kenlm n-gram language model nhanh nhất, python binding
- https://github.com/facebookresearch/fastText word embedding & text classifier

RESEARCH

- [ ] Chọn dữ liệu tương đồng với 1 tập dữ liệu đã có
  - [ ] Dùng [dsir](https://github.com/p-lambda/dsir) để lọc news có liên quan tới pháp luật

- [ ] Loại bỏ dữ liệu kém
  - [x] lọc theo tỉ lệ âm tiết và độ dài văn bản
  - [x] Các thuật toán dedup
    - [x] minhash
    - [x] SuffixArray Substring
    - [ ] Áp dụng minhash, suffix-array vào âm tiết TV (sau khi đã đánh số = u16)
  - Tham khảo
    - https://github.com/CarperAI/pilev2/tree/main/pile/processing/dedup
    - https://github.com/CarperAI/squeakily
    - Check [quality of dataset using kenlm](https://github.com/huggingface/olm-datasets/blob/main/pipeline_scripts/common_crawl/apply_bigscience_filters.py)

- [ ] Cân bằng giữa các loại dữ liệu
  - [ ] Xem https://stanford-cs324.github.io/winter2022/lectures/data
  - [ ] Xem [unimax](./docs/unimax.md)

- [x] Chọn dữ liệu tốt để huấn luyện trước (cách lấy mẫu khôn ngoan)
  - [x] Cramming paper


- - -

DONE

- [x] Lọc [OSCAR vi](https://huggingface.co/datasets/oscar-corpus/OSCAR-2201/tree/main/compressed/vi_meta) (99GB, lọc từ cc)
  - Mỗi doc là 1 string của trường `content` trong file `.jsonl`
  - Vẫn còn nhiễu `... 10PHUT Combo 2 của sách 10PHUT Combo 3 của sách 10PHUTCombo của sách 1200 Combo 2 của sách 1200 Combo 3 ..`, cần train classifier ở để lọc quảng cáo hoặc lọc cảm tính theo tỉ lệ uniq syllables / độ dài doc
  - Còn code nhúng `ông Trịnh...\nAugust 3, 2017\n'); var formated_str = arr_splits[i].replace(/\\surl\\(\\'(?!data\\:)/gi, function regex_function(str)` lẫn trong nội dung doc
  - Còn những từ rất dài `KôngIcelandIndonesiaIranIraqIrelandIsraelJamaicaJerseyJordanKazakhstanKenyaKiribatiKuwaitKyrgyzstanLatviaLebanonLesothoLiberiaLibyaLiechtensteinLithuaniaLuxembourgLàoLãnh`
  - Đã lọc các docs quá ngắn < 800 tokens và các docs có hàm lượng tiếng Việt thấp
  - [Sample extracted text](https://huggingface.co/datasets/tiendung/vi500/blob/main/00112131415061718191.txt.7z)
  - [Sample pre-processing](https://huggingface.co/datasets/tiendung/vi500/blob/main/00112131415061718191.utf8.7z)

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
