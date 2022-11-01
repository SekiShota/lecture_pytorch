"""
画像データをキーワード検索で効率的に収集する方法（Python「icrawler」のBing検索）
https://atmarkit.itmedia.co.jp/ait/articles/2010/28/news018.html
"""

from icrawler.builtin import BingImageCrawler

def scraping(save_dir, keyword, n):
    bing_crawler=BingImageCrawler(
        downloader_threads=4,
        storage={'root_dir':save_dir}
    )
    bing_crawler.crawl(
        keyword=keyword,
        max_num=n
    )

#齊藤京子：kyonko
scraping(save_dir="./images/kyonko/", keyword="齊藤京子", n=400)
#加藤史帆：katoshi
scraping(save_dir="./images/katoshi/", keyword="加藤史帆", n=400)
#高本彩花：otake
scraping(save_dir="./images/otake/", keyword="高本彩花", n=400)
#守屋麗奈：rena
scraping(save_dir="./images/rena/", keyword="守屋麗奈", n=400)
#田村保乃：hono
scraping(save_dir="./images/hono/", keyword="田村保乃", n=400)

