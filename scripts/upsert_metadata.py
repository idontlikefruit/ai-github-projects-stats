#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
项目元数据 upsert（update-insert）脚本
- 以 full_name 为主键，把多个来源按"更新或插入"语义合并成一份规范化元数据存储。
- 幂等：重复运行结果一致；新增来源/项目只会更新或插入，不会清空已有字段。
- llama.cpp 别名：ggerganov/llama.cpp 与 ggml-org/llama.cpp 视为同一仓库。

用法： python3 scripts/upsert_metadata.py
输出： data/projects-metadata.csv  （规范化元数据存储）
"""
import csv, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'data')

ALIAS = {'ggerganov/llama.cpp': 'ggml-org/llama.cpp'}
def key(fn): return ALIAS.get(fn, fn)
PLACE = {'', '—', '—(待补)', '未标注', 'null', 'None'}

CANON = ['full_name','name','url','stars','rank_top100','trending_today','trending_stars_today',
         'category','ai_related','platform','primary_lang','dev_langs','frontend','backend',
         'database','llm_runtime','tags','license','owner','forks','open_issues','description',
         'sources','last_updated']

def meaningful(v): return v is not None and str(v).strip() not in PLACE
def first_set(cur, new):
    """更新或插入：新值有意义且当前为空 → 写入；否则保留当前。"""
    return new if (meaningful(new) and not meaningful(cur)) else cur

store = {}  # key -> row dict

def upsert(row, source):
    fn = row.get('full_name','')
    if not fn: return
    k = key(fn)
    r = store.get(k)
    if r is None:
        r = {c: '' for c in CANON}
        r['full_name'] = fn
        r['sources'] = source
        store[k] = r
    else:
        if source not in r['sources']:
            r['sources'] = (r['sources'] + ',' + source) if r['sources'] else source
    # 主语言/平台/前后端/数据库/LLM/协议/owner/类别/描述/dev_langs/tags：仅当当前为空才填(不覆盖已有更丰富值)
    for f in ['name','url','category','platform','primary_lang','dev_langs','frontend','backend',
              'database','llm_runtime','license','owner','description']:
        r[f] = first_set(r[f], row.get(f))
    # tags：取更"丰富"的那个(逗号多者胜)，否则保留
    nt = row.get('tags','')
    if meaningful(nt):
        if not meaningful(r['tags']) or nt.count(',') > r['tags'].count(','):
            r['tags'] = nt
    # stars：取较大值
    try:
        ns = int(str(row.get('stars','')).replace(',',''))
    except: ns = 0
    try: cs = int(str(r['stars']).replace(',',''))
    except: cs = 0
    if ns > cs: r['stars'] = ns
    # rank_top100
    rt = row.get('rank_top100') or row.get('rank','')
    if meaningful(rt) and not meaningful(r['rank_top100']): r['rank_top100'] = rt
    # ai_related：任一来源"是"即为"是"
    if str(row.get('ai_related','')).strip() == '是':
        r['ai_related'] = '是'
    elif not meaningful(r['ai_related']):
        r['ai_related'] = row.get('ai_related','')
    # forks / open_issues
    for f in ['forks','open_issues']:
        v = row.get(f,'')
        if meaningful(v) and not meaningful(r[f]): r[f] = v
    # trending
    tt = row.get('stars_today','')
    if meaningful(tt):
        r['trending_stars_today'] = tt
        r['trending_today'] = '是'
    r['last_updated'] = '2026-07-17'

# 来源1: projects.csv (curated, 最丰富)
p = os.path.join(DATA,'projects.csv')
if os.path.exists(p):
    for r in csv.DictReader(open(p,encoding='utf-8')):
        upsert({**r, 'ai_related':'是'}, 'curated')

# 来源2: top-100-stars.csv (历史总榜, 含 ai_related/tags/category/rank/forks/issues)
p = os.path.join(DATA,'top-100-stars.csv')
if os.path.exists(p):
    for r in csv.DictReader(open(p,encoding='utf-8')):
        upsert(r, 'top100')

# 来源3: trending-daily.csv (今日热榜, 含 ai_related/tags/stars_today)
p = os.path.join(DATA,'trending-daily.csv')
if os.path.exists(p):
    for r in csv.DictReader(open(p,encoding='utf-8')):
        upsert({**r, 'stars': r.get('total_stars','')}, 'trending')

# 写出
out = os.path.join(DATA,'projects-metadata.csv')
rows = sorted(store.values(), key=lambda x: -(int(str(x['stars']).replace(',','')) if str(x['stars']).replace(',','').isdigit() else 0))
with open(out,'w',newline='',encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=CANON); w.writeheader()
    for r in rows: w.writerow(r)

from collections import Counter
c = Counter(r['sources'] for r in rows)
print(f"upsert 完成: 共 {len(rows)} 个项目 -> data/projects-metadata.csv")
print("来源分布:", dict(c))
print("AI 相关:", sum(1 for r in rows if r['ai_related']=='是'), "/", len(rows))
