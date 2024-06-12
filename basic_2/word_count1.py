# 単語に分割するver
text = input("文章を入力してください")
word_list = text.split()
print(word_list)
num_words = len(word_list)
print(f"単語数: {num_words}")

# 一文字ずつ分割するver
word_list = list(text)
print(word_list)
num_words = len(word_list)
print(f"文字数:{num_words}")

# 空白文字を除外するver
for word in word_list:
    if word == " ":
        word_list.remove(word)
print(word_list)
num_words = len(word_list)
print(f"{num_words}")
