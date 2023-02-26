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
