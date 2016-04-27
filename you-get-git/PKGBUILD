# Maintainer: lilydjwg <lilydjwg@gmail.com>
pkgname=you-get-git
pkgdesc="A YouTube/Youku/Sohu/Tudou/QQ/Sina/PPTV/Xiami/Vimeo/ifeng/AcFun/bilibili/CNTV/... video downloader written in Python 3."
pkgver=0.4.365.20160427.1233
pkgrel=1
arch=('any')
url="http://www.soimort.org/you-get/"
license=('MIT')
depends=('python' 'python-setuptools')
makedepends=('git')
conflicts=(python-you-get-git python-you-get)
replaces=(python-you-get-git)
source=("git://github.com/soimort/you-get.git#branch=develop")
md5sums=(SKIP)

_repo_name=you-get

pkgver() {
  cd "$srcdir/$_repo_name"
  _author_ver=$(git describe | sed -e 's/-.*//' -e 's/v//')
  _last_commit_date=$(git log -1 --pretty='%cd' --date=short | tr -d '-')
  _commit_count="$(git rev-list --count HEAD)"
  echo $_author_ver.$_last_commit_date.$_commit_count
}

build() {
  cd "$srcdir/$_repo_name"

  msg "GIT checkout done or server timeout"
  msg "Starting make..."

  python3 setup.py build
}

package() {
  cd "$srcdir/$_repo_name"
  python3 setup.py install --root=$pkgdir/ --optimize=1
}
