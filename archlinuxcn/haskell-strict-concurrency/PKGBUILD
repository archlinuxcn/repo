_hkgname=strict-concurrency
pkgname=haskell-strict-concurrency
pkgver=0.2.4.3
pkgrel=1
pkgdesc="Strict concurrency abstractions"
url="https://github.com/ygale/strict-concurrency"
license=('BSD-3-Clause')
arch=('x86_64')
depends=('ghc-libs' 'haskell-deepseq')
makedepends=('ghc')
source=("https://hackage.haskell.org/package/$_hkgname-$pkgver/$_hkgname-$pkgver.tar.gz")
sha256sums=('02d934ec5053d3d42031798e5a3cd25547ccde5973d562f9fc943d635d9956c0')

build() {
    cd "$_hkgname-$pkgver"
    
    runhaskell Setup configure -O --enable-shared --enable-executable-dynamic --disable-library-vanilla \
        --prefix=/usr --docdir=/usr/share/doc/$pkgname --datasubdir=$pkgname \
        --dynlibdir=/usr/lib --libsubdir=\$compiler/site-local/\$pkgid \
        --ghc-option=-optl-Wl\,-z\,relro\,-z\,now \
        --ghc-option=-pie
    runhaskell Setup build $MAKEFLAGS
    runhaskell Setup register --gen-script
    runhaskell Setup unregister --gen-script
    sed -i -r -e "s|ghc-pkg.*update[^ ]* |&'--force' |" register.sh
    sed -i -r -e "s|ghc-pkg.*unregister[^ ]* |&'--force' |" unregister.sh
}

check() {
    cd "$_hkgname-$pkgver"
    runhaskell Setup test
}

package() {
    cd "$_hkgname-$pkgver"
    
    install -D -m744 register.sh "$pkgdir"/usr/share/haskell/register/$pkgname.sh
    install -D -m744 unregister.sh "$pkgdir"/usr/share/haskell/unregister/$pkgname.sh
    runhaskell Setup copy --destdir="$pkgdir"
    install -D -m644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname/
    rm -f "$pkgdir"/usr/share/doc/$pkgname/LICENSE
}
