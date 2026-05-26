import urllib.request
import re

# സുരക്ഷാ ലോക്ക് മറികടക്കാൻ ഗൂഗിൾ ട്രാൻസ്ലേറ്റ് വഴിയുള്ള ഒരു പ്രത്യേക ട്രിക്ക്
url = "https://translate.google.com/translate?sl=en&tl=ml&u=https://tulnit.com/channel/malayalam/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

try:
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req).read().decode('utf-8')
    
    # മലയാളം ചാനലുകളുടെ പേജുകൾ കണ്ടുപിടിക്കുന്നു
    channels = re.findall(r'tulnit\.com/live/([^"\'&]+)', html)
    channels = list(set(channels))
    
    m3u_content = "#EXTM3U\n\n"
    
    if channels:
        for ch in channels:
            # ചാനലിന്റെ പേര് ഭംഗിയാക്കുന്നു
            ch_name = ch.replace("-", " ").title()
            ch_link = f"https://tulnit.com/live/{ch}/"
            
            try:
                # ഓരോ ചാനൽ പേജിലും കയറുന്നു
                ch_url = f"https://translate.google.com/translate?sl=en&tl=ml&u={ch_link}"
                ch_req = urllib.request.Request(ch_url, headers=headers)
                ch_html = urllib.request.urlopen(ch_req).read().decode('utf-8')
                
                # ആ പേജിലെ യഥാർത്ഥ ലൈവ് വീഡിയോ ലിങ്ക് (.m3u8 അല്ലെങ്കിൽ .mpd) കണ്ടെത്തുന്നു
                stream_links = re.findall(r'(https?://[^\s"\'&]+\.(?:m3u8|mpd)[^\s"\'&]*)', ch_html)
                
                if stream_links:
                    live_url = stream_links[0]
                    live_url = live_url.replace('/jeo/', '/jio/')
                    
                    # പ്ലേലിസ്റ്റിലേക്ക് ചാനൽ വിവരങ്ങളും ആവശ്യമായ Referer-ഉം ചേർക്കുന്നു
                    m3u_content += f'#EXTINF:-1, {ch_name}\n#EXTVLCOPT:http-user-agent=Mozilla/5.0\n#EXTVLCOPT:http-referrer=https://tulnit.com/\n{live_url}|Referer=https://tulnit.com/\n\n'
            except:
                continue
                
        with open("playlist.m3u", "w", encoding="utf-8") as f:
            f.write(m3u_content)
        print("Success: All Malayalam Channels Added!")
    else:
        print("Failed to bypass security, trying direct method.")
except Exception as e:
    print(f"Error: {e}")
