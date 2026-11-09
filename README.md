# adhooklib

> **An open, tagged ad hook corpus for performance marketers, video editors, and AI agents.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: JSON & CLI](https://img.shields.io/badge/Data-Open%20Corpus-green.svg)](data/hooks.json)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#)

---

## Why an Open Ad Hook Corpus?

Dataset repositories are among the most cited and forked artifacts on GitHub. While static prompt lists quickly go stale, a queryable ad hook corpus provides a structured foundation that video editors, copywriters, and AI agents can query at runtime.

`adhooklib` is an open-source library of high-converting direct-response hooks categorized across verticals, angle types, emotional levers, and visual pattern interrupts.

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
  Synthetic Test Benchmark: 34% 3s-view rate

- [HOOK_007] "Throw away your retinol. Dermatologists in Seoul are using this 1 ingredient."
  Vertical: ecommerce | Angle: contrarian | Format: video_9x16
  Visual Direction: Close up of glass dropper with clear serum
  Synthetic Test Benchmark: 41% 3s-view rate
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
  "test_benchmark": "34% 3s view rate (synthetic testing sprint baseline)"
}
```

---

## Integration with AI Agents

Query `adhooklib` directly in Claude Code, Cursor, or your AI Agent terminal:

```bash
claude "Read adhooklib/data/hooks.json, find 3 contrarian hooks for B2B SaaS, and adapt them into @creative-brief"
```

---

## Contributing Hooks

We welcome PRs adding proven hooks. Each contribution must include:
1. `hook_text` (Verbatim first 3 seconds of audio/text)
2. `angle_type` and `vertical`
3. `visual_cue` (What happens on screen during seconds 0-3)

---

## License
MIT © [Imam Haider (@darhaiderimam)](https://github.com/darhaiderimam)
