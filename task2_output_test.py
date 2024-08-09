import pandas as pd
import itertools

groupnum = input("Please input your group number:")
df = pd.read_csv("{}_channel_list.csv".format(groupnum.zfill(3)))
df_col = ["channel_id", "all_comment_count", "eng_comment_count"]
assert all(df.columns == df_col) == True, "check your csv columns!"

print("Task 2 csv file passed!")

with open("{}_vocab.txt".format(groupnum.zfill(3)), "r") as file:
    vocab = file.readlines()
try:
    vocab = [each.strip().split(":") for each in vocab]
except:
    raise ValueError("Vocab file structured incorrectly!")

print("Task 2 vocab file passed!")

with open("{}_countvec.txt".format(groupnum.zfill(3)), "r") as file:
    countvec = file.readlines()

countvec = [each.strip().split(",") for each in countvec]
assert (
    all([":" not in each[0] for each in countvec]) == True
), "The channel id in countvec doesn't look right!"
try:
    allcounts = list(itertools.chain.from_iterable([each[1:] for each in countvec]))
    ind_counts = [each.split(":") for each in allcounts]
    # testing whether the ind:count can be parsed as numerical values
    [(int(each[0]), int(each[1])) for each in ind_counts]
except:
    raise ValueError("The ind:count part of your countvec doesnt look right!")

print("Task 2 countvec file passed!")
