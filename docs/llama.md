https://github.com/facebookresearch/llama

https://twitter.com/GuillaumeLample/status/1629151231800115202

LLaMA-13B outperforms OPT and GPT-3 175B on most benchmarks. LLaMA-65B is competitive with Chinchilla 70B and PaLM 540B.

The weights for all models are open and available at https://research.facebook.com/publications/llama-open-and-efficient-foundation-language-models/

All our models were __trained on at least 1T tokens, much more than what is typically used at this scale__.
Interestingly, even after 1T tokens the 7B model was still improving.

| ![](https://pbs.twimg.com/media/FpvTXeJXwAAGmDU?format=png) | ![](https://pbs.twimg.com/media/FpvTcVtWYAEx6CD?format=png) |
|---|---|

- - -

Unlike Chinchilla, PaLM, or GPT-3, we only use datasets publicly available, making our work compatible with open-sourcing and reproducible, while most existing models rely on data which is either not publicly available or undocumented.
![](https://pbs.twimg.com/media/FpvTkckWYAAroWL?format=png)

__English CommonCrawl [67%]__. We preprocess five CommonCrawl dumps, ranging from 2017 to 2020.
- __deduplicates the data at the line level__ (vì cc lưu data at line level)
- performs language identification with a fastText linear classifier to remove non-English pages and 
- filters low quality content with an n-gram language model (question [here](https://github.com/facebookresearch/llama/issues/7))
- trained a linear model to classify pages used as references in Wikipedia v.s. randomly sampled pages, 
  and discarded pages not classified as references.

__C4 [15%]__. During exploratory experiments, we observed that using diverse pre-processed CommonCrawl datasets improves performance. We thus included the publicly available C4 dataset in our data. 
- The main difference with CCNet is the quality filtering, which mostly relies on __heuristics such as presence of punctuation marks or the number of words and sentences in a webpage__.

- - -

## Tokenizer
We tokenize the data with the bytepair encoding (BPE) algorithm, using the implementation from SentencePiece.
Notably, we __split all numbers into individual digits__, and fallback to bytes to decompose unknown UTF-8 characters.

## Mỗi token được train 1 lần ngoại trừ wikipedia
Overall, our entire training dataset contains roughly __1.4T tokens__ after tokenization. For most of
our training data, __each token is used only once during training__, with the exception of the Wikipedia
and Books domains, over which we perform approximately two epochs.

