# Project Instructions

## 1. Update `xxx.yaml` File
- Modify the `path` to the directory containing data.
- Create a folder named `txt` inside the `data` folder.
- Update the name of the txt file.
- Update the Classes name.

## 2. Modify `create_txt.py` File
- Line 19: Update `folder = '/root/disk4tb/tiny_data'` to the path of the data directory.
- Update the name of the txt file (suffix) in the line: `with open(f'txt/{type_folder}_pizza.txt', 'w') as f:`.

## 3. Run `create_txt.py` to Generate New txt Files
```bash
python create_txt.py
