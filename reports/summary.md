# GitHub 知名 AI 项目技术选型统计

> 数据采集日期：**2026-07-15**
> 数据来源：GitHub REST API（star 数、主语言、协议、描述为接口实时返回）+ 各仓库公开技术栈整理。
> 完整结构化数据见 [`../data/projects.csv`](../data/projects.csv)，共 **36** 个项目。
> 技术栈以官方仓库实际为准；标注 `NOASSERTION` 表示使用自定义/附加条款协议。

---

## 一、按 Star 排行的总表

| # | 项目 | ⭐ Stars | 类型 | 主语言 | 前端 | 后端 | 链接 |
|---|------|---------|------|--------|------|------|------|
| 1 | n8n | 196516 | 工作流/Agent 平台 | TypeScript | Vue 3 | Node.js | [repo](https://github.com/n8n-io/n8n) |
| 2 | AutoGPT | 185549 | 编程/自主 Agent | Python | Next.js | FastAPI | [repo](https://github.com/Significant-Gravitas/AutoGPT) |
| 3 | Ollama | 176144 | 本地模型运行时 | Go | —(CLI/桌面) | Go | [repo](https://github.com/ollama/ollama) |
| 4 | stable-diffusion-webui | 164243 | 图像生成 WebUI | Python | Gradio | Python | [repo](https://github.com/AUTOMATIC1111/stable-diffusion-webui) |
| 5 | transformers | 162622 | 模型库/框架 | Python | — | Python(库) | [repo](https://github.com/huggingface/transformers) |
| 6 | Langflow | 151896 | 工作流/Agent 平台 | Python | React | FastAPI | [repo](https://github.com/langflow-ai/langflow) |
| 7 | Firecrawl | 151275 | Web 抓取/数据 | TypeScript | Next.js | Node.js | [repo](https://github.com/firecrawl/firecrawl) |
| 8 | Dify | 148901 | LLM 应用平台 | TypeScript | Next.js | Python(Flask) | [repo](https://github.com/langgenius/dify) |
| 9 | Open WebUI | 145489 | AI 聊天界面 | Python | Svelte(SvelteKit) | FastAPI | [repo](https://github.com/open-webui/open-webui) |
| 10 | LangChain | 141816 | LLM 应用框架 | Python | — | Python(库) | [repo](https://github.com/langchain-ai/langchain) |
| 11 | ComfyUI | 120796 | 图像生成节点 GUI | Python | TypeScript(节点编辑器) | Python(aiohttp) | [repo](https://github.com/Comfy-Org/ComfyUI) |
| 12 | llama.cpp | 120441 | LLM 推理引擎 | C++ | — | C/C++ | [repo](https://github.com/ggerganov/llama.cpp) |
| 13 | Whisper | 104976 | 语音识别 | Python | — | Python(库) | [repo](https://github.com/openai/whisper) |
| 14 | vLLM | 86308 | LLM 推理服务 | Python | — | Python(FastAPI) | [repo](https://github.com/vllm-project/vllm) |
| 15 | OpenHands | 80849 | 编程 Agent | Python | React | Python(运行时) | [repo](https://github.com/All-Hands-AI/OpenHands) |
| 16 | LobeHub | 79865 | AI 聊天/Agent | TypeScript | Next.js | Next.js Server | [repo](https://github.com/lobehub/lobe-chat) |
| 17 | LLaMA-Factory | 73296 | 模型微调 | Python | Gradio | Python | [repo](https://github.com/hiyouga/LLaMA-Factory) |
| 18 | gpt_academic | 71084 | 学术助手 | Python | Gradio | Python | [repo](https://github.com/binary-husky/gpt_academic) |
| 19 | Open Interpreter | 65088 | 编程 Agent | Rust | — | Rust | [repo](https://github.com/OpenInterpreter/open-interpreter) |
| 20 | Mem0 | 60879 | Agent 记忆层 | TypeScript | — | Python + TS SDK | [repo](https://github.com/mem0ai/mem0) |
| 21 | AutoGen | 59741 | 多 Agent 框架 | Python | —(Studio: React) | Python | [repo](https://github.com/microsoft/autogen) |
| 22 | CrewAI | 55556 | Agent 编排框架 | Python | — | Python(库) | [repo](https://github.com/crewAIInc/crewAI) |
| 23 | Flowise | 54636 | 工作流/Agent 平台 | TypeScript | React + MUI | Node.js(Express) | [repo](https://github.com/FlowiseAI/Flowise) |
| 24 | LlamaIndex | 50865 | 数据/RAG 框架 | Python | — | Python(库) | [repo](https://github.com/run-llama/llama_index) |
| 25 | text-generation-webui | 47450 | 本地 LLM WebUI | Python | Gradio | Python | [repo](https://github.com/oobabooga/text-generation-webui) |
| 26 | Aider | 47398 | 编程 Agent/结对 | Python | — | Python(库) | [repo](https://github.com/Aider-AI/aider) |
| 27 | Milvus | 45232 | 向量数据库 | Go | — | Go | [repo](https://github.com/milvus-io/milvus) |
| 28 | DeepSpeed | 42710 | 训练优化库 | Python | — | Python(库) | [repo](https://github.com/microsoft/DeepSpeed) |
| 29 | Quivr | 39211 | RAG 平台 | Python | Next.js | FastAPI + Celery | [repo](https://github.com/QuivrHQ/quivr) |
| 30 | Continue | 34883 | 编程助手(IDE 插件) | TypeScript | React(WebView) | TypeScript(Node) | [repo](https://github.com/continuedev/continue) |
| 31 | Tabby | 33701 | 编程助手(自托管) | Rust | React | Rust | [repo](https://github.com/TabbyML/tabby) |
| 32 | Qdrant | 33292 | 向量数据库 | Rust | — | Rust | [repo](https://github.com/qdrant/qdrant) |
| 33 | SillyTavern | 30699 | LLM 聊天前端 | JavaScript | 原生 JS/jQuery | Node.js(Express) | [repo](https://github.com/SillyTavern/SillyTavern) |
| 34 | STORM | 30086 | 知识/报告生成 | Python | — | Python(库) | [repo](https://github.com/stanford-oval/storm) |
| 35 | FastGPT | 28979 | 知识库/RAG 平台 | TypeScript | Next.js + Mantine | Node.js(Next.js API) | [repo](https://github.com/labring/FastGPT) |
| 36 | Chroma | 28793 | 向量数据库 | Rust | — | Rust + Python | [repo](https://github.com/chroma-core/chroma) |

---

## 二、按类别分组

### 1. LLM 应用平台 / Agent 工作流（可视化，前后端俱全）
Dify · n8n · Langflow · Flowise · FastGPT · Quivr
> 典型形态：Web 控制台 + 工作流编排 + RAG + 多模型接入。**最值得做技术选型参考的一类。**

### 2. AI 聊天 / 交互界面
Open WebUI · LobeHub · SillyTavern · gpt_academic · stable-diffusion-webui · ComfyUI · text-generation-webui
> 前端形态多样：Svelte / Next.js / Gradio / 原生 JS。

### 3. 编程 Agent / AI 编程助手
AutoGPT · OpenHands · Open Interpreter · Aider · Continue · Tabby
> 形态：CLI、Web、IDE 插件。语言覆盖 Python / Rust / TypeScript。

### 4. LLM 应用 / Agent 框架（库）
LangChain · LlamaIndex · CrewAI · AutoGen · Mem0
> 纯库，无前端/后端服务，作为后端依赖。

### 5. LLM 推理 / 运行时 / 训练引擎
Ollama · llama.cpp · vLLM · DeepSpeed · Whisper · transformers · LLaMA-Factory
> 基础设施层：C/C++/Go/Rust 为主，性能导向。

### 6. 向量数据库
Milvus · Qdrant · Chroma
> Go / Rust 系高性能存储。

### 7. Web 数据 / 其他
Firecrawl（抓取） · STORM（报告生成）

---

## 三、统计分布

### 主语言分布（36 个项目）

| 语言 | 数量 | 占比 | 代表项目 |
|------|------|------|---------|
| Python | 20 | 55.6% | AutoGPT · Dify(后端) · LangChain · vLLM · ComfyUI |
| TypeScript | 8 | 22.2% | n8n · LobeHub · Flowise · FastGPT · Continue |
| Rust | 4 | 11.1% | Open Interpreter · Tabby · Qdrant · Chroma |
| Go | 2 | 5.6% | Ollama · Milvus |
| C++ | 1 | 2.8% | llama.cpp |
| JavaScript | 1 | 2.8% | SillyTavern |

**结论**：Python 仍是 AI 生态绝对主力；TypeScript 统治「有前端的 AI 应用」；Rust 在推理/存储/编程助手等性能场景崛起。

### 前端框架分布（仅计有 Web 界面的项目）

| 前端 | 项目 |
|------|------|
| **Next.js / React** | Dify · LobeHub · OpenHands · Quivr · Langflow · Flowise · Tabby · Continue · Firecrawl · FastGPT · AutoGPT |
| **Svelte / SvelteKit** | Open WebUI |
| **Vue 3** | n8n |
| **Gradio**（Python 快速 UI） | stable-diffusion-webui · LLaMA-Factory · gpt_academic · text-generation-webui |
| 原生 JS/jQuery | SillyTavern |
| 自定义节点编辑器(TS) | ComfyUI |

**结论**：**Next.js + React** 是 AI Web 应用前端的事实标准；Python 系图像/科研工具普遍用 Gradio；Svelte/Vue 各有代表作。

### 后端框架分布

| 后端 | 项目 |
|------|------|
| **Python — FastAPI** | Open WebUI · vLLM · Langflow · Quivr |
| **Python — Flask/运行时** | Dify(Flask) · AutoGPT · OpenHands · ComfyUI(aiohttp) · A1111 |
| **Node.js / Express** | n8n · Flowise · SillyTavern · Firecrawl |
| **Next.js API(全栈一体)** | LobeHub · FastGPT |
| **Rust** | Tabby · Qdrant · Chroma · Open Interpreter |
| **Go** | Ollama · Milvus |
| **C/C++** | llama.cpp |
| **纯库(无服务)** | LangChain · LlamaIndex · CrewAI · AutoGen · Mem0 · Aider · transformers · Whisper · DeepSpeed · STORM |

**结论**：后端呈「Python 系(FastAPI/Flask)做应用层 + Node 系做全栈 + Rust/Go/C++ 做基础设施」三层结构。

### 数据库选型

| 数据库 | 项目 |
|--------|------|
| PostgreSQL（含 PgVector） | Dify · Quivr · n8n · Flowise · Milvus-like |
| SQLite（轻量/默认） | n8n · Open WebUI · Langflow · Flowise · Tabby |
| MongoDB | FastGPT |
| 向量库内置/专精 | Milvus · Qdrant · Chroma |
| Redis | Dify（缓存/队列） |
| IndexedDB（纯前端） | LobeHub |

---

## 四、技术选型要点

1. **想做「LLM 应用平台」** → 参考 Dify / FastGPT / Langflow / Flowise：前端 Next.js+React，后端 Python(FastAPI/Flask) 或 Node，存储 PostgreSQL + 向量库。
2. **想做「AI 聊天前端」** → Next.js+React(LobeHub 风格) 或 SvelteKit(Open WebUI 风格)。
3. **想做「编程助手」** → IDE 插件用 TypeScript(Continue)，自托管推理用 Rust(Tabby)，CLI 用 Python(Aider)。
4. **高性能/基础设施** → Rust/Go/C++，参考 Ollama / vLLM / llama.cpp / Qdrant。
5. **多 Agent 编排** → 用 LangChain / CrewAI / AutoGen 作后端库，前端另搭。

> 声明：star 数为 2026-07-15 接口实时值，会持续变化；前端/后端框架基于仓库结构与公开信息整理，如有重构以官方仓库为准。
