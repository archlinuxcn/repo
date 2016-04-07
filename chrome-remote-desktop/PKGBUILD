# Maintainer: Dave Blair <mail@dave-blair.de>
# Contributor: James An <james@jamesan.ca>
# Contributor: Mateus Rodrigues Costa <charles [dot] costar [at] gmail [dot] com>

pkgname=chrome-remote-desktop
pkgver=50.0.2661.22
pkgrel=1
pkgdesc="Allows you to securely access your computer over the Internet through Chrome."
url="https://chrome.google.com/webstore/detail/gbchcmhmhahfdphkhkmpfmihenigjmpp"
arch=('x86_64')
license=('BSD')
install=$pkgname.install
depends=('python2' 'python2-psutil' 'gconf' 'gtk2' 'nss'
         'xorg-xdpyinfo' 'xorg-setxkbmap' 'xorg-server-xvfb' 'xorg-xauth' 'nano')

#source_i686=("http://dl.google.com/linux/chrome-remote-desktop/deb/pool/main/${pkgname:0:1}/${pkgname}/${pkgname}_${pkgver}_i386.deb")
source_x86_64=("http://dl.google.com/linux/chrome-remote-desktop/deb/pool/main/${pkgname:0:1}/${pkgname}/${pkgname}_${pkgver}_amd64.deb")
source=("$pkgname.service"
        "crd")
#md5sums_i686=('bf9135f439fa4bfa1daf16e96c62d87a')
md5sums_x86_64=('dbfe3bc9634e6ad8eac16123fe1388b5')
md5sums=('6f6083ff37f036f590702c7b1319445b'
         '5e9fa07e85d0d490de675bf258a0c511')

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
  
  msg2 "Adding runnable crd command"
  install -Dm755 "crd" "$pkgdir/usr/bin/crd"

  msg2 "Creating symlinks for Chromium compatibility"
  install -dm755 "$pkgdir/etc/chromium/native-messaging-hosts"
  for _file in $(find "$pkgdir/etc/opt/chrome/native-messaging-hosts" -type f); do
    _filename=${_file##*/}
    if [[ ! -f "/etc/chromium/native-messaging-hosts/${_filename}" ]]; then
      ln -s "/etc/opt/chrome/native-messaging-hosts/${_filename}" \
	    "$pkgdir/etc/chromium/native-messaging-hosts/${_filename}"
    fi
  done
}
