import urllib.request

try:
    m3u_content = "#EXTM3U\n\n"
    
    # ബ്ലോക്ക് ആകാത്ത ഒറിജിനൽ ലോഗോകളും ഡയറക്ട് സ്ട്രീമും അടങ്ങിയ ലിസ്റ്റ്
    channels = [
        {"name": "Asianet HD", "url": "https://anettv.tulnit.workers.dev/starasianet1_live_https/index.m3u8", "logo": "https://raw.githubusercontent.com/manishb20/Tv-logos/main/asianet.png"},
        {"name": "Asianet Movies HD", "url": "https://anettv.tulnit.workers.dev/asianetmovies_live_https/index.m3u8", "logo": "https://raw.githubusercontent.com/manishb20/Tv-logos/main/asianetmovies.png"},
        {"name": "Asianet Plus", "url": "https://anettv.tulnit.workers.dev/asianetplus_live_https/index.m3u8", "logo": "https://raw.githubusercontent.com/manishb20/Tv-logos/main/asianetplus.png"},
        {"name": "Surya TV HD", "url": "https://anettv.tulnit.workers.dev/suryatv_live_https/index.m3u8", "logo": "https://raw.githubusercontent.com/manishb20/Tv-logos/main/suryatv.png"},
        {"name": "Surya Movies", "url": "https://anettv.tulnit.workers.dev/suryamovies_live_https/index.m3u8", "logo": "https://raw.githubusercontent.com/manishb20/Tv-logos/main/suryamovies.png"},
        {"name": "Surya Comedy", "url": "https://anettv.tulnit.workers.dev/suryacomedy_live_https/index.m3u8", "logo": "https://raw.githubusercontent.com/manishb20/Tv-logos/main/suryacomedy.png"},
        {"name": "Surya Music", "url": "https://anettv.tulnit.workers.dev/suryamusic_live_https/index.m3u8", "logo": "https://raw.githubusercontent.com/manishb20/Tv-logos/main/suryamusic.png"},
        {"name": "Kochu TV", "url": "https://anettv.tulnit.workers.dev/kochutv_live_https/index.m3u8", "logo": "https://raw.githubusercontent.com/manishb20/Tv-logos/main/kochutv.png"},
        {"name": "Mazhavil Manorama HD", "url": "https://anettv.tulnit.workers.dev/mmtv_live_https/index.m3u8", "logo": "https://raw.githubusercontent.com/manishb20/Tv-logos/main/mazhavilmanorama.png"},
        {"name": "Flowers TV HD", "url": "https://anettv.tulnit.workers.dev/flowerstv_live_https/index.m3u8", "logo": "https://raw.githubusercontent.com/manishb20/Tv-logos/main/flowerstv.png"},
        {"name": "Asianet News HD", "url": "https://anettv.tulnit.workers.dev/asianetnews_live_https/index.m3u8", "logo": "https://raw.githubusercontent.com/manishb20/Tv-logos/main/asianetnews.png"},
        {"name": "24 News HD", "url": "https://anettv.tulnit.workers.dev/twentytofournews_live_https/index.m3u8", "logo": "https://raw.githubusercontent.com/manishb20/Tv-logos/main/24news.png"},
        {"name": "Mathrubhumi News", "url": "https://anettv.tulnit.workers.dev/mbnews_live_https/index.m3u8", "logo": "https://raw.githubusercontent.com/manishb20/Tv-logos/main/mathrubhuminews.png"},
        {"name": "News18 Kerala", "url": "https://anettv.tulnit.workers.dev/news18kerala_live_https/index.m3u8", "logo": "https://raw.githubusercontent.com/manishb20/Tv-logos/main/news18kerala.png"},
        {"name": "MediaOne", "url": "https://anettv.tulnit.workers.dev/mediaone_live_https/index.m3u8", "logo": "https://raw.githubusercontent.com/manishb20/Tv-logos/main/mediaone.png"},
        {"name": "Janam TV", "url": "https://anettv.tulnit.workers.dev/janamtv_live_https/index.m3u8", "logo": "https://raw.githubusercontent.com/manishb20/Tv-logos/main/janamtv.png"}
    ]
    
    for ch in channels:
        m3u_content += f'#EXTINF:-1 tvg-logo="{ch["logo"]}" group-title="Malayalam", {ch["name"]}\n'
        m3u_content += "#EXTVLCOPT:http-user-agent=AppleCoreMedia/1.0.0.16G77 (iPhone; U; CPU iPhone OS 12_4 like Mac OS X; en_us)\n"
        m3u_content += "#EXTVLCOPT:http-referrer=https://tulnit.com/\n"
        m3u_content += f"{ch['url']}|User-Agent=AppleCoreMedia/1.0.0.16G77 (iPhone; U; CPU iPhone OS 12_4 like Mac OS X; en_us)&Referer=https://tulnit.com/\n\n"
        
    with open("playlist.m3u", "w", encoding="utf-8") as f:
        f.write(m3u_content)
    print("Success: Final Verified Malayalam Playlist Built Perfectly!")

except Exception as e:
    print(f"Error: {e}")
