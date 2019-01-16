# Maintainer: Ding Xiao <tinocodfcdsa10@mails.tsinghua.edu.cn>
# Contributor: Firmy <firmianay@gmail.com>
pkgname=python2-pwntools
pkgver=3.13.0beta0
_pkgver=3.12.1
pkgrel=4
pkgdesc='A CTF framework and exploit development library.'
arch=('any')
url='https://github.com/Gallopsled/pwntools'
license=('MIT' 'GPL2' 'BSD')
makedepends=('lib32-glibc'
             'python2-setuptools')
depends=('python2>=2.7'
         'python2-mako'
         'python2-paramiko'
         'python2-pyelftools'
         'python2-capstone'
         'python2-pyserial'
         'python2-requests'
         'python2-psutil'
         'python2-tox'
         'python2-pysocks'
         'python2-dateutil'
         'python2-pygments'
         'python2-pypandoc'
         'python2-packaging'
         'python2-unicorn'
         'python2-intervaltree'
         'python2-pip'
         'ropgadget')
provides=('python2-pwntools')
conflicts=('python2-pwntools')
options=('strip')
source=("${pkgname}-${_pkgver}.tar.gz::https://github.com/Gallopsled/pwntools/archive/${_pkgver}.tar.gz")
sha256sums=('dfea4140d345f2749086e07ed9c08d5625e50e0f969e2894509e69f9d4755c3d')

_repodir="pwntools-${_pkgver}"

prepare() {
  cd ${srcdir}/${_repodir}
}

package() {
  cd ${srcdir}/${_repodir}
  python2 setup.py install --root=${pkgdir}/ --optimize=1 --only-use-pwn-command
  install -D -m 644 LICENSE-pwntools.txt ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
  rm ${pkgdir}/usr/lib/python*/site-packages/*.{txt,md}
}
