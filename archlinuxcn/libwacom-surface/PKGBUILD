# Maintainer: Maximilian Luz <luzmaximilian@gmail.com>
# Based on official Arch Linux PKGBUILD

pkgname=libwacom-surface
pkgver=1.9
pkgrel=1
pkgdesc="Patched libwacom for Microsoft Surface devices"
arch=('x86_64')
url="https://github.com/linux-surface/libwacom"
license=('MIT')
depends=('glib2' 'systemd' 'libgudev')
makedepends=('libxml2' 'meson')
checkdepends=('python-pytest' 'python-libevdev' 'python-pyudev')
validpgpkeys=('3C2C43D9447D5938EF4551EBE23B7E70B467F0BF')
conflicts=('libwacom')
provides=("libwacom=${pkgver}")

source=(
    '0001-Add-support-for-BUS_VIRTUAL.patch'
    '0002-Add-support-for-Intel-Management-Engine-bus.patch'
    '0003-data-Add-Microsoft-Surface-pro-4.patch'
    '0004-data-Add-Microsoft-Surface-pro-5.patch'
    '0005-data-Add-Microsoft-Surface-pro-6.patch'
    '0006-data-Add-Microsoft-Surface-pro-7.patch'
    '0007-data-Add-Microsoft-Surface-Book.patch'
    '0008-data-Add-Microsoft-Surface-Book-2-13.5.patch'
    '0009-data-Add-Microsoft-Surface-Book-2-15.patch'
    '0010-data-Add-Microsoft-Surface-Book-3-13.5.patch'
    '0011-data-Add-Microsoft-Surface-Book-3-15.patch'
    "https://github.com/linuxwacom/libwacom/releases/download/libwacom-${pkgver}/libwacom-${pkgver}.tar.bz2"{,.sig}
)
sha256sums=('bee93db7423a1250f24172e5409166116568e47fe951569f178bfe5ce06129a6'
            '6c41619a307cb1325997730fece7aacc0fce728b1c3f80244aa06289cf5611f3'
            '136233738a219c4ee24b293bfdf73e8de2211c14ce6321a60018ad02b7c56c57'
            '06a8b07b8446dc9d32bd0295e1b7c584f4d8e32840578366603e68b995bce6a7'
            'af37d7ff44f201e6e7d2f90a8bea2fe1c162e9f1dab420b7e648d52a01549bb9'
            '2cd478c179d42174c3e44c319bb8eb759c0b7a1dd6792523296cfe607e6e6270'
            'f464d6f4911545b2fc776defadd231f07289e7aab64ac47e5337072701736cca'
            'cefffa6d243215b71c5029db72921c12ac5cfce6f0232d6b1017f0002b8e65fd'
            'a8c887074b89f3a2349c9dbe47f2e6a5bd6e4aa0675882f6486fcd0cec4a8243'
            '6de413ca309288ef0daa4145db99cdc615ca5ac8b61250cf9ad336688a6bee97'
            '37384fdd70039443d5d81b77a9bdb6dd00fb4c1143e90f3272fbca1096aee0b1'
            '68b14d4e3b75fed9f590bf6eaea361a72dc23e933b7725094c779477acf665c7'
            'SKIP')

prepare() {
    cd "libwacom-${pkgver}"

    for p in "${srcdir}/"*.patch ; do
        patch -Np1 -i "${p}" || true
    done
}

build() {
    meson build "libwacom-${pkgver}" --prefix="/usr"
    ninja -C build
}

check() {
    ninja test -C build
}

package() {
    DESTDIR="${pkgdir}" ninja install -C build
    install -D -m644 "libwacom-${pkgver}/COPYING" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
