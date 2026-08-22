# Scenario English — Listening Guide

> 目标：把课程从“看懂句子”升级为“在真实语速、真实变体和信息压力下听懂关键内容并继续完成任务”。

## 1. 为什么单独设计 Listening Layer

旅行交流里，学习者常见失败点不是完全不会说，而是：

- 对方说法和教材不一样；
- 句子被弱读、连读或缩短；
- 数字、时间、金额、站台号等关键信息没听准；
- 环境嘈杂、广播失真、隔着玻璃或电话交流；
- 听漏一个词以后整段对话停住；
- 只会听完整标准句，不会从短句、碎片句中抓任务信息。

因此每个 Core Scene 都应该包含独立的 Listening Drill，而不是只把文字对话朗读一遍。

## 2. Listening Drill 的四层结构

### L1 — Canonical Input

先听本课最标准、最容易识别的表达。

例：

- `Are you checking in any bags today?`
- `What time does boarding start?`
- `Could I see your passport, please?`

目标：建立“意图 → 关键词 → 回应”的基础映射。

### L2 — Natural Variants

同一个意图至少准备 3–6 种真实说法，避免学习者只记住一个固定句型。

例如“你有托运行李吗？”：

- `Are you checking in any bags today?`
- `Any bags to check?`
- `Are you checking anything in?`
- `Just hand luggage today?`
- `How many bags are you checking?`

学习者不需要逐词翻译，只需要识别：`bag / check / hand luggage`，然后给出正确回应。

### L3 — Critical Information

专门训练不能听错的信息：

- 时间：`10:15 / 10:50`
- 数字：`13 / 30`、`14 / 40`
- 金额：`£15 / £50`
- Gate / Platform / Room number
- 日期
- 姓名拼写
- 地址、postcode、电话号码

训练原则：

1. 每轮随机替换信息；
2. 学习者必须复述或确认；
3. 不确定时必须使用 conversation repair；
4. 不允许靠上下文猜关键数字。

推荐回应：

- `Sorry, did you say Gate 13 or 30?`
- `So, just to confirm, boarding starts at 10:15?`
- `Could you say the postcode again, please?`

### L4 — Pressure Listening

在已经能完成任务后加入真实干扰：

- 更快语速；
- 弱读和自然停顿；
- 句子缩短；
- 同义改写；
- 背景噪音；
- 广播音质；
- 电话音质；
- 一次给两个信息点；
- 中途插入更正信息。

目标不是“全部听写正确”，而是：

> 抓住完成任务所需的信息，并在不确定时主动修复对话。

## 3. 每个 Core Scene 建议新增的 Listening 模块

建议在正式 Scene 中增加：

```markdown
## Listening Drill

### A. Same intent, different wording

Intent: 托运行李确认

1. Are you checking in any bags today?
2. Any bags to check?
3. Just hand luggage today?
4. How many bags are you checking?

Task: 听到任意一种表达后，3 秒内回答。

### B. Critical information

Staff: Boarding starts at 10:15 from Gate 30.
Task: 复述 boarding time 和 gate。

### C. Repair required

Staff: Your platform has changed from 13 to 30.
Task: 主动确认新站台，不允许直接猜。

### D. Pressure round

- faster speech
- one paraphrase
- one changed number
- one repair moment
```

## 4. 音频文件建议结构

```text
audio/
└── 001-counter-check-in/
    ├── l1-canonical/
    ├── l2-variants/
    ├── l3-critical-info/
    └── l4-pressure/
```

文件命名建议：

```text
001-l2-bag-check-01.mp3
001-l2-bag-check-02.mp3
001-l3-gate-time-01.mp3
001-l4-pressure-01.mp3
```

音频生成或录制时，文本 source 应保存在 Scene 或对应 manifest 中，避免只有不可审查的二进制音频。

## 5. Accent 策略

课程以 UK-first 为主，但口音训练的目标是 recognition，不要求学习者模仿。

核心阶段建议优先覆盖：

1. Standard Southern British / 接近主流公共服务语音；
2. London / Estuary 的轻度自然口音；
3. Northern England 的轻度口音；
4. Scottish 的轻度口音。

原则：

- 不使用极端方言作为初学者门槛；
- 同一个高频意图可以跨 speaker 重复；
- 口音变化不应和生词、复杂流程同时首次出现；
- Accent 是 Pressure Test 的变量之一，不是独立炫技内容。

## 6. Reduced Speech / Natural Speech

学习者需要认识真实语流中的常见变化，例如：

- `Would you like to ...?`
- `Have you got ...?`
- `Do you wanna ...?`（recognition only）
- `You all right?`
- `There you go.`
- `You're all set.`
- `That'll be twenty pounds.`
- `Just the one bag?`

不要要求学习者主动模仿所有缩略形式；输出仍优先使用清楚、稳定、通用的表达。

## 7. Listening Pass Criteria

Core Scene 的听力通关建议满足：

- [ ] 10 个高频工作人员输入中至少识别 8 个意图；
- [ ] 同一意图换 3 种说法后仍能正确回应；
- [ ] 数字 / 时间 / 金额题正确率至少 8/10；
- [ ] 遇到不确定信息时主动确认，而不是猜；
- [ ] 至少使用 3 种 conversation repair；
- [ ] Pressure Round 中即使漏掉部分单词，仍能把任务继续推进。

## 8. 与现有课程的关系

- `SCENE_TEMPLATE.md`：定义每个 Scene 如何放入 Listening Drill；
- `PATTERN_BANK.md`：提供确认、重复、降速等 repair Pattern；
- `LEARNING_PATH.md`：安排 D0 / D2 / D7 / D21 的重复暴露；
- `SIMULATIONS.md`：把多个 Scene 的听力输入混合起来，取消章节提示；
- `STYLEGUIDE.md`：继续负责语言自然度、地区差异和内容质量。

Listening Layer 不增加大量新知识点，而是把已经存在的知识变成可以在真实语音条件下调用的能力。
