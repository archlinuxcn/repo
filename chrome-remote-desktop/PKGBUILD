# Maintainer: James An <james@jamesan.ca>
# Contributor: Mateus Rodrigues Costa <charles [dot] costar [at] gmail [dot] com>

pkgname=chrome-remote-desktop
pkgver=40.0.2214.44
pkgrel=1
pkgdesc="Allows you to securely access your computer over the Internet through Chrome."
url="https://chrome.google.com/webstore/detail/gbchcmhmhahfdphkhkmpfmihenigjmpp"
arch=('i686' 'x86_64')
license=('BSD')
install=$pkgname.install
depends=('python2' 'python2-psutil' 'gconf' 'gtk2' 'nss'
         'xorg-xdpyinfo' 'xorg-setxkbmap' 'xorg-server-xvfb' 'xorg-xauth')

_arch=i386
[ "$CARCH" == x86_64 ] && _arch=amd64
source=("$pkgname.service"
        "https://dl.google.com/linux/direct/${pkgname}_current_${_arch}.deb")
md5sums=('cde1758e875ff114cc8153edb7087d2a'
         'SKIP')

pkgver() {
  bsdtar -xf control.tar.gz -O control | grep '^Version: ' | cut -f2 -d' '
}

prepare() {
  cd "$srcdir"

  msg2 'Extracting data from debian package'
  bsdtar -xf data.tar.gz -C .

  msg2 'Patching Python script'
  sed -e '1 s/python/python2/' \
      -e '/^.*sudo_command =/ s/"gksudo .*"/"pkexec"/' \
      -e '/^.*command =/ s/s -- sh -c/s sh -c/' \
      -i opt/google/chrome-remote-desktop/chrome-remote-desktop
}

build() {
  cd "$srcdir"

  msg2 'Removing unnecessary files'
  rm -R etc/cron.daily
  rm -R etc/init.d
  rm -R etc/pam.d
}

package() {
  cd "$srcdir"

  mv etc $pkgdir
  mv opt $pkgdir

  msg2 'Packaging copyright file'
  install -Dm644 usr/share/doc/$pkgname/copyright "$pkgdir/usr/share/licenses/$pkgname/copyright"

  msg2 "Adding systemd user service file"
  install -Dm644 "$pkgname.service" "$pkgdir/usr/lib/systemd/user/$pkgname.service"

  msg2 "Creating symlinks for chromium compatibility"
  install -dm755 "$pkgdir/etc/chromium/native-messaging-hosts"
  ln -sr "$pkgdir/etc/opt/chrome/native-messaging-hosts/*" "$pkgdir/etc/chromium/native-messaging-hosts"
}
