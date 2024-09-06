# Maintainer: katt <magunasu.b97@gmail.com>
# Contributor: LLL2yu <lll2yu@protonmail.com>

pkgname=gallery-dl
pkgver=1.27.4
pkgrel=1
pkgdesc='Command-line program to download image-galleries and collections from several image hosting sites'
arch=(any)
url=https://github.com/mikf/gallery-dl
license=(GPL-2.0-or-later)
depends=(python python-requests)
makedepends=(python-build python-installer python-setuptools python-wheel git)
checkdepends=(yt-dlp)
optdepends=('ffmpeg: Pixiv Ugoira conversion'
            'yt-dlp: Video downloads'
            'youtube-dl: Video downloads'
            'python-pysocks: SOCKS proxy support'
            'python-brotli: Brotli compression support'
            'python-brotlicffi: Brotli compression support'
            'python-yaml: YAML configuration file support'
            'python-toml: TOML configuration file support for Python<3.11'
            'python-secretstorage: GNOME keyring passwords for --cookies-from-browser')
source=(git+"${url}".git#tag=v"${pkgver}"?signed)
validpgpkeys=(3E09F5908333DD83DBDCE7375680CA389D365A88) #Mike Fährmann
sha512sums=('a5f216ee73ba7f8a4dc2f95f0182723d44a418a9ec279f06c689ca024ba4c9c96b4b46d82843f1cb353f98ad32163eb257b0dca4ffdd1c523c82b2981faee64b')

prepare() {
    # Clean out old wheels etc.
    git -C "${pkgname}" clean -dfx
}

build() {
    cd ${pkgname}
    make
    python -m build --wheel --no-isolation
}

check() {
    make -C ${pkgname} test
}

package() {
    cd ${pkgname}
    python -m installer --destdir="$pkgdir" dist/*.whl
}
