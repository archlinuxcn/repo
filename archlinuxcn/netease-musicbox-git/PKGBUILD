# Maintainer: Jiachen Yang <farseerfc@gmail.com>
# Maintainer: Ariel AxionL <axionl@aosc.io>

pkgname=netease-musicbox-git
_gitname=musicbox
pkgver=0.3.1.r1.gcd2874e
pkgrel=2
pkgdesc="A sexy command line interface musicbox for NetEase based on Python"
arch=(any)
url="https://github.com/darknessomi/musicbox"
depends=('mpg123' 'python-pycryptodomex' 'python-requests' 'python-future' 
         'python-fuzzywuzzy' 'python-requests-cache' 'python-importlib-metadata')
makedepends=('python-setuptools' 'python-poetry' 'git')
optdepends=('aria2: music caching'
            'libnotify: notifications'
            'qt5-base: lyrics support'
            'python-qtpy: lyrics support'
            'python-pyqt5: lyrics support'
            'python-dbus: lyrics support'
            'python-levenshtein: fuzzy search support')
provides=('netease-musicbox')
conflicts=('netease-musicbox')
license=('MIT')

source=("${_gitname}::git+https://github.com/darknessomi/musicbox"
        "LICENSE::https://raw.githubusercontent.com/darknessomi/musicbox/master/LICENSE")

sha256sums=('SKIP'
            '40aaf7aea7939284b07c487929472fa9cc5a842ff5f0c1e474ac93e6de7aa64e')

pkgver() {
  cd "${srcdir}/${_gitname}"
  git describe --long --tags | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  cd "${srcdir}/${_gitname}"
  poetry build -f sdist
  export mainver=$(echo "${pkgver}" | cut -d "." -f1-3)
  tar xvf "./dist/NetEase-MusicBox-${mainver}.tar.gz"
}

package() {
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  
  cd "${srcdir}/${_gitname}/NetEase-MusicBox-${mainver}"
  python setup.py install --root="${pkgdir}/" --optimize=1
}
# vim:set ts=2 sw=2 et:
