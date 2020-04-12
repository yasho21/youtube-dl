from __future__ import unicode_literals
from .common import InfoExtractor

class koreusIE(InfoExtractor):
    _VALID_URL = r'https:\/\/www\.koreus\.com/video/(?P<id>\S+)'

    _TESTS = {

    }

    def _real_extract(self, url):
        video_id = self._match_id(url)

        webpage = self._download_webpage(
            url, video_id
        )

        title = self._html_search_regex(r'<title>(.+?)</title>', webpage, 'title')

        download_url = self._html_search_regex(

            r'<source src="(https://embed\.koreus\.com/[0-9]+/[0-9]+/[a-z-]+\.mp4)" type="video/mp4"',
              #https://embed.koreus.com/00071/201905/technique-emballer-velo-pliant.mp4
            webpage, "download_url"
            )

        return {
        'id': video_id,
        'url': download_url,
        'title': title

            }






   
