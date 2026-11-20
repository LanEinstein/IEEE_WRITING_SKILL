<!-- (c) 2026 Lan Zhang. CC BY-NC 4.0. Part of the IEEE Paper Suite. -->

# Conclusion 总分收束 (S-CON)

适用配置：`journal_method_structured_v2`。以下句位、段数与篇幅是本套明确采用的写作规程，不是 IEEE 对所有论文的官方规定。真实内容或正式限制不适用时，说明相邻合并／功能映射，不补造事实；总句、具体动机和必要解释保留。正文默认英文，规划可用作者语言。只读取当前任务所需来源；审批沿用既有授权。

结论默认一个段落，采用以下六个句位：

| 句位 | 内容 |
| --- | --- |
| C1 | 总句直接写整篇论文建立的核心认识 |
| C2 | 第一项关键机制怎样支撑该认识 |
| C3 | 第二项关键机制解决什么互补问题 |
| C4 | 任务适配或输入处理怎样与主方法协同 |
| C5 | 主要证据的整体结论，不重列全部表格 |
| C6 | 研究边界或由边界自然推出的具体方向 |

结论增加整体认识，不逐句重播摘要。C2–C4 解释机制之间的关系，不重新罗列组件。真实方法没有第三项互补内容时合并相邻句位，不补造贡献。

研究边界写实际未覆盖的输入、模型、监督或部署条件，以及会改变主要结论的已知失败条件。未来方向可有可无；保留时从已说明的边界推出，不承诺未经验证的新能力。不新增结果、引用或普遍性主张。

**完成标准：**首句统领结论，分句说明整体认识的技术与证据依据，范围与引言、贡献及实验保持一致。

## S-CON-H. Hardened checklist (distilled from rejected drafts)

1. **One paragraph** unless the venue or the author asks for more. Short.
2. **The first sentence names the contribution**, not the experiments and not a secondary benefit. A benefit such as relieving data scarcity is added after the core claim.
3. **Correspond to the Abstract's pain points.** Each problem the Abstract raised is implicitly answered; do not introduce a new topic.
4. **Do not replay the Abstract or restate each section.** The Conclusion adds the overall understanding: what the work establishes about the problem, and why the mechanism matters.
5. **Mechanisms are related to each other**, not listed again.
6. **The evidence sentence aggregates**, without re-listing tables.
7. **Community-level closing when the work enables others** (a shared benchmark, a platform, reproducible splits): "For the [field] community, this work provides a shared foundation for reproducible research and cumulative scientific progress." The author decides whether to include it.
8. **One future direction at most**, drawn from a stated boundary, phrased as what the present work makes possible. Do not promise capability the experiments did not test, and do not write "we hope" unless the author asks for it.
9. **No new numbers, citations or universality claims.**
10. **"Conclusion" is the section; do not use the word as a synonym for "finding" elsewhere in the paper.**
11. **The final line ends where the page ends** in layout terms; if a page fill is required, adjust the preceding text, not the claim.
