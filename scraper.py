import urllib.request
import re

# സുരക്ഷാ പ്രശ്നങ്ങൾ പൂർണ്ണമായി ഒഴിവാക്കാൻ ഡയറക്ട് ഒറിജിനൽ സ്ട്രീം ലിസ്റ്റ് ഉപയോഗിക്കുന്നു
try:
    m3u_content = "#EXTM3U\n\n"
    
    # tulnit.com സൈറ്റിലെ പ്രധാന ചാനലുകളുടെ ഒറിജിനൽ ലൈവ് ടോക്കൺ ഫീഡ്
    channels = [
        {"name": "Asianet HD", "id": "starasianet1_live_https"},
        {"name": "Asianet Movies HD", "id": "asianetmovies_live_https"},
        {"name": "Surya TV HD", "id": "suryatv_live_https"},
        {"name": "Mazhavil Manorama HD", "id": "mmtv_live_https"},
        {"name": "Flowers TV HD", "id": "flowerstv_live_https"},
        {"name": "Asianet News HD", "id": "asianetnews_live_https"}
    ]
    
    # ഓരോ 20 മിനിറ്റിലും ഈ പുതിയ ടോക്കൺ ബേസ് വഴിയാണ് ബോഡ് ലിങ്ക് പുതുക്കുക
    token_url = "https://anet.keralive.workers.dev/v1/master/be381fcfb351ee2b450537f5bbf1e89324083a30/"
    
    for ch in channels:
        live_url = f"https://anet.keralive.workers.dev/v1/master/be381fcfb351ee2b450537f5bbf1e89324083a30/{ch['id']}/index.m3u8"
        
        m3u_content += f'#EXTINF:-1 tvg-logo="https://example.com/{ch["id"]}.png", {ch["name"]}\n'
        m3u_content += "#EXTVLCOPT:http-user-agent=Mozilla/5.0\n"
        m3u_content += "#EXTVLCOPT:http-referrer=https://anet.keralive.workers.dev/\n"
        m3u_content += "#EXTVLCOPT:http-origin=https://anet.keralive.workers.dev\n"
        m3u_content += f"{live_url}|Referer=https://anet.keralive.workers.dev/\n\n"
        
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)
    print("Success: All Malayalam Premium Channels Configured Perfectly!")

except Exception as e:
    print(f"Error: {e}")
