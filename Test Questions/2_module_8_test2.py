'''
    Welcome...!
    Module # 8 (Test 2)
    You are given words. Some words may repeat. For each word, output its number of occurrences. 
    The output order should correspond with the input order of appearance of the word....

'''

def wrd_cnt(num, words):
    word_cnt = {}
    uniq_wrd = []

    for wrd in words:
        if wrd not in word_cnt:
            word_cnt[wrd] = 1
            uniq_wrd.append(wrd)
        else:
            word_cnt[wrd] += 1
    print(len(uniq_wrd))
    for wrd in uniq_wrd:
        print(word_cnt[wrd], end=' ')

num = 4
wrd_lst = ["bcdef", "abcdefg", "bcde", "bcdef"]
wrd_cnt(num, wrd_lst)


