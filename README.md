# AI GitHub 知名项目技术选型统计

本目录用于统计线上 GitHub 上非常出名的 AI 相关项目，记录其类型、前后端技术选型等信息，作为技术选型参考。

## 目录结构

```
ai-github-projects-stats/
├── README.md            # 说明文件
├── data/                # 汇总数据（CSV / JSON / 表格）
├── projects/            # 每个项目的详细分析（一项目一文件）
└── reports/             # 统计报告与可视化图表
```

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
