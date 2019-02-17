# Maintainer: David Birks <david@tellus.space>
# Maintainer: Jake <aur@ja-ke.tech>
# Contributor: Jonas Heinrich <onny@project-insanity.org>
# Contributor: Alda <alda@leetchee.fr>
# Contributor: mrxx <mrxx at cyberhome dot at>
# Contributor: Jonhoo <jon at thesquareplanet.com>
# Contributor: torvic9 <vic999 at mailbox.org>
pkgname=signal
pkgver=1.21.2
pkgrel=1
license=('GPL3')
pkgdesc='Signal Private Messenger for the Desktop'
depends=('electron' 'openssl-1.0')
makedepends=('python' 'python2' 'npm' 'yarn' 'git' 'nodejs-lts-dubnium')
provides=('signal')
conflicts=('signal-desktop' 'signal-desktop-beta' 'signal-desktop-bin')
arch=("i686" "x86_64")
url='https://github.com/signalapp/Signal-Desktop'
source=("${pkgname}-git-repo::git+https://github.com/signalapp/Signal-Desktop.git#tag=v${pkgver}"
        "${pkgname}.sh"
        "${pkgname}.desktop"
        "${pkgname}-tray.desktop"
        "openssl-linking.patch")
sha512sums=('SKIP'
            '5cd854481c21720a18c3cf743a8dcccdcc4792151106889096c5b51d55740477084be313ec3fbbf1f5876e8aba29c2acdc23acb13a62d43e16ad5a6eb79c9dc6'
            'a264bfc7a4a7aac747daa588a2acbf1eddfd201bc795f0fbc18460a9b25f4460f364124e227a527fec22631cd84bc9e190f9f4978069e9c119eb556b9ff2d327'
            'ced228d19303abe951c55f7874004cb9e4cd062dbda48c7ea80b0a6fb9adf5716a37164c01c9921a91f00653b0737fed80e3c5e684b0f3bcec375c265d6d8e5c'
            '05efc65a78b2006f3ffdd728dd5a96923ee9c909a3707833f8d55935c18e507051aabdbefff270bb2c58d7f151147966b550c9bbc2a115dae177f51955720482')

prepare() {
  cd "${pkgname}-git-repo"  
  # Upgrade electron
  sed -i 's/"electron": "3.0.14"/"electron": "3.1.1"/' package.json

  # Allow higher node minor versions
  sed -i 's/"node": "/&^/' package.json
  
  # Download modules
  yarn install
  
  # use dynamic linking
  patch -Np1 -i "../openssl-linking.patch"
}

build() {
  cd "${pkgname}-git-repo"

  export npm_config_cache="$srcdir/npm_cache"

  # Build Signal
  yarn generate
  yarn build-release --dir
}

package() {
  cd "${pkgname}-git-repo"

  install -dm755 "${pkgdir}/usr/lib/${pkgname}"
  cp -r release/linux-unpacked/resources "${pkgdir}/usr/lib/${pkgname}/"

  install -dm755 "${pkgdir}/usr/share/icons/hicolor"
  for i in 16 24 32 48 64 128 256 512; do
    install -Dm644 build/icons/png/${i}* "${pkgdir}/usr/share/icons/hicolor/${i}x${i}/apps/${pkgname}.png"
  done

  install -dm755 "${pkgdir}/usr/bin"
  install -Dm755 "${srcdir}/${pkgname}.sh" "${pkgdir}/usr/bin/${pkgname}-desktop"

  install -Dm644 "${srcdir}"/${pkgname}.desktop "${pkgdir}"/usr/share/applications/${pkgname}.desktop
  install -Dm644 "${srcdir}"/${pkgname}-tray.desktop "${pkgdir}"/usr/share/applications/${pkgname}-tray.desktop
}
