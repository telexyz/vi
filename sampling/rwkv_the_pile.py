# https://github.com/BlinkDL/RWKV-LM/blob/main/RWKV-v4neo/src/dataset.py

# Dữ liệu vi100 dự kiến ~15b tokens, mô hình 1b5 params(L24 D2048)

def __init__():
    self.samples_per_epoch = args.epoch_steps * args.real_bsz
    assert self.samples_per_epoch == 40320
    rank_zero_info(f"########## Pile 20b-tokenized stage {args.my_pile_stage} ##########")
    dataset_slot = self.data_size // args.ctx_len
    assert MaybeIsPrime(args.magic_prime)
    assert args.magic_prime % 3 == 2
    assert args.magic_prime / dataset_slot > 0.99 and args.magic_prime / dataset_slot <= 1


def __getitem__(self, idx):

    args = self.args
    rank = self.global_rank # unique identifier assigned to each process in the distributed training job
    epoch = self.real_epoch #  the number of passes through the entire training dataset that have been completed during the training process
    world_size = self.world_size # the number of compute nodes or devices being used for training
    # print(f"epoch {epoch} idx {idx} rank {rank}/{world_size}")

    ctx_len = args.ctx_len
    req_len = ctx_len + 1
    magic_prime = args.magic_prime
    data = self.data

    if args.my_pile_stage > 0 and args.my_pile_stage != 4:
        ii = 1 + epoch * self.samples_per_epoch + (idx * world_size) + rank

        if args.my_qa_mask > 0:
            ii_orig = ii
            if ii % 2 == 0:
                ii = (ii // 2) * args.magic_prime
                if   args.ctx_len == 1024: magic_prime = 324331313
                elif args.ctx_len == 2048: magic_prime = 162165671
                elif args.ctx_len == 4096: magic_prime = 81082817
                data = self.data_pile
            else:
                ii = ii // 2

        factor = (math.sqrt(5) - 1) / 2
        factor = int(magic_prime * factor)
        i = ((factor * ii * ii * ii) % magic_prime) * ctx_len
        if (args.my_qa_mask == 0) or (data == self.data_pile):
            i = i + args.my_pile_shift
        # print(f"epoch {epoch} idx {idx} rank {rank}/{world_size} ii {ii} pos {round(i / self.data_size, 3)}")
    else:
        # cheat: pick a random spot in dataset
        i = np.random.randint(0, self.data_size - req_len)

    if args.data_type == "binidx":
        dix = data.get(idx=0, offset=i, length=req_len).astype(int)
