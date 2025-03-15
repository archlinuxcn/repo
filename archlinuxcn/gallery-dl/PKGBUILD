# Maintainer: katt <magunasu.b97@gmail.com>
# Contributor: LLL2yu <lll2yu@protonmail.com>

pkgname=gallery-dl
pkgver=1.29.2
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
            'python-secretstorage: GNOME keyring passwords for --cookies-from-browser'
            'python-psycopg: PostgreSQL support')
source=(git+"${url}".git#tag=v"${pkgver}"?signed)
validpgpkeys=(3E09F5908333DD83DBDCE7375680CA389D365A88) #Mike Fährmann
sha512sums=('561543714daad3eb15b7a31061100865e311295b81a5a695aceff602361c3c80a1779b989206c8a074e49fce71fbbce6d08be944cfa848a8e86bfebb9bb980a6')

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
