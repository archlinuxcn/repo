# Maintainer: Jiachen Yang <farseerfc@gmail.com>
# Contributor: Ariel AxionL <axionl@aosc.io>

pkgbase=netease-musicbox-git
pkgname=(netease-musicbox-git netease-musicbox-py2-git)
_gitname=musicbox
pkgver=r557.f4a7dfa
pkgrel=2
pkgdesc="A sexy command line interface musicbox for NetEase based on Python"
arch=(any)
url="https://github.com/darknessomi/musicbox"
depends=('mpg123')
optdepends=('aria2: music caching'
            'libnotify: notifications'
           )
license=('MIT')
_py2depends=('python2' 'mpg123' 'python2-beautifulsoup4' 
             'python2-requests' 'python2-setuptools' 
             'python2-crypto' 'python2-future' 'python2-lxml' 
             'python2-cryptography' )
_py3depends=('python' 'mpg123' 'python-beautifulsoup4' 
             'python-requests' 'python-setuptools' 
             'python-crypto' 'python-future' 'python-lxml' 
             'python-cryptography')
makedepends=('git'
  ${_py2depends[@]}
  ${_py3depends[@]}
) # both python and python2 depends goes to makedepends
options=(!emptydirs)
provides=('netease-musicbox')
conflicts=('netease-musicbox')
install=$pkgname.install

source=("git+https://github.com/darknessomi/musicbox")

sha256sums=('SKIP')

pkgver() {
  cd $_gitname
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package_netease-musicbox-py2-git() {
  replace=("netease-musicbox-git<=r515.7dfd3fe-1")
  depends=(${_py2depends[@]})
  optdepends=('aria2: music caching'
            'python2-keybinder2: global keybindings'
            'libnotify: notifications'
            'python2-pyqt4: lyrics support'
            'python2-dbus: lyrics support'
           )
  cd "$srcdir/$_gitname"
  python2 setup.py install --root="$pkgdir/" --optimize=1
  mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
  install -m755 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/"
}

package_netease-musicbox-git() {
  depends=(${_py3depends[@]})
  optdepends=('aria2: music caching'
            'libnotify: notifications'
            'python-pyqt4: lyrics support'
            'python-dbus: lyrics support'
           )
  cd "$srcdir/$_gitname"
  python setup.py install --root="$pkgdir/" --optimize=1
  mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
  install -m755 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/"
}
# vim:set ts=2 sw=2 et:
