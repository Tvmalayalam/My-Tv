import requests
import re
from urllib.parse import urljoin

# മെയിൻ മലയാളം പേജ്
main_url = "https://tulnit.com/channel/malayalam/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://tulnit.com/',
    'Connection': 'keep-alive'
}

try:
    # സെഷൻ ആരംഭിച്ച് കുക്കികൾ തനിയെ മാനേജ് ചെയ്യുന്നു
    session = requests.Session()
    response = session.get(main_url, headers=headers, timeout=15)
    html = response.text
    
    # പേജിലുള്ള എല്ലാ ചാനൽ ലിങ്കുകളും തനിയെ കണ്ടുപിടിക്കുന്നു (Detecting links)
    raw_channels = re.findall(r'href=["\'](https?://tulnit\.com/live/[^"\'/]+)/?["\']', html)
    channels = list(set(raw_channels)) # ഡ്യൂപ്ലിക്കേറ്റ് ഒഴിവാക്കുന്നു
    
    m3u_content = "#EXTM3U\n\n"
    detected_count = 0
    
    if channels:
        print(f"Found {len(channels)} channels. Scanning live streams...")
        
        for ch_link in channels:
            # ലിങ്കിൽ നിന്ന് ചാനലിന്റെ പേര് തനിയെ ഉണ്ടാക്കുന്നു
            ch_id = ch_link.split("/")[-1] if ch_link.split("/")[-1] else ch_link.split("/")[-2]
            ch_name = ch_id.replace("-", " ").title()
            
            try:
                # ഓരോ ചാനലിന്റെയും ഉള്ളിലേക്ക് കയറുന്നു
                ch_response = session.get(ch_link, headers=headers, timeout=10)
                ch_html = ch_response.text
                
                # ആ പേജിന്റെ ഉള്ളിലുള്ള യഥാർത്ഥ പ്ലേബാക്ക് ലിങ്ക് കണ്ടെത്തുന്നു (.m3u8 അല്ലെങ്കിൽ .mpd)
                stream_links = re.findall(r'["\'](https?://[^\s"\'&]+\.(?:m3u8|mpd)[^\s"\'&]*)["\']', ch_html)
                
                if not stream_links:
                    stream_links = re.findall(r'(https?://[^\s"\']+\.(?:m3u8|mpd)[^\s"\']*)', ch_html)
                
                if stream_links:
                    live_url = stream_links[0]
                    
                    # ജിയോ സെർവർ എറർ ഉണ്ടെങ്കിൽ തിരുത്തുന്നു
                    if '/jeo/' in live_url:
                        live_url = live_url.replace('/jeo/', '/jio/')
                    
                    # ഒഫീഷ്യൽ ലോഗോ ലിങ്ക് തനിയെ ഉണ്ടാക്കുന്നു
                    logo_url = f"https://raw.githubusercontent.com/manishb20/Tv-logos/main/{ch_id.replace('-','')}.png"
                    
                    m3u_content += f'#EXTINF:-1 tvg-logo="{logo_url}" group-title="Malayalam", {ch_name}\n'
                    m3u_content += "#EXTVLCOPT:http-user-agent=AppleCoreMedia/1.0.0.16G77 (iPhone; U; CPU iPhone OS 12_4 like Mac OS X; en_us)\n"
                    m3u_content += f"#EXTVLCOPT:http-referrer={ch_link}\n"
                    m3u_content += f"{live_url}|User-Agent=AppleCoreMedia/1.0.0.16G77 (iPhone; U; CPU iPhone OS 12_4 like Mac OS X; en_us)&Referer={ch_link}\n\n"
                    detected_count += 1
            except:
                continue
                
        # കണ്ടെത്തിയ ചാനലുകൾ ഫയലിലേക്ക് മാറ്റുന്നു
        if detected_count > 0:
            with open("playlist.m3u", "w", encoding="utf-8") as f:
                f.write(m3u_content)
            print(f"Success: {detected_count} Malayalam channels detected and saved!")
        else:
            print("Security Blocked: Could not read stream urls.")
            
    else:
        print("Security Blocked: No channel links detected on the page.")

except Exception as e:
    print(f"Error: {e}")
