import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));

test("a missing TLC dependency returns an error without publishing output", () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "statechart-dependencies-"));
  try {
    const out = path.join(dir, "out");
    const spec = path.join(here, "corpus/Counter/Counter.tla");
    const result = spawnSync(process.execPath, [path.join(here, "../statechart.ts"), spec, "--out", out], {
      encoding: "utf8",
      env: { ...process.env, TLA2TOOLS: "" },
    });
    assert.equal(result.status, 2);
    assert.equal(result.stdout, "");
    assert.match(result.stderr, /Set TLA2TOOLS to the absolute path of tla2tools.jar/);
    assert.deepEqual(fs.readdirSync(dir), []);
  } finally {
    fs.rmSync(dir, { recursive: true, force: true });
  }
});
