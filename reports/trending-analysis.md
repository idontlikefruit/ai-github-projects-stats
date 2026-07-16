# GitHub Trending 今日热榜产品分析

> **数据来源**：https://github.com/trending （全语言，daily）
> **采集日期**：2026-07-16
> **结构化数据**：[`data/trending-daily.csv`](../data/trending-daily.csv)，共 **14** 个项目
> 注：GitHub 无官方 Trending API，数据由抓取 trending 页面 HTML 解析得到。

## 今日热榜总表

| # | 项目 | 今日⭐ | 主语言 | 简介 | 是否已在 56 总表 |
|---|------|--------|--------|------|------------------|
| 1 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) | +1,664 | TypeScript | 开源 CapCut 替代品（视频剪辑） | 否 |
| 2 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | +1,277 | CSS | 反 AI-slop 设计技能，适配 Claude Code / Cursor | 否 |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | +2,130 | Shell | 工程师实战技能，取自作者 .claude 目录 | ✅ (#12) |
| 4 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | +110 | TypeScript | 自托管、可拥有的 Grok 伴侣 | 否 |
| 5 | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | +471 | Rust | 拦截危险命令的守卫(dcg) | 否 |
| 6 | [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | +915 | Python | 个人交易 Agent | 否 |
| 7 | [OpenInterpreter/openinterpreter](https://github.com/OpenInterpreter/openinterpreter) | +299 | Rust | 面向低成本模型的编程 Agent | ✅ (#39) |
| 8 | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | +172 | Python | 终身个性化 AI 导师 | 否 |
| 9 | [HenryNdubuaku/maths-cs-ai-compendium](https://github.com/HenryNdubuaku/maths-cs-ai-compendium) | +725 | TypeScript | AI/ML 研究工程师进阶资料 | 否 |
| 10 | [injaneity/pi-computer-use](https://github.com/injaneity/pi-computer-use) | +103 | TypeScript | 让 Pi 控制你 macOS/Windows 上的应用 | 否 |
| 11 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | +1,236 | Python | 100+ 可运行的 AI Agent & RAG 应用 | ✅ (#28) |
| 12 | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | +340 | JavaScript | Claude Code / AI Agent 的营销技能(CRO 等) | 否 |
| 13 | [YimMenu/YimMenuV2](https://github.com/YimMenu/YimMenuV2) | +38 | C++ | GTA5 增强版实验性菜单 | 否（非 AI） |
| 14 | [hasaneyldrm/exercises-dataset](https://github.com/hasaneyldrm/exercises-dataset) | +949 | HTML | 1324 项健身数据集(动画 GIF) | 否（非 AI） |

## 产品分析

### 1. AI / Agent 占比：今日热榜 ≈ 10/14（约 71%）

14 个里明确 AI/Agent 相关的至少 10 个（#2 #3 #4 #6 #7 #8 #9 #10 #11 #12），非 AI 仅 3 个（#1 视频剪辑工具、#13 GTA 模组、#14 健身数据集），#5 命令守卫属 Agent 安全基础设施。**今日热榜的 AI 浓度（~71%）甚至高于历史总榜（32%）**，说明 AI 不是存量热度，而是当前仍在加速的增量。

### 2. 最热风向：「Claude Code Skills」生态

- #2 hallmark、#3 mattpocock/skills、#12 marketingskills 都是围绕 Claude Code / Cursor 的「技能包」——把工程/设计/营销 know-how 打包成 Agent 可调用的 skill。
- 结合 56 总表里的 superpowers / ECC / anthropics/skills / gstack / agency-agents / andrej-karpathy-skills，**「Agent Skills 即新插件生态」** 已是 2026 GitHub 最确定的趋势：.skills 类仓库同时霸榜历史总榜与今日热榜。

### 3. 新涌现的 AI 产品形态（垂直 Agent）

- **交易 Agent**：#6 Vibe-Trading（HKUDS 出品，港大数据科学实验室）
- **教育 Agent**：#8 DeepTutor（终身个性化导师，同 HKUDS）
- **Computer-Use Agent**：#10 pi-computer-use（控制桌面应用，走向 GUI 自动化）
- **AI 伴侣**：#4 airi（自托管 Grok 伴侣，容器化、可拥有）
- **反 AI-slop 工具**：#2 hallmark（对抗 AI 生成内容的同质化设计）
- **Agent 安全**：#5 destructive_command_guard（拦危险命令，Agent 执行环境防护）

→ 趋势：从「通用 Agent 框架」(AutoGPT/LangChain) 转向**「垂直场景 Agent 产品 + Agent 安全/技能配套」**。

### 4. 语言分布

| 语言 | 数量 | 代表 |
|------|------|------|
| TypeScript | 5 | OpenCut / hallmark / airi / pi-computer-use / maths-cs-ai-compendium |
| Python | 4 | Vibe-Trading / DeepTutor / awesome-llm-apps / openinterpreter(已转 Rust) |
| Rust | 2 | destructive_command_guard / openinterpreter |
| Shell / JS / CSS / C++ / HTML | 各 1 | skills 系列 / marketingskills / hallmark / YimMenu / exercises |

TypeScript 仍是「有前端的 AI/工具产品」首选；Rust 在 Agent 安全/底层（dcg、openinterpreter）持续渗透。

### 5. 与 56 总表的重叠

仅 3 个重叠：mattpocock/skills、openinterpreter、awesome-llm-apps。说明 trending 主要反映**新项目/近期爆发项目**，与历史总榜(存量 star)互补——结合两者可同时看「长青项目」与「当期风口」。

## 选型启示

1. 做 AI 产品：**TypeScript(Next.js/React) 前端 + Python/Rust 后端** 仍是当下最主流组合（与 56 总表结论一致）。
2. 想抓住风口：关注 **Agent Skills 生态**（.claude 技能包）与**垂直 Agent**（交易/教育/computer-use/伴侣）这两个增量赛道。
3. 新机会：**Agent 安全与反 AI-slop 工具** 正在被需要，是 Agent 普及后的衍生刚需。

> ⚠️ Trending 为日榜，波动大；上述为 2026-07-16 当日快照，仅作趋势参考。
