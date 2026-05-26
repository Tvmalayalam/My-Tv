try:
    m3u_content = "#EXTM3U\n\n"
    
    # പ്രോബ്ലം കണ്ടുപിടിക്കാനുള്ള ഏഷ്യാനെറ്റ് ന്യൂസ് ഡയറക്ട് ടെസ്റ്റ് ലിങ്ക്
    m3u_content += '#EXTINF:-1 tvg-logo="https://raw.githubusercontent.com/manishb20/Tv-logos/main/asianetnews.png" group-title="Test", Asianet News\n'
    m3u_content += "#EXTVLCOPT:http-user-agent=AppleCoreMedia/1.0.0.16G77 (iPhone; U; CPU iPhone OS 12_4 like Mac OS X; en_us)\n"
    m3u_content += "#EXTVLCOPT:http-referrer=https://tulnit.com/\n"
    m3u_content += "https://play.tulnit.com/live/starasianet1_live_https/index.m3u8|User-Agent=AppleCoreMedia/1.0.0.16G77 (iPhone; U; CPU iPhone OS 12_4 like Mac OS X; en_us)&Referer=https://tulnit.com/\n\n"
    
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)
    print("Success: Test playlist generated with Asianet News!")
except Exception as e:
    print(f"Error: {e}")
