pkgname=pacaur
pkgver=4.6.1
pkgrel=1
pkgdesc="An AUR helper that minimizes user interaction"
arch=('any')
url="https://github.com/rmarquis/pacaur"
license=('ISC')
depends=('cower' 'expac' 'sudo' 'git')
makedepends=('perl')
backup=('etc/xdg/pacaur/config')
source=("https://github.com/rmarquis/$pkgname/archive/$pkgver.tar.gz")
md5sums=('975666818e96cf3254dbd2056bed96b3')

build() {
    cd "$pkgname-$pkgver"
    pod2man --utf8 --section=8 --center="Pacaur Manual" --name="PACAUR"\
        --release="$pkgname $pkgver" ./README.pod > ./pacaur.8
}

package() {
    cd "$pkgname-$pkgver"

    mkdir -p $pkgdir/etc/xdg/pacaur
    install -D -m644 ./config $pkgdir/etc/xdg/pacaur/config
    mkdir -p $pkgdir/usr/bin
    install -D -m755 ./$pkgname $pkgdir/usr/bin/$pkgname
    mkdir -p $pkgdir/usr/share/bash-completion/completions
    install -D -m644 ./bash.completion\
        $pkgdir/usr/share/bash-completion/completions/$pkgname
    mkdir -p $pkgdir/usr/share/zsh/site-functions
    install -D -m644 ./zsh.completion\
        $pkgdir/usr/share/zsh/site-functions/_pacaur
    mkdir -p $pkgdir/usr/share/man/man8
    install -D -m644 ./pacaur.8 $pkgdir/usr/share/man/man8/pacaur.8
    mkdir -p $pkgdir/usr/share/licenses/pacaur
    install -D -m644 ./LICENSE $pkgdir/usr/share/licenses/pacaur/LICENSE
    mkdir -p $pkgdir/usr/share/locale/{ca,de,es,fr,hu,it,ja,nl,pl,pt,ru,sk,tr}/LC_MESSAGES/
    msgfmt ./po/ca.po -o $pkgdir/usr/share/locale/ca/LC_MESSAGES/pacaur.mo
    msgfmt ./po/de.po -o $pkgdir/usr/share/locale/de/LC_MESSAGES/pacaur.mo
    msgfmt ./po/es.po -o $pkgdir/usr/share/locale/es/LC_MESSAGES/pacaur.mo
    msgfmt ./po/fr.po -o $pkgdir/usr/share/locale/fr/LC_MESSAGES/pacaur.mo
    msgfmt ./po/hu.po -o $pkgdir/usr/share/locale/hu/LC_MESSAGES/pacaur.mo
    msgfmt ./po/it.po -o $pkgdir/usr/share/locale/it/LC_MESSAGES/pacaur.mo
    msgfmt ./po/ja.po -o $pkgdir/usr/share/locale/ja/LC_MESSAGES/pacaur.mo
    msgfmt ./po/nl.po -o $pkgdir/usr/share/locale/nl/LC_MESSAGES/pacaur.mo
    msgfmt ./po/pl.po -o $pkgdir/usr/share/locale/pl/LC_MESSAGES/pacaur.mo
    msgfmt ./po/pt.po -o $pkgdir/usr/share/locale/pt/LC_MESSAGES/pacaur.mo
    msgfmt ./po/ru.po -o $pkgdir/usr/share/locale/ru/LC_MESSAGES/pacaur.mo
    msgfmt ./po/sk.po -o $pkgdir/usr/share/locale/sk/LC_MESSAGES/pacaur.mo
    msgfmt ./po/tr.po -o $pkgdir/usr/share/locale/tr/LC_MESSAGES/pacaur.mo
}

