import urllib.request
import re

# മലയാളം കാറ്റഗറി പേജ്
url = "https://tulnit.com/channel/malayalam/" 

try:
    # വെബ്‌സൈറ്റ് ഓപ്പൺ ചെയ്യുന്നു
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    
    # പേജിലുള്ള എല്ലാ ചാനലുകളുടെയും ലിങ്കുകൾ തനിയെ കണ്ടുപിടിക്കുന്നു
    channels = re.findall(r'href="(https?://tulnit\.com/live/[^"\']+)"', html)
    # ഒരേ ലിങ്കുകൾ ആവർത്തിച്ചു വരാതിരിക്കാൻ ഫിൽട്ടർ ചെയ്യുന്നു
    channels = list(set(channels))
    
    m3u_content = "#EXTM3U\n\n"
    
    if channels:
        for ch_link in channels:
            # ചാനലിന്റെ പേര് ലിങ്കിൽ നിന്ന് വേർതിരിച്ചെടുക്കുന്നു
            ch_name = ch_link.split("/")[-2].replace("-", " ").title()
            
            # ഓരോ ചാനൽ പേജിലും കയറി അതിന്റെ യഥാർത്ഥ .m3u8 അല്ലെങ്കിൽ .mpd ലിങ്ക് സ്ക്രാപ്പ് ചെയ്യുന്നു
            try:
                ch_req = urllib.request.Request(ch_link, headers={'User-Agent': 'Mozilla/5.0'})
                ch_html = urllib.request.urlopen(ch_req).read().decode('utf-8')
                
                # വീഡിയോ സ്ട്രീം ലിങ്കുകൾ കണ്ടെത്തുന്നു
                stream_links = re.findall(r'(https?://[^\s"\']+\.(?:m3u8|mpd)[^\s"\']*)', ch_html)
                
                if stream_links:
                    live_url = stream_links[0]
                    # തെറ്റായ സ്പെല്ലിംഗ് ഉണ്ടെങ്കിൽ തിരുത്തുന്നു
                    live_url = live_url.replace('/jeo/', '/jio/')
                    
                    # M3U ഫോർമാറ്റിലേക്ക് മാറ്റുന്നു ഒപ്പം Referer ലോക്കും ചേർക്കുന്നു
                    m3u_content += f'#EXTINF:-1, {ch_name}\n#EXTVLCOPT:http-user-agent=Mozilla/5.0\n#EXTVLCOPT:http-referrer=https://tulnit.com/\n{live_url}|Referer=https://tulnit.com/\n\n'
            except:
                continue
                
        # പ്ലേലിസ്റ്റ് ഫയൽ ഉണ്ടാക്കി സേവ് ചെയ്യുന്നു
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write(m3u_content)
        print("Success: Playlist created with active channels!")
    else:
        print("No channels found on the page.")
except Exception as e:
    print(f"Error: {e}")
