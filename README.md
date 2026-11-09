# hooklib

> **An open, tagged ad hook corpus for performance marketers, video editors, and AI agents.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: JSON & CLI](https://img.shields.io/badge/Data-Open%20Corpus-green.svg)](data/hooks.json)
[![Forks Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#)

---

## Why a Public Ad Hook Corpus?

Dataset repositories are the most cited, most forked artifacts on GitHub. While prompt repos get bookmarked and forgotten, a structured dataset becomes a core dependency that other developers and AI agents query at runtime.

`hooklib` is an open-source library of proven ad hooks categorized across verticals, angle types, emotional triggers, and visual patterns.

---

## CLI Usage

### Search by Vertical & Angle
```bash
python cli.py search --vertical ecommerce --angle contrarian
```

### Output
```text
[+] Found 2 matching hooks:

- [HOOK_001] "Stop drinking synthetic chalk. It's destroying your gut."
  Vertical: ecommerce | Angle: contrarian | Format: video_9x16
  Visual Direction: Violently throwing neon powder packet into trash can
  Hook Rate Benchmark: 34%

- [HOOK_007] "Throw away your retinol. Dermatologists in Seoul are using this 1 ingredient."
  Vertical: ecommerce | Angle: contrarian | Format: video_9x16
  Visual Direction: Close up of glass dropper with clear serum
  Hook Rate Benchmark: 41%
```

### Random Inspiration Hook
```bash
python cli.py random --vertical b2b_saas
```

---

## Data Schema (`data/hooks.json`)

```json
{
  "id": "HOOK_001",
  "hook_text": "Stop drinking synthetic chalk. It's destroying your gut.",
  "vertical": "ecommerce",
  "sub_vertical": "supplements",
  "angle_type": "contrarian",
  "emotional_lever": "disgust_skepticism",
  "format": "video_9x16",
  "visual_cue": "Violently throwing neon powder packet into trash can",
  "hold_rate_benchmark": "34%"
}
```

---

## How to Import into Agent Workflows

You can query `hooklib` directly inside Claude Code, Cursor, or your AI Agent:

```bash
claude "Read hooklib/data/hooks.json, find 3 contrarian hooks for B2B SaaS, and use them in @creative-brief"
```

---

## Contributing Hooks

We welcome PRs adding proven hooks. Each contribution must include:
1. `hook_text` (Verbatim first 3 seconds of audio/text)
2. `angle_type` and `vertical`
3. `visual_cue` (What happens on screen during seconds 0-3)
4. Estimated hook rate benchmark

---

## License
MIT © [Haider (@darimamhaider)](https://github.com/darimamhaider)
