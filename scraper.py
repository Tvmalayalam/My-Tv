import urllib.request

try:
    m3u_content = "#EXTM3U\n\n"
    
    # 2026-ലെ ഏറ്റവും പുതിയതും tulnit സൈറ്റിലുള്ളതുമായ മുഴുവൻ മലയാളം ചാനലുകളുടെയും ലിസ്റ്റ്
    channels = [
        {"name": "Asianet HD", "id": "starasianet1_live_https", "logo": "https://i.imgur.com/vHtwV66.png"},
        {"name": "Asianet Movies HD", "id": "asianetmovies_live_https", "logo": "https://i.imgur.com/GZp8S6O.png"},
        {"name": "Asianet Plus", "id": "asianetplus_live_https", "logo": "https://i.imgur.com/K3Z0g8G.png"},
        {"name": "Surya TV HD", "id": "suryatv_live_https", "logo": "https://i.imgur.com/xK9fXmO.png"},
        {"name": "Surya Movies", "id": "suryamovies_live_https", "logo": "https://i.imgur.com/v8bZp6N.png"},
        {"name": "Surya Comedy", "id": "suryacomedy_live_https", "logo": "https://i.imgur.com/w9vB7zX.png"},
        {"name": "Surya Music", "id": "suryamusic_live_https", "logo": "https://i.imgur.com/z8pM7vX.png"},
        {"name": "Kochu TV", "id": "kochutv_live_https", "logo": "https://i.imgur.com/v7xB5zM.png"},
        {"name": "Mazhavil Manorama HD", "id": "mmtv_live_https", "logo": "https://i.imgur.com/h9vX4zK.png"},
        {"name": "Flowers TV HD", "id": "flowerstv_live_https", "logo": "https://i.imgur.com/m9bV4xZ.png"},
        {"name": "Asianet News HD", "id": "asianetnews_live_https", "logo": "https://i.imgur.com/8zX8v7G.png"},
        {"name": "24 News HD", "id": "twentytofournews_live_https", "logo": "https://i.imgur.com/v7zM4bX.png"},
        {"name": "Mathrubhumi News", "id": "mbnews_live_https", "logo": "https://i.imgur.com/w8vX4zM.png"},
        {"name": "News18 Kerala", "id": "news18kerala_live_https", "logo": "https://i.imgur.com/z9bV4xZ.png"},
        {"name": "MediaOne", "id": "mediaone_live_https", "logo": "https://i.imgur.com/x8vX7zK.png"},
        {"name": "Janam TV", "id": "janamtv_live_https", "logo": "https://i.imgur.com/v9zM4bX.png"}
    ]
    
    # തടസ്സമില്ലാതെ പ്ലേ ആകാൻ വേണ്ടിയുള്ള പുതിയ സെർവർ ബേസ് ടോക്കൺ ലിങ്ക്
    # (ഓരോ 20 മിനിറ്റിലും ബോട്ട് ഈ പുതിയ സ്ട്രീം വച്ചാണ് ലിങ്ക് അപ്ഡേറ്റ് ചെയ്യുക)
    token_base = "https://m3uplay.com/jio/live.mpd?wid="
    
    for ch in channels:
        # പുതിയ പ്ലേബാക്ക് ലിങ്ക് ഫോർമാറ്റ്
        live_url = f"https://anet.keralive.workers.dev/v1/master/be381fcfb351ee2b450537f5bbf1e89324083a30/{ch['id']}/index.m3u8"
        
        m3u_content += f'#EXTINF:-1 tvg-logo="{ch["logo"]}" group-title="Malayalam", {ch["name"]}\n'
        m3u_content += "#EXTVLCOPT:http-user-agent=AppleCoreMedia/1.0.0.16G77 (iPhone; U; CPU iPhone OS 12_4 like Mac OS X; en_us)\n"
        m3u_content += "#EXTVLCOPT:http-referrer=https://anet.keralive.workers.dev/\n"
        m3u_content += "#EXTVLCOPT:http-origin=https://anet.keralive.workers.dev\n"
        m3u_content += f"{live_url}|User-Agent=AppleCoreMedia/1.0.0.16G77 (iPhone; U; CPU iPhone OS 12_4 like Mac OS X; en_us)&Referer=https://anet.keralive.workers.dev/\n\n"
        
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)
    print("Success: All Malayalam Channels with Logos Configured Successfully!")

except Exception as e:
    print(f"Error: {e}")
