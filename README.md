# AI GitHub 知名项目技术选型统计

本目录用于统计线上 GitHub 上非常出名的 AI 相关项目，记录其类型、前后端技术选型等信息，作为技术选型参考。

---

## 📊 GitHub 全站历史总榜 Top-100 分析

> **数据来源**：[EvanLi/Github-Ranking · Top-100-stars](https://github.com/EvanLi/Github-Ranking/blob/master/Top100/Top-100-stars.md)
> **采集日期**：2026-07-15（与源文件同步当日更新）
> **原始存档**：[`data/source-top-100-stars.md`](data/source-top-100-stars.md)　**结构化数据**：[`data/top-100-stars.csv`](data/top-100-stars.csv)

### 一句话结论

GitHub 全站历史 Star 总榜前 100 名里，**有 32 个是 AI / Agent 生态项目**（占比近 1/3），且大量占据榜单**头部**（第 6/14/18/20/26/27/30 名等）。2026 年的 GitHub 已被 AI / Claude Code 生态深度重塑。

### 类别分布（人工分类，共 100）

| 类别 | 数量 | 占比 | 说明 |
|------|------|------|------|
| 🤖 AI / Agent 生态 | 32 | 32% | 编程 Agent、技能框架、LLM 应用平台、推理引擎、提示词库等 |
| 📚 学习资源 / Awesome / 书籍 | 26 | 26% | awesome-*、面试/算法/路线图、免费书籍 |
| 🛠️ 工具 / 应用 / 其他 | 18 | 18% | 下载器、远程桌面、代理客户端、激活脚本等 |
| 🧩 前端 / UI 框架 | 12 | 12% | react / vue / next.js / shadcn / three.js 等 |
| ⚙️ 系统 / 运行时 / 语言 / 基础设施 | 12 | 12% | linux / kubernetes / electron / node / rust / deno 等 |

### 主语言分布（GitHub 接口返回，精确）

| 语言 | 数量 | 语言 | 数量 |
|------|------|------|------|
| Python | 22 | C | 3 |
| TypeScript | 16 | Markdown / Jupyter Notebook | 各 2 |
| 未标注（多为 Markdown/列表） | 13 | Batchfile / Dart / MDX / Java / C# / Swift | 各 1 |
| JavaScript | 10 | | |
| Shell / Rust | 各 6 | | |
| C++ / Go | 各 5 | | |
| HTML | 4 | | |

**要点**：Python(22) + TypeScript(16) 合计占 38%，是榜单绝对主力；Rust(6) 已与 Shell 持平，超过 Go(5)/C++(5)。

### 🤖 AI / Agent 相关项目子表（32 个，按 Star 排）

| 榜号 | 项目 | ⭐ Stars | 主语言 | 简介 |
|------|------|---------|--------|------|
| 6 | [openclaw/openclaw](https://github.com/openclaw/openclaw) | 382,957 | TypeScript | 个人 AI 助手，跨 OS/平台 |
| 14 | [obra/superpowers](https://github.com/obra/superpowers) | 254,814 | Shell | Agent 技能框架与软件开发方法论 |
| 18 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | 229,791 | JavaScript | Agent harness 性能优化系统(Claude Code/Codex 等) |
| 20 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 214,956 | Python | 与你共同成长的 Agent |
| 23 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | 196,468 | TypeScript | 原生 AI 能力的工作流自动化平台 |
| 24 | [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) | 196,359 | C++ | 开源机器学习框架 |
| 26 | [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | 194,764 | Rust | 无人干预维护的 Agent 展品项目 |
| 27 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 192,359 | — | 改进 Claude Code 行为的单个 CLAUDE.md |
| 30 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | 185,906 | TypeScript | 开源编程 Agent |
| 32 | [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 185,544 | Python | 面向所有人的自主 AI Agent |
| 40 | [ollama/ollama](https://github.com/ollama/ollama) | 176,120 | Go | 本地运行 LLM(Kimi/GLM/DeepSeek/Qwen 等) |
| 43 | [mattpocock/skills](https://github.com/mattpocock/skills) | 170,663 | Shell | 来自作者 .claude 目录的工程师技能 |
| 44 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | 166,028 | Python | 文件/Office 文档转 Markdown(AI 管道常用) |
| 45 | [f/prompts.chat](https://github.com/f/prompts.chat) | 165,760 | HTML | ChatGPT 提示词分享/自托管 |
| 47 | [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | 164,241 | Python | Stable Diffusion Web UI |
| 48 | [huggingface/transformers](https://github.com/huggingface/transformers) | 162,612 | Python | SOTA 模型定义/训练框架 |
| 50 | [anthropics/skills](https://github.com/anthropics/skills) | 161,194 | Python | Anthropic 官方 Agent Skills 仓库 |
| 52 | [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | 151,886 | Python | 可视化构建/部署 AI Agent 与工作流 |
| 53 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 151,119 | TypeScript | 大规模网页搜索/抓取/交互 API |
| 54 | [langgenius/dify](https://github.com/langgenius/dify) | 148,861 | TypeScript | 生产级 agentic 工作流开发平台 |
| 57 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | 145,455 | Python | 用户友好的 AI 界面(支持 Ollama/OpenAI) |
| 58 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | 141,925 | — | 各 AI 编程工具的系统提示词与模型合集 |
| 59 | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 141,796 | Python | Agent 工程平台 |
| 63 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | 137,895 | Python | Anthropic 官方终端 agentic 编程工具 |
| 69 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 131,518 | Shell | 一站式 AI agency 的专门化 Agent 集合 |
| 77 | [garrytan/gstack](https://github.com/garrytan/gstack) | 121,936 | TypeScript | Garry Tan 的 Claude Code 配置(23 个工具) |
| 78 | [github/spec-kit](https://github.com/github/spec-kit) | 121,331 | Python | 规约驱动开发(Spec-Driven Dev)工具包 |
| 79 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 121,050 | Python | 100+ 可直接运行的 AI Agent & RAG 应用 |
| 80 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 120,758 | Python | 模块化扩散模型 GUI/API/后端 |
| 81 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 120,405 | C++ | C/C++ 高效 LLM 推理 |
| 86 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | 117,286 | Rust | Claude Code/Codex/Gemini CLI 多助手桌面端 |
| 92 | [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) | 113,004 | Jupyter | 21 课生成式 AI 入门教程 |

### 关键观察

1. **AI 占据头部**：前 10 名中有 4 个 AI 项目（#6 openclaw、#14 superpowers、#18 ECC、#20 hermes-agent），前 30 名中有 12 个。AI 已不是榜单边缘品类，而是核心品类。
2. **Claude Code 生态爆炸**：32 个 AI 项目里至少 10 个直接围绕 Claude Code / Agent Skills / 提示词（openclaw、superpowers、ECC、andrej-karpathy-skills、opencode、mattpocock/skills、anthropics/skills、claude-code、gstack、cc-switch、system-prompts）。说明「AI 编程助手 + 技能/配置生态」是 2026 年最热的开源方向。
3. **语言格局**：AI 项目仍以 **Python**（运行时/库/教程）和 **TypeScript**（Agent 应用前端）为主；**Rust** 在推理/桌面端（claw-code、cc-switch）与底层（tauri/deno/rustdesk）崛起；**Shell** 因 skills 类配置仓库增多而意外上榜。
4. **榜单性质变化**：传统的 awesome-list / 学习资源 / 面试指南（build-your-own-x、freeCodeCamp、system-design-primer 等）仍占 26 个，但增速已被 AI 项目反超。

> ⚠️ 说明：榜单中部分 Agent Skills / 配置类仓库（如 openclaw、claw-code、ECC、gstack 等）描述较为特殊，star 增长可能受 2026 AI 热潮与社区效应影响，仅作趋势参考；具体技术选型仍建议优先关注 dify / langchain / langflow / ollama / llama.cpp / vLLM / ComfyUI 等工程级项目。

---

## 目录结构

```
ai-github-projects-stats/
├── README.md                       # 本文件（含 Top-100 分析展示）
├── data/                           # 汇总数据
│   ├── source-top-100-stars.md     # Top-100 原始榜单存档
│   ├── top-100-stars.csv           # Top-100 结构化数据(含 category 列)
│   ├── projects.csv                # 36 个 AI 项目技术选型数据
│   └── merged-ai-projects.csv      # 合并去重总表(56 个,18 字段)
├── projects/                       # 每个项目详细分析（一项目一文件）
└── reports/                        # 统计报告
    ├── summary.md                 # 36 个 AI 项目技术选型统计
    └── merged-ai-projects.md      # 合并去重总表(56 个)展示
```

## 已有数据

- **[`reports/merged-ai-projects.md`](reports/merged-ai-projects.md)**：**合并去重总表 56 个**（36 curated + Top-100 AI 子集 32，去重 12），含来源标注与待补清单。
- **[`data/merged-ai-projects.csv`](data/merged-ai-projects.csv)**：合并去重结构化数据，18 字段（含 `source`/`rank_top100`）。
- **[`reports/summary.md`](reports/summary.md)**：36 个知名 AI 项目技术选型统计（star / 主语言 / 前端 / 后端 / 数据库 / LLM / 协议），含分布图表与选型建议。
- **[`data/top-100-stars.csv`](data/top-100-stars.csv)**：GitHub 全站历史总榜 Top-100，含 rank / stars / forks / language / category / description / last_commit。
- **[`data/projects.csv`](data/projects.csv)**：36 个 AI 项目的 14 字段技术选型表。

## 采集字段（每个项目记录以下信息）

| 字段 | 说明 |
|------|------|
| name | 项目名称 |
| repo | GitHub 仓库地址 |
| stars | Star 数（采集日期） |
| category | 项目类型（LLM 应用 / Agent 框架 / RAG / 编程助手 / 多模态 / 模型推理 等） |
| description | 一句话简介 |
| frontend | 前端技术栈 |
| backend | 后端技术栈 |
| database | 数据库 / 存储 |
| llm | 使用的大模型 / 推理后端 |
| deploy | 部署方式（Docker / K8s / Serverless 等） |
| license | 开源协议 |
| company | 维护方 / 公司 |
| last_updated | 信息采集日期 |

## 统计维度

- 项目类型分布
- 前端技术选型分布（React / Vue / Next.js / Svelte …）
- 后端语言分布（Python / Node / Go / Rust …）
- 后端框架分布（FastAPI / Express / NestJS / Gin …）
- 数据库选型分布
- LLM / 推理后端选型分布

## 采集流程

1. 选定知名 AI 开源项目清单
2. 在 `projects/` 下逐个分析并记录
3. 汇总到 `data/projects.csv`
4. 在 `reports/` 输出统计报告
