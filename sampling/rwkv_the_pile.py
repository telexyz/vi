# https://github.com/BlinkDL/RWKV-LM/blob/main/RWKV-v4neo/train.py
if args.my_pile_stage > 0:
    magic_prime_bak = args.magic_prime

    if args.ctx_len == 1024:
        args.magic_prime = 324331313
        args.epoch_count = 8043
 
    elif args.ctx_len == 2048:
        args.magic_prime = 162165671
        args.epoch_count = 4021
 
    elif args.ctx_len == 4096:
        args.magic_prime = 81082817
        args.epoch_count = 2010

    if args.my_pile_shift < 0:
        if   args.ctx_len == 1024: args.my_pile_shift = 0
        elif args.ctx_len == 2048: args.my_pile_shift = 512
        elif args.ctx_len == 4096: args.my_pile_shift = 768

    if magic_prime_bak > 0:
        args.magic_prime = magic_prime_bak

    args.epoch_steps = 40320 // args.real_bsz
    assert args.epoch_steps * args.real_bsz == 40320

    if args.my_pile_stage == 2: # Fine-tune
        assert args.lr_final == args.lr_init


# https://github.com/BlinkDL/RWKV-LM/blob/main/RWKV-v4neo/src/dataset.py
# Dữ liệu vi100 dự kiến ~15b tokens, mô hình 1b5 params(L24 D2048)

def __init__():
    self.samples_per_epoch = args.epoch_steps * args.real_bsz
    assert self.samples_per_epoch == 40320
    rank_zero_info(f"########## Pile 20b-tokenized stage {args.my_pile_stage} ##########")
    self.data_size = len(self.data._bin_buffer) // 2
    dataset_slot = self.data_size // args.ctx_len
    assert MaybeIsPrime(args.magic_prime)
    assert args.magic_prime % 3 == 2
    assert args.magic_prime / dataset_slot > 0.99 and args.magic_prime / dataset_slot <= 1


def __getitem__(self, idx):
    args = self.args
    rank = self.global_rank # unique identifier assigned to each process in the distributed training job
    epoch = self.real_epoch
    world_size = self.world_size # the number of compute nodes or devices being used for training
    # print(f"epoch {epoch} idx {idx} rank {rank}/{world_size}")

    ctx_len = args.ctx_len
    req_len = ctx_len + 1
    magic_prime = args.magic_prime
    data = self.data

    # if args.my_pile_stage > 0 and args.my_pile_stage != 4:
    ii = 1 + epoch * self.samples_per_epoch + (idx * world_size) + rank

    factor = (math.sqrt(5) - 1) / 2
    factor = int(magic_prime * factor)
    i = ((factor * ii * ii * ii) % magic_prime) * ctx_len
    i = i + args.my_pile_shift
    # print(f"epoch {epoch} idx {idx} rank {rank}/{world_size} ii {ii} pos {round(i / self.data_size, 3)}")
    dix = data.get(idx=0, offset=i, length=req_len).astype(int)
