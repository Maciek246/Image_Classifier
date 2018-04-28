from PIL import Image
from os import listdir, rename, makedirs
import os.path
import csv


def get_data(dir_name):
    tab = []
    with open(os.path.join(dir_name, "decor.csv"), newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter="*", quotechar=",")
        for row in reader:
            tab.append(row[0].split(","))
        tab.pop(0)
    return tab

def make_dirs(tab, dest_dir):
    folders = []
    for _ in tab:
        if _[3] not in folders:
            folders.append(_[3])

    if not os.path.exists(os.path.join(dest_dir,'decor')):
        makedirs(os.path.join(dest_dir,'decor'))

    for _ in folders:
        if not os.path.exists(os.path.join(dest_dir,'decor',_)):
            makedirs(os.path.join(dest_dir,'decor',_))
            
def select_products(data):
    return [_ for _ in data if _[5] == 'product']

def input_selected_data_into_folders(data, data_dir, dest_dir):
    for _ in data:
        if os.path.isfile(os.path.join(data_dir,'decor',_[-1])):
            im = Image.open(os.path.join(data_dir,'decor',_[-1]))
            img = im.convert('RGB')
            jpg = ''
            if _[-1].endswith('.png'):
                jpg = _[-1].replace('.png','.jpg')
            img.save(os.path.join(dest_dir,_[3], jpg))

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath('__file__'))
    DEST_DIR = os.path.join(BASE_DIR,'tensorflow-for-poets-2','tf_files')
    DATA_DIR = os.path.join(BASE_DIR,'traditional-decor-patterns')

    data = select_products(get_data(DATA_DIR))
    make_dirs(data, DEST_DIR)
    input_selected_data_into_folders(data, DATA_DIR, os.path.join(DEST_DIR,'decor'))

    if 'Wycinanki Ĺ‚owickie' in listdir(os.path.join(DEST_DIR,'decor',)):
        rename(os.path.join(DEST_DIR,'decor','Wycinanki Ĺ‚owickie'), os.path.join(DEST_DIR,'decor','Wycinanki lowickie'))
    
