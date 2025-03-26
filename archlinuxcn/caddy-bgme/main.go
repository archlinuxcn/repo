// Copyright 2015 Matthew Holt and The Caddy Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Package main is the entry point of the Caddy application.
// Most of Caddy's functionality is provided through modules,
// which can be plugged in by adding their import below.
//
// There is no need to modify the Caddy source code to customize your
// builds. You can easily build a custom Caddy with these simple steps:
//
//  1. Copy this file (main.go) into a new folder
//  2. Edit the imports below to include the modules you want plugged in
//  3. Run `go mod init caddy`
//  4. Run `go install` or `go build` - you now have a custom binary!
//
// Or you can use xcaddy which does it all for you as a command:
// https://github.com/caddyserver/xcaddy
package main

import (
	caddycmd "github.com/caddyserver/caddy/v2/cmd"

	// plug in Caddy modules here
	_ "github.com/caddyserver/caddy/v2/modules/standard"

	// naive proxy
	_ "github.com/caddyserver/forwardproxy"

	// ip sources
	_ "github.com/WeidiDeng/caddy-cloudflare-ip"
	_ "github.com/digilolnet/caddy-bunny-ip"
	_ "github.com/fvbommel/caddy-combine-ip-ranges"
	_ "github.com/fvbommel/caddy-dns-ip-range"
	_ "github.com/xcaddyplugins/caddy-trusted-cloudfront"

	// match
	_ "github.com/lanrat/caddy-dynamic-remoteip"
	_ "github.com/tuzzmaniandevil/caddy-dynamic-clientip"

	// WAF
	_ "github.com/corazawaf/coraza-caddy"

	// cache
	_ "github.com/caddyserver/cache-handler"
	_ "github.com/darkweak/storages/nuts/caddy"

	// dns.providers
	_ "github.com/caddy-dns/cloudflare"

	// encoders
	_ "github.com/dunglas/caddy-cbrotli"

	// storage
	_ "github.com/silinternational/certmagic-storage-dynamodb/v3"

	// geoip
	_ "github.com/zhangjiayin/caddy-geoip2"

	// ratelimit
	_ "github.com/mholt/caddy-ratelimit"

	// response handler
	_ "github.com/caddyserver/replace-response"

	// cli
	_ "github.com/abiosoft/caddy-json-schema"
)

func main() {
	caddycmd.Main()
}
