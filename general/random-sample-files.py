import os, pathlib, shutil, random
import pdb; pdb.set_trace()

base_dir = pathlib.Path("/home/chris/imdb/aclImdb")
# target validation directory
# contains a % of train
val_dir = base_dir / "val"
train_dir = base_dir / "train"

for category in ("neg", "pos"):
    os.makedirs(val_dir / category)
    files = os.listdir(train_dir / category)
    random.Random(42).shuffle(files)

    # get the index of where to cutoff the list of files
    num_val_samples = int(0.2 * len(files))

    # capture all files after the val_samples index
    val_files = files[-num_val_samples:]
    for fname in val_files:
        shutil.move(train_dir / category / fname, \
            val_dir / category / fname)