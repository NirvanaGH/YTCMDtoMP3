import requests
import yt_dlp as youtube_dl
import os

def search_youtube(query, api_key):
    url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&key={api_key}&type=video'
    
    try:
        response = requests.get(url)
        response.raise_for_status()

        results = response.json()
        
        if 'items' in results:
            video_ids = []
            for i, item in enumerate(results['items'][:5]):
                title = item['snippet']['title']
                video_id = item['id']['videoId']
                print(f"{i + 1}: {title} (https://www.youtube.com/watch?v={video_id})")
                video_ids.append(video_id)
            return video_ids
        else:
            print('No results found.')
            return []

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return []

def download_video(video_id, output_path):
    try:
        url = f'https://www.youtube.com/watch?v={video_id}'
        print(f'Downloading: {url}')
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # Set output path here
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ffmpeg_location': 'C:/ffmpeg/bin'  # Adjust this path if needed
        }
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            return os.path.join(output_path, f"{video_id}.mp3")  # Return the full path of the MP3 file
    except Exception as e:
        print(f'Error downloading video: {e}')
        return None

    
if __name__ == '__main__':
    api_key = 'YOUR_API_KEY_HERE'  # Replace with your YouTube Data API key
    query = input("Enter search query: ")
    
    output_path = input("Enter the output path (e.g., C:/Downloads): ")  # Get output path from user

    video_ids = search_youtube(query, api_key)
    
    if video_ids:
        selection = int(input("Select a video (1-5): ")) - 1
        if 0 <= selection < len(video_ids):
            video_id = video_ids[selection]
            mp3_file = download_video(video_id, output_path)  # Pass output path here
            if mp3_file:
                print(f'Converted to MP3: {mp3_file}')
        else:
            print("Invalid selection.")
    else:
        print("No videos available to download.")

