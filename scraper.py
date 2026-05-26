import requests
import re

# മെയിൻ മലയാളം പേജ്
main_url = "https://tulnit.com/channel/malayalam/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://tulnit.com/',
    'Connection': 'keep-alive'
}

try:
    session = requests.Session()
    response = session.get(main_url, headers=headers, timeout=15)
    html = response.text
    
    # സൈറ്റിലുള്ള എല്ലാ ചാനൽ ലിങ്കുകളും തനിയെ ഡിറ്റക്റ്റ് ചെയ്യുന്നു
    raw_channels = re.findall(r'href=["\'](https?://tulnit\.com/live/[^"\'/]+)/?["\']', html)
    channels = list(set(raw_channels))
    
    m3u_content = "#EXTM3U\n\n"
    detected_count = 0
    
    if channels:
        for ch_link in channels:
            ch_id = ch_link.split("/")[-1] if ch_link.split("/")[-1] else ch_link.split("/")[-2]
            ch_name = ch_id.replace("-", " ").title()
            
            try:
                ch_response = session.get(ch_link, headers=headers, timeout=10)
                ch_html = ch_response.text
                
                # തുൽനിത് സൈറ്റിന്റെ പ്ലെയറിലുള്ള യഥാർത്ഥ വീഡിയോ സ്ട്രീം ലിങ്ക് കണ്ടെത്തുന്നു
                stream_links = re.findall(r'["\'](https?://[^\s"\'&]+\.(?:m3u8|mpd)[^\s"\'&]*)["\']', ch_html)
                if not stream_links:
                    stream_links = re.findall(r'(https?://[^\s"\']+\.(?:m3u8|mpd)[^\s"\']*)', ch_html)
                
                if stream_links:
                    live_url = stream_links[0]
                    
                    # ⚠️ തുൽനിത് ഇപ്പോൾ ഉപയോഗിക്കുന്ന ഏറ്റവും പുതിയ ഒറിജിനൽ ലൈവ് സെർവർ ഡൊമെയ്ൻ ഇതാണ്
                    # പഴയ 'anettv.tulnit.workers.dev' മാറ്റി പുതിയ ഒഫീഷ്യൽ സെർവറിലേക്ക് തിരിച്ചുവിടുന്നു
                    if 'tulnit.workers.dev' in live_url or 'keralive.workers.dev' in live_url:
                        # ലിങ്കിന്റെ തുടക്കം tulnit-ന്റെ സ്വന്തം മെയിൻ ലൈവ് ഗേറ്റ്‌വേയിലേക്ക് മാറ്റുന്നു
                        live_url = re.sub(r'https?://[^\s/]+/v1/master/[^\s/]+/', 'https://play.tulnit.com/live/', live_url)
                    elif '/jeo/' in live_url:
                        live_url = live_url.replace('/jeo/', '/jio/')
                    
                    # ലോഗോകൾ കൃത്യമായി വരാൻ ഗിറ്റ്ഹബ്ബ് ലിങ്ക് നൽകുന്നു
                    logo_url = f"https://raw.githubusercontent.com/manishb20/Tv-logos/main/{ch_id.replace('-','')}.png"
                    
                    m3u_content += f'#EXTINF:-1 tvg-logo="{logo_url}" group-title="Malayalam", {ch_name}\n'
                    m3u_content += "#EXTVLCOPT:http-user-agent=AppleCoreMedia/1.0.0.16G77 (iPhone; U; CPU iPhone OS 12_4 like Mac OS X; en_us)\n"
                    m3u_content += "#EXTVLCOPT:http-referrer=https://tulnit.com/\n"
                    m3u_content += "#EXTVLCOPT:http-origin=https://tulnit.com\n"
                    m3u_content += f"{live_url}|User-Agent=AppleCoreMedia/1.0.0.16G77 (iPhone; U; CPU iPhone OS 12_4 like Mac OS X; en_us)&Referer=https://tulnit.com/&Origin=https://tulnit.com\n\n"
                    detected_count += 1
            except:
                continue
                
        if detected_count > 0:
            with open("playlist.m3u", "w", encoding="utf-8") as f:
                f.write(m3u_content)
            print(f"Success: {detected_count} Channels Updated with latest Tulnit server!")
        else:
            print("No active streams found.")
except Exception as e:
    print(f"Error: {e}")
