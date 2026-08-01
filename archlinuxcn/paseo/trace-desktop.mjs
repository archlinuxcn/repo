#!/usr/bin/env node
// Companion to upstream scripts/trace-daemon.mjs: emit the extra files the
// Electron desktop main process needs at runtime, computed by static
// module-graph tracing (@vercel/nft) from the built desktop entry points.
//
// Run from the repo root after the build, with node_modules populated.
// Concatenate with the trace-daemon.mjs output to get the full runtime
// closure installed under /usr/lib/paseo.

import { createRequire } from "node:module";
import { glob } from "node:fs/promises";
import path from "node:path";

const REPO_ROOT = process.cwd();
// Resolve @vercel/nft from the repo's node_modules (this script lives in the
// AUR package dir, outside the npm tree).
const repoRequire = createRequire(path.join(REPO_ROOT, "package.json"));
const { nodeFileTrace } = repoRequire("@vercel/nft");

const entries = [
  "packages/desktop/dist/main.js",
  // Loaded by Electron through an fs path (webPreferences.preload), not
  // require(), so nft cannot reach it from main.js.
  "packages/desktop/dist/preload.js",
  // CLI passthrough entry, resolved at runtime via
  // require.resolve("@getpaseo/cli/dist/run.js") which nft cannot follow.
  "packages/cli/dist/run.js",
];

// Files read at runtime via fs APIs or resolved relative to the install
// layout rather than required through the module graph.
const additionalInputs = [
  // Workspace symlink crossed by the desktop's runtime
  // require.resolve("@getpaseo/cli/...") calls; nft only records symlinks
  // it traverses statically.
  "node_modules/@getpaseo/cli",
  // Spawned by path (never required) for daemon/CLI child processes.
  "packages/desktop/dist/daemon/node-entrypoint-runner.js",
  // Expo web export served to the renderer via the paseo:// protocol.
  "packages/app/dist/**",
  // Window icon candidates resolved relative to packages/desktop/dist.
  "packages/desktop/assets/**",
  // Bundled agent skills, resolved from the repo root in unpackaged mode.
  "skills/**",
  // Workspace manifest next to the desktop dist tree.
  "packages/desktop/package.json",
  // node-pty native addon compiled by `npm rebuild node-pty`;
  // node-gyp-build prefers build/Release over the npm-shipped prebuilds.
  "node_modules/node-pty/build/Release/*.node",
];

const { fileList, warnings } = await nodeFileTrace(entries, {
  base: REPO_ROOT,
  ignore: [
    // Provided by the Electron runtime, never resolved from node_modules.
    "electron/**",
    "node_modules/electron/**",
    "**/*.test.js",
    "**/*.e2e.test.js",
  ],
});

for (const w of warnings) {
  const msg = w.message ?? String(w);
  if (/electron/.test(msg)) continue;
  console.error("trace warning:", msg);
}

const expanded = new Set(fileList);
for (const pattern of additionalInputs) {
  if (pattern.includes("*")) {
    for await (const file of glob(pattern, { cwd: REPO_ROOT })) {
      expanded.add(file);
    }
  } else {
    expanded.add(pattern);
  }
}

for (const p of [...expanded].sort()) {
  console.log(p);
}
