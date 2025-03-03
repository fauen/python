import feedparser as fp

def main() -> None:
    url = "https://www.svt.se/rss.xml"
    feed = fp.parse(url)

    print(f"Title: {feed.feed.title}")
    print(f"Description: {feed.feed.description}")
    print(f"Link: {feed.feed.link}")

    for entry in feed.entries:
        print(f"Title: {entry.title} ({entry.link})") 
        # print(f"Link: {entry.link}")
        # print(f"Published: {entry.published}")
        # print(f"Summary: {entry.summary}")
        # print("\n")

if __name__ == "__main__":
    main()
