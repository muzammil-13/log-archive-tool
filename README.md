# Log Archive Tool

The Log Archive Tool is a command-line utility designed to compress and archive log files. This helps in managing and maintaining system logs effectively, ensuring that old logs are stored in a compressed format for future reference while keeping the system clean.

## Features

- **Command-line Interface:** Easily specify the log directory to archive via the command line.
- **Compression:** Compresses logs into a `.tar.gz` file.
- **Timestamped Archives:** Archives are saved with the current date and time in their filename.
- **Automation Friendly:** Can be integrated into scheduled tasks or cron jobs for regular log archiving.

## Requirements

- Python 3.x
- Access to the log directory (e.g., `/var/log` on Unix-based systems)

## Installation

Clone the repository to your local machine:

```sh
git clone https://github.com/your-username/log-archive-tool.git
cd log-archive-tool
```

## Usage

Run the script from the command line with the required arguments:

**sh**Copy

```
python log_archive.py <log_directory> <output_directory>
```

* `<log_directory>`: Path to the log directory to be archived.
* `<output_directory>`: Path to the directory where the archive will be stored.

### Example

**sh**Copy

```
python log_archive.py /var/log /path/to/archive_dir
```

## How It Works

1. **Accepts Arguments:** The tool accepts the log directory and the output directory as command-line arguments.
2. **Creates Archive:** It compresses the specified log directory into a `.tar.gz` file.
3. **Timestamps Archive:** The archive is named with the current date and time, e.g., `logs_archive_20240816_100648.tar.gz`.
4. **Stores Archive:** The archive is stored in the specified output directory.

## Project Page

For more details and updates, visit the [project page](https://roadmap.sh/projects/log-archive-tool?form=MG0AV3).

## Contributing

Feel free to submit pull requests to enhance the functionality or fix issues. Contributions are welcome!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
