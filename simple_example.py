from img2dataset import download
import shutil
import os
import sys

source_parquets = '../../data/parquet_datas'
save_folder_name = '../../data/laion5b_images_folder'

root_path=sys.path[0]
input_dir = os.path.join(root_path, source_parquets)
output_dir = os.path.join(root_path, save_folder_name)


if __name__ == '__main__':   
    print(input_dir, output_dir)     
    download(
        # processes_count=16,
        # thread_count=32,
        processes_count=4,
        thread_count=8,
        url_list=input_dir,
        image_size=128,
        # resize_mode="no",
        input_format="parquet",
        output_folder=output_dir,
        output_format="webdataset",
        url_col="URL",
        caption_col="TEXT",
        enable_wandb=False,
        number_sample_per_shard=1000,
        # require SAMPLE_ID to write id file
        save_additional_columns=["SAMPLE_ID", "NSFW", "similarity", "LICENSE"],
        distributor="multiprocessing",
        oom_shard_count=6
    )

# rm -rf bench
