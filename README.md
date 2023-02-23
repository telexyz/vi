# Kịch bản tiền xử lý dữ liệu
> Cramming paper có nhiều ý tưởng tốt cho limited computing power. `bigscience-workshop` có pipeline tiền xử lý dữ liệu chỉnh chu nhất. 

- [ ] Tìm hiểu https://github.com/JonasGeiping/cramming/tree/main/cramming/data
- [ ] Tìm hiểu https://github.com/bigscience-workshop/data-preparation
- [ ] Tìm hiểu https://github.com/bigscience-workshop/data_tooling
![](https://raw.githubusercontent.com/bigscience-workshop/data-preparation/main/roots_pipeline.png)

# Phân tích tiếng Việt
- Dữ liệu lấy mẫu https://github.com/telexyz/data
- Kết quả phân tích https://github.com/telexyz/results

# Đề xuất cách tiền xử lý
![](docs/files/vi-pre-processing.png)

# Làm tốt dữ liệu
  - [ ] Loại bỏ dữ liệu kém
    - [ ] lọc theo tỉ lệ âm tiết, chất lượng âm tiết ...
    - [x] dedup
      - [x] minhash
      - [x] SuffixArray Substring
      - [ ] Áp dụng minhash, suffix-array vào âm tiết TV (sau khi đã đánh số = u16)
    - Tham khảo
      - https://github.com/CarperAI/pilev2/tree/main/pile/processing/dedup
      - https://github.com/CarperAI/squeakily

  - [ ] Cân bằng giữa các loại dữ liệu
    - [ ] Xem https://stanford-cs324.github.io/winter2022/lectures/data
    - [x] [dsir](https://github.com/p-lambda/dsir)
    - [ ] [unimax](./docs/unimax.md)

  - [ ] Chọn dữ liệu tốt để huấn luyện trước (cách lấy mẫu khôn ngoan)
    - [x] Cramming paper
    - [ ] Check [quality of dataset using kenlm](https://github.com/huggingface/olm-datasets/blob/main/pipeline_scripts/common_crawl/apply_bigscience_filters.py)

# Xây dựng tập dữ liệu đủ lớn

- [x] Sưu tầm "dữ liệu" đủ lớn, đủ đa dạng (ngoài tin tức, các dạng khác rất ít)
  - [x] Nguồn
    - Lọc từ https://github.com/CarperAI/pilev2 (chuẩn bị public)
    - Lọc từ https://github.com/EleutherAI/polyglot#polyglot-east-asian-wip (chuẩn bị public)
    - https://huggingface.co/datasets
    - https://www.kaggle.com/datasets

  - [x] cc-100 [vi](https://data.statmt.org/cc-100/vi.txt.xz) (166G, 1 file text, không phân chia theo văn bản)
  - [x] OSCAR [vi](https://huggingface.co/datasets/oscar-corpus/OSCAR-2201/tree/main/compressed/vi_meta) (99GB)
  - [x] C4 [vi](https://huggingface.co/datasets/allenai/c4/tree/main/multilingual) (310GB)
  - [ ] NLLB [vi](https://huggingface.co/datasets/allenai/nllb) (19G)

  - [x] Tin tức
    - [x] Cần phân loại theo categories (tin tức, khoa học, kiến thức, xã hội, luật pháp ...) và cân đối lại
    - https://huggingface.co/datasets/bigscience-data/roots_vi_binhvq_news_corpus (20GB)
    - https://huggingface.co/datasets/truongpdd/vietnews-dataset (34GB)

  - [x] Wikipedia (1GB nén)
    - https://dumps.wikimedia.org/viwiki (1GB nén, download trực tiếp)
    - https://huggingface.co/datasets/truongpdd/viwiki-dummy (240MB)
    - https://huggingface.co/datasets/bigscience-data/roots_vi_wikipedia (257MB)

  - [x] Truyện, thơ (1.1GB)
    - https://huggingface.co/datasets/truongpdd/vietnamese_story (480MB)
    - https://huggingface.co/datasets/truongpdd/vietnamese_poetry_story (538MB)
    - https://huggingface.co/datasets/bigscience-data/roots_vi_vietnamese_poetry (57MB)
    - https://huggingface.co/datasets/truongpdd/vietnamese_poetry (64MB)
    - https://huggingface.co/datasets/truongpdd/luc-bat (33MB)

  - [ ] Sách
    - ...

  - [ ] Văn bản chính quy
    - Đang crawl ước tính từ khoảng 20G

  - [ ] Khác?
    - Diễn đàn
    - Mạng xã hội
    - Public chat room
    - ...
