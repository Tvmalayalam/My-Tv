try:
    # പുതിയ ലൈവ് ടോക്കൺ അടങ്ങിയ 100% വർക്കിംഗ് ലിങ്കുകൾ
    m3u_content = (
        "#EXTM3U\n\n"
        '#EXTINF:-1 tvg-logo="https://example.com/asianet.png", Asianet HD\n'
        "#EXTVLCOPT:http-user-agent=Mozilla/5.0\n"
        "#EXTVLCOPT:http-referrer=https://anet.keralive.workers.dev/\n"
        "#EXTVLCOPT:http-origin=https://anet.keralive.workers.dev\n"
        "https://anet.keralive.workers.dev/v1/master/be381fcfb351ee2b450537f5bbf1e89324083a30/starasianet1_live_https/index.m3u8\n\n"
        
        '#EXTINF:-1 tvg-logo="https://example.com/asianetmovies.png", Asianet Movies HD\n'
        "#EXTVLCOPT:http-user-agent=Mozilla/5.0\n"
        "#EXTVLCOPT:http-referrer=https://anet.keralive.workers.dev/\n"
        "#EXTVLCOPT:http-origin=https://anet.keralive.workers.dev\n"
        "https://anet.keralive.workers.dev/v1/master/be381fcfb351ee2b450537f5bbf1e89324083a30/asianetmovies_live_https/index.m3u8\n"
    )
    
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)
    print("Success: Live Playlist Updated Perfectly!")

except Exception as e:
    print(f"Error: {e}")
