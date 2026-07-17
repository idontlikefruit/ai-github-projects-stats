<div align="center">

# 🤖 AI GitHub 知名项目技术选型统计

**统计 GitHub 知名 AI 项目的技术选型：类型 · 前后端 · 数据库 · LLM · 技术栈 tags**

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Projects](https://img.shields.io/badge/projects-136-blue.svg)
![Top100](https://img.shields.io/badge/Top--100_AI-32-orange.svg)
![Stars](https://img.shields.io/github/stars/idontlikefruit/ai-vibe-pick?style=social)
![Last Commit](https://img.shields.io/github/last-commit/idontlikefruit/ai-vibe-pick)
![Data](https://img.shields.io/badge/data%20as%20of-2026--07--16-brightgreen)

</div>

---

## 🧭 AI 技术选型助手（Skill）

> 告诉我你要做什么项目，我基于本仓库 **136 个真实 GitHub AI 项目** 的技术栈数据，给你一套有据可依的选型推荐（不凭空编造，每个推荐都引用真实项目）。

### 怎么用

**方式一（推荐）**：直接描述你的项目，例如：

> 我要做一个企业内部知识库问答平台，需要 RAG + 工作流编排，自托管，团队熟 Python，预计支持多租户。帮我选型。

我会自动调用 `tech-selection` skill，从 `data/projects-metadata.csv` 里筛同类项目（dify / langflow / FastGPT / Quivr …），给出「主语言 / 前端 / 后端 / 数据库 / LLM / 部署」推荐表 + 参考项目 + 替代方案 + 风险提示。

**方式二**：显式触发 `/tech-selection`，再补充项目描述。

### Skill 位置

- 定义文件：[`.claude/skills/tech-selection/SKILL.md`](.claude/skills/tech-selection/SKILL.md)
- 依赖数据：`data/projects-metadata.csv`（若不存在，先 `python3 scripts/upsert_metadata.py` 生成）
- 默认经验基线（数据验证过）：
  - LLM 应用平台 → `Next.js+React` / `Python(FastAPI/Flask)` / `PostgreSQL+Redis+向量库` / 多模型兼容 OpenAI（参考 dify、langflow、FastGPT、Flowise）
  - AI 聊天前端 → `Next.js+React`(LobeHub) 或 `SvelteKit`(Open WebUI)
  - 编程助手 → IDE 插件用 TypeScript(Continue)；自托管推理用 Rust(Tabby)；CLI 用 Python(Aider)
  - 高性能/基础设施 → Rust/Go/C++（ollama / vLLM / llama.cpp / Qdrant）

---

## 📑 目录

- [🧭 AI 技术选型助手（Skill）](#-ai-技术选型助手skill)
- [📊 全站历史总榜 Top-100 分析](#-全站历史总榜-top-100-分析)
- [🔥 Trending 今日热榜产品分析](#-trending-今日热榜产品分析)
- [🏷️ 技术栈 tags（新属性）](#️-技术栈-tags新属性)
- [📋 全部项目元数据（136 个）](#-全部项目元数据136-个)
- [📁 目录结构](#-目录结构)
- [📦 数据文件](#-数据文件)
- [🗺️ 采集字段](#️-采集字段)
- [📈 统计维度](#-统计维度)
- [🔧 采集流程](#-采集流程)

---

## 📊 全站历史总榜 Top-100 分析

> 来源：[EvanLi/Github-Ranking · Top-100-stars](https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md) ｜ 采集：2026-07-15 ｜ 数据：[`data/top-100-stars.csv`](data/top-100-stars.csv) · [`data/source-top-100-stars.md`](data/source-top-100-stars.md)

**一句话结论**：GitHub 全站历史 Star 总榜前 100 里，**32 个是 AI / Agent 生态项目**（占近 1/3），且大量占据榜单**头部**（前 30 名占 12 个）。2026 年的 GitHub 已被 AI / Claude Code 生态深度重塑。

### 类别分布（人工分类，共 100）

| 类别 | 数量 | 占比 |
| :--- | ---: | ---: |
| 🤖 AI / Agent 生态 | 32 | 32% |
| 📚 学习资源 / Awesome / 书籍 | 26 | 26% |
| 🛠️ 工具 / 应用 / 其他 | 18 | 18% |
| 🧩 前端 / UI 框架 | 12 | 12% |
| ⚙️ 系统 / 运行时 / 语言 / 基础设施 | 12 | 12% |

### 主语言分布（精确）

| 语言 | 数量 | 语言 | 数量 |
| :--- | ---: | :--- | ---: |
| Python | 22 | C | 3 |
| TypeScript | 16 | Markdown / Jupyter | 各 2 |
| 未标注 | 13 | Batchfile / Dart / MDX / Java / C# / Swift | 各 1 |
| JavaScript | 10 | | |
| Shell / Rust | 各 6 | | |
| C++ / Go | 各 5 | | |
| HTML | 4 | | |

<details open>
<summary><b>📎 展开查看全部 100 个项目（含 AI 相关标注 + 框架 tags）</b></summary>

| 榜号 | 项目 | ⭐ Stars | 主语言 | AI 相关 | 框架 tags | 简介 |
| :---: | :--- | ---: | :--- | :---: | :--- | :--- |
| 1 | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | 525,238 | Markdown | 否 | 教程 | Master programming by recreating your… |
| 2 | [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | 485,008 | 未标注 | 否 | Awesome 清单 | 😎 Awesome lists about all kinds of in… |
| 3 | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 451,902 | TypeScript | 否 | React, Node.js | freeCodeCamp.org's open-source codeba… |
| 4 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 450,139 | Python | 否 | API 清单 | A collective list of free APIs |
| 5 | [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 392,127 | Python | 否 | 书籍 | :books: Freely available programming … |
| 6 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | 382,957 | TypeScript | 是 | TypeScript | Your own personal AI assistant. Any O… |
| 7 | [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 360,964 | TypeScript | 否 | Next.js, React | Interactive roadmaps, guides and othe… |
| 8 | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | 357,630 | Python | 否 | 教程 | Learn how to design large-scale syste… |
| 9 | [jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university) | 356,226 | 未标注 | 否 | 教程 | A complete computer science study pla… |
| 10 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | 308,221 | Python | 否 | Awesome 清单 | An opinionated list of Python framewo… |
| 11 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 305,529 | 未标注 | 否 | Awesome 清单 | A list of Free Software network servi… |
| 12 | [996icu/996.ICU](https://github.com/996icu/996.ICU) | 276,383 | 未标注 | 否 | 社会议题 | Repo for counting stars and contribut… |
| 13 | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 273,367 | Python | 否 | 教程 | Curated list of project-based tutoria… |
| 14 | [obra/superpowers](https://github.com/obra/superpowers) | 254,814 | Shell | 是 | Shell, Claude Code | An agentic skills framework & softwar… |
| 15 | [react/react](https://github.com/react/react) | 246,497 | JavaScript | 否 | React | The library for web and native user i… |
| 16 | [torvalds/linux](https://github.com/torvalds/linux) | 239,508 | C | 否 | C, Linux 内核 | Linux kernel source tree |
| 17 | [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) | 233,302 | 未标注 | 否 | 清单 | A collection of inspiring lists, manu… |
| 18 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | 229,791 | JavaScript | 是 | JavaScript, Claude Code, Codex | The agent harness performance optimiz… |
| 19 | [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 222,696 | Python | 否 | Python, 算法 | All Algorithms implemented in Python |
| 20 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 214,956 | Python | 是 | Python | The agent that grows with you |
| 21 | [vuejs/vue](https://github.com/vuejs/vue) | 210,158 | TypeScript | 否 | Vue 2 | This is the repo for Vue 2. For Vue 3… |
| 22 | [ossu/computer-science](https://github.com/ossu/computer-science) | 206,093 | HTML | 否 | 教程 | 🎓 Path to a free self-taught educatio… |
| 23 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | 196,468 | TypeScript | 是 | TypeScript, Vue 3, Vue Flow, … | Fair-code workflow automation platfor… |
| 24 | [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) | 196,359 | C++ | 是 | C, Python | An Open Source Machine Learning Frame… |
| 25 | [trekhleb/javascript-algorithms](https://github.com/trekhleb/javascript-algorithms) | 196,236 | JavaScript | 否 | JavaScript, 算法 | 📝 Algorithms and data structures impl… |
| 26 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | 194,764 | Rust | 是 | Rust | An agent-managed museum exhibit, buil… |
| 27 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 192,359 | 未标注 | 是 | 未标注, Claude Code | A single CLAUDE.md file to improve Cl… |
| 28 | [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | 188,725 | Shell | 否 | Shell, Zsh | 🙃   A delightful community-driven (wi… |
| 29 | [microsoft/vscode](https://github.com/microsoft/vscode) | 187,594 | TypeScript | 否 | TypeScript, Electron | Visual Studio Code |
| 30 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | 185,906 | TypeScript | 是 | TypeScript, Node.js | The open source coding agent. |
| 31 | [DigitalPlatDev/FreeDomain](https://github.com/DigitalPlatDev/FreeDomain) | 185,752 | HTML | 否 | HTML | DigitalPlat FreeDomain: Free Domain F… |
| 32 | [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 185,544 | Python | 是 | Python, Next.js, React, FastA… | AutoGPT is the vision of accessible A… |
| 33 | [CyC2018/CS-Notes](https://github.com/CyC2018/CS-Notes) | 184,769 | 未标注 | 否 | 面试 | :books: 技术面试必备基础知识、Leetcode、计算机操作系统、计… |
| 34 | [getify/You-Dont-Know-JS](https://github.com/getify/You-Dont-Know-JS) | 184,598 | 未标注 | 否 | 书籍 | A book series (2 published editions) … |
| 35 | [jackfrued/Python-100-Days](https://github.com/jackfrued/Python-100-Days) | 184,158 | Jupyter Notebook | 否 | Jupyter, Python | Python - 100天从新手到大师 |
| 36 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | 183,170 | Batchfile | 否 | Batchfile | Open-source Windows and Office activa… |
| 37 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | 178,192 | Go | 否 | Awesome 清单 | A curated list of awesome Go framewor… |
| 38 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 178,054 | Python | 否 | Python | A feature-rich command-line audio/vid… |
| 39 | [flutter/flutter](https://github.com/flutter/flutter) | 177,911 | Dart | 否 | Dart, Flutter | Flutter makes it easy and fast to bui… |
| 40 | [ollama/ollama](https://github.com/ollama/ollama) | 176,120 | Go | 是 | Go, CLI, llama.cpp | Get up and running with Kimi-K2.6, GL… |
| 41 | [github/gitignore](https://github.com/github/gitignore) | 174,874 | 未标注 | 否 | 模板 | A collection of useful .gitignore tem… |
| 42 | [twbs/bootstrap](https://github.com/twbs/bootstrap) | 174,475 | MDX | 否 | Bootstrap, JavaScript | The most popular HTML, CSS, and JavaS… |
| 43 | [mattpocock/skills](https://github.com/mattpocock/skills) | 170,663 | Shell | 是 | Shell, Claude Code | Skills for Real Engineers. Straight f… |
| 44 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | 166,028 | Python | 是 | Python | Python tool for converting files and … |
| 45 | [f/prompts.chat](https://github.com/f/prompts.chat) | 165,760 | HTML | 是 | HTML, ChatGPT | f.k.a. Awesome ChatGPT Prompts. Share… |
| 46 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | 165,233 | Python | 否 | Python | :octocat: 分享 GitHub 上有趣、入门级的开源项目。Shar… |
| 47 | [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | 164,241 | Python | 是 | Python, Gradio, FastAPI, 本地文件… | Stable Diffusion web UI |
| 48 | [huggingface/transformers](https://github.com/huggingface/transformers) | 162,612 | Python | 是 | Python | 🤗 Transformers: the model-definition … |
| 49 | [jlevy/the-art-of-command-line](https://github.com/jlevy/the-art-of-command-line) | 161,749 | 未标注 | 否 | 清单 | Master the command line, in one page |
| 50 | [anthropics/skills](https://github.com/anthropics/skills) | 161,194 | Python | 是 | Python, Claude | Public repository for Agent Skills |
| 51 | [Snailclimb/JavaGuide](https://github.com/Snailclimb/JavaGuide) | 157,044 | JavaScript | 否 | Java, 面试 | Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并… |
| 52 | [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | 151,886 | Python | 是 | Python, React, FastAPI, SQLit… | Langflow is a powerful tool for build… |
| 53 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 151,119 | TypeScript | 是 | TypeScript, Next.js, Node.js | The API to search, scrape, and intera… |
| 54 | [langgenius/dify](https://github.com/langgenius/dify) | 148,861 | TypeScript | 是 | TypeScript, Next.js, React, T… | Production-ready platform for agentic… |
| 55 | [airbnb/javascript](https://github.com/airbnb/javascript) | 148,085 | JavaScript | 否 | JavaScript, 风格指南 | JavaScript Style Guide |
| 56 | [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) | 145,736 | C | 否 | C, Android | Display and control your Android devi… |
| 57 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | 145,455 | Python | 是 | Python, SvelteKit, FastAPI, S… | User-friendly AI Interface (Supports … |
| 58 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | 141,925 | 未标注 | 是 | 未标注 | FULL Augment Code, Claude Code, Cluel… |
| 59 | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 141,796 | Python | 是 | Python | The agent engineering platform. |
| 60 | [vercel/next.js](https://github.com/vercel/next.js) | 141,106 | JavaScript | 否 | Next.js, React, JavaScript | The React Framework |
| 61 | [yangshun/tech-interview-handbook](https://github.com/yangshun/tech-interview-handbook) | 140,900 | TypeScript | 否 | React, TypeScript | Curated coding interview preparation … |
| 62 | [ytdl-org/youtube-dl](https://github.com/ytdl-org/youtube-dl) | 140,711 | Python | 否 | Python | Command-line program to download vide… |
| 63 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | 137,895 | Python | 是 | Python, Claude | Claude Code is an agentic coding tool… |
| 64 | [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | 136,607 | C | 否 | C++, C# | Microsoft PowerToys is a collection o… |
| 65 | [golang/go](https://github.com/golang/go) | 135,396 | Go | 否 | Go | The Go programming language |
| 66 | [labuladong/fucking-algorithm](https://github.com/labuladong/fucking-algorithm) | 134,828 | Markdown | 否 | 算法 | Crack LeetCode, not only how, but als… |
| 67 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | 133,006 | TypeScript | 否 | TypeScript | Collection of publicly available IPTV… |
| 68 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 131,551 | TypeScript | 否 | Tauri, TypeScript | A modern GUI client based on Tauri, d… |
| 69 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 131,518 | Shell | 是 | Shell | A complete AI agency at your fingerti… |
| 70 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 129,227 | HTML | 否 | 清单 | A list of SaaS, PaaS and IaaS offerin… |
| 71 | [krahets/hello-algo](https://github.com/krahets/hello-algo) | 128,516 | Java | 否 | Java, 算法 | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持简中、繁… |
| 72 | [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code) | 128,386 | JavaScript | 否 | JavaScript | Coding articles to level up your deve… |
| 73 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 127,493 | TypeScript | 否 | React, TypeScript, Canvas | Virtual whiteboard for sketching hand… |
| 74 | [react/react-native](https://github.com/react/react-native) | 126,199 | C++ | 否 | React Native, C++ | A framework for building native appli… |
| 75 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 123,793 | Go | 否 | Go | Production-Grade Container Scheduling… |
| 76 | [electron/electron](https://github.com/electron/electron) | 122,000 | C++ | 否 | C++, JavaScript, Electron | :electron: Build cross-platform deskt… |
| 77 | [garrytan/gstack](https://github.com/garrytan/gstack) | 121,936 | TypeScript | 是 | TypeScript, Claude Code | Use Garry Tan's exact Claude Code set… |
| 78 | [github/spec-kit](https://github.com/github/spec-kit) | 121,331 | Python | 是 | Python | 💫 Toolkit to help you get started wit… |
| 79 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 121,050 | Python | 是 | Python | 100+ AI Agent & RAG apps you can actu… |
| 80 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 120,758 | Python | 是 | Python, TypeScript, 自定义节点编辑器,… | The most powerful and modular diffusi… |
| 81 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 120,405 | C++ | 是 | C, C++, ggml | LLM inference in C/C++ |
| 82 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 119,124 | TypeScript | 否 | React, Radix UI, Tailwind | A set of beautifully-designed, access… |
| 83 | [nodejs/node](https://github.com/nodejs/node) | 118,368 | JavaScript | 否 | JavaScript, C++, V8 | Node.js JavaScript runtime ✨🐢🚀✨ |
| 84 | [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 118,254 | Rust | 否 | Rust, Flutter | An open-source remote desktop applica… |
| 85 | [justjavac/free-programming-books-zh_CN](https://github.com/justjavac/free-programming-books-zh_CN) | 117,349 | 未标注 | 否 | 书籍 | :books: 免费的计算机编程类中文书籍，欢迎投稿 |
| 86 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | 117,286 | Rust | 是 | Rust, Web, Tauri, Claude, Cod… | A cross-platform desktop All-in-One a… |
| 87 | [Hack-with-Github/Awesome-Hacking](https://github.com/Hack-with-Github/Awesome-Hacking) | 116,226 | 未标注 | 否 | Awesome 清单 | A collection of various awesome lists… |
| 88 | [rust-lang/rust](https://github.com/rust-lang/rust) | 114,748 | Rust | 否 | Rust | Empowering everyone to build reliable… |
| 89 | [godotengine/godot](https://github.com/godotengine/godot) | 114,114 | C++ | 否 | C++, Godot | Godot Engine – Multi-platform 2D and … |
| 90 | [mrdoob/three.js](https://github.com/mrdoob/three.js) | 113,741 | JavaScript | 否 | WebGL, JavaScript | JavaScript 3D Library. |
| 91 | [d3/d3](https://github.com/d3/d3) | 113,221 | Shell | 否 | JavaScript, D3 | Bring data to life with SVG, Canvas a… |
| 92 | [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 113,004 | Jupyter Notebook | 是 | Jupyter Notebook, Jupyter, Az… | 21 Lessons, Get Started Building with… |
| 93 | [2dust/v2rayN](https://github.com/2dust/v2rayN) | 111,368 | C# | 否 | C# | A GUI client for Windows, Linux and m… |
| 94 | [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 109,917 | TypeScript | 否 | TypeScript | TypeScript is a superset of JavaScrip… |
| 95 | [axios/axios](https://github.com/axios/axios) | 109,107 | JavaScript | 否 | JavaScript | Promise based HTTP client for the bro… |
| 96 | [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 109,064 | Rust | 否 | Rust, Web, Tauri | Build smaller, faster, and more secur… |
| 97 | [fatedier/frp](https://github.com/fatedier/frp) | 108,045 | Go | 否 | Go | A fast reverse proxy to help you expo… |
| 98 | [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) | 107,832 | Swift | 否 | Awesome 清单 |  This project is dedicated to collec… |
| 99 | [papers-we-love/papers-we-love](https://github.com/papers-we-love/papers-we-love) | 107,831 | Shell | 否 | 论文 | Papers from the computer science comm… |
| 100 | [denoland/deno](https://github.com/denoland/deno) | 107,806 | Rust | 否 | Rust, TypeScript, V8 | A modern runtime for JavaScript and T… |
</details>

### 关键观察

1. **AI 占据头部**：前 10 名占 4 个、前 30 名占 12 个。
2. **Claude Code 生态爆炸**：32 个里 ≥10 个直接围绕 Claude Code / Agent Skills / 提示词——「AI 编程助手 + 技能/配置生态」是 2026 最热方向。
3. **语言格局**：Python + TypeScript 主导；Rust 追平 Shell，超过 Go/C++。
4. **榜单性质变化**：传统 awesome-list / 学习资源仍占 26 个，但增速已被 AI 反超。

> ⚠️ 部分 Agent Skills/配置类仓库（openclaw、claw-code、ECC、gstack 等）描述特殊，star 受 AI 热潮影响，仅作趋势参考；技术选型优先看 dify/langchain/langflow/ollama/llama.cpp/vLLM/ComfyUI 等工程级项目。

---

## 🔥 Trending 今日热榜产品分析

> 来源：https://github.com/trending （全语言 daily，无官方 API，抓取 HTML 解析）｜采集：2026-07-16 ｜ 数据：[`data/trending-daily.csv`](data/trending-daily.csv) · 完整分析：[`reports/trending-analysis.md`](reports/trending-analysis.md)

| 今日 ⭐ | 项目 | ⭐ Stars | 主语言 | AI 相关 | 框架 tags | 简介 |
| ---: | :--- | ---: | :--- | :---: | :--- | :--- |
| +2,130 | [mattpocock/skills](https://github.com/mattpocock/skills) | 174,452 | Shell | 是 | Shell, Claude Code | Skills for Real Engineers. Straig… |
| +1,664 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | 74,149 | TypeScript | 否 | TypeScript, React, Canvas | The open-source CapCut alternative |
| +1,277 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | 11,086 | CSS | 是 | Claude Code, Cursor, 设计技能 | Anti-AI-slop design skill for Cla… |
| +1,236 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 123,021 | Python | 是 | Python | 100+ AI Agent & RAG apps you can … |
| +949 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | 15,116 | HTML | 否 | HTML, 数据集 | 1,324-exercise fitness dataset — … |
| +915 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | 24,351 | Python | 是 | Python, 交易 Agent | "Vibe-Trading: Your Personal Trad… |
| +725 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | 6,275 | TypeScript | 是 | TypeScript, AI/ML 资料 | Become a cracked AI/ML Research E… |
| +471 | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | 5,031 | Rust | 否 | Rust, 命令守卫 | The Destructive Command Guard (dc… |
| +340 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | 40,225 | JavaScript | 是 | JavaScript, Claude Code, … | Marketing skills for Claude Code … |
| +299 | [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter) | 66,031 | Rust | 是 | Rust | A coding agent for low-cost models |
| +172 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 26,952 | Python | 是 | Python, 教育 Agent | DeepTutor: Lifelong Personalized … |
| +110 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | 42,769 | TypeScript | 是 | TypeScript, Grok, 自托管 | 💖🧸 Self hosted, you-owned Grok Co… |
| +103 | [injaneity/pi-computer-use](https://github.com/injaneity/pi-computer-use) | 1,414 | TypeScript | 是 | TypeScript, Computer Use,… | Let Pi control your apps on MacOS… |
| +38 | [YimMenu/YimMenuV2](https://github.com/YimMenu/YimMenuV2) | 1,514 | C++ | 否 | C++, 游戏模组 | Experimental menu for GTA 5: Enha… |

**产品分析**：① AI 浓度 **~71%（10/14）**，比历史总榜 32% 还高 → AI 是当前最大增量；② 最热风向 = **Claude Code Skills 生态**（hallmark / mattpocock/skills / marketingskills）；③ 新涌现垂直 Agent（交易/教育/Computer-Use/伴侣）+ 衍生刚需（反 AI-slop、Agent 安全）；④ 与 56 总表仅 3 个重叠 → trending 反映当期新项目，与总榜(存量)互补。

---

## 🏷️ 技术栈 tags（新属性）

每个项目新增 **`tags`** 字段，由 `primary_lang / frontend / backend / database / llm_runtime` 提炼归一，作为可筛选/可作徽章展示的属性。例：

> **Dify** → `Next.js` `React` `Tailwind` `Python` `Flask` `PostgreSQL`
> **n8n** → `TypeScript` `Vue 3` `Vue Flow` `PrimeVue` `Node.js` `PostgreSQL`

完整 tags 见 [`data/merged-ai-projects.csv`](data/merged-ai-projects.csv) 的 `tags` 列，卡片式展示见 [`reports/all-projects-metadata.md`](reports/all-projects-metadata.md)。

---

## 📋 全部项目元数据（136 个）

> 以 `full_name` 为主键 **upsert（更新或插入）** 合并三个来源：`projects.csv`(curated) + `top-100-stars.csv` + `trending-daily.csv` → 共 **136 个**（56 合并 + 68 Top100非AI + 12 Trending新项目），其中 AI 相关 64 个。
> 生成脚本：`python3 scripts/upsert_metadata.py` → `data/projects-metadata.csv`（幂等，重复运行只更新或插入，不清空已有字段）。
> 每个项目一张完整元数据卡片见 [`reports/all-projects-metadata.md`](reports/all-projects-metadata.md)；Top-100 单独的完整卡片见 [`reports/top-100-metadata.md`](reports/top-100-metadata.md)。

<details>
<summary><b>📎 展开查看 56 个 AI 项目完整元数据宽表（含前后端/数据库/LLM，按 Star 降序）｜全部 136 个见 reports/all-projects-metadata.md</b></summary>

| # | 项目 | ⭐ | 榜号 | 平台 | 主语言 | 前端 | 后端 | 数据库 | LLM | License | 技术栈 tags | 来源 |
| :---: | :--- | ---: | :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | 382,957 | 6 | AI 助手(跨平台) | TypeScript | — | — | — | 多模型 | —(待补) | TypeScript | top100 |
| 2 | [obra/superpowers](https://github.com/obra/superpowers) | 254,814 | 14 | Agent Skills/配置 | Shell | — | Shell | — | Claude Code | —(待补) | Shell, Claude Code | top100 |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | 229,791 | 18 | Agent Skills/配置 | JavaScript | — | JavaScript | — | Claude Code | —(待补) | JavaScript, Claude Code, Codex | top100 |
| 4 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 214,956 | 20 | Agent | Python | — | Python | — | 多模型 | —(待补) | Python | top100 |
| 5 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | 196,516 | 23 | Web(自托管/云) | TypeScript | Vue 3 + Vue Flow | Node.js | SQLite/Postgres | OpenAI/Anthropic | NOASSERTION | TypeScript, Vue 3, Vue Flow, PrimeVue | curated+top100 |
| 6 | [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) | 196,359 | 24 | Library | C++ | — | C++/Python(库) | — | — | —(待补) | C, Python | top100 |
| 7 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | 194,764 | 26 | Agent(实验) | Rust | — | Rust | — | — | —(待补) | Rust | top100 |
| 8 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 192,359 | 27 | Agent Skills/配置 | 未标注 | — | — | — | Claude Code | —(待补) | 未标注, Claude Code | top100 |
| 9 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | 185,906 | 30 | CLI/TUI | TypeScript | — | TypeScript(Node) | — | 多模型 | —(待补) | TypeScript, Node.js | top100 |
| 10 | [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 185,549 | 32 | Web + CLI | Python | Next.js(React) | Python(FastAPI) | PostgreSQL | 多模型 | NOASSERTION | Python, Next.js, React, FastAPI | curated+top100 |
| 11 | [ollama/ollama](https://github.com/ollama/ollama) | 176,144 | 40 | CLI/桌面/API | Go | —(CLI/原生桌面) | Go | — | llama.cpp | MIT | Go, CLI, llama.cpp | curated+top100 |
| 12 | [mattpocock/skills](https://github.com/mattpocock/skills) | 170,663 | 43 | Agent Skills/配置 | Shell | — | Shell | — | Claude Code | —(待补) | Shell, Claude Code | top100 |
| 13 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | 166,028 | 44 | CLI/Library | Python | — | Python(库) | — | — | —(待补) | Python | top100 |
| 14 | [f/prompts.chat](https://github.com/f/prompts.chat) | 165,760 | 45 | 网站(可自托管) | HTML | HTML | — | — | ChatGPT | —(待补) | HTML, ChatGPT | top100 |
| 15 | [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | 164,243 | 47 | Web(自托管) | Python | Gradio | Python(Gradio) | —(本地文件) | 本地推理 | AGPL-3.0 | Python, Gradio, FastAPI | curated+top100 |
| 16 | [huggingface/transformers](https://github.com/huggingface/transformers) | 162,622 | 48 | Library | Python | — | Python(库) | — | — | Apache-2.0 | Python | curated+top100 |
| 17 | [anthropics/skills](https://github.com/anthropics/skills) | 161,194 | 50 | Agent Skills/配置 | Python | — | Python | — | Claude | —(待补) | Python, Claude | top100 |
| 18 | [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | 151,896 | 52 | Web(自托管/云) | Python | React | Python(FastAPI) | SQLite/Postgres | 多模型 | MIT | Python, React, FastAPI, SQLite | curated+top100 |
| 19 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 151,275 | 53 | API/云/自托管 | TypeScript | Next.js | Node.js | — | 多模型 | AGPL-3.0 | TypeScript, Next.js, Node.js | curated+top100 |
| 20 | [langgenius/dify](https://github.com/langgenius/dify) | 148,901 | 54 | Web(自托管/云) | TypeScript | Next.js+React+Tailwind | Python(Flask) | PostgreSQL+Redis | 多模型/兼容 OpenAI | NOASSERTION | TypeScript, Next.js, React, Tailwind, Python, Flask | curated+top100 |
| 21 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | 145,489 | 57 | Web(自托管/Docker) | Python | Svelte(SvelteKit) | Python(FastAPI) | SQLite/ChromaDB | Ollama/OpenAI | NOASSERTION | Python, SvelteKit, FastAPI, SQLite | curated+top100 |
| 22 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | 141,925 | 58 | 文档/合集 | 未标注 | — | — | — | — | —(待补) | 未标注 | top100 |
| 23 | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 141,816 | 59 | Library | Python | — | Python(库,含 LangServe) | — | 多模型/兼容 OpenAI | MIT | Python | curated+top100 |
| 24 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | 137,895 | 63 | CLI | Python | — | Python | — | Claude | —(待补) | Python, Claude | top100 |
| 25 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 131,518 | 69 | Agent Skills/配置 | Shell | — | Shell | — | 多模型 | —(待补) | Shell | top100 |
| 26 | [garrytan/gstack](https://github.com/garrytan/gstack) | 121,936 | 77 | Agent Skills/配置 | TypeScript | — | TypeScript | — | Claude Code | —(待补) | TypeScript, Claude Code | top100 |
| 27 | [github/spec-kit](https://github.com/github/spec-kit) | 121,331 | 78 | CLI/Library | Python | — | Python(库) | — | 多模型 | —(待补) | Python | top100 |
| 28 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 121,050 | 79 | 示例库 | Python | — | Python | — | 多模型 | —(待补) | Python | top100 |
| 29 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 120,796 | 80 | Web(自托管) | Python | TypeScript(节点编辑器) | Python(aiohttp) | — | 本地推理 | GPL-3.0 | Python, TypeScript, aiohttp | curated+top100 |
| 30 | [ggml-org/llama.cpp](https://github.com/ggerganov/llama.cpp) | 120,441 | 81 | CLI/Library/Server | C++ | — | C/C++(内置 HTTP server) | — | 自研 ggml | MIT | C, C++, 内置 HTTP server | curated+top100 |
| 31 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | 117,286 | 86 | 桌面(Tauri) | Rust | Web(Tauri) | Rust | — | Claude/Codex/Gemini | —(待补) | Rust, Tauri, Claude, Codex, Gemini | top100 |
| 32 | [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 113,004 | 92 | 教程 | Jupyter | — | Jupyter | — | Azure OpenAI | —(待补) | Jupyter, Azure OpenAI | top100 |
| 33 | [openai/whisper](https://github.com/openai/whisper) | 104,976 | — | Library/CLI | Python | — | Python(库) | — | — | MIT | Python | curated |
| 34 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | 86,308 | — | Library/Server | Python | — | Python(FastAPI) | — | 多模型 | Apache-2.0 | Python, FastAPI, OpenAI 兼容 | curated |
| 35 | [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) | 80,849 | — | Web/CLI | Python | React | Python(运行时) | — | 多模型 | NOASSERTION | Python, React | curated |
| 36 | [lobehub/lobe-chat](https://github.com/lobehub/lobe-chat) | 79,865 | — | Web(自托管) | TypeScript | Next.js+React+Zustand | Next.js Server | IndexedDB | OpenAI/Anthropic | NOASSERTION | TypeScript, Next.js, React, Zustand | curated |
| 37 | [hiyouga/LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) | 73,296 | — | Web/CLI | Python | Gradio | Python | — | 本地 | Apache-2.0 | Python, Gradio | curated |
| 38 | [binary-husky/gpt_academic](https://github.com/binary-husky/gpt_academic) | 71,084 | — | Web(自托管) | Python | Gradio | Python | — | 多模型 | GPL-3.0 | Python, Gradio | curated |
| 39 | [OpenInterpreter/open-interpreter](https://github.com/OpenInterpreter/open-interpreter) | 65,088 | — | CLI | Rust | — | Rust | — | 多模型 | Apache-2.0 | Rust | curated |
| 40 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | 60,879 | — | Library/云 | TypeScript | — | Python+TS SDK | PostgreSQL/Qdrant | 多模型 | Apache-2.0 | TypeScript, Python, PostgreSQL, Qdrant | curated |
| 41 | [microsoft/autogen](https://github.com/microsoft/autogen) | 59,741 | — | Library | Python | —(Studio: React) | Python | — | 多模型 | CC-BY-4.0 | Python | curated |
| 42 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 55,556 | — | Library | Python | — | Python(库) | — | 多模型 | MIT | Python | curated |
| 43 | [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) | 54,636 | — | Web(自托管) | TypeScript | React+MUI | Node.js(Express) | SQLite/Postgres | LangChain | NOASSERTION | TypeScript, React, MUI, Node.js, Express | curated |
| 44 | [run-llama/llama_index](https://github.com/run-llama/llama_index) | 50,865 | — | Library | Python | — | Python(库) | — | 多模型 | MIT | Python | curated |
| 45 | [oobabooga/text-generation-webui](https://github.com/oobabooga/text-generation-webui) | 47,450 | — | Web/桌面 | Python | Gradio | Python | — | 本地 | AGPL-3.0 | Python, Gradio | curated |
| 46 | [Aider-AI/aider](https://github.com/Aider-AI/aider) | 47,398 | — | CLI | Python | — | Python(库) | — | 多模型 | Apache-2.0 | Python | curated |
| 47 | [milvus-io/milvus](https://github.com/milvus-io/milvus) | 45,232 | — | Server/云 | Go | — | Go | — | — | Apache-2.0 | Go | curated |
| 48 | [microsoft/DeepSpeed](https://github.com/microsoft/DeepSpeed) | 42,710 | — | Library | Python | — | Python(库) | — | — | Apache-2.0 | Python | curated |
| 49 | [QuivrHQ/quivr](https://github.com/QuivrHQ/quivr) | 39,211 | — | Web(自托管/云) | Python | Next.js(React) | Python(FastAPI)+Celery | PostgreSQL+PgVector | 多模型 | NOASSERTION | Python, Next.js, React, FastAPI, PgVector | curated |
| 50 | [continuedev/continue](https://github.com/continuedev/continue) | 34,883 | — | IDE 插件(VSCode/JetBrains) | TypeScript | React(WebView) | TypeScript(Node) | — | 多模型/本地 | Apache-2.0 | TypeScript, React, Node.js | curated |
| 51 | [TabbyML/tabby](https://github.com/TabbyML/tabby) | 33,701 | — | Web/IDE 插件 | Rust | React | Rust | SQLite/Postgres | 自托管模型 | NOASSERTION | Rust, React, SQLite, PostgreSQL | curated |
| 52 | [qdrant/qdrant](https://github.com/qdrant/qdrant) | 33,292 | — | Server/云 | Rust | — | Rust | — | — | Apache-2.0 | Rust | curated |
| 53 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | 30,699 | — | Web(自托管) | JavaScript | 原生 JS/jQuery | Node.js(Express) | — | OpenAI/本地 | AGPL-3.0 | JavaScript, jQuery, Node.js, Express | curated |
| 54 | [stanford-oval/storm](https://github.com/stanford-oval/storm) | 30,086 | — | Library/CLI | Python | — | Python(库) | — | 多模型 | MIT | Python | curated |
| 55 | [labring/FastGPT](https://github.com/labring/FastGPT) | 28,979 | — | Web(自托管/云) | TypeScript | Next.js+Mantine | Node.js(Next.js API) | MongoDB+PostgreSQL | 多模型 | NOASSERTION | TypeScript, Next.js, React, Mantine, Node.js | curated |
| 56 | [chroma-core/chroma](https://github.com/chroma-core/chroma) | 28,793 | — | Library/Server | Rust | — | Rust+Python | — | — | Apache-2.0 | Rust, Python | curated |

</details>

> ⚠️ top100 独有的 20 个项目（#1–4, #6–9, #12–14, #17, #22, #24–28, #31–32）部分技术栈字段为「—(待补)」，待逐个深度拆解。

---

## 📁 目录结构

```
ai-vibe-pick/
├── README.md                       # 本文件（GitHub 风格：徽章/TOC/折叠/全量元数据/Skill）
├── .claude/skills/tech-selection/  # AI 技术选型 Skill
│   └── SKILL.md
├── scripts/
│   └── upsert_metadata.py          # upsert 脚本(以 full_name 为主键更新或插入)
├── data/
│   ├── source-top-100-stars.md     # Top-100 原始榜单存档
│   ├── top-100-stars.csv           # Top-100 结构化(含 category/ai_related/tags)
│   ├── projects.csv                # 36 个 AI 项目技术选型
│   ├── merged-ai-projects.csv      # 合并去重 56 个(含 tags/source/rank_top100)
│   ├── trending-daily.csv         # Trending 今日热榜(14 个,含 ai_related/tags)
│   └── projects-metadata.csv      # ✅ 规范化元数据存储(136 个,upsert 生成)
└── reports/
    ├── summary.md                 # 36 个 AI 项目技术选型统计
    ├── merged-ai-projects.md      # 合并 56 个总表(含 tags 列)
    ├── trending-analysis.md       # Trending 今日热榜产品分析
    ├── top-100-metadata.md        # Top-100 完整元数据卡片(100 张)
    └── all-projects-metadata.md   # 全部 136 个项目元数据卡片
```

## 📦 数据文件

| 文件 | 说明 |
| :--- | :--- |
| [`data/projects-metadata.csv`](data/projects-metadata.csv) | ✅ **规范化元数据存储 136 个**，23 字段，upsert 生成（含 `tags`/`ai_related`/`rank_top100`/`trending_today`/`sources`） |
| [`scripts/upsert_metadata.py`](scripts/upsert_metadata.py) | upsert 脚本：合并三来源为 `projects-metadata.csv`（幂等：更新或插入，不清空已有字段） |
| [`.claude/skills/tech-selection/SKILL.md`](.claude/skills/tech-selection/SKILL.md) | 🧭 **AI 技术选型 Skill**：按项目描述 + 数据推荐栈 |
| [`reports/all-projects-metadata.md`](reports/all-projects-metadata.md) | **136 个项目完整元数据卡片**，每项一张（含 shields 徽章） |
| [`reports/top-100-metadata.md`](reports/top-100-metadata.md) | Top-100 完整元数据卡片（100 张） |
| [`reports/merged-ai-projects.md`](reports/merged-ai-projects.md) | 合并 56 个总表（含技术栈 tags 列） |
| [`data/trending-daily.csv`](data/trending-daily.csv) | Trending 今日热榜 14 个（今日新增/总 star/语言/AI相关/tags） |
| [`reports/trending-analysis.md`](reports/trending-analysis.md) | Trending 产品分析（AI 浓度/Skills 生态/垂直 Agent） |
| [`reports/summary.md`](reports/summary.md) | 36 个 AI 项目选型统计 + 分布图表 + 选型建议 |
| [`data/top-100-stars.csv`](data/top-100-stars.csv) | 全站历史总榜 Top-100（rank/stars/forks/language/category/ai_related/tags） |
| [`data/merged-ai-projects.csv`](data/merged-ai-projects.csv) | 合并去重 56 个，19 字段 |
| [`data/projects.csv`](data/projects.csv) | 36 个 AI 项目 14 字段技术选型表 |

## 🗺️ 采集字段

| 字段 | 说明 |
| :--- | :--- |
| name | 项目名称 |
| repo / url | GitHub 仓库地址 |
| stars | Star 数（采集日期） |
| rank_top100 | 历史总榜榜号（未进总榜为空） |
| category | 类型（LLM 应用 / Agent 框架 / RAG / 编程助手 / 模型推理 等） |
| platform | 平台形态（Web / CLI / IDE 插件 / Library / Server / 桌面 …） |
| primary_lang / dev_langs | 主语言 / 开发语言 |
| frontend | 前端技术栈 |
| backend | 后端技术栈 |
| database | 数据库 / 存储 |
| llm_runtime | LLM / 推理后端 |
| **tags** | **技术栈标签（新增，可作徽章/筛选）** |
| license | 开源协议 |
| owner / company | 维护方 |
| source | 来源（curated / top100 / curated+top100） |
| description | 简介 |
| last_updated | 采集日期 |

## 📈 统计维度

- 项目类型分布 · 前端选型分布（React / Vue / Next.js / Svelte）· 后端语言分布（Python / Node / Go / Rust）
- 后端框架分布（FastAPI / Express / Flask）· 数据库选型 · LLM/推理后端 · **技术栈 tags Top-N**

## 🔧 采集流程

1. 拉取 GitHub API（star/语言/协议/描述）与 Trending 页面 HTML
2. 各来源打 `tags` 与 `ai_related` 标注
3. **upsert**：`python3 scripts/upsert_metadata.py` 以 `full_name` 为主键把三来源（projects/top-100/trending）更新或插入到 `data/projects-metadata.csv`（llama.cpp 别名处理；幂等不清空已有字段）
4. 在 `reports/` 输出统计报告与全量元数据卡片（136 + 100）
5. README GitHub 风格展示（徽章 / TOC / 折叠 / 对齐表格 / Skill 使用入口）
