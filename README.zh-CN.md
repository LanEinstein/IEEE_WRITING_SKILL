<div align="center">

# IEEE Paper Suite

**以硬门控、单一真相源的工作流<br>完成 IEEE 顶刊论文的写作、润色与模拟审稿。**

<br>

[![English](https://img.shields.io/badge/English-README-2ea44f?style=for-the-badge)](README.md)
[![Chinese](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-%E8%AF%B4%E6%98%8E%E6%96%87%E6%A1%A3-1f6feb?style=for-the-badge)](README.zh-CN.md)

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-ready-d97757.svg)](#安装使用)
[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-ready-412991.svg)](#安装使用)
[![Model Agnostic](https://img.shields.io/badge/core-model--agnostic-8a2be2.svg)](adapters/generic/QUICKSTART.md)

</div>

---

## 开发背景

通用 AI 写作工具产出的论文机器味明显,达不到顶刊语言水准。差距不在模型,
而在缺失的手艺:资深作者在真实改稿中逐段执行的那套规范。本套件把这套手艺
固化下来。规范提炼自一篇 IEEE Transactions 稿件的逐段改稿实录与五篇已发表
IEEE TIP 论文的逐节分析,落成单一权威规则库与硬门控工作流,任何步骤不可绕过。

## 主要功能

| 工作流 | 功能 | 硬门控 |
|:--|:--|:--|
| **`/ieee-write`** | 扫描代码库产出事实表,交付大纲,批准后按方法、实验、相关工作、引言、摘要、结论逐段撰写 | 大纲审批 + 每段明确 `go` |
| **`/ieee-polish`** | 对任意 `.tex` 逐段给出"原文 → 新文"提案表,按内建规范逐句体检 | 未经 `go` 不落一字 |
| **`/ieee-review`** | 五人设模拟外审(编辑、方法统计、领域、写作、魔鬼代言人)+ 仅作者可见的合规审计,附决策预估 | 只读,绝不改稿 |

典型优势:

- **单源规则库**:全局文风、分章节规范、披露策略、引用政策、绘图标准、
  验证协议全部收敛于 `core/`,工作流整文件读取,规则无从漂移。
- **一切实测、绝不编造**:字数、页数、编译健康度、零容忍文风扫描均由脚本
  给出逐条计数;引用经 Crossref/OpenAlex 实时核验,配 venue 分层门禁与
  arXiv 拦截。
- **会反击的审稿面板**:盲评预承诺、魔鬼代言人反谄媚机制、逐条附原文证据的
  按严重度排序意见、校准过的决策预估。
- **模型无关内核**:纯 markdown 与脚本;自带 Claude Code 与 Codex 适配层,
  任何能读文件、跑命令的 agent 均可驱动。

## 安装使用

```bash
git clone git@github.com:LanEinstein/IEEE_WRITING_SKILL.git ieee-paper-suite
cd ieee-paper-suite
./install.sh            # Claude Code(symlink 至 ~/.claude/skills/)
./install.sh --codex    # Codex CLI(斜杠 prompt + AGENTS.md 片段)
./install.sh --all      # 两者
```

随后在论文项目中唤醒 `/ieee-write`、`/ieee-polish` 或 `/ieee-review`。
依赖:`pdflatex`、`bibtex`、`pdftotext`、POSIX 工具链、可联网的 Python 3。

## 目录结构

```
skills/     三个入口:ieee-write / ieee-polish / ieee-review(各含 SKILL.md)
core/       单一权威:rules/ 规则、templates/ 模板、review/ 审稿、literature/ 文献
scripts/    verify_tex、sweep_prose、wordcount_abstract、check_figures_text、
            verify_citations、leak_scan
adapters/   codex/(prompt 与 AGENTS 片段)、generic/(任意 agent 快速接入)
local/      机器本地配置(除示例外均被 gitignore)
```

## 致谢

诚挚感谢山东大学卢教授(Prof. Xiankai Lu)的指导与支持。

## 许可证

<div align="center">

© Lan Zhang · [CC BY-NC 4.0](LICENSE) · 禁止商用 · 转载须署名并标明出处

</div>
