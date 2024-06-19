import os, hashlib, base64, pandas as pd


def tsv_maker(books, prefix, bk_dir, root):
    '''
    makes a tsv file from a list of files
    saves the tsv file to the books directory
    :param list:  list of files
    :return: None
    '''
    outlist = []
    outlist.append(['TsvHttpData-1.0'])  # add the header
    for txt in books:  # for each file in the list
        url = prefix + txt  # get the url
        filepath = bk_dir + "\\" + txt  # create the file path
        file = open(filepath, "rb")  # open the file
        content = file.read()  # read in the file
        meta = os.path.getsize(filepath)  # get the file size
        md5_hash = hashlib.md5(content).digest()  # get the md5 hash
        md5 = base64.b64encode(md5_hash).decode()  # encode the md5 hash
        outlist.append([url, meta, md5])  # append the url, meta, and md5 to the outlist
        file.close()  # close the file
    # write the outlist to a tsv file using pandas (for ease)
    pd.DataFrame(outlist).to_csv(root + '\\books.tsv', sep='\t', index=False, header=False)


if __name__ == "__main__":
    PREFIX = 'https://raw.githubusercontent.com/cd-public/books/main/'
    root = os.path.dirname(os.path.realpath('make_tsv.py'))  # get the root directory
    BK_DIR = root + '/books'
    bk_list = os.listdir(BK_DIR) # get the list of books

    tsv_maker(bk_list, prefix=PREFIX, bk_dir=BK_DIR, root=root)  # make the tsv file
