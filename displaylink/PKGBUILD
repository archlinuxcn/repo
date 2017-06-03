# Maintainer: PlusMinus
# Contributor: rhabbachi

pkgname=displaylink
pkgver=1.3.52
pkgrel=1
pkgdesc="Linux driver for DL-5xxx, DL-41xx and DL-3x00"
arch=('i686' 'x86_64')
url="http://www.displaylink.com/downloads/ubuntu.php"
license=('custom' 'GPL2' 'LGPL2.1')
depends=('evdi>=1.3.43' 'libusb>=1.0.0')
makedepends=('grep' 'gawk')
install=
changelog="release-note.txt"
source=(displaylink-driver-$pkgver.zip::http://www.displaylink.com/downloads/file\?id\=744
	udev.sh
        99-displaylink.rules 
	displaylink.service 
        displaylink-sleep.sh)

# Update with > updpkgsums
md5sums=('2df66116bdf2f6f0fd14fb492d63abc5'
         'd5de775e41af06edbd8073adc490139d'
         '20495d81c7d2540910ef86dc437b7fac'
         'c141a15e973481c7d961f8e135627ca4'
         '7cbd9ab2ac79ba66e8297689c6e5483e')

package() {
  echo "Adding udev rule for DisplayLink DL-3xxx/5xxx devices"
  install -D -m644 99-displaylink.rules "$pkgdir/etc/udev/rules.d/99-displaylink.rules"
  install -D -m755 udev.sh "$pkgdir/opt/displaylink/udev.sh"

  echo "Installing DLM systemd service"
  install -D -m644 displaylink.service "$pkgdir/usr/lib/systemd/system/displaylink.service"
  install -D -m755 displaylink-sleep.sh "$pkgdir/usr/lib/systemd/system-sleep/displaylink.sh"
  
  COREDIR="$pkgdir/usr/lib/displaylink"
  install -d -m755 $COREDIR
  install -d -m755 "$pkgdir/var/log/displaylink"

  echo "Extracting DisplayLink Driver Package"
  cd $srcdir
  chmod +x displaylink-driver-$pkgver.run
  ./displaylink-driver-$pkgver.run --target $pkgname-$pkgver --noexec
  cd "$pkgname-$pkgver"
  
  if [ "$CARCH" == "i686" ]; then
    ARCH="x86"
  elif [ "$CARCH" == "x86_64" ]; then
    ARCH="x64"
  fi

  ARCH+="-ubuntu-1604"
  
  echo "Installing DisplayLink Manager $ARCH"
  install -D -m755 $ARCH/DisplayLinkManager $COREDIR/DisplayLinkManager

  # I wonder if this is even necessary but I'm too lazy to find out
  echo "Creating symlinks for evdi and libusb"
  ln -s $(ldconfig -p | grep libevdi | awk 'NR==1{print $4}') $COREDIR/libevdi.so

  ln -s $(ldconfig -p | grep libusb- | awk 'NR==1{print $4}') $COREDIR/libusb-1.0.so.0.1.0
  ln -s $(ldconfig -p | grep libusb- | awk 'NR==1{print $4}') $COREDIR/libusb-1.0.so.0
  ln -s $(ldconfig -p | grep libusb- | awk 'NR==1{print $4}') $COREDIR/libusb-1.0.so
  
  echo "Installing firmware packages"
  install -D -m644 *.spkg $COREDIR

  echo "Installing license file"
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
