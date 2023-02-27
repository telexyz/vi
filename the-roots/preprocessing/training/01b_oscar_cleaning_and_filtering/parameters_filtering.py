import string
import emoji  # Use version emoji==1.6.1, otherwise it won't have UNICODE_EMOJI


main_special_characters = string.punctuation + string.digits + string.whitespace
other_special_characters = (
    "    　    ￼’“”–ー一▬…✦�­£​•€«»°·═"
    "×士＾˘⇓↓↑←→（）§″′´¿−±∈﻿¢ø‚„½¼¾¹²³―⁃，ˌ¸‹›ʺˈʻ¦‐⠀‰‑≤≥‖"
    "◆●■►▼▲▴∆▻¡★☆✱ːº。¯˜¥ɪ≈†上ン：∼⁄・♡✓⊕․．⋅÷１‟；،、¨ाাी्े◦˚"
    "゜ʼ≖ʼ¤ッツシ℃√！【】‿∞➤～πه۩☛₨➩☻๑٪♥ıॽ《‘©﴿٬？▷Г♫∟™ª₪®「—❖"
    "」﴾》"
)
emoji = list(emoji.UNICODE_EMOJI["en"].keys())

special_characters_default = set(main_special_characters + other_special_characters)
special_characters_default.update(emoji)


parameters_filtering_default = {
    "cond_uniform_whitespace": True,
    "cond_replace_unicode_punctuation": False,
    "cond_remove_words_with_incorrect_substrings": False,
    "incorrect_word_substrings": ["http", "www", ".com", "href", "//"],
    "cond_remove_long_words": False,
    "length_word_max_cutoff": 50,
    "cond_check_number_words": True,
    "tokenization": False,
    "strip_characters": special_characters_default,
    "number_words_min_cutoff": 10,
    "number_words_max_cutoff": 100000,
    "cond_check_character_repetition_removal": True,
    "character_repetition_length": 10,
    "character_repetition_max_cutoff": 0.2,
    "cond_check_word_repetition_removal": True,
    "word_repetition_length": 5,
    "word_repetition_max_cutoff": 0.3,
    "cond_check_special_characters": True,
    "special_characters": special_characters_default,
    "special_characters_max_cutoff": 0.4,
    "cond_words_augmentation": False,
    "words_augmentation_group_sizes": [],
    "words_augmentation_join_char": "",
    "cond_check_stopwords": True,
    "stopwords_min_cutoff": 0.1,
    "cond_check_flagged_words": True,
    "flagged_words_max_cutoff": 0.1,
    "cond_check_lang_id": True,
    "lang_id_min_cutoff": 0.70,
    "cond_check_perplexity": True,
    "perplexity_max_cutoff": 10000,
}

parameters_filtering_ar = {
    "cond_uniform_whitespace": True,
    "cond_replace_unicode_punctuation": False,
    "cond_remove_words_with_incorrect_substrings": True,
    "incorrect_word_substrings": ["http", "www", ".com", "href", "//"],
    "cond_remove_long_words": True,
    "length_word_max_cutoff": 25,
    "cond_check_number_words": True,
    "tokenization": False,
    "strip_characters": special_characters_default,
    "number_words_min_cutoff": 20,
    "number_words_max_cutoff": 100000,
    "cond_check_character_repetition_removal": True,
    "character_repetition_length": 10,
    "character_repetition_max_cutoff": 0.20,
    "cond_check_word_repetition_removal": True,
    "word_repetition_length": 5,
    "word_repetition_max_cutoff": 0.34,
    "cond_check_special_characters": True,
    "special_characters": special_characters_default,
    "special_characters_max_cutoff": 0.30,
    "cond_words_augmentation": False,
    "words_augmentation_group_sizes": [],
    "words_augmentation_join_char": "",
    "cond_check_stopwords": True,
    "stopwords_min_cutoff": 0.07,
    "cond_check_flagged_words": True,
    "flagged_words_max_cutoff": 0.03,
    "cond_check_lang_id": True,
    "lang_id_min_cutoff": 0.81,
    "cond_check_perplexity": True,
    "perplexity_max_cutoff": 2300,
}

parameters_filtering_bn = {
    "cond_uniform_whitespace": True,
    "cond_replace_unicode_punctuation": False,
    "cond_remove_words_with_incorrect_substrings": True,
    "incorrect_word_substrings": ["http", "www", ".com", "href", "//"],
    "cond_remove_long_words": True,
    "length_word_max_cutoff": 20,
    "cond_check_number_words": True,
    "tokenization": False,
    "strip_characters": special_characters_default,
    "number_words_min_cutoff": 33,
    "number_words_max_cutoff": 100000,
    "cond_check_character_repetition_removal": True,
    "character_repetition_length": 10,
    "character_repetition_max_cutoff": 0.13,
    "cond_check_word_repetition_removal": True,
    "word_repetition_length": 5,
    "word_repetition_max_cutoff": 0.21,
    "cond_check_special_characters": True,
    "special_characters": special_characters_default,
    "special_characters_max_cutoff": 0.45,
    "cond_words_augmentation": False,
    "words_augmentation_group_sizes": [],
    "words_augmentation_join_char": "",
    "cond_check_stopwords": True,
    "stopwords_min_cutoff": 0.002,
    "cond_check_flagged_words": True,
    "flagged_words_max_cutoff": 0.001,
    "cond_check_lang_id": True,
    "lang_id_min_cutoff": 0.95,
    "cond_check_perplexity": True,
    "perplexity_max_cutoff": 2000,
}

parameters_filtering_ca = {
    "cond_uniform_whitespace": True,
    "cond_replace_unicode_punctuation": False,
    "cond_remove_words_with_incorrect_substrings": True,
    "incorrect_word_substrings": ["http", "www", ".com", "href", "//"],
    "cond_remove_long_words": True,
    "length_word_max_cutoff": 20,
    "cond_check_number_words": True,
    "tokenization": False,
    "strip_characters": special_characters_default,
    "number_words_min_cutoff": 15,
    "number_words_max_cutoff": 100000,
    "cond_check_character_repetition_removal": True,
    "character_repetition_length": 10,
    "character_repetition_max_cutoff": 0.2,
    "cond_check_word_repetition_removal": True,
    "word_repetition_length": 5,
    "word_repetition_max_cutoff": 0.4,
    "cond_check_special_characters": True,
    "special_characters": special_characters_default,
    "special_characters_max_cutoff": 0.25,
    "cond_words_augmentation": False,
    "words_augmentation_group_sizes": [],
    "words_augmentation_join_char": "",
    "cond_check_stopwords": True,
    "stopwords_min_cutoff": 0.25,
    "cond_check_flagged_words": True,
    "flagged_words_max_cutoff": 0.1,
    "cond_check_lang_id": True,
    "lang_id_min_cutoff": 0.8,
    "cond_check_perplexity": True,
    "perplexity_max_cutoff": 2500,
}

parameters_filtering_en = {
    "cond_uniform_whitespace": True,
    "cond_replace_unicode_punctuation": False,
    "cond_remove_words_with_incorrect_substrings": True,
    "incorrect_word_substrings": ["http", "www", ".com", "href", "//"],
    "cond_remove_long_words": True,
    "length_word_max_cutoff": 25,
    "cond_check_number_words": True,
    "tokenization": False,
    "strip_characters": special_characters_default,
    "number_words_min_cutoff": 20,
    "number_words_max_cutoff": 100000,
    "cond_check_character_repetition_removal": True,
    "character_repetition_length": 10,
    "character_repetition_max_cutoff": 0.106,
    "cond_check_word_repetition_removal": True,
    "word_repetition_length": 5,
    "word_repetition_max_cutoff": 0.19,
    "cond_check_special_characters": True,
    "special_characters": special_characters_default,
    "special_characters_max_cutoff": 0.4,
    "cond_words_augmentation": False,
    "words_augmentation_group_sizes": [],
    "words_augmentation_join_char": "",
    "cond_check_stopwords": True,
    "stopwords_min_cutoff": 0.3,
    "cond_check_flagged_words": True,
    "flagged_words_max_cutoff": 0.01,
    "cond_check_lang_id": True,
    "lang_id_min_cutoff": 0.80,
    "cond_check_perplexity": True,
    "perplexity_max_cutoff": 1500,
}

parameters_filtering_es = {
    "cond_uniform_whitespace": True,
    "cond_replace_unicode_punctuation": False,
    "cond_remove_words_with_incorrect_substrings": True,
    "incorrect_word_substrings": ["http", "www", ".com", "href", "//"],
    "cond_remove_long_words": True,
    "length_word_max_cutoff": 25,
    "cond_check_number_words": True,
    "tokenization": False,
    "strip_characters": special_characters_default,
    "number_words_min_cutoff": 16,
    "number_words_max_cutoff": 100000,
    "cond_check_character_repetition_removal": True,
    "character_repetition_length": 10,
    "character_repetition_max_cutoff": 0.14,
    "cond_check_word_repetition_removal": True,
    "word_repetition_length": 5,
    "word_repetition_max_cutoff": 0.25,
    "cond_check_special_characters": True,
    "special_characters": special_characters_default,
    "special_characters_max_cutoff": 0.34,
    "cond_words_augmentation": False,
    "words_augmentation_group_sizes": [],
    "words_augmentation_join_char": "",
    "cond_check_stopwords": True,
    "stopwords_min_cutoff": 0.4,
    "cond_check_flagged_words": True,
    "flagged_words_max_cutoff": 0.01,
    "cond_check_lang_id": True,
    "lang_id_min_cutoff": 0.8,
    "cond_check_perplexity": True,
    "perplexity_max_cutoff": 1300,
}

parameters_filtering_eu = {
    "cond_uniform_whitespace": True,
    "cond_replace_unicode_punctuation": False,
    "cond_remove_words_with_incorrect_substrings": True,
    "incorrect_word_substrings": ["http", "www", ".com", "href", "//"],
    "cond_remove_long_words": True,
    "length_word_max_cutoff": 28,
    "cond_check_number_words": True,
    "tokenization": False,
    "strip_characters": special_characters_default,
    "number_words_min_cutoff": 8,
    "number_words_max_cutoff": 100000,
    "cond_check_character_repetition_removal": True,
    "character_repetition_length": 10,
    "character_repetition_max_cutoff": 0.20,
    "cond_check_word_repetition_removal": True,
    "word_repetition_length": 5,
    "word_repetition_max_cutoff": 0.40,
    "cond_check_special_characters": True,
    "special_characters": special_characters_default,
    "special_characters_max_cutoff": 0.31,
    "cond_words_augmentation": False,
    "words_augmentation_group_sizes": [],
    "words_augmentation_join_char": "",
    "cond_check_stopwords": True,
    "stopwords_min_cutoff": 0.05,
    "cond_check_flagged_words": True,
    "flagged_words_max_cutoff": 0.1,
    "cond_check_lang_id": True,
    "lang_id_min_cutoff": 0.70,
    "cond_check_perplexity": True,
    "perplexity_max_cutoff": 3000,
}

parameters_filtering_fr = {
    "cond_uniform_whitespace": True,
    "cond_replace_unicode_punctuation": False,
    "cond_remove_words_with_incorrect_substrings": True,
    "incorrect_word_substrings": ["http", "www", ".com", "href", "//"],
    "cond_remove_long_words": True,
    "length_word_max_cutoff": 45,
    "cond_check_number_words": True,
    "tokenization": False,
    "strip_characters": special_characters_default,
    "number_words_min_cutoff": 13,
    "number_words_max_cutoff": 100000,
    "cond_check_character_repetition_removal": True,
    "character_repetition_length": 10,
    "character_repetition_max_cutoff": 0.14,
    "cond_check_word_repetition_removal": True,
    "word_repetition_length": 5,
    "word_repetition_max_cutoff": 0.13,
    "cond_check_special_characters": True,
    "special_characters": special_characters_default,
    "special_characters_max_cutoff": 0.34,
    "cond_words_augmentation": False,
    "words_augmentation_group_sizes": [],
    "words_augmentation_join_char": "",
    "cond_check_stopwords": True,
    "stopwords_min_cutoff": 0.27,
    "cond_check_flagged_words": True,
    "flagged_words_max_cutoff": 0.008,
    "cond_check_lang_id": True,
    "lang_id_min_cutoff": 0.8,
    "cond_check_perplexity": True,
    "perplexity_max_cutoff": 1770,
}

parameters_filtering_hi = {
    "cond_uniform_whitespace": True,
    "cond_replace_unicode_punctuation": False,
    "cond_remove_words_with_incorrect_substrings": True,
    "incorrect_word_substrings": ["http", "www", ".com", "href", "//"],
    "cond_remove_long_words": True,
    "length_word_max_cutoff": 25,
    "cond_check_number_words": True,
    "tokenization": False,
    "strip_characters": special_characters_default,
    "number_words_min_cutoff": 38,
    "number_words_max_cutoff": 100000,
    "cond_check_character_repetition_removal": True,
    "character_repetition_length": 10,
    "character_repetition_max_cutoff": 0.18,
    "cond_check_word_repetition_removal": True,
    "word_repetition_length": 5,
    "word_repetition_max_cutoff": 0.47,
    "cond_check_special_characters": True,
    "special_characters": special_characters_default,
    "special_characters_max_cutoff": 0.45,
    "cond_words_augmentation": False,
    "words_augmentation_group_sizes": [],
    "words_augmentation_join_char": "",
    "cond_check_stopwords": True,
    "stopwords_min_cutoff": 0.01,
    "cond_check_flagged_words": True,
    "flagged_words_max_cutoff": 0.005,
    "cond_check_lang_id": True,
    "lang_id_min_cutoff": 0.90,
    "cond_check_perplexity": True,
    "perplexity_max_cutoff": 1517,
}

parameters_filtering_id = {
    "cond_uniform_whitespace": True,
    "cond_replace_unicode_punctuation": False,
    "cond_remove_words_with_incorrect_substrings": True,
    "incorrect_word_substrings": ["http", "www", ".com", "href", "//"],
    "cond_remove_long_words": True,
    "length_word_max_cutoff": 30,
    "cond_check_number_words": True,
    "tokenization": False,
    "strip_characters": special_characters_default,
    "number_words_min_cutoff": 15,
    "number_words_max_cutoff": 100000,
    "cond_check_character_repetition_removal": True,
    "character_repetition_length": 10,
    "character_repetition_max_cutoff": 0.15,
    "cond_check_word_repetition_removal": True,
    "word_repetition_length": 5,
    "word_repetition_max_cutoff": 0.20,
    "cond_check_special_characters": True,
    "special_characters": special_characters_default,
    "special_characters_max_cutoff": 0.34,
    "cond_words_augmentation": False,
    "words_augmentation_group_sizes": [],
    "words_augmentation_join_char": "",
    "cond_check_stopwords": True,
    "stopwords_min_cutoff": 0.15,
    "cond_check_flagged_words": True,
    "flagged_words_max_cutoff": 0.01,
    "cond_check_lang_id": True,
    "lang_id_min_cutoff": 0.7,
    "cond_check_perplexity": True,
    "perplexity_max_cutoff": 5000,
}

parameters_filtering_pt = {
    "cond_uniform_whitespace": True,
    "cond_replace_unicode_punctuation": False,
    "cond_remove_words_with_incorrect_substrings": True,
    "incorrect_word_substrings": ["http", "www", ".com", "href", "//"],
    "cond_remove_long_words": True,
    "length_word_max_cutoff": 19,
    "cond_check_number_words": True,
    "tokenization": False,
    "strip_characters": special_characters_default,
    "number_words_min_cutoff": 19,
    "number_words_max_cutoff": 100000,
    "cond_check_character_repetition_removal": True,
    "character_repetition_length": 10,
    "character_repetition_max_cutoff": 0.25,
    "cond_check_word_repetition_removal": True,
    "word_repetition_length": 5,
    "word_repetition_max_cutoff": 0.98,
    "cond_check_special_characters": True,
    "special_characters": special_characters_default,
    "special_characters_max_cutoff": 0.35,
    "cond_words_augmentation": False,
    "words_augmentation_group_sizes": [],
    "words_augmentation_join_char": "",
    "cond_check_stopwords": True,
    "stopwords_min_cutoff": 0.2,
    "cond_check_flagged_words": True,
    "flagged_words_max_cutoff": 0.007,
    "cond_check_lang_id": True,
    "lang_id_min_cutoff": 0.6,
    "cond_check_perplexity": True,
    "perplexity_max_cutoff": 3038,
}

parameters_filtering_ur = {
    "cond_uniform_whitespace": True,
    "cond_replace_unicode_punctuation": False,
    "cond_remove_words_with_incorrect_substrings": True,
    "incorrect_word_substrings": ["http", "www", ".com", "href", "//"],
    "cond_remove_long_words": True,
    "length_word_max_cutoff": 20,
    "cond_check_number_words": True,
    "tokenization": False,
    "strip_characters": special_characters_default,
    "number_words_min_cutoff": 25,
    "number_words_max_cutoff": 100000,
    "cond_check_character_repetition_removal": True,
    "character_repetition_length": 10,
    "character_repetition_max_cutoff": 0.19,
    "cond_check_word_repetition_removal": True,
    "word_repetition_length": 7,
    "word_repetition_max_cutoff": 0.5,
    "cond_check_special_characters": True,
    "special_characters": special_characters_default,
    "special_characters_max_cutoff": 0.25,
    "cond_words_augmentation": False,
    "words_augmentation_group_sizes": [],
    "words_augmentation_join_char": "",
    "cond_check_stopwords": True,
    "stopwords_min_cutoff": 0.01,
    "cond_check_flagged_words": True,
    "flagged_words_max_cutoff": 0.025,
    "cond_check_lang_id": True,
    "lang_id_min_cutoff": 0.90,
    "cond_check_perplexity": True,
    "perplexity_max_cutoff": 1495,
}

parameters_filtering_vi = {
    "cond_uniform_whitespace": True,
    "cond_replace_unicode_punctuation": False,
    "cond_remove_words_with_incorrect_substrings": True,
    "incorrect_word_substrings": ["http", "www", ".com", "href", "//"],
    "cond_remove_long_words": True,
    "length_word_max_cutoff": 25,
    "cond_check_number_words": True,
    "tokenization": False,
    "strip_characters": special_characters_default,
    "number_words_min_cutoff": 30,
    "number_words_max_cutoff": 100000,
    "cond_check_character_repetition_removal": True,
    "character_repetition_length": 10,
    "character_repetition_max_cutoff": 0.15,
    "cond_check_word_repetition_removal": True,
    "word_repetition_length": 5,
    "word_repetition_max_cutoff": 0.20,
    "cond_check_special_characters": True,
    "special_characters": special_characters_default,
    "special_characters_max_cutoff": 0.34,
    "cond_words_augmentation": True,
    "words_augmentation_group_sizes": [2],
    "words_augmentation_join_char": " ",
    "cond_check_stopwords": True,
    "stopwords_min_cutoff": 0.08,
    "cond_check_flagged_words": True,
    "flagged_words_max_cutoff": 0.005,
    "cond_check_lang_id": True,
    "lang_id_min_cutoff": 0.90,
    "cond_check_perplexity": True,
    "perplexity_max_cutoff": 1600,
}

parameters_filtering_zh = {
    "cond_uniform_whitespace": True,
    "cond_replace_unicode_punctuation": False,
    "cond_remove_words_with_incorrect_substrings": False,
    "incorrect_word_substrings": ["http", "www", ".com", "href", "//"],
    "cond_remove_long_words": False,
    "length_word_max_cutoff": 1000,
    "cond_check_number_words": True,
    "tokenization": True,
    "strip_characters": special_characters_default,
    "number_words_min_cutoff": 1,
    "number_words_max_cutoff": 1000000,
    "cond_check_character_repetition_removal": True,
    "character_repetition_length": 3,
    "character_repetition_max_cutoff": 0.2,
    "cond_check_word_repetition_removal": True,
    "word_repetition_length": 5,
    "word_repetition_max_cutoff": 0.96,
    "cond_check_special_characters": True,
    "special_characters": special_characters_default,
    "special_characters_max_cutoff": 0.3,
    "cond_words_augmentation": True,
    "words_augmentation_group_sizes": [2],
    "words_augmentation_join_char": "",
    "cond_check_stopwords": True,
    "stopwords_min_cutoff": 0.1691,
    "cond_check_flagged_words": True,
    "flagged_words_max_cutoff": 0.001,
    "cond_check_lang_id": True,
    "lang_id_min_cutoff": 0.85,
    "cond_check_perplexity": True,
    "perplexity_max_cutoff": 2095,
}

parameters_filtering = {
    "default": parameters_filtering_default,
    "ar": parameters_filtering_ar,
    "bn": parameters_filtering_bn,
    "ca": parameters_filtering_ca,
    "en": parameters_filtering_en,
    "es": parameters_filtering_es,
    "eu": parameters_filtering_eu,
    "fr": parameters_filtering_fr,
    "hi": parameters_filtering_hi,
    "id": parameters_filtering_id,
    "pt": parameters_filtering_pt,
    "ur": parameters_filtering_ur,
    "vi": parameters_filtering_vi,
    "zh": parameters_filtering_zh,
}