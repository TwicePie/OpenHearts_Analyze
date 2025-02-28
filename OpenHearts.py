from googleapiclient.discovery import build
import time
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API Key from environment variable
API_KEY = os.getenv('YOUTUBE_API_KEY')

# ID Video YouTube dari link yang Anda berikan
VIDEO_ID = 'll6sBa3Dafs'

# Inisialisasi YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_video_comments(video_id, max_results=1500):
    """Get comments from a YouTube video"""
    comments = []
    next_page_token = None
    
    try:
        print(f"Mengambil komentar untuk video ID: {video_id}")
        
        while True:  # Changed to infinite loop, will break when no more comments
            # Request comment threads
            response = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                maxResults=100,  # Maximum allowed by API per request
                pageToken=next_page_token,
                textFormat='plainText'
            ).execute()
            
            # Process comments in this batch
            for item in response.get('items', []):
                comment = item['snippet']['topLevelComment']['snippet']
                text = comment['textDisplay']
                comments.append(text)
            
            # Check if there are more comments
            next_page_token = response.get('nextPageToken')
            if not next_page_token or (max_results and len(comments) >= max_results):
                break
            
            # Add longer delay to avoid quota issues
            time.sleep(1)
            
            print(f"Sudah mengambil {len(comments)} komentar...")
            
        print(f"Berhasil mengambil {len(comments)} komentar.")
        return comments
        
    except Exception as e:
        print(f"Error saat mengambil komentar: {str(e)}")
        if 'quota' in str(e).lower():
            print("Quota API YouTube telah habis. Coba lagi besok atau gunakan API key yang berbeda.")
        return comments

# Main execution
print("=== YOUTUBE COMMENT RETRIEVER ===")

# Get comments
comments = get_video_comments(VIDEO_ID, max_results=1500)  # Set to retrieve 1500 comments

if comments:
    # Display sample
    print("\n=== CONTOH KOMENTAR ===")
    for i, comment in enumerate(comments[:5]):  # Show just 5 comments as sample
        print(f"{i+1}. {comment[:100]}{'...' if len(comment) > 100 else ''}")
        print()
        
    # Save to file
    with open("video_comments.txt", "w", encoding="utf-8") as file:
        for comment in comments:
            file.write(f"{comment}\n\n")
            
    print(f"\nSemua {len(comments)} komentar berhasil disimpan di 'video_comments.txt'")
else:
    print("Tidak ada komentar yang ditemukan.")