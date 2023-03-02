python3 ../gpt-neox/preprocess_data.py \
            --input laws_txt.jsonl \
            --output-prefix laws \
            --dataset-impl mmap \
            --tokenizer-type SPMTokenizer \
            --vocab-file sp_txt_16384.model
