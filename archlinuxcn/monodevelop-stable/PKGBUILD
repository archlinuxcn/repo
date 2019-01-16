# $Id$
# Maintainer: Doctorzeus <simmlog@gmail.com>
# Contributor: Malah <malah@neuf.fr>
# Contributor: Brenton Horne <brentonhorne77@gmail.com>
# Contributor: Daniel Isenmann <daniel@archlinux.org>
# Contributor: Timm Preetz <timm@preetz.us>
# Contributor: Giovanni Scafora <giovanni@archlinux.org>

pkgname=monodevelop-stable
_pkgname=monodevelop
pkgver=7.8.0.1471
pkgrel=1
pkgdesc="An IDE primarily designed for C# and other .NET languages"
arch=('x86_64' 'i686')
url="http://www.monodevelop.com"
license=('GPL')
depends=('mono>=5.10.1.47' 'mono-addins>=0.6.2' 'gtk-sharp-2' 'fsharp>=4.5.0' 'libssh2' 'curl' 'msbuild-stable')
makedepends=('rsync' 'cmake' 'git' 'nuget' 'openssl-1.0' 'xterm')
replaces=('monodevelop-debugger-gdb')
provides=('monodevelop' 'monodevelop-debugger-gdb')
conflicts=('monodevelop')
options=(!makeflags)
optdepends=('xsp: To run ASP.NET pages directly from monodevelop')
source=(git://github.com/mono/monodevelop.git#tag=monodevelop-$pkgver)
sha256sums=('SKIP')
TERM=xterm
SHELL=/bin/bash

prepare() {
  cd $_pkgname
  git submodule update --init --recursive || return 1
  git checkout tags/$_pkgname-$pkgver
  git clean -dfx
}

build() {
  cd $_pkgname

  export PKG_CONFIG_PATH=/usr/lib/openssl-1.0/pkgconfig
  export CFLAGS+=" -I/usr/include/openssl-1.0"
  export LDFLAGS+=" -L/usr/lib/openssl-1.0 -lssl"
  export MONO_IOMAP=all

  ./configure --prefix=/usr --profile=stable
  XDG_CONFIG_HOME="$srcdir"/config make
}

package() {
  cd $_pkgname
  
  XDG_CONFIG_HOME="$srcdir"/config LD_PRELOAD="" make DESTDIR="$pkgdir" install
  # delete conflicting files
  find "$pkgdir"/usr/share/mime/ -type f -delete

  # NuGet.exe is missing somehow, fixed FS#43423
  #install -Dm755 "${srcdir}"/monodevelop/main/external/nuget-binary/nuget.exe "${pkgdir}"/usr/lib/monodevelop/AddIns/MonoDevelop.PackageManagement/nuget.exe
}

