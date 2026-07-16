# 合并去重：知名 AI 项目总表（56 个）

> **合并来源**：`data/projects.csv`(curated 36) + Top-100 AI 子集(32)，去重 12 → 56。
> **采集日期**：2026-07-15　**结构化数据**：[`data/merged-ai-projects.csv`](../data/merged-ai-projects.csv)（含 `tags` 技术栈属性）
> 去重规则：按 `full_name` 去重；`ggerganov/llama.cpp` ↔ `ggml-org/llama.cpp` 同仓库(已重定向)。

## 合并结果

| 来源 | 数量 | 说明 |
|------|------|------|
| curated + top100 | 12 | 两边都有，保留 curated 完整技术栈 + 补 top100 榜号 |
| curated 独有 | 24 | 仅 36 清单（未进 Top-100 总榜） |
| top100 独有 | 20 | 仅历史总榜 AI 子集；部分技术栈待补 |
| **合计** | **56** | |

## 总表（按 Star 排序，含技术栈 tags）

| # | 项目 | ⭐ Stars | 榜号 | 平台 | 主语言 | 技术栈 tags | 来源 |
|---|------|---------|------|------|--------|------------|------|
| 1 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | 382,957 | 6 | AI 助手(跨平台) | TypeScript | TypeScript | top100 |
| 2 | [obra/superpowers](https://github.com/obra/superpowers) | 254,814 | 14 | Agent Skills/… | Shell | Shell, Claude Code | top100 |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | 229,791 | 18 | Agent Skills/… | JavaScript | JavaScript, Claude Code, Codex | top100 |
| 4 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 214,956 | 20 | Agent | Python | Python | top100 |
| 5 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | 196,516 | 23 | Web(自托管/云) | TypeScript | TypeScript, Vue 3, Vue Flow, PrimeVue, … | curated+top100 |
| 6 | [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) | 196,359 | 24 | Library | C++ | C, Python | top100 |
| 7 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | 194,764 | 26 | Agent(实验) | Rust | Rust | top100 |
| 8 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 192,359 | 27 | Agent Skills/… | 未标注 | 未标注, Claude Code | top100 |
| 9 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | 185,906 | 30 | CLI/TUI | TypeScript | TypeScript, Node.js | top100 |
| 10 | [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 185,549 | 32 | Web + CLI | Python | Python, Next.js, React, FastAPI, Postgr… | curated+top100 |
| 11 | [ollama/ollama](https://github.com/ollama/ollama) | 176,144 | 40 | CLI/桌面/API | Go | Go, CLI, llama.cpp | curated+top100 |
| 12 | [mattpocock/skills](https://github.com/mattpocock/skills) | 170,663 | 43 | Agent Skills/… | Shell | Shell, Claude Code | top100 |
| 13 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | 166,028 | 44 | CLI/Library | Python | Python | top100 |
| 14 | [f/prompts.chat](https://github.com/f/prompts.chat) | 165,760 | 45 | 网站(可自托管) | HTML | HTML, ChatGPT | top100 |
| 15 | [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | 164,243 | 47 | Web(自托管) | Python | Python, Gradio, FastAPI, 本地文件, 本地推理 | curated+top100 |
| 16 | [huggingface/transformers](https://github.com/huggingface/transformers) | 162,622 | 48 | Library | Python | Python | curated+top100 |
| 17 | [anthropics/skills](https://github.com/anthropics/skills) | 161,194 | 50 | Agent Skills/… | Python | Python, Claude | top100 |
| 18 | [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | 151,896 | 52 | Web(自托管/云) | Python | Python, React, FastAPI, SQLite, Postgre… | curated+top100 |
| 19 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 151,275 | 53 | API/云/自托管 | TypeScript | TypeScript, Next.js, Node.js | curated+top100 |
| 20 | [langgenius/dify](https://github.com/langgenius/dify) | 148,901 | 54 | Web(自托管/云) | TypeScript | TypeScript, Next.js, React, Tailwind, P… | curated+top100 |
| 21 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | 145,489 | 57 | Web(自托管/Docke… | Python | Python, SvelteKit, FastAPI, SQLite, Chr… | curated+top100 |
| 22 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | 141,925 | 58 | 文档/合集 | 未标注 | 未标注 | top100 |
| 23 | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 141,816 | 59 | Library | Python | Python | curated+top100 |
| 24 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | 137,895 | 63 | CLI | Python | Python, Claude | top100 |
| 25 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 131,518 | 69 | Agent Skills/… | Shell | Shell | top100 |
| 26 | [garrytan/gstack](https://github.com/garrytan/gstack) | 121,936 | 77 | Agent Skills/… | TypeScript | TypeScript, Claude Code | top100 |
| 27 | [github/spec-kit](https://github.com/github/spec-kit) | 121,331 | 78 | CLI/Library | Python | Python | top100 |
| 28 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 121,050 | 79 | 示例库 | Python | Python | top100 |
| 29 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 120,796 | 80 | Web(自托管) | Python | Python, TypeScript, 自定义节点编辑器, aiohttp, … | curated+top100 |
| 30 | [ggml-org/llama.cpp](https://github.com/ggerganov/llama.cpp) | 120,441 | 81 | CLI/Library/S… | C++ | C, 内置 HTTP server, 自研 ggml | curated+top100 |
| 31 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | 117,286 | 86 | 桌面(Tauri) | Rust | Rust, Web, Tauri, Claude, Codex, Gemini | top100 |
| 32 | [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 113,004 | 92 | 教程 | Jupyter Not… | Jupyter Notebook, Jupyter, Azure OpenAI | top100 |
| 33 | [openai/whisper](https://github.com/openai/whisper) | 104,976 | — | Library/CLI | Python | Python | curated |
| 34 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | 86,308 | — | Library/Server | Python | Python, FastAPI OpenAI | curated |
| 35 | [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) | 80,849 | — | Web/CLI | Python | Python, React | curated |
| 36 | [lobehub/lobe-chat](https://github.com/lobehub/lobe-chat) | 79,865 | — | Web(自托管) | TypeScript | TypeScript, Next.js, React, Zustand, Da… | curated |
| 37 | [hiyouga/LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) | 73,296 | — | Web/CLI | Python | Python, Gradio | curated |
| 38 | [binary-husky/gpt_academic](https://github.com/binary-husky/gpt_academic) | 71,084 | — | Web(自托管) | Python | Python, Gradio | curated |
| 39 | [OpenInterpreter/open-interpreter](https://github.com/OpenInterpreter/open-interpreter) | 65,088 | — | CLI | Rust | Rust | curated |
| 40 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | 60,879 | — | Library/云 | TypeScript | TypeScript, Python, TS, PostgreSQL, Qdr… | curated |
| 41 | [microsoft/autogen](https://github.com/microsoft/autogen) | 59,741 | — | Library | Python | Python | curated |
| 42 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 55,556 | — | Library | Python | Python | curated |
| 43 | [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) | 54,636 | — | Web(自托管) | TypeScript | TypeScript, React, MUI, Node.js, Expres… | curated |
| 44 | [run-llama/llama_index](https://github.com/run-llama/llama_index) | 50,865 | — | Library | Python | Python | curated |
| 45 | [oobabooga/text-generation-webui](https://github.com/oobabooga/text-generation-webui) | 47,450 | — | Web/桌面 | Python | Python, Gradio | curated |
| 46 | [Aider-AI/aider](https://github.com/Aider-AI/aider) | 47,398 | — | CLI | Python | Python | curated |
| 47 | [milvus-io/milvus](https://github.com/milvus-io/milvus) | 45,232 | — | Server/云 | Go | Go | curated |
| 48 | [microsoft/DeepSpeed](https://github.com/microsoft/DeepSpeed) | 42,710 | — | Library | Python | Python | curated |
| 49 | [QuivrHQ/quivr](https://github.com/QuivrHQ/quivr) | 39,211 | — | Web(自托管/云) | Python | Python, Next.js, React, Vercel AI, Fast… | curated |
| 50 | [continuedev/continue](https://github.com/continuedev/continue) | 34,883 | — | IDE 插件(VSCode… | TypeScript | TypeScript, React, WebView, Node.js | curated |
| 51 | [TabbyML/tabby](https://github.com/TabbyML/tabby) | 33,701 | — | Web/IDE 插件 | Rust | Rust, React, SQLite, PostgreSQL, 自托管模型 | curated |
| 52 | [qdrant/qdrant](https://github.com/qdrant/qdrant) | 33,292 | — | Server/云 | Rust | Rust | curated |
| 53 | [SillyTavern/SillyTavern](https://github.com/SillyTavern/SillyTavern) | 30,699 | — | Web(自托管) | JavaScript | JavaScript, 原生 JS, jQuery, Node.js, Exp… | curated |
| 54 | [stanford-oval/storm](https://github.com/stanford-oval/storm) | 30,086 | — | Library/CLI | Python | Python | curated |
| 55 | [labring/FastGPT](https://github.com/labring/FastGPT) | 28,979 | — | Web(自托管/云) | TypeScript | TypeScript, Next.js, React, Mantine, No… | curated |
| 56 | [chroma-core/chroma](https://github.com/chroma-core/chroma) | 28,793 | — | Library/Server | Rust | Rust, Python | curated |

## 技术栈 tags 说明

`tags` 字段由每个项目的 `primary_lang / frontend / backend / database / llm_runtime` 提炼归一，作为可筛选/可作徽章展示的属性（如 `Next.js, React, Tailwind, Python, Flask, PostgreSQL`）。完整明细见 CSV 的 `frontend`/`backend`/`database`/`llm_runtime` 列。

> ⚠️ 部分Agent Skills/配置类仓库描述较特殊，star 受 2026 AI 热潮影响，仅作趋势参考。