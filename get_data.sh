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

# https://huggingface.co/datasets/allenai/c4/resolve/main/multilingual/c4-vi.tfrecord-00001-of-??????.json.gz

wget https://huggingface.co/datasets/oscar-corpus/OSCAR-2201/resolve/main/compressed/vi_meta/vi_meta_part_45.jsonl.gz
tar vxfz vi_meta_part_45.jsonl.gz
sed -e 's|.*content\"\:\"\([^"]*\).*|\1|' vi_meta_part_45.jsonl > vi_meta_part_45.txt
telexify vi_meta_part_45.txt vi_meta_part_45.utf8 utf8
# Note: telexify được biên dịch từ https://github.com/telexyz/engine trên Ubuntu 64-bit