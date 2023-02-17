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

wget https://huggingface.co/datasets/oscar-corpus/OSCAR-2201/resolve/main/compressed/vi_meta/vi_meta_part_46.jsonl.gz
telexify vi_meta_part_46.txt vi_meta_part_46.utf8 utf8