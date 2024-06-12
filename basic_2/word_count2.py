text = input("文章を入力してください")
target = input("検索する単語を入力してください")
word_list = text.split()
count = 0
for word in word_list:
    if word == target:
        count += 1
print(f"{target}は{count}個含まれています")
