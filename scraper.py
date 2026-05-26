import requests
import re

# പ്രോബ്ലം കണ്ടുപിടിക്കാൻ നമ്മൾ ടെസ്റ്റ് ചെയ്യുന്ന ഏഷ്യാനെറ്റ് ന്യൂസ് പേജ്
test_url = "https://tulnit.com/live/asianet-news/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://tulnit.com/',
    'Connection': 'keep-alive'
}

try:
    session = requests.Session()
    response = session.get(test_url, headers=headers, timeout=15)
    html = response.text
    
    # പേജിന്റെ ഉള്ളിലുള്ള യഥാർത്ഥ പ്ലേബാക്ക് ലിങ്ക് (.m3u8 അല്ലെങ്കിൽ .mpd) കണ്ടെത്തുന്നു
    stream_links = re.findall(r'["\'](https?://[^\s"\'&]+\.(?:m3u8|mpd)[^\s"\'&]*)["\']', html)
    if not stream_links:
        stream_links = re.findall(r'(https?://[^\s"\']+\.(?:m3u8|mpd)[^\s"\']*)', html)
        
    m3u_content = "#EXTM3U\n\n"
    
    if stream_links:
        live_url = stream_links[0]
        print(f"Detected Stream URL: {live_url}")
        
        # പ്ലേലിസ്റ്റ് ഫയലിലേക്ക് ഏഷ്യാനെറ്റ് ന്യൂസ് മാത്രം എഴുതുന്നു
        m3u_content += '#EXTINF:-1 tvg-logo="https://raw.githubusercontent.com/manishb20/Tv-logos/main/asianetnews.png" group-title="Test", Asianet News\n'
        m3u_content += "#EXTVLCOPT:http-user-agent=AppleCoreMedia/1.0.0.16G77 (iPhone; U; CPU iPhone OS 12_4 like Mac OS X; en_us)\n"
        m3u_content += f"#EXTVLCOPT:http-referrer={test_url}\n"
        m3u_content += f"{live_url}|User-Agent=AppleCoreMedia/1.0.0.16G77 (iPhone; U; CPU iPhone OS 12_4 like Mac OS X; en_us)&Referer={test_url}\n\n"
        
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write(m3u_content)
        print("Success: Asianet News test link saved to playlist.m3u")
    else:
        print("Failed: No stream link found on Asianet News page.")

except Exception as e:
    print(f"Error: {e}")
