# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgbase=rofi-themes
pkgname=('rofi-theme-android-1080p'
         'rofi-theme-android-720p'
         'rofi-theme-applet-1080p'
         'rofi-theme-applet-720p'
         'rofi-theme-launcher-1080p'
         'rofi-theme-launcher-720p'
         'rofi-theme-menu-1080p'
         'rofi-theme-menu-720p'
         'rofi-theme-powermenu-1080p'
         'rofi-theme-powermenu-720p'
         'rofi-theme-used'
         'rofi-theme-fonts')
pkgver=1.6.1
pkgrel=2
pkgdesc="A large collection of Rofi based custom Menu, Applets, Launchers & Powermenus"
arch=('any')
url="https://github.com/dctxmei/rofi-themes"
license=('GPL3')
groups=('rofi-themes')
depends=("rofi>=${pkgver}")
optdepends=('papirus-icon-theme: for default icon'
            'xorg-xbacklight: for Backlight'
            'acpi: for Battery'
            'mpc: for MPD'
            'mpd: for MPD'
            'networkmanager: for Network'
            'termite: for Network'
            'systemd: for Powermenu'
            'i3lock: for Powermenu'
            'betterlockscreen: for Powermenu'
            'firefox: for Quicklinks'
            'chromium: for Quicklinks'
            'midori: for Quicklinks'
            'scrot: for Screenshot'
            'viewnior: for Screenshot'
            'coreutils: for Time'
            'alsa-utils: for Volume')
source=("${pkgbase}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('d6eb21bdceaf2016a7310ebfd78b3f73ebd6c4f9d78b007a678de155de50d0e9')

prepare() {
    cd "${srcdir}"/"${pkgbase}-${pkgver}"/
    find 1080p/ -type f -exec sed 's|$HOME/.config/rofi/|/usr/share/rofi/1080p/|' -i {} \;
    find 720p/ -type f -exec sed 's|$HOME/.config/rofi/|/usr/share/rofi/720p/|' -i {} \;
}

package_rofi-theme-used() {
    groups+=('rofi-themes-1080p'
             'rofi-themes-720p')
    conflicts=('rofi-theme-used-git')
    cd "${srcdir}"/"${pkgbase}-${pkgver}"/
    install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/rofi-theme-used/
    install -Dm 644 1080p/bin/usedcpu -t "${pkgdir}"/usr/bin/
    install -Dm 644 1080p/bin/usedram -t "${pkgdir}"/usr/bin/
}

package_rofi-theme-fonts() {
    groups+=('rofi-themes-1080p'
             'rofi-themes-720p')
    conflicts=('rofi-theme-fonts-git')
    cd "${srcdir}"/"${pkgbase}-${pkgver}"/
    cd fonts/
    find . -type d -exec install -vd "${pkgdir}"/usr/share/fonts/rofi-theme-fonts/{} \;
    find . -type f -exec install -vm 644 {} "${pkgdir}"/usr/share/fonts/rofi-theme-fonts/{} \;
}

_package() {
    cd "${srcdir}"/"${pkgbase}-${pkgver}"/
    install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/"${name}-${resolution}"/
    install -d "${pkgdir}"/usr/bin/
    if [[ "${name}" == 'android' ]]; then
        find "${resolution}"/applets/android/ -type d -exec install -vd "${pkgdir}"/usr/share/rofi/{} \;
        find "${resolution}"/applets/android/ -type f -exec install -vm 644 {} "${pkgdir}"/usr/share/rofi/{} \;
        install -Dm 666 "${resolution}"/applets/android/colors.rasi -t "${pkgdir}"/usr/share/rofi/"${resolution}"/applets/android/
        install -d "${pkgdir}"/etc/rofi/"${resolution}"/applets/android/
        ln -s /usr/share/rofi/"${resolution}"/applets/android/colors.rasi "${pkgdir}"/etc/rofi/"${resolution}"/applets/android/colors.rasi
        install -Dm 666 "${resolution}"/applets/android/colors.rasi -t "${pkgdir}"/etc/rofi/"${resolution}"/applets/android/
        ln -fs /etc/rofi/"${resolution}"/applets/android/colors.rasi "${pkgdir}"/usr/share/rofi/"${resolution}"/applets/android/colors.rasi
        install -d "${pkgdir}"/etc/rofi/"${resolution}"/applets/android/
        for scripts in 'apps' 'backlight' 'mpd' 'powermenu' 'quicklinks' 'screenshot' 'volume'; do
            install -Dm 755 "${resolution}"/applets/android/"${scripts}".sh -t "${pkgdir}"/usr/share/rofi/"${resolution}"/applets/android/
            ln -s /usr/share/rofi/"${resolution}"/applets/android/"${scripts}".sh "${pkgdir}"/etc/rofi/"${resolution}"/applets/android/"${scripts}".sh
            ln -s /usr/share/rofi/"${resolution}"/applets/android/"${scripts}".sh "${pkgdir}"/usr/bin/android_"${scripts}"_"${resolution}"
        done
    elif [[ "${name}" == 'applet' ]]; then
        find "${resolution}"/applets/applets/ -type d -exec install -vd "${pkgdir}"/usr/share/rofi/{} \;
        find "${resolution}"/applets/applets/ -type f -exec install -vm 644 {} "${pkgdir}"/usr/share/rofi/{} \;
        find "${resolution}"/applets/styles/ -type d -exec install -vd "${pkgdir}"/usr/share/rofi/{} \;
        find "${resolution}"/applets/styles/ -type f -exec install -vm 644 {} "${pkgdir}"/usr/share/rofi/{} \;
        install -Dm 666 "${resolution}"/applets/styles/colors.rasi -t "${pkgdir}"/usr/share/rofi/"${resolution}"/applets/styles/
        install -d "${pkgdir}"/etc/rofi/"${resolution}"/applets/styles/
        ln -s /usr/share/rofi/"${resolution}"/applets/styles/colors.rasi "${pkgdir}"/etc/rofi/"${resolution}"/applets/styles/colors.rasi
        install -d "${pkgdir}"/etc/rofi/"${resolution}"/applets/applets/
        for scripts in 'apps' 'backlight' 'battery' 'mpd' 'network' 'powermenu' 'quicklinks' 'screenshot' 'time' 'volume'; do
            install -Dm 755 "${resolution}"/applets/applets/"${scripts}".sh -t "${pkgdir}"/usr/share/rofi/"${resolution}"/applets/applets/
            ln -s /usr/share/rofi/"${resolution}"/applets/applets/"${scripts}".sh "${pkgdir}"/etc/rofi/"${resolution}"/applets/applets/"${scripts}".sh
            ln -s /usr/share/rofi/"${resolution}"/applets/applets/"${scripts}".sh "${pkgdir}"/usr/bin/applet_"${scripts}"_"${resolution}"
        done
        install -Dm 755 "${resolution}"/applets/applets/style.sh -t "${pkgdir}"/usr/share/rofi/"${resolution}"/applets/applets/
        ln -s /usr/share/rofi/"${resolution}"/applets/applets/style.sh "${pkgdir}"/etc/rofi/"${resolution}"/applets/applets/style.sh
    elif [[ "${name}" == 'launcher' ]]; then
        find "${resolution}"/launchers/ -type d -exec install -vd "${pkgdir}"/usr/share/rofi/{} \;
        find "${resolution}"/launchers/ -type f -exec install -vm 644 {} "${pkgdir}"/usr/share/rofi/{} \;
        install -Dm 666 "${resolution}"/launchers/colorful/colors.rasi -t "${pkgdir}"/usr/share/rofi/"${resolution}"/launchers/colorful/
        install -d "${pkgdir}"/etc/rofi/"${resolution}"/launchers/colorful/
        ln -s /usr/share/rofi/"${resolution}"/launchers/colorful/colors.rasi "${pkgdir}"/etc/rofi/"${resolution}"/launchers/colorful/colors.rasi
        for colors in 'ribbon' 'slate' 'text'; do
            install -Dm 666 "${resolution}"/launchers/"${colors}"/styles/colors.rasi -t "${pkgdir}"/usr/share/rofi/"${resolution}"/launchers/"${colors}"/styles/
            install -dm 777 "${pkgdir}"/usr/share/rofi/"${resolution}"/launchers/"${colors}"/styles/
            install -d "${pkgdir}"/etc/rofi/"${resolution}"/launchers/"${colors}"/styles/
            ln -s /usr/share/rofi/"${resolution}"/launchers/"${colors}"/styles/colors.rasi "${pkgdir}"/etc/rofi/"${resolution}"/launchers/"${colors}"/styles/colors.rasi
        done
        for scripts in 'colorful' 'misc' 'ribbon' 'slate' 'text'; do
            install -Dm 755 "${resolution}"/launchers/"${scripts}"/launcher.sh -t "${pkgdir}"/usr/share/rofi/"${resolution}"/launchers/"${scripts}"/
            install -d "${pkgdir}"/etc/rofi/"${resolution}"/launchers/"${scripts}"/
            ln -s /usr/share/rofi/"${resolution}"/launchers/"${scripts}"/launcher.sh "${pkgdir}"/etc/rofi/"${resolution}"/launchers/"${scripts}"/launcher.sh
            ln -s /usr/share/rofi/"${resolution}"/launchers/"${scripts}"/launcher.sh "${pkgdir}"/usr/bin/launcher_"${scripts}"_"${resolution}"
        done
    elif [[ "${name}" == 'menu' ]]; then
        find "${resolution}"/applets/menu/ -type d -exec install -vd "${pkgdir}"/usr/share/rofi/{} \;
        find "${resolution}"/applets/menu/ -type f -exec install -vm 644 {} "${pkgdir}"/usr/share/rofi/{} \;
        install -d "${pkgdir}"/etc/rofi/"${resolution}"/applets/menu/
        for scripts in 'apps' 'backlight' 'battery' 'mpd' 'network' 'powermenu' 'quicklinks' 'screenshot' 'time' 'volume'; do
            install -Dm 755 "${resolution}"/applets/menu/"${scripts}".sh -t "${pkgdir}"/usr/share/rofi/"${resolution}"/applets/menu/
            ln -s /usr/share/rofi/"${resolution}"/applets/menu/"${scripts}".sh "${pkgdir}"/etc/rofi/"${resolution}"/applets/menu/"${scripts}".sh
            ln -s /usr/share/rofi/"${resolution}"/applets/menu/"${scripts}".sh "${pkgdir}"/usr/bin/menu_"${scripts}"_"${resolution}"
        done
        install -Dm 755 "${resolution}"/applets/menu/style.sh -t "${pkgdir}"/usr/share/rofi/"${resolution}"/applets/menu/
        install -d "${pkgdir}"/etc/rofi/"${resolution}"/applets/menu/
        ln -s /usr/share/rofi/"${resolution}"/applets/menu/style.sh "${pkgdir}"/etc/rofi/"${resolution}"/applets/menu/style.sh
    elif [[ "${name}" == 'powermenu' ]]; then
        find "${resolution}"/powermenu/ -type d -exec install -vd "${pkgdir}"/usr/share/rofi/{} \;
        find "${resolution}"/powermenu/ -type f -exec install -vm 644 {} "${pkgdir}"/usr/share/rofi/{} \;
        install -Dm 666 "${resolution}"/powermenu/styles/colors.rasi -t "${pkgdir}"/usr/share/rofi/"${resolution}"/powermenu/styles/
        install -dm 777 "${pkgdir}"/usr/share/rofi/"${resolution}"/powermenu/styles/
        install -d "${pkgdir}"/etc/rofi/"${resolution}"/powermenu/styles/
        ln -s /usr/share/rofi/"${resolution}"/powermenu/styles/colors.rasi "${pkgdir}"/etc/rofi/"${resolution}"/powermenu/styles/colors.rasi
        install -Dm 755 "${resolution}"/powermenu/powermenu.sh -t "${pkgdir}"/usr/share/rofi/"${resolution}"/powermenu/
        ln -s /usr/share/rofi/"${resolution}"/powermenu/powermenu.sh "${pkgdir}"/etc/rofi/"${resolution}"/powermenu/powermenu.sh
        ln -s /usr/share/rofi/"${resolution}"/powermenu/powermenu.sh "${pkgdir}"/usr/bin/powermenu_"${resolution}"
    fi
}

main() {
    for _pkgname in "${pkgname[@]}"; do
        unset _groups
        unset _depends
        unset _backup
        if [[ "${_pkgname}" == 'rofi-theme-android-1080p' ]]; then
            _groups=('rofi-themes-1080p')
            _depends=('rofi-theme-applet-1080p')
            _backup=('etc/rofi/1080p/applets/android/colors.rasi'
                     'etc/rofi/1080p/applets/android/apps.sh'
                     'etc/rofi/1080p/applets/android/backlight.sh'
                     'etc/rofi/1080p/applets/android/mpd.sh'
                     'etc/rofi/1080p/applets/android/powermenu.sh'
                     'etc/rofi/1080p/applets/android/quicklinks.sh'
                     'etc/rofi/1080p/applets/android/screenshot.sh'
                     'etc/rofi/1080p/applets/android/volume.sh')
        elif [[ "${_pkgname}" == 'rofi-theme-android-720p' ]]; then
            _groups=('rofi-themes-720p')
            _depends=('rofi-theme-applet-720p')
            _backup=('etc/rofi/720p/applets/android/colors.rasi'
                     'etc/rofi/720p/applets/android/apps.sh'
                     'etc/rofi/720p/applets/android/backlight.sh'
                     'etc/rofi/720p/applets/android/mpd.sh'
                     'etc/rofi/720p/applets/android/powermenu.sh'
                     'etc/rofi/720p/applets/android/quicklinks.sh'
                     'etc/rofi/720p/applets/android/screenshot.sh'
                     'etc/rofi/720p/applets/android/volume.sh')
        elif [[ "${_pkgname}" == 'rofi-theme-applet-1080p' ]]; then
            _groups=('rofi-themes-1080p')
            _backup=('etc/rofi/1080p/applets/styles/colors.rasi'
                     'etc/rofi/1080p/applets/applets/apps.sh'
                     'etc/rofi/1080p/applets/applets/backlight.sh'
                     'etc/rofi/1080p/applets/applets/battery.sh'
                     'etc/rofi/1080p/applets/applets/mpd.sh'
                     'etc/rofi/1080p/applets/applets/network.sh'
                     'etc/rofi/1080p/applets/applets/powermenu.sh'
                     'etc/rofi/1080p/applets/applets/quicklinks.sh'
                     'etc/rofi/1080p/applets/applets/screenshot.sh'
                     'etc/rofi/1080p/applets/applets/style.sh'
                     'etc/rofi/1080p/applets/applets/time.sh'
                     'etc/rofi/1080p/applets/applets/volume.sh')
        elif [[ "${_pkgname}" == 'rofi-theme-applet-720p' ]]; then
            _groups=('rofi-themes-720p')
            _backup=('etc/rofi/720p/applets/styles/colors.rasi'
                     'etc/rofi/720p/applets/applets/apps.sh'
                     'etc/rofi/720p/applets/applets/backlight.sh'
                     'etc/rofi/720p/applets/applets/battery.sh'
                     'etc/rofi/720p/applets/applets/mpd.sh'
                     'etc/rofi/720p/applets/applets/network.sh'
                     'etc/rofi/720p/applets/applets/powermenu.sh'
                     'etc/rofi/720p/applets/applets/quicklinks.sh'
                     'etc/rofi/720p/applets/applets/screenshot.sh'
                     'etc/rofi/720p/applets/applets/style.sh'
                     'etc/rofi/720p/applets/applets/time.sh'
                     'etc/rofi/720p/applets/applets/volume.sh')
        elif [[ "${_pkgname}" == 'rofi-theme-launcher-1080p' ]]; then
            _groups=('rofi-themes-1080p')
            _backup=('etc/rofi/1080p/launchers/ribbon/styles/colors.rasi'
                     'etc/rofi/1080p/launchers/slate/styles/colors.rasi'
                     'etc/rofi/1080p/launchers/text/styles/colors.rasi'
                     'etc/rofi/1080p/launchers/colorful/launcher.sh'
                     'etc/rofi/1080p/launchers/misc/launcher.sh'
                     'etc/rofi/1080p/launchers/ribbon/launcher.sh'
                     'etc/rofi/1080p/launchers/slate/launcher.sh'
                     'etc/rofi/1080p/launchers/text/launcher.sh')
        elif [[ "${_pkgname}" == 'rofi-theme-launcher-720p' ]]; then
            _groups=('rofi-themes-720p')
            _backup=('etc/rofi/720p/launchers/ribbon/styles/colors.rasi'
                     'etc/rofi/720p/launchers/slate/styles/colors.rasi'
                     'etc/rofi/720p/launchers/text/styles/colors.rasi'
                     'etc/rofi/720p/launchers/colorful/launcher.sh'
                     'etc/rofi/720p/launchers/misc/launcher.sh'
                     'etc/rofi/720p/launchers/ribbon/launcher.sh'
                     'etc/rofi/720p/launchers/slate/launcher.sh'
                     'etc/rofi/720p/launchers/text/launcher.sh')
        elif [[ "${_pkgname}" == 'rofi-theme-menu-1080p' ]]; then
            _groups=('rofi-themes-1080p')
            _depends=('rofi-theme-applet-1080p')
            _backup=('etc/rofi/1080p/applets/menu/apps.sh'
                     'etc/rofi/1080p/applets/menu/backlight.sh'
                     'etc/rofi/1080p/applets/menu/battery.sh'
                     'etc/rofi/1080p/applets/menu/mpd.sh'
                     'etc/rofi/1080p/applets/menu/network.sh'
                     'etc/rofi/1080p/applets/menu/powermenu.sh'
                     'etc/rofi/1080p/applets/menu/quicklinks.sh'
                     'etc/rofi/1080p/applets/menu/screenshot.sh'
                     'etc/rofi/1080p/applets/menu/style.sh'
                     'etc/rofi/1080p/applets/menu/time.sh'
                     'etc/rofi/1080p/applets/menu/volume.sh')
        elif [[ "${_pkgname}" == 'rofi-theme-menu-720p' ]]; then
            _groups=('rofi-themes-720p')
            _depends=('rofi-theme-applet-720p')
            _backup=('etc/rofi/720p/applets/menu/apps.sh'
                     'etc/rofi/720p/applets/menu/backlight.sh'
                     'etc/rofi/720p/applets/menu/battery.sh'
                     'etc/rofi/720p/applets/menu/mpd.sh'
                     'etc/rofi/720p/applets/menu/network.sh'
                     'etc/rofi/720p/applets/menu/powermenu.sh'
                     'etc/rofi/720p/applets/menu/quicklinks.sh'
                     'etc/rofi/720p/applets/menu/screenshot.sh'
                     'etc/rofi/720p/applets/menu/style.sh'
                     'etc/rofi/720p/applets/menu/time.sh'
                     'etc/rofi/720p/applets/menu/volume.sh')
        elif [[ "${_pkgname}" == 'rofi-theme-powermenu-1080p' ]]; then
            _groups=('rofi-themes-1080p')
            _backup=('etc/rofi/1080p/powermenu/styles/colors.rasi'
                     'etc/rofi/1080p/powermenu/powermenu.sh')
        elif [[ "${_pkgname}" == 'rofi-theme-powermenu-720p' ]]; then
            _groups=('rofi-themes-720p')
            _backup=('etc/rofi/720p/powermenu/styles/colors.rasi'
                     'etc/rofi/720p/powermenu/powermenu.sh')
        elif [[ "${_pkgname}" == 'rofi-theme-used' ]]; then
            continue
        elif [[ "${_pkgname}" == 'rofi-theme-fonts' ]]; then
            continue
        fi
        eval "package_${_pkgname}() {
            groups+=("${_groups}")
            depends+=("${_depends}"
                      'rofi-theme-used'
                      'rofi-theme-fonts')
            conflicts=("${_pkgname}-git")
            backup=("${_backup[@]}")
            name="$(echo ${_pkgname} | sed 's/rofi-theme-//' | awk -F '-' '{print $1}')"
            resolution="$(echo ${_pkgname} | sed 's/rofi-theme-//' | awk -F '-' '{print $2}')"
            _package
        }"
    done
}

main
