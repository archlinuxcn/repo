pkgname=ttf-go-noto-universal-temporal
pkgver=7.0
pkgrel=1
pkgdesc='Noto fonts go universal! Merged Noto fonts according to time of usage.'
arch=(any)
url='https://github.com/satbyy/go-noto-universal'
source=(https://github.com/satbyy/go-noto-universal/releases/download/v${pkgver}/GoNotoCurrent-Regular.ttf
        https://github.com/satbyy/go-noto-universal/releases/download/v${pkgver}/GoNotoCurrent-Bold.ttf
        https://github.com/satbyy/go-noto-universal/releases/download/v${pkgver}/GoNotoCurrentSerif.ttf
        https://github.com/satbyy/go-noto-universal/releases/download/v${pkgver}/GoNotoAncient.ttf
        https://github.com/satbyy/go-noto-universal/releases/download/v${pkgver}/GoNotoAncientSerif.ttf
        10-go-noto-current.conf
        46-go-noto-universal-temporal.conf
        66-go-noto-universal-temporal.conf)
sha256sums=('882afbab965608c2d2bc627fd8016b962aa5a6be2d358f9de24a7b5967c5632e'
            '5ebee1a38f7ef50d6c38263af5522f7518d30abf30d355a8c7c4eb314751ebc2'
            'd656d56938493cafc10500bcc988b9ebfe4866f66a25a8a6f9653837a7b02e41'
            '07e24101c936b67581c5c44a7582adbd616ab4f9da88a5cec855d2eaf68e7578'
            '38b86d5bd172e81aad7f84a2a6ccba5e341879409ed5c7a958f8713e5da4848b'
            'c4c4f09ff52fd81f3a007ed67b9af5488ac2079dac11eb3c0e1b7754da800f81'
            '3a3a2bdeb5f3f02310978810e3907c7f7aaf2194e9b8c68e40dd7c9fae3540af'
            '4363f20915f020d30f404dc8ec920a3ffc159ad419c94c8a760d0f5fd0827c81')

package() {
  install -Dm644 GoNoto*.ttf -t "$pkgdir"/usr/share/fonts/go-noto-universal

  install -Dm644 "$srcdir"/*-go-noto-*.conf -t "$pkgdir"/usr/share/fontconfig/conf.avail/
  install -d "$pkgdir"/usr/share/fontconfig/conf.default
  ln -rs "$pkgdir"/usr/share/fontconfig/conf.avail/* "$pkgdir"/usr/share/fontconfig/conf.default
}
