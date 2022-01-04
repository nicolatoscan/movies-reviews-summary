# %%
from urllib.request import urlopen
import pandas as pd
from multiprocessing import Pool
from lxml.html import parse
from tqdm import tqdm

# %%
df = pd.read_csv('data/dataset.csv', sep='\t')

# %%
ids = list(df['url'].unique())

# %%
def getTitle(id):
    try:
        title = parse(urlopen(f"https://www.imdb.com/title/{id}/")).find(".//title").text
        return id, title.strip(' - IMDb')
    except:
        return id, '||ERROR||'


with open('data/titles.csv', 'w') as f:
    pool = Pool(processes=128)
    for id, title in tqdm(pool.imap_unordered(getTitle, ids), total=len(ids)):
        f.write(f"{id}\t{title}\n")


# %%

# %%
