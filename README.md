# Chuẩn bị huấn luyện và các thử nghiệm

- [ ] Chuẩn bị 9G dữ liệu newslaws, 8G để train, 1G để test
  - Thử nghiệm với mô hình 300m params
  - Nên lọc các news liên quan tới laws để dữ liệu cùng một domain (dùng bi-gram)

- [ ] Tknz newslaws theo symato_2944

- [ ] Xây dựng bộ từ vựng symato_16k

- [ ] So sánh hiệu năng (khả năng nén) giữa symato_16k và sentencepiece_16k và sentencepiece_32k

- [ ] Huấn luyện 02 mô hình trên symato_16k và sentencepiece_32k và so sánh hiệu năng
  - Bộ từ vựng lớn hơn sẽ làm giảm số lượng tokens của tập dữ liệu nên cần ít computing hơn
  - Bộ dữ liệu nhỏ ngược lại, cần nhiều computing hơn để đạt tới cùng loss

- [ ] Lên kịch bản lấy mẫu và quản lý [lấy mẫu huấn luyện](./sampling/README.md)

- [ ] Tokenize dữ liệu và lưu dưới định dạng binidx theo kịch bản lấy mẫu

- [ ] Huấn luyện trên 02 GPUs

- [ ] Ước lượng thời gian huấn luyện khi chạy mô hình lớn


# Huấn luyện mô hình 1.5 tỉ tham số trên ~15 tỉ tokens
. . .

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
