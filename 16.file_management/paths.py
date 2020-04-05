from pathlib import Path
import os
from glob import glob
import shutil

p = os.getcwd()
print(p)
os.mkdir('os_dir')

my_path = os.path.join(p, 'os_dir')
in_path = os.path.join(p, 'filetomove.txt')
out_path = os.path.join(my_path, 'filetomove.txt')

os.rename(in_path, out_path)

all_py_files = glob('*.py', recursive=True)
for i in all_py_files:
    shutil.copy(i, my_path)
print(all_py_files)
print(os.listdir(my_path))

remove_path = os.path.join(my_path, '*')
all_files = glob(remove_path, recursive=True)
for i in all_files:
    os.remove(i)

os.rmdir(my_path)

###

p = Path.cwd()
my_path = p.joinpath( "pathlib_dir")
my_path.mkdir(mode=0o777, parents=False, exist_ok=True)
in_path = p.joinpath('filetomove.txt')
out_path = my_path.joinpath('filetomove.txt')
#in_path.replace(out_path)

all_py_files = p.glob('*.py')
for i in all_py_files:
    shutil.copy(i, my_path)

all_files = list(my_path.glob('*'))
print(all_files)

for i in all_files:
    i.unlink()

my_path.rmdir()


