import io
import logging
import re
import sys

from lxml import etree
import requests
import tornado.template


logger = logging.getLogger(__name__)


def main(pkgver):
    all_languages = {}

    mozilla_translations_page = requests.get(
        'https://pontoon.mozilla.org/projects/thunderbird/ajax/',
        headers={'X-Requested-With': 'XMLHttpRequest'},
    ).text

    parser = etree.HTMLParser()
    tree = etree.parse(io.StringIO(mozilla_translations_page), parser)
    for lang_td in tree.findall('.//td[@class="name"]'):
        lang_iso639 = lang_td.attrib['data-slug']
        lang_name = lang_td.find('.//a').text
        all_languages[lang_iso639] = lang_name
    all_languages['en-US'] = 'English'

    sha256sums_data = requests.get(
        f'https://ftp.mozilla.org/pub/thunderbird/releases/{pkgver}/SHA256SUMS'
    ).text

    sha256sums = []
    available_languages = []
    for line in sha256sums_data.strip().split('\n'):
        sha256sum, filename = line.split(maxsplit=1)
        if not filename.startswith('linux-x86_64/xpi/'):
            continue
        sha256sums.append(sha256sum)
        available_languages.append(
            filename[len('linux-x86_64/xpi/'):][:-len('.xpi')])
    available_languages = sorted(available_languages)

    logger.info('Collected languages: %s', available_languages)

    languages = {}
    for lang_iso639 in available_languages:
        languages[lang_iso639] = all_languages[lang_iso639]
    loader = tornado.template.Loader('.')
    content = loader.load('PKGBUILD.tmpl').generate(
        pkgver=pkgver,
        min_pkgver=re.sub(r'b\d', 'b0', pkgver),
        languages=languages,
        sha256sums=sha256sums,
    )

    with open('PKGBUILD', 'wb') as f:
        f.write(content)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main(sys.argv[1])
