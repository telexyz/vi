# Mấu chốt

- Làm thế nào để có metrics đánh giá "độ tốt" của văn bản?
  - Để có thể chọn văn bản từ tốt tới xấu cho đến một độ lớn nhất định thì dừng lại
  - Để khi huấn luyện chọn ra một tỉ lệ nhất định các văn bản tốt huấn luyện trước?

- Làm thế nào để lọc ra văn bản vừa "tốt" vừa "đa dạng" từ nhiều nguồn?
  - Cân bằng về số lượng tokens giữa các categories?

- - -

TODOs

- [x] Chọn [OSCAR vi](https://huggingface.co/datasets/oscar-corpus/OSCAR-2201/tree/main/compressed/vi_meta) (99GB, lọc từ cc) làm thử nghiệm với, cần scan qua để xem thể loại nội dung
  - Mỗi doc là 1 string của trường `content` trong file `.jsonl`
  - Vẫn còn nhiễu `... 10PHUT Combo 2 của sách 10PHUT Combo 3 của sách 10PHUTCombo của sách 1200 Combo 2 của sách 1200 Combo 3 ..`, cần train classifier ở để lọc quảng cáo hoặc lọc cảm tính theo tỉ lệ uniq syllables / độ dài doc
  - Còn code nhúng `ông Trịnh...\nAugust 3, 2017\n'); var formated_str = arr_splits[i].replace(/\\surl\\(\\'(?!data\\:)/gi, function regex_function(str)` lẫn trong nội dung doc
  - Còn những từ rất dài `KôngIcelandIndonesiaIranIraqIrelandIsraelJamaicaJerseyJordanKazakhstanKenyaKiribatiKuwaitKyrgyzstanLatviaLebanonLesothoLiberiaLibyaLiechtensteinLithuaniaLuxembourgLàoLãnh`
  - Lỗi chính tả, dính từ ...

- [ ] Thống kê dữ liệu OSCAR vi, bao nhiêu docs, thể loại, độ dài ngắn, số lượng âm tiết / doc, độ phủ tiếng Việt ...

- [ ] Lọc một phần dữ liệu để train tokenizer. Note: Với kiểu dữ liệu khác nhau có thể cần cách tokenizer khác nhau cho phù hợp.

- [ ] Build symato+ tokenizer, so sánh hiệu năng (khả năng nén) của symato+ vs sentencepiece vs wordpiece

- [ ] Chọn tokenizer phù hợp nhất

- [ ] Tokenize dữ liệu và lưu dưới định dạng binidx

- [ ] Thử huấn luyện trước mô hình 200m params trong lúc chờ phần cứng tốt hơn


- - -


RESEARCH

- [ ] Tìm hiểu https://oscar-project.org, datasets và pipeline của họ rất tốt !!!

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
> Cramming paper có nhiều ý tưởng tốt cho limited computing power. `bigscience-workshop` có pipeline tiền xử lý dữ liệu chỉnh chu nhất.

- https://github.com/JonasGeiping/cramming/tree/main/cramming/data
- https://github.com/bigscience-workshop/data-preparation
- https://github.com/bigscience-workshop/data_tooling
![](https://raw.githubusercontent.com/bigscience-workshop/data-preparation/main/roots_pipeline.png)

# Công cụ mạnh để xử lý ngữ liệu lớn
- https://github.com/telexyz/engine phân tách âm tiết tiếng Việt và thống kê dữ liệu
- https://github.com/kpu/kenlm n-gram language model nhanh nhất, python binding
- https://github.com/facebookresearch/fastText word embedding & text classifier

# Phân tích tiếng Việt
- Dữ liệu lấy mẫu https://github.com/telexyz/data
- Kết quả phân tích https://github.com/telexyz/results

# 500GB ngữ liệu tiếng Việt

- [x] OSCAR [vi](https://huggingface.co/datasets/oscar-corpus/OSCAR-2201/tree/main/compressed/vi_meta) (99GB, lọc từ cc)

- [x] Văn bản pháp luật https://huggingface.co/datasets/th1nhng0/vietnamese_legal_corpus (6G raw text)

- [x] Wikipedia
  - https://dumps.wikimedia.org/viwiki (1GB nén, raw, download trực tiếp)
  - https://huggingface.co/datasets/truongpdd/viwiki-dummy (240MB, cần kiểm tra chất lượng)
  - https://huggingface.co/datasets/bigscience-data/roots_vi_wikipedia (257MB, có thể bị cắt nhỏ, cần kiểm tra)

- [ ] Sách
  - Chưa có nguồn

- [ ] Văn bản chính quy
  - Mới được 6G văn bản luật, cần crawl thêm ...

- [ ] Khác (cần crawl thêm nguồn dữ liệu lớn và đa dạng này)
  - Diễn đàn
  - Mạng xã hội
  - Public chat room
  - ...


- - -


- [x] C4 [vi](https://huggingface.co/datasets/allenai/c4/tree/main/multilingual) (310GB, lọc từ cc)
  - Vì cùng lọc từ cc nên dùng OSCAR rồi thì thôi C4?

- [x] NLLB [vi](https://huggingface.co/datasets/allenai/nllb) (19G, dịch giữa các ngôn ngữ)
  - Có thể trùng với OSCAR và C4 => thôi?

- [x] Tin tức https://huggingface.co/datasets/truongpdd/vietnews-dataset (34GB đã lọc (theo tác giả))
  - OSCAR đã bao gồm cả news nên có thể bỏ quan news datasets khác 
  - Nên phân rã và cân đối theo categories (tin tức, khoa học, kiến thức, xã hội, luật pháp ...) và cân đối lại
  - Có thể dùng dsir để lọc theo định hướng

  - [x] cc-100 [vi](https://data.statmt.org/cc-100/vi.txt.xz) (166G, 1 file text, xxxx-2020, mỗi doc là 1 line?)
    - Bỏ qua vì chưa đọc lọc. Dùng OSCAR.

  - [x] Truyện, thơ (1.1GB chưa nén, thơ OK + lowercases, truyện bị lẫn news)
    - Không nhiều, có thể bỏ qua
    - https://huggingface.co/datasets/truongpdd/vietnamese_story (480MB)
    - https://huggingface.co/datasets/truongpdd/vietnamese_poetry_story (538MB)
    - https://huggingface.co/datasets/bigscience-data/roots_vi_vietnamese_poetry (57MB)
    - https://huggingface.co/datasets/truongpdd/vietnamese_poetry (64MB)
    - https://huggingface.co/datasets/truongpdd/luc-bat (33MB)

- [x] Sưu tầm "dữ liệu" đủ lớn, đủ đa dạng (ngoài tin tức, các dạng khác rất ít)
  - [x] Nguồn
    - Lọc từ https://github.com/CarperAI/pilev2 (chuẩn bị public)
    - Lọc từ https://github.com/EleutherAI/polyglot#polyglot-east-asian-wip (chuẩn bị public)
    - https://huggingface.co/datasets
    - https://www.kaggle.com/datasets


- - -


![](docs/files/vi-pre-processing.png)
