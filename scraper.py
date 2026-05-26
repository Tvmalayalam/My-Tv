import urllib.request
import re
import json

# സൈറ്റിന്റെ സെക്യൂരിറ്റി ബൈപാസ് ചെയ്യാൻ ഡയറക്ട് കാറ്റഗറി പേജ് തന്നെയാണ് ഉപയോഗിക്കുന്നത്
url = "https://tulnit.com/channel/malayalam/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://tulnit.com/',
    'Connection': 'keep-alive'
}

try:
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req).read().decode('utf-8')
    
    # പേജിലുള്ള എല്ലാ ചാനലുകളുടെയും പേര് അടങ്ങിയ ലിങ്കുകൾ കൃത്യമായി എടുക്കുന്നു
    channels = re.findall(r'href="https://tulnit\.com/live/([^"\'/]+)/?"', html)
    channels = list(set(channels))
    
    m3u_content = "#EXTM3U\n\n"
    
    if channels:
        for ch in channels:
            ch_name = ch.replace("-", " ").title()
            ch_link = f"https://tulnit.com/live/{ch}/"
            
            try:
                # ഓരോ ചാനൽ പേജിന്റെയും ഉള്ളിലേക്ക് കയറി ലിങ്ക് സ്ക്രാപ്പ് ചെയ്യുന്നു
                ch_req = urllib.request.Request(ch_link, headers=headers)
                ch_html = urllib.request.urlopen(ch_req).read().decode('utf-8')
                
                # വീഡിയോ പ്ലെയറിന്റെ ഉള്ളിലുള്ള യഥാർത്ഥ .m3u8 അല്ലെങ്കിൽ .mpd ലിങ്ക് കണ്ടെത്തുന്നു
                stream_links = re.findall(r'["\'](https?://[^\s"\'&]+\.(?:m3u8|mpd)[^\s"\'&]*)["\']', ch_html)
                
                if not stream_links:
                    # മറ്റൊരു ഫോർമാറ്റിൽ ആണെങ്കിൽ അതും കണ്ടെത്താൻ
                    stream_links = re.findall(r'(https?://[^\s"\']+\.(?:m3u8|mpd)[^\s"\']*)', ch_html)
                
                if stream_links:
                    live_url = stream_links[0]
                    # ജീയോ ലിങ്ക് ഫോർമാറ്റ് കൃത്യമാക്കുന്നു
                    if '/jeo/' in live_url:
                        live_url = live_url.replace('/jeo/', '/jio/')
                    
                    m3u_content += f'#EXTINF:-1, {ch_name}\n#EXTVLCOPT:http-user-agent=Mozilla/5.0\n#EXTVLCOPT:http-referrer=https://tulnit.com/\n{live_url}|Referer=https://tulnit.com/\n\n'
            except:
                continue
        
        # ഫയലിലേക്ക് ലിസ്റ്റ് എഴുതുന്നു
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write(m3u_content)
        print("Success: All Malayalam Channels Scraped Successfully!")
        
    else:
        # ഒരു കാരണവശാലും ഫയൽ കാലിയാകാതിരിക്കാൻ ബാക്കപ്പ് ലിങ്ക് എപ്പോഴും നിലനിർത്തുന്നു
        print("No channels found, adding main channels as fallback.")
        m3u_content += (
            '#EXTINF:-1, Asianet HD\n#EXTVLCOPT:http-user-agent=Mozilla/5.0\n#EXTVLCOPT:http-referrer=https://tulnit.com/\nhttps://anet.keralive.workers.dev/v1/master/be381fcfb351ee2b450537f5bbf1e89324083a30/starasianet1_live_https/index.m3u8|Referer=https://tulnit.com/\n\n'
            '#EXTINF:-1, Asianet Movies HD\n#EXTVLCOPT:http-user-agent=Mozilla/5.0\n#EXTVLCOPT:http-referrer=https://tulnit.com/\nhttps://anet.keralive.workers.dev/v1/master/be381fcfb351ee2b450537f5bbf1e89324083a30/asianetmovies_live_https/index.m3u8\n'
        )
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write(m3u_content)

except Exception as e:
    print(f"Error: {e}")
