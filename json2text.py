from save import save
import json
from save import save

dir_path = '/Users/bayashihi/Documents/VScode/paper/scrapbox' 
#path of directry which you want to save text files converted.

with open('scrapbox.json') as f: #put your JSON file named "scrapbox.json" in the root directry.
    js = json.load(f) # 
    f.close()

cont_list = js['pages']

for a in cont_list:
    # a = cont_list[i] #i番目のdictを取得
    title = a['title']
    cont_pre = a['lines']
    content = '\n'.join(cont_pre)
    
    save(dir_path, title + '.md', content)