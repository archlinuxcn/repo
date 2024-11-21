# Maintainer: Score_Under <seejay 11@gmail com>
options=(!strip)  # Don't strip libs because there aren't any

pkgname=hydrus
_pkgname=hydrus
pkgver=599
pkgrel=1
pkgdesc="Danbooru-like image tagging and searching system for the desktop"
arch=(any)
license=(custom)
url=http://hydrusnetwork.github.io/hydrus/
depends=(python python-opencv python-beautifulsoup4 python-yaml
         'python-lz4>=0.10.1' python-numpy python-twisted python-pillow
         python-pysocks python-psutil python-send2trash python-html5lib
         python-requests python-qtpy emoji-font python-mpv
         python-lxml python-urllib3 python-typing_extensions
         python-service-identity  # required by twisted for https hostname verification
         qt6-multimedia  # https://aur.archlinux.org/packages/hydrus#comment-914337
         qt6-svg  # https://aur.archlinux.org/packages/hydrus#comment-923550
         pyside6)
makedepends=(git)
optdepends=('ffmpeg: show duration and other information on video thumbnails'
            'miniupnpc: automatic port forwarding'
            'desktop-file-utils: to add Hydrus to your desktop environment menus'
            'hydrus-docs: offline documentation'
            'python-cbor2: cbor support in client-server communication'
            'python-chardet: detect text encoding more accurately'
            'python-cloudscraper: bypass cloudflare "checking your browser" challenges'
            'python-dateutil: improved fuzzy date search'
            'python-dateparser: date string to timestamp parser for predicate system'
            'python-psd-tools: handle PSD files and extract thumbnails'
            'python-pympler: debug menus to profile memory usage'
            # 'python-pyqt6-charts: display bandwidth usage charts'
            'python-cryptography: to generate certificates for accessing client API and server via HTTPS'
            'python-olefile: support legacy microsoft office file formats'
            'python-pyopenssl: to generate certificates for accessing client API and server via HTTPS'
            'qt6-webengine: to display PDF thumbnails'
            # 'python-pyparsing: currently unused'
            # 'speedcopy: may speed up file transfers'
            'swftools: to display SWF thumbnails')
conflicts=(hydrus-docs-dummy)
source=("${_pkgname}::git+https://github.com/hydrusnetwork/${_pkgname}.git#commit=528f4330f4fbf756604ad1ef6f8bd8292a4a7870"
        paths-in-opt.patch
        hydrus-client
        hydrus-server
        hydrus.desktop)
sha256sums=('SKIP'
            'f9f5a5927c7f2c016dbab3e4135a921918617ba393babd9b6a903ff5d0154cdd'
            '39d3404b75320be6a9e33dc256f4fc313c65fe11458e96bd5af6268c2f78eaf0'
            '5956d418d29fe19f54263acf47adce7c6d134d19ec65e2810d4517ce83529480'
            '9b8c2603a8040ae80152ff9a718ad3e8803fdc3029a939e3c0e932ea35ded923')

prepare() {
  cd "${srcdir}/${_pkgname}"
  patch -Np1 < ../paths-in-opt.patch
}

build() {
  cd "${srcdir}/${_pkgname}"

  msg 'Compiling .py files...'
  python -OO -m compileall -fq .
}

package() {
  cd "${srcdir}/${_pkgname}"

  # Create /opt/hydrus and copy hydrus files to there
  install -m755 -d "${pkgdir}/opt/hydrus"
  cp -r hydrus static hydrus_client.py hydrus_server.py "${pkgdir}/opt/hydrus/"

  # Remove unit tests
  rm -rf "${pkgdir}/opt/hydrus/hydrus/test" "${pkgdir}/opt/hydrus/static/testing"

  # Create and populate /opt/hydrus/bin
  install -d -m755 "${pkgdir}/opt/hydrus/bin"
  ln -s /usr/bin/upnpc "${pkgdir}/opt/hydrus/bin/upnpc_linux"
  ln -s /usr/bin/ffmpeg "${pkgdir}/opt/hydrus/bin/ffmpeg"
  ln -s /usr/bin/swfrender "${pkgdir}/opt/hydrus/bin/swfrender_linux"

  # Install hydrus-client and hydrus-server executables
  install -d -m755 "${pkgdir}/usr/bin"
  install -m755 ../hydrus-{client,server} "${pkgdir}/usr/bin/"

  # Install .desktop shortcut
  install -d -m755 "${pkgdir}/usr/share/applications"
  install -m644 ../hydrus.desktop "${pkgdir}/usr/share/applications/io.github.hydrusnetwork.hydrus.desktop"

  # Install license files
  install -d -m755 "${pkgdir}/usr/share/licenses/${_pkgname}"
  install -m644 COPYING "${pkgdir}/usr/share/licenses/${_pkgname}/"
  install -m644 license.txt "${pkgdir}/usr/share/licenses/${_pkgname}/"
}

# Tests (they don't pass!)
# makedepends+=(python-httmock)
# check() {
#   cd "${srcdir}/${_pkgname}"
#   python -m unittest discover -s hydrus/test -p 'Test*.py'
# }
