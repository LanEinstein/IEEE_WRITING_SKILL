# IEEE Paper Suite

从空白文稿或指定段落开始，写作、润色与审查一篇有可核查论证的 IEEE 期刊论文或顶会论文（CVPR/ICCV、NeurIPS、ICML、ICLR、AAAI）。本套规则是模型无关的 Markdown：每条规则写清它约束什么、由哪个文件负责、用什么检查让它可见。

[English](README.md) · [许可证](LICENSE)

## 选一个入口，直接说任务

| 入口 | 任务 | 写入方式 |
| --- | --- | --- |
| `ieee-write` | 从零起草、指定节写作、主线重构 | 完成已授权的初稿；明确要求先审查时先提案 |
| `ieee-polish` | 学术英文、段落结构、一轮修改润色 | 按已有授权应用；仅提案请求不落正文 |
| `ieee-review` | 方法、协议、证据与主张的模拟审稿 | 正文、参考文献、图与原构建产物只读，产出报告 |
| `ieee-style` | 结构、句位、术语、图表与投稿格式检查 | 同样只读，按请求范围检查 |

不再强制每段等一次 go。审查与修改范围由用户决定；段落总分结构、句位和机制分析仍严格执行。小任务只用简短工作卡；已有主线、协议与事实表直接复用。

## 可直接复制的请求

> 使用 ieee-polish。只改第 5.2 节，保留数值和比较范围。每个自然段以提案形式给出原文、改后全文和理由，我批准后落盘。

> 使用 ieee-write。基于当前项目的方法说明和最终表格，完成一版可审查的期刊论文初稿。沿用正式主稿和已有主线，不改数值，不新增实验。

> 使用 ieee-style。只审查相关工作：每个小节的第二段和定位逻辑。给出建议，暂不改正文。

入口会读取[共享工作流](core/WORKFLOW.md)和**当前单元的完整规则**。[一页清单](QUICK_REFERENCE.md) · [句位索引](core/templates/sentence-plan.md) · [工作区模板](core/templates/writing-workspace.md)。

## 规则覆盖什么

`core/rules/` 下有九个共享规则文件；六个章节规程末尾各附一份从退稿中提炼的 `S-*-H` 加固清单。

| 关注点 | 规则文件 |
| --- | --- |
| 推销自己的工作、正面表述、主张边界、敏感应用表述 | [voice-and-positioning.md](core/rules/voice-and-positioning.md) |
| 一段一个论证、首句总领、观察后必分析、段末落点 | [paragraph-architecture.md](core/rules/paragraph-architecture.md) |
| 信息顺序、连接词真值、重复控制、指代、标点 | [sentence-craft.md](core/rules/sentence-craft.md) |
| 用词语域、禁用形式与替换建议 | [lexicon.md](core/rules/lexicon.md) |
| 不译中文：八类中式结构及其改法 | [translation-discipline.md](core/rules/translation-discipline.md) |
| 润色范围、保护清单、检查顺序、交付前自审 | [revising.md](core/rules/revising.md) |
| 模拟审稿、真人意见处理、多轮联读、审阅页 | [review-loops.md](core/rules/review-loops.md) |
| 术语、缩写、符号、公式 | [terminology-and-notation.md](core/rules/terminology-and-notation.md) |
| 版面预算、间距、孤行、TeX 与 PDF 卫生 | [layout-and-build.md](core/rules/layout-and-build.md) |

章节规程：[摘要 A1–A9](core/rules/section-abstract.md) · [引言 P1–P8](core/rules/section-introduction.md) · [相关工作](core/rules/section-related-work.md) · [方法](core/rules/section-methodology.md) · [实验 E1–E6](core/rules/section-experiments.md) · [结论](core/rules/section-conclusion.md)。证据与授权：[evidence-and-claims.md](core/rules/evidence-and-claims.md)、[citations-policy.md](core/rules/citations-policy.md)、[workflow-gates.md](core/rules/workflow-gates.md)。图：[figure-standards.md](core/rules/figure-standards.md)。

## 可以立即运行的检查

纯 Python 3，无第三方依赖，无网络：

```bash
python3 scripts/prose_lint.py main.tex --quiet        # H 必须为 0，再逐条看 S
python3 scripts/pronoun_check.py main.tex --quiet     # this/these/it/its 等的候选先行词
python3 scripts/review_page.py round.json -o round.html   # 勾选+评论页，导出 JSON
```

`prose_lint.py` 报告：中式语序与句首从属结构、因果连词成对、分词开头、禁用词表、正文冒号、同段重复连接词、句内重复短语、超长句、绝对词；并列出每个文件里重复最多的实词。H 为硬错误（必须改写），S 供人工判断，I 是给阅读测试的提示。caption 始终被扫描，`--include-floats` 另外扫描图表主体，`--banned file` 加入项目自己的词表。

`review_page.py` 把一轮提案变成一个离线 HTML 页面：原文、改后（逐词差异）、理由、同意勾选、评论框、可选版本、本地保存、导出 JSON，对应 [review-loops.md](core/rules/review-loops.md) §RL4 的流程。

Bash 诊断工具仍然可用：`sweep_prose.sh`、`wordcount_abstract.sh`、`check_figures_text.sh`、`verify_tex.sh`、`leak_scan.sh`、`verify_citations.py`。它们只是线索：零命中不等于正确，命中要结合上下文。范围与限制见[验证协议](core/rules/verification-protocol.md)。

## 安装与调用

```bash
./install.sh            # Claude Code 技能链接
./install.sh --codex    # Codex 技能链接、兼容 prompt 和可选 AGENTS 片段
./install.sh --all      # 两者
./install.sh --check    # 自检：链接、脚本、规则文件引用
```

Codex 安装后使用 `$ieee-write`、`$ieee-polish`、`$ieee-review`、`$ieee-style`；Claude Code 使用相应 `/ieee-*`。其他 agent 直接读取指定入口，见[通用接入](adapters/generic/QUICKSTART.md)。宿主缓存技能列表时，开新会话后生效。

安装器不改动项目或全局 AGENTS，已有的无关技能目录受保护。`local/config.md` 只放机器路径或本地材料指针；论文主稿、目标、文风与授权属于当前会话或项目。项目可以扩展词表（`--banned`），无须改本套文件。

普通写作只需能读材料。可选检查使用 Python 3、Bash/GNU 工具、pdfLaTeX+BibTeX 和 Poppler；文献索引需要网络。优先沿用项目实际引擎；缺工具时交可用的正文，并明确标出未完成的检查。

## 这套规程强制什么

- 摘要 A1–A9、引言 P1–P8：每句有任务，动机链真实，贡献与方法、证据一一对应。
- 相关工作每主题两段；定位段两至三句、35–65 词、不长于第一段，只写继承、缺口与回应。
- 方法：标题、主图节点、符号、轴、公式、输入输出与训练／推理状态彼此一致。
- 实验：每段先总后分，观察之后必有分析（E1–E6），反例保留，推论限定在证据范围。
- 润色：主张、数值、比较对象不变；未经允许不加长；每轮结束写清已应用、已否决、仍待定。

以上是本套期刊方法论文的写作规程，不是 IEEE 对所有论文的统一规定。真实研究内容和当前目标（会议、年份、轨道）的正式要求优先约束模板；不凑模块、贡献或新实验。理论、系统、应用类论文按其自身的证据形态适配；不存在一刀切的页数上限、只按期刊层级筛引文的规则或必须的画图要求。

## 致谢与许可证

诚挚感谢山东大学卢教授（Prof. Xiankai Lu）的指导与支持。

© 2026 Lan Zhang · [CC BY-NC 4.0](LICENSE) · 禁止商用，转载须署名。
