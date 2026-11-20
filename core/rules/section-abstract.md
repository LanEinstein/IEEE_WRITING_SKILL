<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Abstract 逐句规程 (S-ABS)

适用配置：`journal_method_structured_v2`。以下句位、段数与篇幅是本套明确采用的写作规程，不是 IEEE 对所有论文的官方规定。真实内容或正式限制不适用时，说明相邻合并／功能映射，不补造事实；总句、具体动机和必要解释保留。正文默认英文，规划可用作者语言。只读取当前任务所需来源；审批沿用既有授权。

## S-ABS-1. 九句的先后功能固定

摘要采用“价值 → 合理路线 → 具体障碍 → 方法 → 总体设计 → 核心机制一 → 核心机制二 → 必要配套设计 → 证据”的九句骨架。S1–S3 建立动机，S4 引出方法，S5–S8 只讲方法，S9 报告证据。方法出现后不再返回一般背景，也不在方法句之间插入结果。

| 句位 | 必须写的内容 | 与前后句怎样连接 | 信息边界 |
| --- | --- | --- | --- |
| A1 | 任务的具体价值，以及任务能提供该价值的原因 | 先让读者知道研究对象和研究意义 | 一句，不列长应用清单，不声称未经验证的真实能力 |
| A2 | 为解决一项明确困难，已有哪条合理路线或资源 | 从需求落到可用路径，先介绍资源或方法，再讨论不足 | 必须点明困难与路线之间的关系 |
| A3 | 路线依赖的条件、当前场景的失配和直接后果 | 用 However 扭转 A2 的合理预期，把动机收敛到技术问题 | 不只写“仍有挑战”，不泛称全部已有方法失败 |
| A4 | 方法名称、所属类型和统一设计原则 | 用 To address [具体问题] 接住 A3 | 只提出一次方法，简称按目标正式要求处理 |
| A5 | 总体结构、参考、表示或关键角色如何建立 | 用 Specifically 把 A4 的原则落到总体操作 | 交代必要角色，不开始罗列所有小模块 |
| A6 | 第一项核心机制比较、变换或优化什么 | 接住 A5 的对象，回答最主要的技术要求 | 给操作和功能，不给公式、层数或搜索范围 |
| A7 | 第二项核心机制怎样补足不同的要求 | 点明“位置、条件、配置或另一项约束”的控制方式 | 不能换词重复 A6，也不能强行把并行机制写成时间步骤 |
| A8 | 必要的任务适配或最终使用性质 | 用 Finally 收束最后一项真实设计 | 不堆辅助模块，不虚构第三项创新 |
| A9 | 数据／任务范围、一个最有信息的结果关系及已有验证 | 用 Experiments on... 结束完整论证 | 指标、比较和量词准确，不逐数据集报数，不添加未做的验证 |

默认先写九行，分别完成 A1–A9，再合成单段。若实际方法没有独立的配套组件，A8 写真实的输出或训练—推理性质，并在规划表中说明功能映射；不补造模块。若投稿硬限制要求压缩，合并相邻功能，但要在审查稿中保留句位映射，不得删掉具体动机或关键机制。

## S-ABS-2. 可直接填写的英文九句骨架

~~~text
A1. [Task] reveals [task-specific information], enabling [specific purpose].
A2. To alleviate [concrete difficulty], [established route/resource] provides
    [relevant capability or prior].
A3. However, [specific mismatch or assumption] limits [operation], leading to
    [precise consequence].
A4. To address [named technical gap], we propose [Method Name], a [method category]
    that [verb phrase expressing the central design principle].
A5. Specifically, [framework/reference/representation] [verified operation] to
    [overall technical role].
A6. [Mechanism A] [compares/transforms/optimizes the defined object] through
    [essential operation].
A7. To control [second requirement], [Mechanism B or selection rule] [operation]
    using [valid criterion].
A8. Finally, [necessary task-aware design or output property] [operation]
    to [verb phrase expressing the distinct role].
A9. Experiments on [actual benchmarks/tasks] show [scoped headline result],
    and [existing analysis, when available] supports [bounded design claim].
~~~

方括号是必须填写并核实的内容，不是把通用名词留在最终摘要的许可。没有对应实验时，A9 只写实际证据，不保留不存在的消融从句。First／Then 只在描述真实步骤时使用；两项设计并行时直接说明各自作用，不为了套开头词虚构执行顺序。

## S-ABS-3. 研究动机在 A2 与 A3 中必须写完整

差的写法：

> Existing methods have limitations. To address the limitations, we propose a novel network.

缺少路线的合理性、具体失配和后果，任何网络都可以填入。

合格的句位内容是：

~~~text
A2：某一资源或路线为什么能缓解当前困难。
A3：该路线的某个具体假设在当前场景中为什么不充分，
    因而限制了哪一项技术作用。
A4：本文用什么统一原则回应上述技术问题。
~~~

## S-ABS-4. 九句完成后的逐句核查

1. A1 的价值有具体对象，A2 的困难与路线对应。
2. A3 具有“失配／假设—受限操作—后果”，不是空转折。
3. A4 与 A3 的问题同一，不额外引入另一套问题。
4. A5 建立角色，A6/A7 分别回答不同要求，A8 只保留必要配套。
5. A9 的比较对象、协议范围和量词能在正式结果中找到。
6. 缩写在摘要内独立检查；是否允许、是否需要展开服从目标要求。
7. 不含引用、脚注、公式和实现超参数等目标禁止的内容。
8. 不出现未验证首创、普遍有效、消除全部差异或显著提升。
9. 用工具量词数。工作预算约 200 个英文词，最终服从目标正式上限与下限。
10. 压缩时先删重复背景和修饰，不删 A3 的动机后果，不把 A6/A7 压成只有模块名字。

## S-ABS-5. 标题与关键词

标题表达研究对象、技术思想和必要的任务限定，避免用 new、novel 等修饰替代内容。方法全称和简称对应，标题、摘要、主图与正文名称一致。

关键词覆盖任务、方法类别和关键表示，采用领域通行术语。IEEE 的一般建议见[文章结构与命名建议](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-the-text-of-your-article/structure-your-article/)，具体机械要求沿用项目已核对的目标配置，参见 [ieee-facts.md](../templates/ieee-facts.md)。

**完成标准：**能逐句指出内容、前提和作用，动机先于方法，机制回应问题，证据收束全文；没有用模板制造不存在的研究事实。

执行：先把 A1–A9 填为真实内容，再交付一个干净英文段落与实测词数。仅改摘要时不要求重建全篇大纲或编译整稿。工具用法见 [verification-protocol.md](verification-protocol.md)。

单一核心机制时，A7 承载已核实的互补必要条件或选择规则并注明功能映射；不能把一般调参升格为第二项创新。最终交付仍检查 A1–A9 的实际作用，不为九句制造研究内容。

## S-ABS-H. Hardened checklist (distilled from rejected drafts)

These items come from sentences that were rejected and then fixed. They refine S-ABS-1..5; they do not replace them.

1. **Open on the pain, not on the field.** The first one or two sentences state a difficulty the reader recognises as real, with its consequence ("emotion-irrelevant cues and unconstrained model selection can lift the score well above chance, so a high score alone does not establish that a method works"). Then say what the paper builds. A sentence that only defines the task reads as boilerplate.
2. **Make the pain acute once, early.** One sentence with a concrete number or a concrete mechanism gives the reader a reason to care. Remove the second and third sentences that repeat the same worry.
3. **No numbers.** No metric values, no counts of comparisons, no percentages. Use precise qualitative wording ("substantially", "consistently across the tested architectures"). Check the exemplar: if the target venue's exemplars carry no numbers in the abstract, carry none.
4. **No competitor names.** The abstract states what this work achieves; naming another method in it advertises them and assumes the reader knows them.
5. **A sentence function is not a sentence slot.** If a project's method has three components and no separate "adaptation" step, A8 states the real output or training/inference property. Never invent a component to fill a slot.
6. **The last sentence sells, and stays true.** It reports the strongest supported outcome (for example the most consistent model on the sealed benchmark), not a rank that implies being second, and not a claim about statistical superiority that the evidence does not establish.
7. **Every sentence states a relation to the previous one.** A definition, then a jump to the protocol problem, is not acceptable: the second sentence must follow from the first. Reject drafts whose sentences each state an independent fact.
8. **No self-undermining framing** ("we re-examine", "a simple attempt"). No "future" framing.
9. **Length** is the project's or the venue's limit; measure it, and state the measured count. If the project requires fewer words than an exemplar, say so and check sentence by sentence.
10. **Read the whole abstract aloud once.** Sentences that cannot be said in one breath are too long; sentence pairs with the same shape are rewritten.
