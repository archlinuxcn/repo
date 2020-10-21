#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.startswith('source=('):
            line = "source=('paw_arch_plymouth_theme_by_kahlil88_d3g34y9.zip::http://web.archive.org/web/20191109074213if_/https://api-da.wixmp.com/_api/download/file?downloadToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsImV4cCI6MTU3MzI4NTkxMywiaWF0IjoxNTczMjg1MzAzLCJqdGkiOiI1ZGM2NmRjMWUwNzE4Iiwib2JqIjpudWxsLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdLCJwYXlsb2FkIjp7InBhdGgiOiJcL2ZcLzhhYTU3MGFkLWU0OTYtNDA4ZC1iZTNiLTIxOTI3MGQ4YzU5N1wvZDNnMzR5OS0xYWQ1MTIxMi00NjA2LTQxMmQtOTRlYS0yODI5NTc0MWM2YTguemlwIiwiYXR0YWNobWVudCI6eyJmaWxlbmFtZSI6InBhd19hcmNoX3BseW1vdXRoX3RoZW1lX2J5X2thaGxpbDg4X2QzZzM0eTkuemlwIn19fQ.GoOsrqsmKaVsmP-JmgSgpHhJde0_eyqQe4PPYie5fIE')"
        print(line)

def post_build():
    aur_post_build()
