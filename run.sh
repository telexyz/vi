# git lfs install
# GIT_LFS_SKIP_SMUDGE=1
# git clone https://huggingface.co/datasets/allenai/c4
# cd c4
# git lfs pull --include "multilingual/c4-vi.*.json.gz"

# git lfs install
# GIT_LFS_SKIP_SMUDGE=1
# git clone https://huggingface.co/datasets/oscar-corpus/OSCAR-2201
# cd OSCAR-2201
# git lfs pull --include "compressed/vi_meta/*.jsonl.gz"

# sed -e 's|.*content\"\:\"\([^"]*\).*|\1|' vi_meta_part_46.jsonl > vi_meta_part_46.txt
# telexify vi_meta_part_46.txt vi_meta_part_46.utf8 utf8

# sed -e 's|.*content\"\:\"\([^"]*\).*|\1|' vi_meta_part_1.jsonl > vi_meta_part_1.txt
# sed -e 's|.*content\"\:\"\([^"]*\).*|\1|' vi_meta_part_12.jsonl > vi_meta_part_12.txt
# sed -e 's|.*content\"\:\"\([^"]*\).*|\1|' vi_meta_part_26.jsonl > vi_meta_part_26.txt
# sed -e 's|.*content\"\:\"\([^"]*\).*|\1|' vi_meta_part_35.jsonl > vi_meta_part_35.txt
# sed -e 's|.*content\"\:\"\([^"]*\).*|\1|' vi_meta_part_46.jsonl > vi_meta_part_46.txt
# sed -e 's|.*content\"\:\"\([^"]*\).*|\1|' vi_meta_part_51.jsonl > vi_meta_part_51.txt
# sed -e 's|.*content\"\:\"\([^"]*\).*|\1|' vi_meta_part_62.jsonl > vi_meta_part_62.txt
# sed -e 's|.*content\"\:\"\([^"]*\).*|\1|' vi_meta_part_79.jsonl > vi_meta_part_79.txt
# sed -e 's|.*content\"\:\"\([^"]*\).*|\1|' vi_meta_part_86.jsonl > vi_meta_part_86.txt
# sed -e 's|.*content\"\:\"\([^"]*\).*|\1|' vi_meta_part_99.jsonl > vi_meta_part_99.txt

# sed -e 's|.*content\"\:\"\([^"]*\).*|\1|' vi_meta_part_2.jsonl > vi_meta_part_2.txt
# sed -e 's|.*content\"\:\"\([^"]*\).*|\1|' vi_meta_part_10.jsonl > vi_meta_part_10.txt
# sed -e 's|.*content\"\:\"\([^"]*\).*|\1|' vi_meta_part_22.jsonl > vi_meta_part_22.txt
# sed -e 's|.*content\"\:\"\([^"]*\).*|\1|' vi_meta_part_32.jsonl > vi_meta_part_32.txt
# sed -e 's|.*content\"\:\"\([^"]*\).*|\1|' vi_meta_part_42.jsonl > vi_meta_part_42.txt
# sed -e 's|.*content\"\:\"\([^"]*\).*|\1|' vi_meta_part_52.jsonl > vi_meta_part_52.txt
# sed -e 's|.*content\"\:\"\([^"]*\).*|\1|' vi_meta_part_60.jsonl > vi_meta_part_60.txt
# sed -e 's|.*content\"\:\"\([^"]*\).*|\1|' vi_meta_part_72.jsonl > vi_meta_part_72.txt
# sed -e 's|.*content\"\:\"\([^"]*\).*|\1|' vi_meta_part_82.jsonl > vi_meta_part_82.txt
# sed -e 's|.*content\"\:\"\([^"]*\).*|\1|' vi_meta_part_92.jsonl > vi_meta_part_92.txt
# cat vi*.txt > 02102232425260728292.txt

./telexify 01122635465162798699.txt 01122635465162798699.utf8 utf8
./telexify 02102232425260728292.txt 02102232425260728292.utf8 utf8


# rm -rf data
# mkdir -p data
# touch data/00__TYPE_COUNT_______
# touch data/10__TYPE_LISTING_____
# touch data/30__ABNORMAL_________
# touch data/40___________________
# touch data/20__N-GRAMS__________
# telexify all.txt all.utf8 utf8 ngram