https://github.com/yuxdux/kinda-llama

__Important note__: in an attempt to enhance number representation, LLAMA authors split all numbers into individual digits. We likely would be better off doing this as well, otherwise models hardly learn mathematics. This could be implemented without changing the legacy 20B_tokenizer.json to keep compatibility with available checkpoints.

If our goal were to surpass the LLAMA dataset, we might think about creating these addons:
- A.1. Add more scientific papers - pubmed and scihub (pubmed was included in Pile-V1 though)
- A.2. Add more science and engineering literature from libgen, OCR-ed if necessary. Some of it doesn't need OCR and could be quickly included with a pipeline similar to 5. ("Books")
- A.3. Add DM-math from Pile-V1
- A.4. Add more code from github - code modeling seems to help LMs.
- A.5. Add more dialogue data
- A.6. Add tokens with reasoning chains like in Galactica (requires source of reasoning)
