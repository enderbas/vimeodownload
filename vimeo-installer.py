import subprocess

def download_videos(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            video_url, video_password = line.strip().split()
            command = [
                'yt-dlp', video_url, '--video-password', video_password
            ]
            try:
                result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(f"Downloaded {video_url} successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Failed to download {video_url}. Error: {e.stderr.decode()}")

if __name__ == '__main__':
    file_path = 'videos.txt'
    download_videos(file_path)
