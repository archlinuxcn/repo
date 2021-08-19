// SPDX-License-Identifier: BSD-3-Clause

#define _GNU_SOURCE

#include <dlfcn.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <sys/prctl.h>
#include <vlc/vlc.h>
#include <vlc/plugins/vlc_common.h>
#include <vlc/plugins/vlc_stream.h>

typedef int(*fn_vlc_stream_vaControl)(stream_t *s, int query, va_list args);

static fn_vlc_stream_vaControl orig_vlc_stream_vaControl;

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

int vlc_stream_vaControl(stream_t *s, int query, va_list args)
{
    if (query == STREAM_GET_CONTENT_TYPE && is_flac(s->psz_url)) {
        *va_arg(args, char **) = strdup("audio/flac");
        return VLC_SUCCESS;
    } else {
        return orig_vlc_stream_vaControl(s, query, args);
    }
}

static void load_sym(void *ptrfunc, void *override_func, const char *name)
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
    *(void **)ptrfunc = ptr;
}

__attribute__((constructor))
static void init(void)
{
    char progname[16] = {0};
    int rc;

    rc = prctl(PR_GET_NAME, progname);
    if (rc != 0) {
        return;
    }
    if (strcmp(progname, "netease-cloud-m") != 0) {
        return;
    }

    load_sym(&orig_vlc_stream_vaControl, vlc_stream_vaControl, "vlc_stream_vaControl");
}
