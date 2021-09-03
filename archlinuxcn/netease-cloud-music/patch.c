// SPDX-License-Identifier: BSD-3-Clause
/**
 * Copyright (c) 2021 kXuan. All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
 * following conditions are met:
 *
 * 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following
 * disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the
 * following disclaimer in the documentation and/or other materials provided with the distribution.
 * 3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote
 * products derived from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
 * INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
 * WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 */
#define _GNU_SOURCE

#include <dlfcn.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <unistd.h>
#include <vlc/vlc.h>
#include <vlc/plugins/vlc_common.h>
#include <vlc/plugins/vlc_stream.h>

static void *load_sym(void *override_func, const char *name)
{
    void *ptr = dlsym(RTLD_NEXT, name);
    if (ptr == NULL) {
        fprintf(stderr, "Cannot load symbol '%s' %s. Please report bug on AUR.\n", name, dlerror());
        exit(1);
    }
    if (ptr == override_func) {
        fprintf(stderr, "circular reference '%s'. Please report bug on AUR.\n", name);
        exit(1);
    }
    return ptr;
}

static int is_flac(const char *url)
{
    static const char suffix[] = ".flac";
    if (!url) {
        return 0;
    }
    size_t len = strlen(url);
    if (len < sizeof(suffix)) {
        return 0;
    }

    return strcasecmp(url + len - sizeof(suffix) + 1, suffix) == 0;
}

/**
 * The netease cloud music server set the Content-Type of .flac format to mpeg/audio, which results vlc unable to decode
 * the music and play.
 *
 * To make vlc works correctly, we rewrite the Content-Type to audio/flac.
 *
 * @param s
 * @param query
 * @param args
 * @return
 */
int vlc_stream_vaControl(stream_t *s, int query, va_list args)
{
    static typeof(vlc_stream_vaControl) *orig_fn;
    if (orig_fn == NULL) {
        orig_fn = load_sym(vlc_stream_vaControl, __func__);
    }
    if (query == STREAM_GET_CONTENT_TYPE && is_flac(s->psz_url)) {
        *va_arg(args, char **) = strdup("audio/flac");
        return VLC_SUCCESS;
    } else {
        return orig_fn(s, query, args);
    }
}

struct string_with_len {
    const char *s;
    size_t len;
};
#define STRING_WITH_LEN_INIT(s) {s, sizeof(s)-1}

/**
 * drop all library fixes.
 *
 * Library fixes should only be applied to the netease-cloud-music main process. Sometime, netease-cloud-music execute
 * external program, such as `xdg-open`, `kde-open5`. Those external programs use newer version qt and other new
 * libraries. If we don't drop these environment variables, those programs may not work, because some symbol may not
 * exist in the bundled old library.
 *
 * @param path
 * @param argv
 * @param envp
 * @return
 */
int execve(const char *path, char *const argv[], char *const envp[])
{
    static typeof(execve) *orig_fn;
    if (orig_fn == NULL) {
        orig_fn = load_sym(execve, "execve");
    }

    static struct string_with_len drop_env[] = {
        STRING_WITH_LEN_INIT("LD_LIBRARY_PATH="),
        STRING_WITH_LEN_INIT("LD_PRELOAD="),
        STRING_WITH_LEN_INIT("QT_PLUGIN_PATH="),
        STRING_WITH_LEN_INIT("QT_QPA_PLATFORM_PLUGIN_PATH="),
        STRING_WITH_LEN_INIT("QT_QPA_PLATFORM="),
    };

    size_t nenv;
    for (nenv = 0; envp[nenv]; nenv++);

    char *new_envp[nenv + 1];
    char *const *src = envp;
    char **dst = new_envp;

    while (*src) {
        for (int i = 0; i < sizeof(drop_env) / sizeof(*drop_env); ++i) {
            if (strncmp(drop_env[i].s, *src, drop_env[i].len) == 0) {
                goto next_env;
            }
        }
        *dst = *src;
        ++dst;
next_env:
        ++src;
    }

    *dst = NULL;
    return orig_fn(path, argv, new_envp);
}
