# vimeodownload

This script allows you to download multiple password-protected Vimeo videos using `yt-dlp`.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.6 or later.
- You have installed `yt-dlp`. If not, you can install it using pip:

    ```bash
    pip install yt-dlp
    ```

## Usage

1. Create a `videos.txt` file in the project directory. Each line should contain a Vimeo video URL and its corresponding password, separated by a space. For example:

    ```
    https://vimeo.com/123456789 pass1
    https://vimeo.com/987654321 pass2
    ```

2. Run the script:

    ```bash
    python vimeo-installer.py
    ```

   The script will read the `videos.txt` file and download each video using `yt-dlp`.

## Script Details

The `vimeo-installer.py` script reads the `videos.txt` file, extracts the video URL and password, and downloads the video using the `yt-dlp` command-line tool. If a download fails, the script will print an error message.
