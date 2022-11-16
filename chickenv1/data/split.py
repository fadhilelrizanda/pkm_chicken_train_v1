import splitfolders

splitfolders.ratio('data_img', output="training",
                   seed=42, ratio=(0.8, 0.2), group_prefix=None)
