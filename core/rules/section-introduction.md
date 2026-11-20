<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Introduction 逐句规程 (S-INT)

适用配置：`journal_method_structured_v2`。以下句位、段数与篇幅是本套明确采用的写作规程，不是 IEEE 对所有论文的官方规定。真实内容或正式限制不适用时，说明相邻合并／功能映射，不补造事实；总句、具体动机和必要解释保留。正文默认英文，规划可用作者语言。只读取当前任务所需来源；审批沿用既有授权。

## S-INT-1. 起草前先排八段功能

本版默认采用八个功能段，按下表逐句起草。每段第一句总领本段。P1–P4 负责建立问题，P5 给方法，P6 列贡献，P7 区分最近邻，P8 导航。不要先写一段方法，再返回背景解释为什么需要方法。

| 段落 | 单一任务 | 默认句数 | 交给下一段的问题 |
| --- | --- | --- | --- |
| P1 | 任务价值与一般困难 | 四句 | 为什么需要外部资源或新的解决路线 |
| P2 | 合理路线与具体障碍 | 五句 | 看似自然的路线为什么不能直接奏效 |
| P3 | 既有路线分类与假设 | 六句 | 到底是哪类接口或约束尚不充分 |
| P4 | 核心技术矛盾与研究问题 | 六句 | 方法必须明确改变什么 |
| P5 | 总体方案及逐项回应 | 七句 | 本文具体形成了哪些贡献 |
| P6 | 贡献清单 | 一句引导加默认三项 | 各贡献与最近邻有何本质区别 |
| P7 | 最近邻区别 | 四句 | 读者应如何定位本文 |
| P8 | 全文导航 | 两句 | 后文各章分别提供什么 |

采用本模板时，先按作者语言填写逐句任务表，再写英文。若最近邻定位已完整放在 P3，允许将 P7 功能并入 P3，但在大纲中标明承载句；不能直接丢失定位。贡献数量服从实际独立内容，不为凑三项发明设计。上述调整需列明对应关系，不能以“自由写作”为由跳过研究动机。

## S-INT-2. P1 任务价值与困难 四句

| 句位 | 必写内容 | 英文句架 |
| --- | --- | --- |
| P1-S1 | 定义研究对象与任务，引用原始或权威来源 | [Task] aims to [specific objective] from [observations]. |
| P1-S2 | 说明该任务能提供何种独特信息或能力 | [Observable property] provides [specific information], enabling [use]. |
| P1-S3 | 给出一至两个与技术目标相关的实际需求 | [Application or scientific need] requires [capability relevant to the task]. |
| P1-S4 | 用物理、统计或计算上的具体困难收束 | However, [weak/limited/heterogeneous input condition] makes [operation] difficult, while [data or resource condition] restricts [learning capability]. |

P1-S4 的每项困难都必须在后文得到回应。背景价值不能夸大成已经验证的应用能力；例如微表情线索不能直接写成客观真实情绪读取。

## S-INT-3. P2 合理路线为何遇到障碍 五句

| 句位 | 必写内容 | 英文句架 |
| --- | --- | --- |
| P2-S1 | 总句承接 P1 的困难，引入最自然的解决路线 | [Established route/resource] offers [specific remedy] for [difficulty]. |
| P2-S2 | 解释路线为何合理，给资源、监督或先验的实际优势 | [Resource] contains/provides [verified property relevant to learning]. |
| P2-S3 | 给出可迁移或可利用的共同基础 | [Source and target / two objects] share [task-relevant basis]. |
| P2-S4 | 转折到当前场景中特定差异 | However, [objects] differ in [precise property affecting the representation]. |
| P2-S5 | 将差异变成一个技术要求 | Therefore, [operation/interface] must [requirement preserving useful information under that difference]. |

## S-INT-4. P3 已有路线怎样处理问题 六句

| 句位 | 必写内容 | 连接与英文句架 |
| --- | --- | --- |
| P3-S1 | 总句给出与本文问题有关的分类依据 | Existing approaches can be grouped by how [resource/constraint] enters [target model]. |
| P3-S2 | 第一类的操作与已有价值，配准确引用 | [Family A] [operation], providing [benefit]. |
| P3-S3 | 第一类在当前问题上的具体条件与后果 | However, [specific condition] leaves [unresolved requirement]. |
| P3-S4 | 第二类怎样补足前类，配准确引用 | In contrast, [Family B] maintains [capability] by [operation]. |
| P3-S5 | 第二类的关键假设，以及当前任务为何不自动满足 | [Operation] assumes [relation], which is not guaranteed under [specified condition]. |
| P3-S6 | 总结已有进展后仍未确定的对象或变量 | The reviewed formulations leave [specific comparison/constraint/choice] to be determined for [current setting]. |

若有第三类，将其压缩为 P3-S6 前的一句，并保留原来的收束句；在句位表中明确新增理由。不要凭模板虚构三类，也不要把本应放在 Related Work 的完整引用综述塞入引言。

## S-INT-5. P4 把一般困难收敛为研究动机 六句

| 句位 | 必写内容 | 英文句架或写法 |
| --- | --- | --- |
| P4-S1 | 总句指出本文真正需要处理的技术矛盾 | The central difficulty concerns [precise relation between objects], because [specific requirement]. |
| P4-S2 | 解释既有约束实际比较或改变了什么 | [Existing operation] compares/updates [object] under [assumption]. |
| P4-S3 | 解释当前条件为何使该假设不足，并说明后果 | Under [current condition], [verified structural fact] limits [what the constraint can guarantee]. |
| P4-S4 | 给支撑该诊断的现有文献、定义或已完成对照 | [Existing evidence or structural observation] identifies [bounded aspect of the problem]. |
| P4-S5 | 引出第二个影响效用的因素或必要条件 | Moreover, [second factor] determines [different aspect of the interface/problem]. |
| P4-S6 | 明确方法必须回答的研究问题 | The resulting problem is to determine [how/objective] and [where/condition] under [scope]. |

本段是研究动机的核心。必须完成“操作—假设—失配—后果—要求”这一链，不能用任务难、数据少、已有方法不充分三句话跳到模型名称。

可用的完整动机链为：

~~~text
困难：目标信号弱且标注有限。
合理路线：利用较充足或较明确的相关先验。
既有假设：在某种对应、统计、监督或条件下传递该先验。
具体矛盾：当前对象在一个与约束有关的属性上不等价。
后果：可用的先验不能通过现有接口被充分利用，或产生不合适约束。
技术要求：明确比较什么，以及在什么条件或位置施加比较。
方法回应：提出与上述要求逐项对应的机制。
~~~

P4-S4 只能使用已经存在的证据。引言保留一项最关键趋势或一个汇总量，不复述消融表。事后观察不得伪装成事先实验假设，也不为填句位要求新实验。

## S-INT-6. P5 方法逐项回应前述问题 七句

| 句位 | 必写内容 | 英文句架 |
| --- | --- | --- |
| P5-S1 | 一次性引出方法名称、类别与核心思想 | Accordingly, we propose [Method], a [category] that [central principle]. |
| P5-S2 | 解释总体架构或核心参考怎样建立，为什么需要 | [Framework/reference] supplies [role] during [phase]. |
| P5-S3 | 回答 P4 的第一个问题，说明核心机制约束什么 | Specifically, [Mechanism A] compares/transforms [object] through [operation]. |
| P5-S4 | 回答第二个问题，说明位置、条件或配置怎样确定 | [Mechanism B / selection rule] determines [second variable] using [valid criterion]. |
| P5-S5 | 明确输入模态或任务所需的配套条件 | For [input modality], [specific geometric/physical requirement] must also be respected. |
| P5-S6 | 说明配套设计怎样满足该条件 | [Supporting component] performs [verified operation], preserving [defined property]. |
| P5-S7 | 说明最终训练与部署关系或方法输出 | During inference, [retained components] produce [output], while [training-only parts] are removed. |

只写原理级操作，不写学习率、投影数量、卷积的逐层细节和完整损失。每句必须能回指一个已建立的问题，不能突然增加没有动机的模块。P5-S5 与 S6 紧接，不能只列一个输入问题而没有回应。

不存在训练专用组件时，P5-S7 写实际输出和使用方式，不照抄删除教师的句子。不存在独立配套设计时，将 S5–S6 映射为核心方法的另一个真实必要条件，并在大纲标注；不补造模块。

## S-INT-7. P6 贡献清单 逐项与证据对应

引导句固定采用自然表达：

> The main contributions are summarized as follows:

默认三项分别写框架或问题重述、核心机制、必要的任务适配与验证。每项用一至两句，采用平行的名词开头，避免全部使用 We propose。

| 条目 | 第一句必须写什么 | 需要第二句时写什么 |
| --- | --- | --- |
| C1 | 框架或问题重述改变的对象、关系与技术能力 | 该框架的关键角色或使用性质，不能重复整个总体流程 |
| C2 | 核心机制改变哪项操作、假设或约束 | 已有证据支持的具体技术作用，不扩大为未经隔离的原因 |
| C3 | 任务适配执行什么操作、满足什么必要条件 | 完整方法的实际评价范围和有限结论，不逐表报数 |

~~~text
C1: A [framework/formulation] is developed to [technical change and capability].
C2: A [core mechanism] is introduced to [specific operation or assumption change],
    with [bounded evidence supporting the technical role].
C3: A [task-aware design] is constructed to [modality/task requirement],
    and the complete method is evaluated under [actual scope].
~~~

贡献必须包含对象、实质改变和作用。不能只列模块名，不能把最高性能当作没有技术内容的一项，也不能把同一概念在 C1/C2 换词写两遍。

起草前建立“引言问题—贡献—方法小节—实验分析”四列对应表。没有方法承载或证据支持的贡献不能进入清单。

## S-INT-8. P7 最近邻区别 四句

| 句位 | 内容 |
| --- | --- |
| P7-S1 | 指出实际最近邻与本文共享的目标或思想，给已核实引用 |
| P7-S2 | 准确说明最近邻处理的对象、假设或机制 |
| P7-S3 | 在同一维度说明本文改变什么 |
| P7-S4 | 说明区别对当前任务的含义与成立范围 |

只选最能避免审稿人混淆的两至三个维度，不写防御清单，不给未经核验的“首次”。若最近邻的实际内容无法确认，保留待核定位，不填想象中的缺陷。

## S-INT-9. P8 导航 两句

~~~text
Section II reviews [relevant research lines], and Section III presents [the method].
Section IV describes [protocol and evidence], and Section V concludes the paper.
~~~

按真实章节改写，不逐小节罗列。导航只出现一次，不在段末再补“接下来先介绍背景”。

## S-INT-10. 引言的转折与动机验收

- P1 的困难在 P2 被接住，P2 的差异在 P3/P4 被具体化。
- P3 每个批评先有对象、操作与已有价值，再写条件和后果。
- P4 同时给出问题对象、假设、失配和技术要求。
- P5 每个设计回指 P2–P4 的要求，不能只有模块名称。
- P6 每项贡献在方法与实验均有位置，排名量词保持一致。
- 最近邻区别不依赖未经验证的文献内容，导航与实际章节一致。
- However 用于转折已有预期，Therefore/Accordingly 用于由前提导出要求或方案，Specifically 用于展开。
- 禁止从“数据有限”直接跳到“因此提出三个模块”；禁止用对比结果替代技术动机；禁止在方法引出后返回宏观背景。

**完成标准：**每一句都有确定任务，读者可沿背景、路线、假设、技术矛盾、方法回应和贡献连续走到全文证据。

只改某一段时，读取其前后文、对应主线与来源即可；无需重写其余七段。整节授权时完成整节再汇报，不插入逐段 go。

## S-INT-H. Hardened checklist (distilled from rejected drafts)

1. **Mirror the exemplar at the level of function, not wording.** Identify, in the target venue's strongest paper on a neighbouring problem, how many paragraphs the Introduction has and what each sentence does. Reproduce that function sequence; never copy sentences.
2. **Word budget per paragraph** at most the exemplar's corresponding paragraph; measure it. Whole-section growth is allowed only when the author says so, and clarity must be reported as the reason.
3. **No numerical results in the Introduction.** Use calibrated qualifiers. A count of comparisons is also a result.
4. **The motivation paragraph argues, it does not report.** Paragraph 2 (route and barrier) makes the case by reasoning about what the protocol permits; own experimental findings belong in the experimental section. If the exemplar does not report its findings there, neither does this paper.
5. **Every difficulty raised in P1 is answered later.** A motivation sentence with no later response is decoration.
6. **P4 must complete the chain**: operation → hidden assumption → current mismatch → consequence → technical requirement. "Data are scarce, therefore three modules" is a rejection.
7. **Contributions**: one lead-in sentence in the form the author approves, then items that each name an object, a substantive change, a capability and support. Use the real number of independent contributions. No parenthetical insertions in the contribution list, no module names alone, no "and MERBase," style tail.
8. **Enumerations are explicit.** If the text announces "the following three aspects", the body uses First/Second/Third at the announced places, and each item starts from a real sentence.
9. **Do not name a method the rest of the Introduction does not introduce**; do not introduce a comparator without saying what it is.
10. **Related-work placement**: if the nearest-neighbour positioning sits inside P3, do not also write P7; if P7 exists, it compares two or three dimensions and ends on what this work changes.
11. **Soften the attitude to prior protocols.** Acknowledge what an existing protocol achieved, state precisely what it leaves unconstrained, and present this work as adding the missing constraints. Do not say or imply that earlier results are wrong.
12. **Sensitive application framing** follows [voice-and-positioning.md](voice-and-positioning.md) VP8.
13. **Navigation**: one or two sentences, matching the real section order; no list of subsections; no second navigation sentence later.
14. **Forward references**: the Introduction may point forward; body sections may not (see [paragraph-architecture.md](paragraph-architecture.md) PA13).
15. **No sentence may be lifted from the Abstract**; the Introduction states the same facts with different functions.
