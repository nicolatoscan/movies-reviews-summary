# %%
from os import listdir
from os.path import join

# %%
def dirParse(dir, urlsPath):
    dir = join('data/aclImdb', dir)
    urlsPath = join('data/aclImdb', urlsPath)

    res = []
    for f in listdir(dir):
        with open(join(dir, f), 'r') as file:
            id = int(f.split('_')[0])
            rating = int(f.split('_')[1].split('.')[0])
            rev = file.readlines()[0].replace('\t', ' ')
            label = 1 if rating > 5 else (-1 if rating == 0 else 0)
            res.append((id, rev, rating, label))
    res.sort()

    with open(urlsPath, 'r') as fUrls:
        urls = [ l.split('/')[-2] for l in fUrls ]
        if len(res) != len(urls):
            print("Error: files and urls have different length")
            return []

        return [
            (id, rev, rating, url, label)
            for (url , (id, rev, rating, label)) in zip(urls, res)
        ]

# %%
trainPos = dirParse('train/pos', 'train/urls_pos.txt')
trainNeg = dirParse('train/neg', 'train/urls_neg.txt')
testPos = dirParse('test/pos', 'test/urls_pos.txt')
testNeg = dirParse('test/neg', 'test/urls_neg.txt')
unsup = dirParse('train/unsup', 'train/urls_unsup.txt')
allRevs = trainPos + trainNeg + testPos + testNeg + unsup

# %%
with open("data/dataset.csv", "w") as f:
    f.write("review\trating\turl\tlabel\n")
    for id, rev, rating, url, label in allRevs:
        f.write(f"{rev}\t{rating}\t{url}\t{label}\n")

# %%
import pandas as pd


# %%
pd.read_csv('data/dataset.csv', sep='\t')
# %%
