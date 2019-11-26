# Maintainer: graysky <graysky AT archlnux DOT us>
# Contributor: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>
# Contributor: Jaroslav Lichtblau <svetlemodry@archlinux.org>
# Contributor: Geoffroy Carrier <geoffroy@archlinux.org>
# Contributor: Joël Schaerer <joel.schaerer@laposte.net>
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>

pkgname=autojump
pkgver=22.5.3
pkgrel=5
pkgdesc="A faster way to navigate your filesystem from the command line"
arch=('any')
url="https://github.com/wting/autojump"
license=('GPL3')
depends=('python>=3.8')
_python=python3.8
source=($pkgname-$pkgver.tar.gz::https://github.com/wting/$pkgname/archive/release-v$pkgver.tar.gz)
sha256sums=('00daf3698e17ac3ac788d529877c03ee80c3790472a85d0ed063ac3a354c37b1')
install=readme.install

prepare() {
  cd $pkgname-release-v$pkgver
  sed -i "s:/env python:/python3:g" bin/$pkgname
}

package() {
  cd $pkgname-release-v$pkgver

  SHELL=/bin/bash ./install.py --destdir "${pkgdir}" \
    --prefix 'usr/' \
    --zshshare 'usr/share/zsh/site-functions'

  cd "${pkgdir}/usr/share/$pkgname"
  for i in $pkgname.*
    do ln -s "/usr/share/$pkgname/$i" "${pkgdir}/etc/profile.d/$i"
  done

  # FS#60929
  install -d "${pkgdir}/usr/lib/$_python/site-packages"
  mv ${pkgdir}/usr/bin/*.py "${pkgdir}/usr/lib/$_python/site-packages"
  python -m compileall -d /usr/lib "${pkgdir}/usr/lib"
  python -O -m compileall -d /usr/lib "${pkgdir}/usr/lib"

  # FS#49601
  install -d "${pkgdir}"/usr/share/fish/completions
  mv "${pkgdir}"/etc/profile.d/$pkgname.fish "${pkgdir}"/usr/share/fish/completions

  # https://github.com/joelthelion/autojump/pull/339
  sed -i "s:/usr/local/:/usr/:g" "${pkgdir}/etc/profile.d/$pkgname.sh"
  sed -i "s:/build/autojump/pkg/autojump/:/:g" "${pkgdir}/etc/profile.d/$pkgname.sh"

  # FS#43762
  sed -i '27,31d' "${pkgdir}/etc/profile.d/$pkgname.sh"
}
