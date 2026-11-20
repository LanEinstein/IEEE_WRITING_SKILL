<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Related Work 两段规程 (S-RW)

适用配置：`journal_method_structured_v2`。以下句位、段数与篇幅是本套明确采用的写作规程，不是 IEEE 对所有论文的官方规定。真实内容或正式限制不适用时，说明相邻合并／功能映射，不补造事实；总句、具体动机和必要解释保留。正文默认英文，规划可用作者语言。只读取当前任务所需来源；审批沿用既有授权。

## S-RW-1. 小节按问题分类 标题覆盖本研究的技术坐标

默认设置三个问题导向的小节：任务与表示、最相关的学习或迁移路线、核心技术的相邻研究。标题采用具体研究对象，例如 [Task and Representation]、[Closest Learning Paradigm]、[Core Technical Principle]。

三个小节共同回答“输入怎样表征、知识怎样进入模型、关键对象怎样比较”。其他研究替换技术内容，但保持与当前论文问题的直接关系，不把综述写成整个领域的历史。

## S-RW-2. 每小节第一段负责梳理研究线

第一段默认四至六句，执行以下句位：

| 句位 | 必写内容 | 英文句架或连接方式 |
| --- | --- | --- |
| R1-S1 | 总句界定研究线及其主要目标 | [Research line] addresses [specific problem] through [organizing principle]. |
| R1-S2 | 一个早期或代表性路线及其操作原理 | [Family A] represents [object] using [mechanism]. |
| R1-S3 | 代表工作及其具体推进 | [Method/Author] introduces [operation] to [capability], with the verified citation. |
| R1-S4 | 后续路线在同一问题上的改进 | More recent approaches [specific change], enabling [capability]. |
| R1-S5 | 与本文最相关的已有技术或条件 | [Closest line] additionally [mechanism relevant to the present problem]. |
| R1-S6 | 收敛到第二段要处理的假设或位置 | The resulting formulations differ in [relevant assumption or object]. |

没有必要的历史步骤可以合并，但每个保留工作必须交代“做了什么、与本问题有什么关系”。不要逐篇堆作者名字，不要求每篇后面跟一个强行编出的缺点。近期工作按相关性补入，经典工作按归因需要保留。

## S-RW-3. 每小节第二段固定为精简定位段

第二段只做“关键条件或差异 → 对当前问题的后果 → 本文原则级回应”。默认两至三句，目标 35–65 个英文词，上限 80 词，且不得长于第一段。这是本套写作的篇幅控制值，不是 IEEE 官方字数规定。

| 句位 | 必写内容 | 禁止内容 |
| --- | --- | --- |
| R2-S1 | 直接指出一个与本文有关的关键假设、未处理条件或最近邻差异 | 重新介绍整个研究线，新增一串论文 |
| R2-S2 | 说明该条件在当前任务中的后果或功能区别 | 泛泛的“存在局限”“仍需改进”，无依据的性能评价 |
| R2-S3 | 用一句话定位本文如何改变比较对象、约束或学习方式 | 模块清单、公式推导、超参数、实验成绩、贡献列表 |

第二段写长时，先把背景、代表方法和必要引用移到第一段。只保留会改变本文定位的一项核心差异。若确有两项独立差异，以两个短句说明，不扩成完整的方法介绍。无法用三句说清时，先检查小节分类是否混杂。

可直接套用：

~~~text
However, [precisely named method family] relies on [verified assumption].
Under [current condition], [specific consequence or distinction].
[Proposed method] [principle-level operation] to [answer to that condition].
~~~

转折针对具体方法或明确子类，不能将少数方法的假设写成全部已有工作的共同缺陷。若不是局限而是互补关系，S1 直接写区别，不强加 However。

## S-RW-4. 精简定位段示例

以下是纯写法示例，假设相邻文献已经支持所述等索引匹配；不将该假设归给全部蒸馏或对比方法：

> However, pointwise feature matching compares activations at equal indices, whose semantic correspondence is not guaranteed across domains. The positional constraint ties supervision to coordinates learned independently by the two branches. The proposed formulation instead compares projected feature statistics, defining a different interface for cross-domain guidance.

三句依次写假设、后果、原则定位。正式使用时必须核实当前方法确有该区别并有对应文献，不能把示例当作研究事实。词数用工具测量；超限先移出背景和方法细节。

## S-RW-5. 相关工作验收项

- 每个小节有清楚的研究对象，第一段梳理路线，第二段精简定位。
- 第二段逐句可标为“条件／后果／回应”，没有新的文献清单。
- 与最近邻比较的是对象、假设、监督、优化或部署，不是抽象的“更有效”。
- 类似思想如 Wasserstein、attention 或 distillation 已存在时，说明具体改变，不把借用的概念本身写成首创。
- 不在相关工作报告本文识别成绩，不复述方法公式，不用结果表批评既有方法。
- 小节结尾直指本文技术位置，不能写成“因此本文有必要”的空结论。

**完成标准：**每小节第二段两至三句、直击一个核心位置或差异，读者能据此理解为什么后续方法需要相应设计。

## S-RW-H. Hardened checklist (distilled from rejected drafts)

1. **The first paragraph credits, the second positions.** P1 says which lines this work follows, what each contributed and what it inspired (borrowing and inspiration are different). P2 says only how this work now goes further: what it inherits, what the earlier work left open, what this paper does about it.
2. **Positioning sentence pattern** (author-approved): "X proposed in [work] inspired us to [operation], yet leaves [specific condition] unconstrained; this work [principle-level change] to [outcome]." One sentence per comparison dimension; every sentence on point.
3. **Length.** P2 is 2–3 sentences, roughly 35–65 words, never longer than P1. If it will not fit, the subsection taxonomy is wrong.
4. **No new citation list in P2, no module inventory, no formula, no result.**
5. **No boilerplate.** A positioning paragraph that only lists what this paper built ("introduces ..., revisits ..., builds ...") is rejected. It must state inheritance, gap and response.
6. **Read the cited paper before saying what it did or left open**, and use its own verb. Claim scope must be checkable in that paper.
7. **Do not criticise peers.** State what a protocol or a design leaves unconstrained; never that a named method fails. Do not imply competition with work on a different task.
8. **Chronology gets connectives.** A research-line paragraph can run in time order only with time markers ("Early methods relied on ...", "Deep networks later learned ...", "More recent work ...").
9. **Do not repeat the Introduction** in the positioning paragraph; say it once, in the place with room for it.
10. **Field-aligned vocabulary.** Use the term the field uses for the operation (for example "combine" for merging databases), not a synonym that sounds more technical.
11. **No subsection heading at the top of Related Work** is required when the section is short; if subsections exist, each keeps the two-paragraph shape and the heading names the technical object, not the paper's argument.
12. **Every claim about "what prior work assumes" is a statement about a named family, not about all prior work.**
