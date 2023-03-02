python3 preprocess_data.py \
            --input ../data/sample.jsonl \
            --output-prefix ../data/mydataset \
            --vocab ../qna/qna2.vocab \
            --dataset-impl mmap \
            --tokenizer-type SPMTokenizer \
            --append-eod