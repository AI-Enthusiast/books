import os, hashlib, base64, pandas as pd
import requests

root = os.path.dirname(os.path.realpath('make_tsv.py')) # get the root directory
BK_DIR = root + '/books'



def tsv_maker(list):
    '''
    makes a tsv file from a list of files
    saves the tsv file to the books directory
    :param list:  list of files
    :return: None
    '''
    outlist = []
    outlist.append(['TsvHttpData-1.0'])
    for txt in list:
        url = PREFIX+txt
        filepath = BK_DIR + "\\" + txt
        file = open(filepath,"rb")
        content = file.read()
        meta = os.path.getsize(filepath)
        md5_hash = hashlib.md5(content).digest()
        md5 = base64.b64encode(md5_hash).decode()
        outlist.append([url,meta,md5])
        file.close()
    pd.DataFrame(outlist).to_csv(BK_DIR+'\\books.tsv',sep='\t',index=False,header=False)

if __name__ == "__main__":
    # tsv_maker(urllist)
    get_books()