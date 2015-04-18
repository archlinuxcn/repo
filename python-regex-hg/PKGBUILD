# Contributor: Spyros Stathopoulos <foucault.online@gmail.com>
pkgname=python-regex-hg
pkgver=153.0b2d7bbed01e
pkgrel=1
pkgdesc="Alternative regular expression module, to replace re."
arch=('i686' 'x86_64')
url="https://code.google.com/p/mrab-regex-hg/"
license=('custom')
depends=('python')
makedepends=('mercurial')
_hgname='mrab-regex-hg'
source=("hg+https://code.google.com/p/$_hgname")
md5sums=(SKIP)

_dist=Python3
_regex=regex_3

pkgver() {
  cd ${_hgname}
  echo $(hg identify -n).$(hg identify -i)
}

build() {
  cd "$srcdir/${_hgname}/PyPI"

  if [ ! -d ${_dist} ] ; then
    mkdir ${_dist}
  fi

  if [ ! -d ${_dist}/../docs ] ; then
    mkdir ${_dist}/../docs
  fi

  cp ../docs/Features.rst ${_dist}/../docs
  cp ../${_regex}/regex/* ${_dist}
  cp ../${_regex}/Python/* ${_dist}
  #cp ../${_regex}/UnicodeProperties.txt ${_dist}

  python setup.py build
}

package() {
  cd "$srcdir/${_hgname}/PyPI"
  python setup.py install --prefix=/usr --root="${pkgdir}" --optimize=1
}

