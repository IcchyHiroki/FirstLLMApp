import tiktoken

# assigning API KEY to initialize openai environment
api_key = "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"

# define encoding
encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')

# 英語のtextを確認する
text_en = "This is a test for tiktoken."
tokens_en = encoding.encode(text_en)
print(len(text_en))  # 28
print(tokens_en)  # [2028, 374, 264, 1296, 369, 87272, 5963, 13]
print(len(tokens_en))  # 8

# 日本語のtextを確認する
text_jp = "今からtiktokenのトークンカウントテストを行います"
tokens_jp = encoding.encode(text_jp)
print(len(text_jp))  # 28
print(tokens_jp)  # [37271, 55031, 83, 1609, 5963, 16144, 20251, 11972, 29220, 16073, 71493, 65299, 52414, 57933, 71634, 30512, 23039, 61689]
print(len(tokens_jp))  # 18