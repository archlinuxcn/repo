_pkgname="skypeforlinux"
_userns="kernel.unprivileged_userns_clone"

post_install() {
    userns="$(sysctl -n $_userns 2>/dev/null)"
    if [[ $? -ne 0 || $userns -ne 1 ]]; then
	echo -ne "\e[34;1m"
	echo ===
	echo === !!! WARNING !!!
	echo ===
	echo === $_userns is not set on this system.
	echo === You will need to set it manually so $_pkgname can start.
	echo ===
    fi
}

post_upgrade() {
    post_install
}
