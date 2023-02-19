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
    - [ ] Tìm hiểu [pile2 dedup](https://github.com/CarperAI/pilev2/tree/main/pile/processing/dedup)
    - [ ] Tìm hiểu [CarperAI data filter](https://github.com/CarperAI/squeakily)
    - [ ] Tìm hiểu https://github.com/bigscience-workshop/data-preparation

  - [ ] Cân bằng giữa các loại dữ liệu
    - [ ] [dsir](https://github.com/p-lambda/dsir)
    - [ ] [unimax](./docs/unimax.md)


# Xây dựng tập dữ liệu đủ lớn

- [ ] Sưu tầm "dữ liệu" đủ lớn, đủ đa dạng (ngoài tin tức, các dạng khác rất ít)
  - [x] Nguồn
    - Lọc từ https://github.com/CarperAI/pilev2?
    - https://huggingface.co/datasets
    - https://www.kaggle.com/datasets

  - [x] cc-100 [vi](https://data.statmt.org/cc-100/vi.txt.xz) (166G, 1 file text, không phân chia theo văn bản)
  - [x] OSCAR [vi](https://huggingface.co/datasets/oscar-corpus/OSCAR-2201/tree/main/compressed/vi_meta) (99GB)
  - [x] C4 [vi](https://huggingface.co/datasets/allenai/c4/tree/main/multilingual) (310GB)
  - [ ] NLLB [vi](https://huggingface.co/datasets/allenai/nllb) (19G)

  - [ ] Tin tức (quá dư)
    - [ ] Cần phân loại theo categories (tin tức, khoa học, kiến thức, xã hội, luật pháp ...) và cân đối lại
    - https://huggingface.co/datasets/bigscience-data/roots_vi_binhvq_news_corpus (20GB)
    - https://huggingface.co/datasets/truongpdd/vietnews-datase (34GB)
    - https://www.kaggle.com/datasets/nekonekonyan/vietnamesenewspapers (70GB gồm cả ảnh)

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
    - ...

  - [ ] Khác?
    - Diễn đàn
    - Mạng xã hội
    - Public chat room
    - ...

