# IEEE Paper Suite

[English](README.md) | **简体中文**

三个可独立唤醒的工作流,把研究代码库做成地道学术英文的 IEEE 顶刊稿:
**ieee-write**(写作)、**ieee-polish**(润色)、**ieee-review**(模拟审稿)。

> 本文件仅为文档;套件运行时加载的全部指令、规则与模板均为英文。

## 开发背景

通用 AI 写作工具产出的论文机器味明显,达不到顶刊语言水准。差距不在模型,
而在缺失的手艺:资深作者在真实改稿中逐段执行的那套规范。本套件把这套手艺
固化下来。规范提炼自一篇 IEEE Transactions 稿件的逐段改稿实录与五篇已发表
IEEE TIP 论文的逐节分析,落成单一权威规则库与硬门控工作流,任何步骤不可绕过。

## 主要功能与典型优势

- **三工作流彼此独立**:写作、润色、审稿各自唤醒,绝不捆绑成流水线。
- **单源规则库**:全局文风、分章节规范(摘要至结论)、披露策略、引用政策、
  验证协议全部收敛于 `core/`,工作流整文件读取,规则无从漂移。
- **硬用户门控**:大纲批准后才动笔,逐段明确 `go` 才推进,润色先提案后落地。
  模型绝不凭自己的判断改稿。
- **一切实测、绝不编造**:字数、页数、编译健康度、零容忍文风扫描均由脚本
  给出逐条计数;引用经 Crossref/OpenAlex 实时核验,配 venue 分层门禁与
  arXiv 拦截,核验不过的文献不得引用。
- **会反击的审稿面板**:五人设(编辑、方法统计、领域、写作、魔鬼代言人),
  含盲评预承诺与反谄媚机制,输出按严重度排序的意见与决策预估,另附
  仅作者可见的内部合规审计层。
- **模型无关**:core 为纯 markdown 与脚本;自带 Claude Code 与 Codex
  适配层,任何能读文件、跑命令的 agent 均可驱动。

## 安装使用

```bash
git clone <repo-url> ieee-paper-suite
cd ieee-paper-suite
./install.sh            # Claude Code(symlink 至 ~/.claude/skills/)
./install.sh --codex    # Codex CLI(斜杠 prompt + AGENTS.md 片段)
./install.sh --all      # 两者
```

在论文项目中:

- `/ieee-write`:扫描代码库产出事实表,交付大纲待批,批准后按
  方法→实验→相关工作→引言→摘要→结论逐段撰写,每段等你 `go`。
- `/ieee-polish`:对任意 .tex 逐段给出"原文→新文"提案表,仅落地你批准的改动。
- `/ieee-review`:输出双层报告——五人设模拟外审与决策预估,以及
  仅作者可见的内部合规审计。

依赖:`pdflatex`、`bibtex`、`pdftotext`、POSIX 工具链、可联网的 Python 3。
机器本地指针(范例稿路径等)写入 `local/config.md`
(参见 `local/config.example.md`),`local/` 内容永不入库。

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

© Lan Zhang。基于 [CC BY-NC 4.0](LICENSE) 许可:禁止商用;
转载或改编须署名作者(Lan Zhang)并标明出处。
