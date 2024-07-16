import os
import glob
print('ok')


def generate_txt(type_folder, folder):
    rootDir = f'{folder}/{type_folder}'

    # Open the output file
    with open(f'txt/{type_folder}_pizza.txt', 'w') as f:
        # Walk through the directory
        for dirName, subdirList, fileList in os.walk(rootDir):
            # Find all .jpg and .png files in the current directory
            for filename in glob.glob(os.path.join(dirName, '*.jpg')) + glob.glob(os.path.join(dirName, '*.png')):
                # Write the full file path to theoutput file
                f.write(filename + '\n')

list_type_folder = ['train', 'test', 'valid']
folder = '/root/disk4tb/tiny_data'
for type_folder in list_type_folder:
    generate_txt(type_folder, folder)
    print('Done with ' + folder)