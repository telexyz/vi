https://twitter.com/GuillaumeLample/status/1629151231800115202

LLaMA-13B outperforms OPT and GPT-3 175B on most benchmarks. LLaMA-65B is competitive with Chinchilla 70B and PaLM 540B.

The weights for all models are open and available at https://research.facebook.com/publications/llama-open-and-efficient-foundation-language-models/

All our models were __trained on at least 1T tokens, much more than what is typically used at this scale__.
Interestingly, even after 1T tokens the 7B model was still improving.

| ![](https://pbs.twimg.com/media/FpvTXeJXwAAGmDU?format=png) | ![](https://pbs.twimg.com/media/FpvTcVtWYAEx6CD?format=png) |
|---|---|

Unlike Chinchilla, PaLM, or GPT-3, we only use datasets publicly available, making our work compatible with open-sourcing and reproducible, while most existing models rely on data which is either not publicly available or undocumented.
![](https://pbs.twimg.com/media/FpvTkckWYAAroWL?format=png)

