# Maintainer: Stefano Capitani <stefanoatmanjarodotorg>

pkgname=inxi
pkgver=3.0.37
pkgrel=1
pkgdesc="Full featured CLI system information tool"
arch=('any')
url="https://github.com/smxi/inxi"
license=('GPL')
depends=('coreutils' 'pciutils' 'perl' 'procps-ng')
optdepends=(
  "bind-tools: -i wlan IP"
  "dmidecode: inxi -M if no sys machine data"
  "file: inxi -o unmounted file system"
  "hddtemp: inxi -Dx show hdd temp"
  "iproute2: inxi -i ip lan"
  "kmod: inxi -Ax,-Nx module version"
  "lm_sensors: inxi -s sensors output"
  "mesa-demos: inxi -G glx info"
  "net-tools: inxi -i ip lan-deprecated"
  "perl-io-socket-ssl: -U; -w,-W; -i (if dig not installed)"
  "perl-json-xs: --output json - required for export (legacy)"
  "systemd-sysvcompat: inxi -I runlevel"
  "sudo: inxi -Dx hddtemp-user;-o file-user"
  "tree: --debugger 20,21 /sys tree"
  "usbutils: inxi -A usb audio;-N usb networking"
  "wmctrl: -S active window manager (not all wm)"
  "xorg-xdpyinfo: inxi -G multi screen resolution"
  "xorg-xprop: inxi -S desktop data"
  "xorg-xrandr: inxi -G single screen resolution"
)
options=('zipman')
source=("${pkgname}-${pkgver}.tar.gz::$url/archive/${pkgver}-1.tar.gz")
sha256sums=('bc16d8b975a8ed064949bc8209e0c01c204c01c9046076f62709366e672bea40')

package() {
    cd "$srcdir/$pkgname-$pkgver-1"
    install -D -m755 $pkgname "$pkgdir/usr/bin/$pkgname"
    install -D -m755 $pkgname.1 "$pkgdir/usr/share/man/man1/$pkgname.1"
}

