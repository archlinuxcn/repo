# Maintainer: Nicolas Reynolds <fauno@kiwwwi.com.ar>
# Contributor: Luke Shumaker <lukeshu@sbcglobal.net>
# Based on haskell-pandoc

pkgname=pandoc-static
_pkgname=pandoc
pkgver=1.13.2.1
pkgrel=1
pkgdesc='Conversion between markup formats (no Haskell libraries)'
url='http://johnmacfarlane.net/pandoc/'
license=('GPL')

replaces=('pandoc')
provides=('pandoc')

arch=('i686' 'x86_64')
depends=('icu>=55' 'icu<56' 'gmp' 'libffi' 'zlib')
makedepends=('ghc' 'sh' 'cabal-install' 'alex' 'happy')
optdepends=('texlive-most: for PDF creation')
options=(strip !makeflags !distcc !emptydirs)
source=(https://repo.parabola.nu/other/${pkgname}/${pkgname}-${pkgver}.tar.xz{,.sig}
        pandoc-citeproc-ghc-7.10.patch)
validpgpkeys=('49F707A1CB366C580E625B3C456032D717A4CD9C')
sha512sums=('614832f1c96bbdd67a50c8ace76f416d87b9dfeb873a7b2de6d8336a1804f68c53e5460ad62c49097fd8ea052f38a1f66163bc56cc808ac18bc57ce76063ecbc'
            'SKIP'
            '22339e9b3dc68151fdf867379bc3b9f600cb5e08b45a26ab755a3d0d2034b461763174d82468fe9f3d6bd8a4a14b1ce30b4ab040c44777f8b99e89915fb4b4ee')

declare -gA _flags
_flags[pandoc]='https make-pandoc-man-pages'
_flags[pandoc_citeproc]='small_base bibutils hexpat unicode_collation'

_packages=(hs-bibutils network hexpat text text-icu hsb2hs
  http-client-tls http-types
  pandoc-${pkgver} pandoc-citeproc)
mkdepends=('ghc' 'cabal-install')
mksource() (
  set -o pipefail
  # building haddock requires an utf8 lang, if you use anything else you
  # have to enable an utf8 locale and run locale-gen
  test "${LANG#*.}" != "utf8" && export LANG="en_US.utf8"
  export HOME="$srcdir"

  mkdir $pkgname-$pkgver
  cd    $pkgname-$pkgver

  cabal update
  cabal fetch "${_packages[@]}"

  # Get the build order
  cabal install --dry-run \
     --flags="embed_data_files ${_flags[*]}" \
    "${_packages[@]}" > BUILDORDER

  # Place all of the downloaded sources in the target directory
  for file in ../.cabal/packages/*/*/*/*.tar.?z; do
    bsdtar xf "$file"
  done
)

prepare() {
  # EC is unfree and makes Parabola TeXLive cry
  # besides, it's unneeded
  find "${srcdir}/${pkgname}-${pkgver}/${_pkgname}-${pkgver}" \
    -name default.latex \
    -exec sed "/fontenc/d" -i {} \;

    # https://github.com/hvr/deepseq-generics/issues/2
    sed "s/\(ghc-prim >= 0.2 && < \)0.4/\10.5/" -i \
    "${srcdir}/${pkgname}-${pkgver}/deepseq-generics-0.1.1.2/deepseq-generics.cabal"

    sed "s/\(base <4.\)8/\19/" -i \
    "${srcdir}/${pkgname}-${pkgver}/split-0.2.2/split.cabal"

    pushd "${srcdir}/${pkgname}-${pkgver}/pandoc-citeproc-0.6/"
    patch -Np1 -i "${srcdir}/pandoc-citeproc-ghc-7.10.patch"
}

build() (
  cd "${srcdir}/${pkgname}-${pkgver}"
  mkdir -p ../build

  # building haddock requires an utf8 lang, if you use anything else you
  # have to enable an utf8 locale and run locale-gen
  test "${LANG#*.}" != "utf8" && export LANG="en_US.utf8"
  export HOME="${srcdir}"
  export PATH="${srcdir}/build/usr/bin:${PATH}"

  while read hkpkg; do
    if [ -d "$srcdir"/build/usr/share/doc/*/"$hkpkg" ]; then
      msg2 'Skipping %s' "$hkpkg"
      continue
    fi

    msg2 'Building %s' "$hkpkg"
    pushd "$hkpkg" >/dev/null
    case "$hkpkg" in
      $_pkgname-$pkgver)
        # Don' bother trying to set --libdir= outside of $pkgdir,
        # libdir is a relative (to prefix) path, never absolute.
        cabal configure -v \
          --flags="embed_data_files ${_flags[pandoc]}" \
          --prefix=/usr
        cabal build
        cabal register --inplace
        ;;
      pandoc-citeproc-*)
        cabal configure -v \
          --flags="embed_data_files ${_flags[pandoc_citeproc]}" \
          --prefix=/usr
        cabal build
        ;;
      *)
        cabal install --prefix="${srcdir}"/build/usr --flags="embed_data_files"
        ;;
    esac
    popd >/dev/null
  done < <(sed -rn 's/(\S*[0-9]+).*/\1/p' BUILDORDER)
)

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  msg2 "Installing pandoc..."
  cd ${_pkgname}-${pkgver}
  cabal copy --destdir="${pkgdir}/"
  install -Dm644 {,"$pkgdir"/usr/share/}man/man1/pandoc.1
  install -Dm644 {,"$pkgdir"/usr/share/}man/man5/pandoc_markdown.5

  msg2 "Installing pandoc-citeproc..."
  cd ../pandoc-citeproc-*
  cabal copy --destdir="${pkgdir}/"

  msg2 "Installing extra executables..."
  cp -av "${srcdir}"/build/usr/bin/* "${pkgdir}"/usr/bin/

  msg2 "Removing library files..."
  rm -rfv "$pkgdir"/usr/lib

  msg2 "Installing licenses..."
  install -d                                 "${pkgdir}"/usr/share/licenses/${pkgname}
  cp -rv "${srcdir}"/build/usr/share/doc/*/* "${pkgdir}"/usr/share/licenses/${pkgname}
  mv -v        "${pkgdir}"/usr/share/doc/*/* "${pkgdir}"/usr/share/licenses/${pkgname}
}
