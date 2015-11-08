# Maintainer: Det
# Contributors: Joris Steyn, Florian Dejonckheere, Tevin Zhang, Andrea Fagiani, Biru Ionut, Paul Bredbury
# Installation order:  freetype2-ubuntu → fontconfig-ubuntu → cairo-ubuntu

pkgname=fontconfig-ubuntu
pkgver=2.11.1
_ubver=0ubuntu6
pkgrel=3
pkgdesc="Library for configuring and customizing font access, with Ubuntu's LCD rendering patches."
arch=('i686' 'x86_64')
url="https://launchpad.net/ubuntu/+source/fontconfig"
license=('custom')
depends=('expat' 'freetype2-ubuntu')
conflicts=('fontconfig')
provides=("fontconfig=$pkgver")
options=('!libtool')
install=$pkgname.install
source=("https://launchpad.net/ubuntu/+archive/primary/+files/fontconfig_$pkgver.orig.tar.bz2"
        "https://launchpad.net/ubuntu/+archive/primary/+files/fontconfig_$pkgver-$_ubver.debian.tar.xz"
        '53-monospace-lcd-filter.patch')
md5sums=('824d000eb737af6e16c826dd3b2d6c90'
         '5d8e082f4d36d6c82853f6b6a5f6997a'
         'a17e48be6a06bc056574be6756cb9738')

prepare() {
  cd fontconfig-$pkgver

  # loop debian patches
  for _f in $(cat ../debian/patches/series); do
    patch -Np1 -i "../debian/patches/$_f"
  done

  # patch
  patch -u conf.d/53-monospace-lcd-filter.conf ../53-monospace-lcd-filter.patch
}

build() {
  cd fontconfig-$pkgver

  # make sure there's no rpath trouble and sane .so versioning - FC and Gentoo do this as well
  msg2 "Running libtoolize.."
  libtoolize -f

  msg2 "Running autoreconf.."
  autoreconf -fi

  # Enable Position Independent Code for prelinking
  export CFLAGS="$CFLAGS -fPIC"
  
  msg2 "Running './configure'.."
  ./configure --prefix=/usr \
    --sysconfdir=/etc \
    --with-templatedir=/etc/fonts/conf.avail \
    --with-xmldir=/etc/fonts \
    --localstatedir=/var \
    --disable-static \
    --with-default-fonts=/usr/share/fonts \
    --with-add-fonts=/usr/share/fonts
	
  msg2 "Running make.."
  make
}

package() {
  cd fontconfig-$pkgver
  
  msg2 "Running make install.."
  make DESTDIR="$pkgdir" install

  # License
  install -Dm0644 COPYING "$pkgdir"/usr/share/licenses/$pkgname/COPYING

  # Docs
  install -Dm0644 ../debian/changelog "$pkgdir"/usr/share/doc/fontconfig/changelog
}
