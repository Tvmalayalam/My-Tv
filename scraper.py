try:
    # യാതൊരുവിധ തടസ്സങ്ങളുമില്ലാത്ത ഡയറക്ട് ഒഫീഷ്യൽ ചാനൽ ലിങ്കുകൾ
    m3u_content = (
        "#EXTM3U\n\n"
        '#EXTINF:-1 tvg-logo="https://example.com/asianet.png", Asianet HD\n'
        "#EXTVLCOPT:http-user-agent=Mozilla/5.0\n"
        "#EXTVLCOPT:http-referrer=https://anet.keralive.workers.dev/\n"
        "#EXTVLCOPT:http-origin=https://anet.keralive.workers.dev\n"
        "https://anet.keralive.workers.dev/v1/master/a0d007312bfd99c47f76b77ae26b1ccdaae76cb1/starasianet1_live_https/index.m3u8\n\n"
        
        '#EXTINF:-1 tvg-logo="https://example.com/asianetmovies.png", Asianet Movies HD\n'
        "#EXTVLCOPT:http-user-agent=Mozilla/5.0\n"
        "#EXTVLCOPT:http-referrer=https://anet.keralive.workers.dev/\n"
        "#EXTVLCOPT:http-origin=https://anet.keralive.workers.dev\n"
        "https://anet.keralive.workers.dev/v1/master/a0d007312bfd99c47f76b77ae26b1ccdaae76cb1/asianetmovies_live_https/index.m3u8\n"
    )
    
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)
    print("Success: Backup Playlist Created Perfectly!")

except Exception as e:
    print(f"Error: {e}")
