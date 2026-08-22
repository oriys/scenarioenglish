# Scenario English — 内容规范

## 1. 课程定位

本课程服务于中国高中英语基础的成年人，目标是 3–6 个月内具备独自在英国旅行约一个月的真实沟通能力。

不以考试、语法覆盖率、词汇量数字为目标；所有内容必须回答一个问题：

> **这个表达能否帮助学习者在真实环境里把事情办成？**

## 2. 场景设计原则

每个文件只对应一个“最小可执行场景”。一个场景应满足：

- 有明确任务起点；
- 有明确成功结果；
- 工作人员或当地人会真实使用这些表达；
- 可以独立做角色扮演训练；
- 不依赖先学习某个语法章节；
- 优先复用已有 Pattern、词汇和技能，不重复造课。

错误示例：
- 一般过去时
- 情态动词
- 酒店英语

正确示例：
- 酒店前台办理入住
- 房间太吵要求换房
- 退房时发现账单多收费

## 3. 场景类型与优先级

`type` 与 `priority` 必须分开维护。

### 3.1 场景类型 type

#### Core

完整核心课。用于高频、可迁移、值得系统训练的真实任务。

建议包含：
- 场景流程；
- 10–20 条高频工作人员输入；
- 必要输出表达；
- New / Review vocabulary；
- 3–5 个 New Patterns；
- 多个 Review Patterns；
- Normal / Problem / Pressure 三层角色扮演；
- 练习与通关标准。

建议学习时间：25–40 分钟，可拆成两次完成。

#### Exception

异常专项课。默认依赖某个 Core Scene，只补充解决异常所需的新输入、新词和处理策略。

例如：
- 行李超重；
- 航班取消；
- 酒店房型错误；
- 卡被拒；
- 行李未到。

原则：
- 不重新讲一遍完整正常流程；
- 优先复用已有 Pattern；
- 新词通常 5–12 个；
- 角色扮演通常 10–20 turns；
- 只有必要时新增 1–2 个 Pattern。

建议学习时间：10–20 分钟。

#### Extension

扩展课。用于低频、地区差异、特定旅行方式、文化背景或“更从容”的表达。

原则：
- 不要求所有学习者完成；
- 可以以输入识别为主；
- 不强制新增 Pattern；
- 不为了凑内容而扩写成长课。

建议学习时间：5–15 分钟。

### 3.2 优先级 priority

- **P0 — Survival**：不会就可能影响行程、支付、安全、就医或关键流程。
- **P1 — Independent Travel**：高频且明显提升独立旅行能力。
- **P2 — Extension**：低频、特定人群或用于提升从容度。

学习路径统一维护在 `LEARNING_PATH.md`。

## 4. 英语风格

### 4.1 表达优先级

表达选择优先级：

1. 高频
2. 容易听懂
3. 容易说出口
4. 可迁移
5. 自然
6. 地道

禁止为了“高级”而牺牲可用性。

### 4.2 英国英语与通用英语

默认使用英国英语，但优先教全球英语环境都能理解的表达。

需要标注差异时使用：

- `[UK]` 英国更常见
- `[US]` 美国更常见
- `[AU/NZ]` 澳大利亚/新西兰更常见
- `[General]` 英语国家普遍适用

例：

- `[UK] single ticket` = 单程票
- `[US] one-way ticket` = 单程票
- `[General] Could I get a ticket to Oxford, please?`

### 4.3 难度

主体输出控制在 CEFR A2–B1 可生产范围；允许在“你会看到的英文”和“工作人员最可能说的话”中出现 B2 级真实词汇，因为真实环境不会主动降级。

复杂输入必须给出关键词抓手；复杂输出必须同时提供更简单的可用说法。

## 5. Scene metadata 规范

每个正式 Scene 文件顶部必须包含：

```yaml
scene_id: 001
type: core
priority: P0
level: A2-B1
estimated_time: 30m
region: UK-first / General English
prerequisites: []
related_scenes:
  - 003
  - 004
  - 005
new_patterns:
  - P001
review_patterns:
  - P003
policy_sensitive: false
last_verified: 2026-08
```

字段说明：

- `scene_id`：全局唯一稳定编号；
- `type`：`core | exception | extension`；
- `priority`：`P0 | P1 | P2`；
- `level`：主要输出难度；
- `estimated_time`：首次学习预计时间；
- `region`：主要英语环境；
- `prerequisites`：建议先学的 Scene；
- `related_scenes`：直接相关或共享技能的 Scene；
- `new_patterns`：本课真正新增的全局 Pattern；
- `review_patterns`：本课复用的旧 Pattern；
- `policy_sensitive`：是否包含法律、交通、医疗、航空、签证、退税等易变化信息；
- `last_verified`：动态信息最近核验月份，格式 `YYYY-MM`。

## 6. 固定内容结构

Core Scene 原则上使用以下结构：

1. 场景介绍
2. 任务目标
3. 正常流程
4. 常见异常
5. 加分场景
6. 你会看到的英文
7. 工作人员最可能说的话
8. 你应该说的话
9. 高频词汇：New / Review / Recognition
10. Pattern：New / Review
11. Role Play A — Normal
12. Role Play B — Problem
13. Role Play C — Pressure Test
14. 听不懂时的万能应对句
15. 英国本地表达
16. 易错点
17. 扩展说明
18. 练习题
19. 场景通关标准
20. Related Scenes

Exception / Extension 可按实际需要缩短，不强制填满所有模块。

## 7. 词汇规范

不再要求每个 Scene 都新增 20–30 个词。

词汇分三类：

### New Vocabulary

本课第一次要求学习者主动掌握的词或短语。

建议：
- Core：8–15 个；
- Exception：5–12 个；
- Extension：按需。

### Review Vocabulary

之前出现过、本场景需要继续使用的词。只需列出必要部分，不重复长篇解释。

### Recognition Vocabulary

学习者主要需要“看到/听到能认出来”，但不要求主动说出的真实环境词汇。

例如：
- signage；
- 系统提示；
- 政策术语；
- 工作人员可能使用但学习者无需主动输出的 B2 词汇。

优先收录：
- 标识上会看到的词；
- 工作人员会说的词；
- 学习者必须说的词；
- 数字、时间、尺寸、证件、动作相关高频词。

不收录与场景关系弱的“主题词汇大全”。

## 8. Pattern 规范

全局可迁移句型统一维护在 `PATTERN_BANK.md`。

### 8.1 New Pattern

Core Scene 通常新增 **3–5 个** Pattern。

新增前必须确认：
- 是否已有 Pattern 只需替换名词/动词即可；
- 是否至少能在 3 个不同 Scene 复用；
- 是否适合 A2–B1 学习者主动说；
- 是否比已有简单表达带来明显新增能力。

### 8.2 Review Pattern

已经学过的 Pattern 应在新场景里反复出现，而不是重新编号。

复习目标是“迁移”：

- `I'd like to...` 从机场迁移到酒店、餐厅、客服；
- `Did you say...?` 从登机口迁移到站台、金额、地址；
- `What are my options?` 从航班异常迁移到酒店和铁路异常。

### 8.3 场景表达 ≠ Pattern

只在一个场景高频的固定说法可以作为“你应该说的话”，但不一定升级为全局 Pattern。

## 9. 工作人员输入规范

Core Scene 建议收录 10–20 句真实高概率输入；Exception / Extension 按需缩短。

优先覆盖：
- yes/no question；
- wh-question；
- instruction；
- confirmation；
- warning；
- alternative。

每句给出“听力抓手”，例如：

> **Are you checking any bags today?**  
> 抓关键词：`checking` + `bags`

不要把所有输入改写成学习者熟悉的教材英语。真实工作人员可以比学习者输出略难。

## 10. Role-play 规范

不再强制所有 Scene 使用一个 ≥30 turns 的大对话。

### Role Play A — Normal

目标：顺利完成任务。

Core 建议 10–16 turns。

### Role Play B — Problem

目标：出现一个常见异常后仍把事情办成。

Core 建议 10–18 turns；Exception 可以把这一段作为主训练。

### Role Play C — Pressure Test

目标：训练真实交流压力，例如：
- 语速更快；
- 数字/时间变化；
- 没听清；
- 对方换一种说法；
- 环境嘈杂；
- 同时出现两个信息点。

通常 8–16 turns 即可。

三个对话加起来不追求固定总长度，追求学习目标清晰和可重复练习。

角色统一使用：
- **Staff:**
- **You:**
- **Officer:**
- **Driver:**
- **Server:**
- **Pharmacist:**

不得逐句全文翻译，避免学习者只读中文。

## 11. Conversation repair 规范

每个 Core Scene 都要训练：
- 请重复；
- 请慢一点；
- 确认关键词；
- 确认数字/时间；
- 换一种说法；
- 指给我看/写下来。

这些能力应优先复用 `PATTERN_BANK.md` 中已有 Pattern。

## 12. 易错点规范

优先写中国学习者真实高频错误：
- 中式直译；
- 过度正式；
- 单复数；
- 数字和日期；
- please 的位置；
- statement / question 混淆；
- 英美词汇差异；
- 发音导致的信息误判。

不要把“语法大全”塞进 Scene。

## 13. 练习与复习规范

Core Scene 至少覆盖：

1. **识别**：看到/听到后理解意思；
2. **替换**：把 New / Review Pattern 换到新信息；
3. **即时应答**：工作人员说一句，3 秒内回应；
4. **异常处理**：不给标准答案提示，自己推进任务；
5. **迁移**：把本课 Pattern 用到另一个场景。

建议增加：
- shadowing；
- 30 秒限时口语；
- role switch；
- 信息差练习。

每个 Core Scene 按 `LEARNING_PATH.md` 执行 D0 / D2 / D7 / D21 间隔复习。

## 14. 通关标准

通关标准必须可观察，不使用“理解”“掌握”等模糊词。

例如：
- 10 秒内说清任务；
- 能回答 8/10 个高频工作人员问题；
- 能主动使用本课 3 个 New Patterns；
- 能把至少 2 个 Review Patterns 迁移到本场景；
- 听不懂时会使用至少 3 种修复表达；
- 出现一个异常时仍能完成任务；
- 不依赖逐句中文翻译。

## 15. 动态信息与来源规范

航空安全、签证/边检、海关、药品、NHS、铁路赔偿、交通票制、退税等信息可能变化。

只要正文包含会影响真实行为的规则，就必须：

1. `policy_sensitive: true`；
2. 记录 `last_verified: YYYY-MM`；
3. 优先引用官方来源；
4. 区分“英语训练重点”和“现实规则”；
5. 对不稳定细节避免写成永久事实。

例如：

> 航空公司通常对备用锂电池和充电宝有随身携带要求；具体容量与数量限制以航空公司和机场当前规则为准。

不要把课程变成政策手册，规则只服务于真实英语任务。

## 16. 重复与跨场景复用

发现两个 Scene 重叠时，不优先删除编号，而优先建立复用关系。

例如：
- 038 “抵达后买 SIM/eSIM”重点是落地快速联网；
- 137 “买 SIM、开通套餐”重点是门店套餐、激活和长期使用。

两者共享词汇和 Pattern 时，后者应标 `prerequisites` / `related_scenes` 并复用已学内容。

同理：
- 120–122 药房技能可以成为 156–158 症状专项的基础；
- 001 值机可以成为 188 回程值机的基础；
- 141 支付技能应被购物、餐饮、酒店等场景复用。

## 17. 文件命名规范

```text
scenes/<主题编号>-<topic>/<子主题编号>-<subtopic>/<scene-id>-<slug>.md
```

例如：

```text
scenes/01-airport-and-flight/01-check-in/001-counter-check-in.md
```

场景编号使用三位数字并保持全局唯一。

## 18. 维护规范

- 新场景优先新增文件，不把多个最小任务塞进一个 Markdown；
- 已发布 Scene ID 与 Pattern ID 不复用；
- 修改表达时优先保持 URL 稳定；
- 新增地区差异必须标注来源地区，不把美式英语误写成“错误英语”；
- 不为了扩大内容量而加入低概率、低迁移价值表达；
- 写新 Scene 前先查 `PATTERN_BANK.md` 和相关 Scene；
- 一个 PR 优先只做一种工作：架构、单课内容、批量元数据或事实核验；
- `CURRICULUM.md` 管“有哪些场景”，`LEARNING_PATH.md` 管“先学什么”。