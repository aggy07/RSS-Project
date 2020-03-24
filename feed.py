# python-feedreader
# =======================================================
# import feedparser
# f = feedparser.parse("https://cloudblog.withgoogle.com/rss/")

# print(f)

# for entry in f.entries:
# 	print(entry.title)


# print(dir(f))
# print(f.keys())
# print(f['feed']['title'])
# print("+++++++++++++++++++++++++++++++++++++++++++++++++")
# print(f.entries[0]['title'])
# print(f.entries[0]['href'])
# =============================================================

import feedparser


def parse(url):
	return feedparser.parse(url)

def get_source(parsed):
	feed = parsed['feed']
	return {
	'title': feed['title'],
	'link': feed['link'],
	'subtitle': feed['subtitle']}

def get_articles(parsed):
	articles = []
	entries = parsed['entries']
	for entry in entries:
		articles.append({
			'title': entry['title'],
			'id': entry['id'],
			'summary': entry['content'][0]['value']
			})
	return articles









