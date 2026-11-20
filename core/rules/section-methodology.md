<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Method 标题、主图、符号和公式 (S-MET)

适用配置：`journal_method_structured_v2`。以下句位、段数与篇幅是本套明确采用的写作规程，不是 IEEE 对所有论文的官方规定。真实内容或正式限制不适用时，说明相邻合并／功能映射，不补造事实；总句、具体动机和必要解释保留。正文默认英文，规划可用作者语言。只读取当前任务所需来源；审批沿用既有授权。

## S-MET-1. 先定方法标题层级

方法章标题采用 Methodology 或 Proposed Method，全文固定一种。一级小节按“任务与总体框架 → 主要表示或核心组件 → 关键技术机制 → 目标与训练推理”的依赖顺序设置。标题描述实际技术对象，不用有效、先进、强大等评价词。

可采用以下骨架，方括号替换为已实现的对象：

~~~text
III. Methodology
A. Problem Formulation and Overall Framework
B. [Canonical Name of the Main Representation or Backbone]
   1) [Canonical Name of Component 1]
   2) [Canonical Name of Component 2]
C. [Canonical Name of the Core Mechanism]
D. Training Objective and Inference
~~~

固定要求：

1. 同级标题采用平行语法，均以技术名词短语命名。不要混用“Why Alignment?”、“Our Powerful Network”和“Feature Adaptation”。
2. 标题层级表达概念包含关系。属于骨干内部的模块放在骨干小节下，不能与整个框架并列。
3. 一个核心问题有一个清楚的展开位置。不要把同一个目标拆进三个名称相近的小节，也不要把两个独立机制塞进“Other Details”。
4. 参数设置、训练轮数和实验超参数不单独包装成方法贡献。辅助算子可合写，不为每个激活函数设标题。
5. 小节排列与主图的计算依赖保持一致。并行分支按声明的阅读顺序讲，不能在介绍输出前突然使用下游变量。
6. 子标题不写识别结果、排名或消融结论。Overview、Discussion 等通用名称只承担明确的概述或讨论功能。
7. 每章和每个技术小节都有总句。章首总句概括全章，模块首句说明该模块处理什么问题及执行什么操作。

## S-MET-2. 子标题与主图必须逐项对应

起草前先建立映射表，图定稿后再核对一次。每个具有独立技术含义的模块子标题，必须在主图节点或已编号的展开面板中找到对应对象；主图中的关键模块也必须能在方法章找到解释位置。

| 方法标题或对象 | 主图规范名称 | 图中位置 | 输入与输出 | 正文与公式定位 |
| --- | --- | --- | --- | --- |
| [Main Representation] | [Declared full name/acronym] | [Branch/panel] | [Defined input → representation] | [Subsection; equation] |
| [Core Alignment Mechanism] | [Canonical node] | [Compared objects/loss edge] | [Representations → constraint] | [Definitions; objective] |
| [Training Objective and Inference] | [Objective/output nodes] | [Training/inference path] | [Loss terms → updates/output] | [Final objective; procedure] |

上表展示对应方式，不要求所有论文采用这些模块。全称与已明确声明的缩写可以对应；不能用三个近义名称指同一组件。图、子标题、图注用三个未声明等价的名称，而没有声明同一对象，属于不合格映射。

图中的大小写、连字符、编号与正文保持一致。对多个子操作的组合标题，逐项注明对应节点，不把整组标题粗略指向“主图右侧”。一组小算子由所在模块解释，无需为每个 Conv 或 LN 增加独立小节。

还必须核对：

- 放大引线与真实计算箭头使用不同视觉语义。
- 重复绘制同构模块不自动表示参数共享。
- 教师冻结、stop-gradient、适配器训练状态和训练专用损失标示准确。
- 图中阶段编号对应实际结构，不能为了形式引入未实现的任意阶段数。
- 若图内符号与正文不同，先统一符号；若图的计算关系有误，修图，不能反向编造正文解释。

## S-MET-3. 章首与总体框架逐句写法

方法章首默认三句：

| 句位 | 必写内容 | 英文句架 |
| --- | --- | --- |
| M0-S1 | 用一句话总述方法由哪些主要部分构成以及共同处理的技术问题 | [Method] integrates [main parts] to [specific technical objective]. |
| M0-S2 | 指向主图，说明整体计算路径与训练／推理角色 | The overall data path in Fig. [X] connects [input], [representations], and [output/objective]. |
| M0-S3 | 按实际小节顺序导航 | The following subsections describe [A], [B], and [C]. |

总体框架段默认四步，按主图讲完一条完整路径：

1. First：输入来自哪里、包含哪些通道或结构、进入哪个模块。
2. Next：主要分支或表示怎样产生，各分支作用是什么。
3. Then：怎样适配、交互或施加核心约束，操作作用于哪个对象。
4. Finally：怎样得到训练目标和预测输出，推理保留哪些部分。

每句都要有对象和操作。不能连续使用“extract features”“process information”而不说明是什么特征、哪条分支和下一步去向。

## S-MET-4. 每个核心模块采用同一展开顺序

| 句位或步骤 | 任务 | 写作要求 |
| --- | --- | --- |
| M1 | 总述局部问题与模块操作 | 接住前一模块的输出，说明当前模块改变什么 |
| M2 | 定义输入与已知量 | 来源、张量形状、索引和坐标系明确 |
| M3 | 解释设计意图并引出公式 | 说明为何采用该运算，不能只写“定义如下” |
| M4 | 给出核心公式 | 保留复现必需的操作，避免堆砌无新含义的展开式 |
| M5 | 解释首次出现的符号与运算轴 | 对样本、空间、通道、类别、阶段逐一辨明 |
| M6 | 解释公式的物理或功能含义 | 解释约束了什么、保留了什么、输出有什么作用 |
| M7 | 说明输出如何进入后续计算 | 回接框架、下一模块或最终目标 |

M4 是公式块，不是额外凑出的一句英文。一个模块有多条重要公式时，重复“M3—M6”单元，而不是先堆全部公式、最后给一串 where。若模块包含两个独立机制，拆成两个总分段落。

## S-MET-5. 符号登记与首次定义必须完整

每个新符号登记“意义—来源—形状／取值域—定义位置—使用位置”。新稿从零建立最少必要符号；已有稿件修订优先复用符号，不为使形式更一般而增加记号。

硬性核查项：

1. 一符一义。阶段数、类别数和投影数不能共用 K；学生下标、阶段索引和阶段集合不能靠几乎相同的 S 勉强区分。
2. 索引范围明确。b 表示样本时不在下一式中改成通道；阶段上标与转置上标需要区分。
3. 标量、向量、矩阵、集合和算子采用一致的体例，文字角色下标与变量下标区分。
4. 第一次使用前或在紧接的定义从句中说明含义，不能先给损失，隔两页才解释投影变量。
5. 所有张量轴都说明。B×C×H×W 中的每一维是什么，重排后每行代表什么，统计沿哪个轴计算。
6. 跨式复用说明来源。例如“the adapted teacher feature in Eq. (...)”之后再定义投影，不能让读者猜中间变量来自哪里。
7. 图内文字、算法、公式、表注和正文采用同一记号。缩写不要为避重改名。
8. 局部省略阶段上标时先声明省略范围，进入下一小节后恢复正确索引。
9. 只在一个位置定义完整含义，后文使用回指；不要反复重新定义为略有不同的对象。

例如 B×(CHW) 与 (BHW)×C 定义的是不同投影空间，B×B 注意力在相应定义下对应 batch 轴而非空间轴。光流位移分量、采样位置和变换后的向量也不是同一种变量。这些差别属于方法含义，不能当作排版或简写处理。

## S-MET-6. 每个公式都要过三个检查层

**含义检查：**公式前有明确目的，公式后有新符号释义、操作解释和下游用途。核心损失不仅说明“第一项、第二项”，还要说明各项对应的比较对象。

**数学检查：**维度可相乘，求和与平均轴明确，概率归一化方向正确，索引闭合，输入输出的取值域相容，空集合和边界条件有定义。均值、方差、标准差、标准差之差的平方分别写清，不能互换。

**实现检查：**重排、插值坐标约定、stop-gradient、归一化统计、随机方向是否共享、数值稳定项、训练和推理分支与实际采用的方法一致。数学关系与稳定化实现分别说明，不用一个“≈”掩盖两种算法。

合格公式单元的英文句架：

~~~text
To [precise purpose], [operation] is applied to [defined inputs]:
[equation]
where [new symbols and domains] denote [meanings].
The [term or operation] controls [operational meaning], while [another term]
controls [different meaning].
The resulting [output] is supplied to [next consumer].
~~~

例如，若某个损失只比较投影均值与标准差，解释时应写投影中心和离散程度。不能把标准差项口头改成未经说明的方差匹配，也不能由前两阶统计推出完整高阶或类别条件分布等价。上述判断应依据损失定义，不以性能提高替代推导。

排版上，公式作为句子的一部分处理标点，编号与文字引用一致；长公式使用合适的对齐和换行，不压成难以阅读的小字。不要同时出现未编号关键式、失效引用和大量没有使用去向的符号。

## S-MET-7. 分开结构 实验取值与最终预测器

结构定义包括真实阶段数、改变运算的卷积核、数据路径、损失形式、坐标关系和必要稳定化说明。实验部分报告本研究采用的输入尺寸、训练轮数、权重、投影次数和选择配置。不能按“出现数字就搬走”机械分类。

完整交代哪些参数冻结、哪些更新，stop-gradient 是否位于可学习适配器之前，归一化状态是否更新，推理保留什么。单模型结构与多模型预测器分别写清。方法章解释操作与可推导性质，不插入识别排名或消融结论。

**完成标准：**标题可映射到主图，主图可复原为公式，公式可追踪到输入和输出；每个符号与每条关键计算均有明确的来源、含义、形状和去向。

可填写台账见 [title-figure-symbol-map.md](../templates/title-figure-symbol-map.md)。没有现成主图时可先交付节点／连接说明和方法正文，不等待作者画完图；不擅自发明图中运算。

## S-MET-H. Hardened checklist (distilled from rejected drafts)

1. **A module paragraph opens with the problem or the purpose, then names the module**, then its construction, then the property it guarantees. Never open with a bare module name or a bare letter.
2. **Module paragraphs do not share one opening frame** and do not use ordinals ("we first propose", "Second,", "The third module"). Each opens from the problem it addresses.
3. **Each module needs a result sentence somewhere** in the evaluation; a component introduced and never measured is a gap the reviewer will find.
4. **Say what the operation does in concrete terms**, checked against the implementation (for example, how a readout maps a feature map to a vector). Do not describe a mechanism with an abstract metaphor.
5. **No design requirement language in an analysis section.** "The readout must preserve location" belongs in the module's design rationale, not in the section that reports the finding.
6. **A definition of a key operation deserves a display**, with the symbol defined in the sentence; a trivial identity does not.
7. **Do not introduce a symbol the main text does not define**, and do not carry a symbol the text dropped.
8. **Training-only components are identified**: what exists at inference, what is removed, and whether the paper reports a search or a fixed configuration.
9. **Do not disclose internal history of a method** (repair rounds, acceptance criteria, variants). State the configuration used.
10. **Figures, headings, symbols, axes and text use one name per object** (see [terminology-and-notation.md](terminology-and-notation.md)).
