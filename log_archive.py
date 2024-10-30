import os
import tarfile
import argparse
from datetime import datetime

def create_archive(log_dir, output_dir):
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"logs_archive_{current_time}.tar.gz"
    archive_path = os.path.join(output_dir, archive_name)

    with tarfile.open(archive_path, "w:gz") as tar:
        tar.add(log_dir, arcname=os.path.basename(log_dir))

    print(f"Logs archived in: {archive_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Archive logs.")
    parser.add_argument("log_directory", help="Path to the log directory to be archived.")
    parser.add_argument("output_directory", help="Path to the directory where the archive will be stored.")
    
    args = parser.parse_args()
    
    create_archive(args.log_directory, args.output_directory)
