import urllib.request
import re

url = "https://tulnit.com/channel/malayalam/" 

# വെബ്‌സൈറ്റിന് ഇതൊരു യഥാർത്ഥ ബ്രൗസർ ആണെന്ന് തോന്നിപ്പിക്കാനുള്ള അപ്‌ഡേറ്റഡ് സെറ്റിങ്സ്
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
}

try:
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req).read().decode('utf-8')
    
    # ചാനൽ പേജുകളുടെ ലിങ്ക് കണ്ടെത്തുന്നു
    channels = re.findall(r'href="(https?://tulnit\.com/live/[^"\']+)"', html)
    channels = list(set(channels))
    
    m3u_content = "#EXTM3U\n\n"
    
    if channels:
        for ch_link in channels:
            ch_name = ch_link.split("/")[-2].replace("-", " ").title()
            
            try:
                ch_req = urllib.request.Request(ch_link, headers=headers)
                ch_html = urllib.request.urlopen(ch_req).read().decode('utf-8')
                
                # യഥാർത്ഥ വീഡിയോ സ്ട്രീം ലിങ്ക് കണ്ടെത്തുന്നു
                stream_links = re.findall(r'(https?://[^\s"\']+\.(?:m3u8|mpd)[^\s"\']*)', ch_html)
                
                if stream_links:
                    live_url = stream_links[0]
                    live_url = live_url.replace('/jeo/', '/jio/')
                    
                    m3u_content += f'#EXTINF:-1, {ch_name}\n#EXTVLCOPT:http-user-agent=Mozilla/5.0\n#EXTVLCOPT:http-referrer=https://tulnit.com/\n{live_url}|Referer=https://tulnit.com/\n\n'
            except:
                continue
                
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write(m3u_content)
        print("Success: Playlist created!")
    else:
        # ചാനലുകൾ ഒന്നും കിട്ടിയില്ലെങ്കിൽ താൽക്കാലികമായി ഒരു ടെസ്റ്റ് ചാനൽ എങ്കിലും ഫയലിൽ എഴുതുന്നു
        print("No channels found, creating backup link.")
        m3u_content += f'#EXTINF:-1, Asianet HD (Backup)\n#EXTVLCOPT:http-user-agent=Mozilla/5.0\n#EXTVLCOPT:http-referrer=https://tulnit.com/\nhttps://anet.keralive.workers.dev/v1/master/a0d007312bfd99c47f76b77ae26b1ccdaae76cb1/starasianet1_live_https/index.m3u8|Referer=https://tulnit.com/\n\n'
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write(m3u_content)

except Exception as e:
    print(f"Error: {e}")
