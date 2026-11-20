<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Experiments 总分与机制分析 (S-EXP)

适用配置：`journal_method_structured_v2`。以下句位、段数与篇幅是本套明确采用的写作规程，不是 IEEE 对所有论文的官方规定。真实内容或正式限制不适用时，说明相邻合并／功能映射，不补造事实；总句、具体动机和必要解释保留。正文默认英文，规划可用作者语言。只读取当前任务所需来源；审批沿用既有授权。

## S-EXP-1. 先让评价过程可核查

在结果之前，交代数据、标签、划分、预处理、模型选择、指标和实现设置。为篇幅可以压缩表述，不能省去会改变结果含义的条件。数据集专用协议分别说明，共同设置集中说明。

训练数据和教师预训练数据的被试重叠检查，应说明排除机制及范围。不能只用“无泄漏”作自我认证。也不能为了写出通用协议，把官方固定划分的数据集强行写成 LOSO。

指标首次定义时交代计算对象、标度、方向和加权方式。分类指标尤其应区分宏平均与微平均、类别平均与样本平均；会影响结果时，说明无支持类别或零分母的处理。主要指标由研究目标确定，不从示例自动继承 UF1（unweighted F1，类别 F1 的非加权平均）。

## S-EXP-2. 写明聚合的顺序和单位

以下是嵌套评价中必须区分的操作示例，仅在实际采用时报告，不强加此流程或重复数：

1. 合并内折验证预测，计算用于 epoch 或配置选择的验证指标。
2. 同一外折内，多个模型对同一样本的类别概率等权平均，再取 argmax。
3. 合并外折的最终预测，形成每个种子的一个混淆矩阵和 UF1。
4. 对多次完整重复得到的 UF1 计算均值与样本标准差。

平均概率、平均 logit、多数投票、平均折指标和合并预测后算指标不是同一操作。正文应采用实际流程，不用熟悉的默认流程补齐空白。

## S-EXP-3. 声明不确定性的含义

“均值 ± 标准差”至少交代重复轴、独立单位、重复次数和估计方式。样本标准差、总体标准差、标准误与置信区间分别表达不同对象。没有逐次结果时，不从表格中反推不存在的检验或区间。

模型种子间变化不能直接当作受试者总体不确定性。单值结果不能仅凭小数位数判断为单次运行或多次均值。确定性方法可以报告单值，但需要确认实际流程是否还包含随机因素。

例如，已确认 q₁,…,qₙ 是 n 次完整重复的指标、n>1 且误差项采用样本标准差时，均值为 Σqᵣ/n，标准差为 sqrt[Σ(qᵣ−均值)²/(n−1)]。这项计算只表达已声明重复轴上的离散程度，不自动产生总体置信区间。

## S-EXP-4. 据实说明基线处理

区分直接引用的文献结果、作者复现、统一协议重新评估和为输入适配而修改的基线。说明会改变可比性的预训练数据、输入、调参、模型选择或资源预算差异。

“所有方法在统一代码库中重新实现”只能在确实发生时使用，不能当作固定公平性套话。最相关、最有解释力的基线优先于仅按发表层级筛选。

## S-EXP-5. 设置部分每段同样采用总分结构

设置段的首句先说明本段采用什么评价规则或交代哪一类设置，再展开必要细节。设置段不写性能结论，也不强加没有证据的机制解释。

| 段落 | 总句任务 | 分述顺序 | 收束信息 |
| --- | --- | --- | --- |
| 数据集与标签 | 总述评价覆盖哪些数据和标签协议 | 数据来源与版本 → 样本范围 → 类别映射与排除条件 | 哪些方法共同采用该样本集合 |
| 预处理与输入 | 总述模型使用什么输入及其构造方式 | 定位与裁剪 → 帧对或采样 → 模态处理 → 输入通道 | 输入怎样进入模型，特殊失败如何处理 |
| 划分与选择 | 总述训练、验证和最终测试如何分工 | 划分单位 → 内外层关系 → epoch／配置选择 → 最终预测 | 哪些数据只用于最终评价 |
| 指标与重复 | 总述主要指标衡量什么、为何适合任务 | 定义与方向 → 聚合顺序 → 重复轴与次数 → 误差项 | 单次指标与最终报告量的关系 |
| 实现设置 | 总述各模型共享哪些实际训练条件 | 优化器与训练日程 → 关键结构与超参数 → 调参依据 | 特殊方法或基线适配的已知差异 |

全局协议在这里讲完整。后面的结果段只补充当前对照特有的控制条件，不重复训练轮数、种子或数据划分。若一个设置段同时承担数据、模型选择和优化三个任务，应按上表拆分并各写总句。

**完成标准：**读者知道每个结果来自什么设置，知道用于选模型的数据与用于报告的数据，知道误差项和基线差异表达什么。

## S-EXP-6. 先为每个小节和段落分配独立问题

实验章按“总体表现 → 核心因素 → 条件与配置 → 支撑组件 → 机制与失败边界”组织证据。小节标题直接命名受检因素，例如 Frozen Teacher versus Joint Training、Effect of Alignment Depth。不要使用 Ablation Study I、More Experiments 等没有判断对象的标题。

写作前列出每段唯一问题。例如匹配目标比较解释比较对象与假设，教师更新比较解释参考映射是否改变，配置比较解释约束作用位置，向量变换比较解释采样与分量坐标，诊断比较解释所测对象和残余差异。每段只承担自己的问题，不反复复制同一背景或机制。

章首段也采用总分：第一句概括全章评价范围，后续句按实际顺序说明协议、比较、消融与诊断，不再返回背景动机。

## S-EXP-7. 结果分析默认采用六句规程

每个结果分析段先总后分。默认写六句，长短按内容调整，但以下功能不能删除。保留条件与数值紧密时可以合句，原因分析不能被压缩成“证明有效”。

| 句位 | 必须写什么 | 可直接填写的英文句架 |
| --- | --- | --- |
| E1 总句 | 当前段落检验的因素、比较对象或核心判断 | The [factor] ablation compares [A] with [B] under [specific setting]. |
| E2 控制 | 当前对照实际改变什么，保留哪些决定解释的条件 | The two settings retain [verified common conditions] and differ in [tested operation]. |
| E3 证据 | 在表图定位下给最关键数值、差值或范围 | The results in Table [X] give [metric relation], with [scope and comparator]. |
| E4 原因一 | 一个条件怎样处理信息或施加约束，解释其功能后果 | [A] applies [verified operation] to [object], so [direct operational consequence]. |
| E5 原因二 | 另一条件在同一维度有什么不同，为什么与当前任务相关 | [B] changes [specific operation], which [relevant functional difference under the stated condition]. |
| E6 推论 | 从证据与解释推出局部设计认识或边界 | The comparison supports [specific design implication] within [evaluated setting]. |

E2 中“其余均相同”必须有材料支持。目标分别调优权重时，明确报告该事实，不假装全部训练条件逐项一致。对主表的跨方法比较，应写可比条件与已知差异，不能冒充单变量干预。

先写 E1，再检查 E2–E6 是否全部支撑 E1。首句不能是 Table X、As shown in Fig. X、一个悬空问题，或一般性的方法动机。图表位置放入证据句，实验任务和科学对象占据主语。

一段默认只保留一组关键现象与一组关键比较。现象描述通常控制在两句内；原因和机制用完整句子展开，篇幅不能被读表取代。存在会改变解释的反例时，在证据或推论中写清，不另开一段没有必要的防御。

## S-EXP-8. 从现象推进到原因的具体办法

分析必须回答三个问题：

1. **运算或约束是什么？**作用于原始输入、中间激活、投影统计、类别关系还是对齐目标？
2. **功能差异是什么？**比较是否依赖等索引对应，参考映射是否改变，向量坐标是否随空间布局变化，信息在提取阶段还是聚合阶段起作用？
3. **为什么与当前结果相关？**该差异怎样对应受检任务中的困难，以及本次对照揭示的收益、下降或例外？

例如，冻结教师的分析应写清“联合训练同时改变学生与产生监督目标的映射；冻结保留源任务预训练的映射，让学生与适配器适应目标数据”。不能只说“冻结更稳定”，也不能无证据宣称测得了灾难性遗忘。

向量重定向的分析应写清“仅重采样改变向量所在位置，却保留原坐标系的分量；重新定向把分量转换到目标坐标系，保持布局与位移的关系”。不能只写“加入该模块后指标更高”。

| 不合格分析 | 为什么不够 | 必须补出的分析 |
| --- | --- | --- |
| Removing the block lowers UF1, demonstrating effectiveness. | 数值换成评价词，没有解释 | 模块提供哪类其他分支没有直接提供的信息 |
| The attention map peaks outside the face. | 只描述位置 | 结合运动强度、已有干预或证据说明当前错误与该位置的关系 |
| Distribution alignment learns better semantics. | 引入未测量对象 | 明确损失比较什么统计量，功能差异限于已定义的约束 |
| Deeper stages perform differently because the features differ. | 用常识重复现象 | 交代层次、分辨率和约束组合怎样改变被比较的对象 |
| The gain is caused by preventing overfitting. | 缺少支持该原因的分析 | 回到已验证操作解释，保留性能效果与机制解释的区别 |

分析原因不等于编造原因。已测效果、可由定义推出的操作性质、未被单独隔离的解释必须分清。明确写出实验条件与被测对象，用 supports 或 indicates 等词连接解释；不以肯定语气替代证据，不用反复的 may/might 掩盖没有内容的猜测。

## S-EXP-9. 不同实验采用不同的分析重点

| 实验类型 | 首句总领什么 | 关键证据 | 必须分析的内容 |
| --- | --- | --- | --- |
| 总体比较 | 哪一类协议下的性能关系 | 最强对照、总体范围、改变排名的例外 | 结合已核实方法与独立消融解释相关设计；主表本身不隔离唯一原因 |
| 加入／移除 | 哪个因素被改变 | 完整模型与变体的差值 | 模块提供的具体操作和信息，其他保留部分为何不能等价替代 |
| 替换比较 | 两种实现或约束的区别 | 同一范围内的替换差值 | 原始实现与替代实现究竟改变了什么 |
| 配置或阶段选择 | 选择规则与固定配置的关系 | 选择相对固定方案的收益、局部失败 | 不同配置对应的约束对象及其与任务的关系 |
| 目标族比较 | 族均值与个体排序分别是什么 | 家族汇总、最强目标、交叉例外 | 优化对象和统计约束的不同，不能把族均值扩大为所有成员 |
| 机制诊断 | 一个已定义的诊断命题 | 诊断量与对照，残余范围 | 量的物理或比较含义、能解释什么、没有测到什么 |
| 失败案例 | 当前一类错误的共同解释 | 真实案例与已有测量／干预 | 干扰、线索不足、线索未充分使用之间的区别 |

组件删除损失不能相加当作完整模型收益。分类成绩与诊断差异分别承担论证任务；投影差异下降不自动说明类别结构改善，测试时名次改变也不自动证明特定模块产生了全部收益。

## S-EXP-10. 数字必须携带比较对象和解释

数值句必须包含或紧接：指标、标度、数据集／协议、比较对象、方向、聚合范围和表图定位。差值与比例用工具计算后再写。

可采用句架：

> Replacing [verified operation A] with [operation B] changes [metric] from [value A] to [value B] on [protocol], an absolute difference of [computed value].

0–1 标度上的绝对差、百分标度上的百分点差与相对百分比不同。例句只是证据句，后文必须解释真实操作的差异，不能以数字句结尾替代分析。

## S-EXP-11. 把反例放进正确的总分论证

反例会改变总句和全文量词。例如：

- 一个目标族的均值较高，但个体目标之间有交叉：保留族均值优势与个体例外。
- 某一协议并非第一：跨协议总述只用实际胜出范围，摘要和结论同步。
- 部分配置比不加该约束更差：解释选择条件，同时限制“加上即有效”的主张。

没有已有证据解释差距时，报告事实及其改变的结论范围。不得编造基线缺陷，也不得因为必须分析原因就填入“数据更复杂”“类别更难”等没有支撑的套话。

## S-EXP-12. 统计与诊断边界保持准确

没有相应检验时，写更高均值、绝对差值或更低种子间样本标准差。误差条重叠、均值接近或未拒绝零差异，不能直接写成统计等价。已有检验需与实际假设、配对单位、指标及重复轴对应。

机制诊断限定到实际数据集、层、配置和统计对象。展示少数投影方向时声明选择方式，并结合已有总体汇总。较低的投影散度支持所测投影对象更接近，不能变成整个域已消除或所有类别结构已对齐。

## S-EXP-13. 完整段落与缺少解释时的处理

先按 E1–E6 写六行实质内容，再合为自然段。完整演示见 [applied-examples.md](../templates/applied-examples.md)。E4/E5 不能删去并改成“有效”；若方法定义足以说明运算区别，写可推导的功能解释并与测量效应分开。若定义本身也缺失，在审查稿标注 `[MECHANISM: 缺少哪项操作定义]`，暂缓依赖该解释的句子，继续其他段落。不得用数据更复杂、特征更好等猜测填空；不得自动增加实验。

**完成标准：**每段先有总句；证据后立即进入原因与机制；分析指出具体功能区别；结尾得到与控制和测量范围相符的认识。

## S-EXP-14. 先确认案例的来源与证明任务

记录权重、代码版本、划分、选择方式、目标类别、batch 与预处理。来自不同配置或历史模型的案例，按相应模型说明，不能自然继承最终表格的协议与性能。关联无法建立时，保留来源状态并缩小案例的证明任务，不靠文字修改消除冲突。

## S-EXP-15. 失败段落采用总句加成对分析

失败分析段默认按以下顺序组织：

| 句位 | 内容 |
| --- | --- |
| F1 | 总句概括本段涉及的错误类型，如干扰运动敏感或局部线索利用不足 |
| F2 | 指明样本范围、模型和所用观测，已在前段说明的协议不重复 |
| F3 | 第一例的关键现象或已有干预 |
| F4 | 紧接第一例的原因解释，说明干预改变什么或测量意味着什么 |
| F5 | 第二例的关键现象或对照 |
| F6 | 紧接第二例的原因解释，与第一例建立具体联系或区别 |
| F7 | 归纳这类案例揭示的局部边界 |

一个段落分析一类问题。不要把头动干扰、几何异常、嘴部弱运动和全部注意力问题塞进同一段。若只有一例，完成“观察—解释—有限结论”，不为凑数量补案例。

例如，去头动后的嘴部平均位移高于正确 Happiness 样本的参考值，和明显低于同一参考值，分别对应“有可用运动线索但利用不足”与“输入线索很弱”。测量出现时就解释高低的比较意义，不能先连续罗列幅值、概率和区域，再统一说“模型仍有局限”。

## S-EXP-16. 解释必须对应当前错误

Grad-CAM 指明目标类别和层，空间变换后对应正确坐标。热图高亮只是一种解释响应，不能直接当作错误原因或 AU 检测结果。

已有干预若改变预测，就说明被去掉或保留的输入信息及预测变化，结论限定于该案例和操作。区域遮蔽还会改变输入分布，不能由一次预测翻转推出全局唯一原因。有正确案例对照时结合已有结果解释，没有时不制造对照。

通用架构描述不能占据案例分析。几何变换的作用只在解释“坐标变换没有自动去掉干扰运动”时进入该段，不能替代对某一错误线索的说明。

**完成标准：**总句统领错误类型，每个观察紧接相应解释，测量的物理与比较意义明确，结论限定在真实来源和现有证据之内。

## S-EXP-H. Hardened checklist (distilled from rejected drafts)

1. **Every experimental paragraph yields at least one insight.** Analysis takes more space than the operation and the numbers. A paragraph that can be summarised as "we ran X and got Y" is rewritten.
2. **The subject is the method, protocol or finding, never the table.** "The ranking in Table 1 holds on ..." is rejected; "Our protocol generalises to unseen subjects, since ..." is accepted, with the table in parentheses.
3. **The topic sentence covers every point** the paragraph makes. Two points, both named.
4. **Each observation is followed by its analysis**, joined by the observation's subject. A separate explanatory sentence that starts a new topic reads as disconnected.
5. **End on the paragraph's own theme**, not on a paper-level selling sentence in an analysis section.
6. **Total–detail or total–detail–total.** When a paragraph ends on a bare comparison, add the closing sentence that states what the comparison shows.
7. **Chapter and subsection structure.** A navigation paragraph is one or two sentences. The relationship between subsections is carried by their titles and by each subsection's first sentence, not by a roadmap. Titles are noun phrases showing progression; no "From X to Y".
8. **Detail follows importance.** The strongest finding gets the fullest chain (phenomenon, mechanism, consequence); secondary findings get one clear sentence; no central finding is left without its insight.
9. **A paragraph about our own method's performance does not end on a competitor being best.** State what this work establishes, with the exact numbers, then the interpretation.
10. **Do not stress a side-step.** If the subsection is about modules, do not foreground configuration selection; if the subsection is about an input, do not foreground forward-pass counts.
11. **Do not name a comparator the main text never defines.** If a comparison needs a term ("test-time averaging"), define it or drop the comparison.
12. **Intervals and per-seed facts.** Keep the per-seed regularity in the prose; leave interval bounds to the figure or supplement unless the interval is the sentence's point.
13. **Ranks**: report a position when it supports a claim ("ranks in the top two of both tasks, which no other method achieves"), never as an incidental second place.
14. **Unfavourable outcomes** are reported honestly and read favourably; a formal criterion that was not met is stated where the review trail expects it, not volunteered in the main text.
15. **Numbers**: metric, scale, protocol, comparator, direction, aggregation. Compute every difference with a tool.
16. **Speculation** only if it states a general regularity the evidence supports; otherwise delete it.
17. **No repetition of the Introduction's motivation** inside a result paragraph; recall it with a short noun phrase and a section pointer.

## S-EXP-I. Section-level internal order

The order of a results section follows the argument, not the order the experiments were run:

1. what the evaluation measures and under which protocol;
2. the headline comparison and what it establishes;
3. the factor analysis that explains the headline;
4. the condition or configuration analysis;
5. the mechanism or diagnostic analysis;
6. the boundary or failure analysis, if the evidence supports one.

Each subsection answers one question, stated in its title and in its first sentence. If two subsections answer the same question, merge them; if a subsection answers no question, delete it.
