# GH PR Summarize

[![GitHub Action](https://img.shields.io/badge/GitHub%20Action-blue?logo=github)](https://github.com/13DJTEQ/gh-pr-summarize)
[![Stars](https://img.shields.io/github/stars/13DJTEQ/gh-pr-summarize?style=social)](https://github.com/13DJTEQ/gh-pr-summarize/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Auto-generates PR summaries with code change explanations, test coverage impact, and deployment risk scoring using AI.

## Features

- **AI-Powered Summaries**: Uses OpenRouter models (GPT-4, Claude, Gemini) for intelligent PR analysis
- **Risk Assessment**: Calculates deployment risk (low/medium/high) based on changes
- **Auto-Commenting**: Posts summary as a comment on the PR
- **Multiple Output Formats**: Markdown or JSON output
- **Free Tier**: Falls back to heuristic summary if no API key provided
- **Zero Config**: Just add the action to your workflow

## Usage

```yaml
name: PR Summary
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  summarize:
    runs-on: ubuntu-latest
    steps:
      - uses: 13DJTEQ/gh-pr-summarize@v1
        with:
          openrouter-api-key: ${{ secrets.OPENROUTER_API_KEY }}
          model: google/gemini-2.5-flash
```

## Inputs

| Input | Required | Default | Description |
|-------|----------|---------|-------------|
| `github-token` | No | `${{ github.token }}` | GitHub token for API access |
| `openrouter-api-key` | No | `''` | OpenRouter API key for AI summaries |
| `model` | No | `google/gemini-2.5-flash` | Model for summarization |
| `output-format` | No | `markdown` | Output format: `markdown` or `json` |
| `auto-comment` | No | `true` | Post summary as PR comment |

## Pricing

- **Free**: Heuristic summary (no AI)
- **Pro ($5/month per user)**: AI models, custom model selection, team config
- **Enterprise ($500/month)**: SSO, audit logs, priority support, private repos

[Subscribe via GitHub Sponsors](https://github.com/sponsors/13DJTEQ)

## License

MIT