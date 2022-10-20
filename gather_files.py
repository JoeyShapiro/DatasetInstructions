import os, hashlib, shutil

counter = 0
BLOCKSIZE = 65536
hashes = []
PATH_TO_SAVE_FILES = '' # The path you'd like to copy the unique files to
for r, d, f in os.walk('C:/'): # The directory you'd like to search for the .exe's
    for file in f:
        file_path = os.path.join(r, file)
        if(file.endswith('.exe')):
            file_path = os.path.join(r, file)
            try:
                counter += 1
                hasher = hashlib.md5()
                with open(file_path, 'rb') as afile:
                    while(True):
                        buf = afile.read(BLOCKSIZE)
                        if(not buf):
                            break
                        hasher.update(buf)
                    file_hash = hasher.hexdigest()
                    if(file_hash not in hashes):
                        hashes.append(file_hash)
                        shutil.copyfile(file_path, PATH_TO_SAVE_FILES+file)
                        print('File: ', file_path, '     MD5 Hash: ', file_hash)
                    else:
                        print('File: ', file_path, ' has already be found\n\n')
            except Exception as e:
                print('Error occountered with file:', file_path)
                print(e)
                pass
print(f"Collected {counter} files.")
