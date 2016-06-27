# Maintainer: Tom Bu <tom.bu[at]openmailbox.org>
# Maintainer: Justin Wong <justin.w.xd[at]gmail.com>
pkgname=bilidan-git
pkgver=20160512
pkgrel=1
pkgdesc="Play videos on Bilibili.com with MPV and Danmaku2ASS"
url="https://github.com/m13253/BiliDan"
arch=('any')
license=('MIT')
depends=('python>=3' 'mpv' 'ffmpeg' 'danmaku2ass-git')
provides=('bilidan')
conflicts=('bilidan')
makedepends=('git')
source=("git+https://github.com/m13253/BiliDan.git"
        "bilidan.sh")
md5sums=('SKIP'
         '859e8e83414767f8740f79700e5d3235')
_reponame=BiliDan

pkgver() {
  cd ${srcdir}/${_reponame}
  echo $(git log -1 --format="%cd" --date=short | tr -d -)
}

package() {
  cd ${srcdir}/${_reponame}
  install -Dm755 bilidan.py ${pkgdir}/usr/share/bilidan/bilidan.py
  install -Dm755 ${srcdir}/bilidan.sh ${pkgdir}/usr/bin/bilidan
  install -Dm644 README.md ${pkgdir}/usr/share/doc/${pkgname}/README.md
  install -Dm644 COPYING ${pkgdir}/usr/share/licenses/${pkgname}/COPYING
}

# vim:set ts=2 sw=2 et:
