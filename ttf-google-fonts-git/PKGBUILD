# Maintainer: Andrew Crerar <crerar@archlinux.org>
# Contributor: Mohammadreza Abdollahzadeh <morealaz at gmail dot com>
# Contributor: FadeMind <fademind@gmail.com>
# Contributor: Vlad M. <vlad@archlinux.net>
# Contributor: Sebastian Stammler <stammler.s@gmail.com>
# Contributor: Sarkasper <echo a2FzcGVyLm1lbnRlbkBnbXguY29tCg== | base64 -d>
# Contributor: Daniel Micay <danielmicay@gmail.com>
# Contributor: Michalis Georgiou <mechmg93@gmail.comr>
# Contributor: Alexander De Sousa <archaur.xandy21@spamgourmet.com>

pkgname=ttf-google-fonts-git
pkgver=r1333.ef5baa48
pkgrel=1
epoch=1
pkgdesc="TrueType fonts from the Google Fonts project (git version)"
arch=('any')
url="https://github.com/google/fonts"
license=('custom:SIL Open Font License' 'custom:Ubuntu Font License v1.0')

depends=('fontconfig'
         'xorg-mkfontdir'
         'xorg-mkfontscale'
         'xorg-fonts-encodings'
         'noto-fonts'
         'noto-fonts-extra'
         'ttf-fira-sans'
         'ttf-fira-mono'
         'ttf-ubuntu-font-family'
         'ttf-croscore'
         'ttf-roboto'
         'ttf-inconsolata'
         'cantarell-fonts'
         'ttf-merriweather'
         'ttf-merriweather-sans'
         'ttf-opensans'
         'ttf-oswald'
         'ttf-quintessential'
         'ttf-signika')
makedepends=('git')
conflicts=('adobe-source-code-pro-fonts'
           'adobe-source-sans-pro-fonts'
           'jsmath-fonts'
           'lohit-fonts'
           'ttf-andika'
           'ttf-anonymous-pro'
           'ttf-cardo'
           'ttf-comfortaa'
           'ttf-lato'
           'ttf-lora-cyrillic'
           'ttf-lekton'
           'ttf-medievalsharp'
           'ttf-nova'
           'ttf-oxygen'
           'ttf-oxygen-git'
           'ttf-pt-fonts'
           'ttf-roboto-mono'
           'ttf-sil-fonts'
           'ttf-source-code-pro-ibx'
           'ttf-source-sans-pro-ibx'
           'ttf-vollkorn-ibx'
           'ttf-arabeyes-fonts')
provides=('adobe-source-code-pro-fonts'
          'adobe-source-sans-pro-fonts'
          'jsmath-fonts'
          'lohit-fonts'
          'ttf-andika'
          'ttf-anonymous-pro'
          'ttf-cardo'
          'ttf-comfortaa'
          'ttf-lato'
          'ttf-lora-cyrillic'
          'ttf-lekton'
          'ttf-medievalsharp'
          'ttf-nova'
          'ttf-oxygen'
          'ttf-oxygen-git'
          'ttf-pt-fonts'
          'ttf-roboto-mono'
          'ttf-sil-fonts'
          'ttf-source-code-pro-ibx'
          'ttf-source-sans-pro-ibx'
          'ttf-vollkorn-ibx')
source=(git+"${url}".git)
sha512sums=('SKIP')

pkgver() {
  cd fonts

  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
  # NOTE: These are the font families that already exist in the [extra] and [community] repos.
  declare -A omitted_font_families=([cantarell]=1 [noto-sans-tamil]=1 [noto-serif]=1
                                    [noto-sans]=1 [fira-sans]=1 [fira-mono]=1
                                    [ubuntu]=1 [ubuntu-mono]=1 [tinos]=1 [arimo]=1
                                    [cousine]=1 [roboto]=1 [roboto-condensed]=1
                                    [inconsolata]=1 [merriweather]=1 [merriweather-sans]=1
                                    [open-sans]=1 [oswald]=1 [quintessential]=1)

  while IFS= read -rd '' file; do
    font_family=$(fc-query -f '%{family[0]|downcase|translate( ,-)}\n' "$file" | sed -n '1p')

    # NOTE: Skip the rest of the loop if we're not supposed to be touching this family
    ((omitted_font_families["$font_family"])) && continue

    pkg_font_path="$pkgdir"/usr/share/fonts/"$font_family"
    install -Dm644 "$file" -t "$pkg_font_path"  # TODO: Check and make sure $font_family is being created

    # NOTE: If the font's license already exists, we don't need to copy the license again.
    src_license_path="${file%/*}"/OFL.txt
    pkg_font_license="$pkgdir"/usr/share/licenses/"$pkgname"/LICENSE."$font_family"
    if [[ -f "$src_license_path" && ! -f "$pkg_font_license" ]]; then
      install -Dm644 "$src_license_path" "$pkg_font_license"
    fi

  done < <(find "$srcdir" -type f -iname \*.ttf -print0)

}
