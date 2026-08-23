# Research — Scene 027 Using UK eGates

> 落地后的第一道门：英国机场的电子护照闸机（eGates）。对大多数旅客来说这是入境最快的方式，但"能不能用、怎么用、机器报错怎么办"是真实痛点。本场景训练从飞机落地到走出闸机的完整流程，重点是识别资格、按机器提示操作、处理失败转人工。

## 1. Research question

哪些人能使用英国 eGates？机器上会看到什么提示？如果 eGates 失败（机器报错/人脸不匹配/未成年/护照非生物识别）会发生什么？学习者需要主动说什么？

The lesson should train the smallest complete task:

> 下飞机 → 跟随 "UK Border / Arrivals / ePassport gates" 标识 → 确认自己符合资格 → 把护照放进扫描口 → 按屏幕提示操作 → 闸机开门 → 通过 → （若失败）被引导转人工通道。

## 2. Real-world flow

### 2.1 资格（GOV.UK，2026-08 核实）

- **英国公民**：护照有生物识别标志（封面上的 `e` 符号）、**8 岁或以上**、**身高 ≥120cm**。8-17 岁必须由成人陪同。
- **欧盟/瑞士/挪威/冰岛/列支敦士登公民**：同样可用 eGates（护照需与 UKVI 账户关联，若有居留身份）。
- **其他国籍**：部分国家护照持有人可用（如美国、加拿大、澳大利亚、日本、韩国、新加坡等——**资格随政策变化**，需以 gov.uk 最新清单为准）。
- **无 ETA/签证不能入境**：非英爱护照游客需提前申请 ETA（£20，有效期 2 年，单次最多停留 6 个月）或相应签证——这是 eGates 能否通过的前提。

### 2.2 闸机操作步骤（真实机器体验）

1. 走到闸机前，**把护照个人信息页朝下**放进扫描口（不同机场方向略有差异，屏幕有图示）。
2. 机器读取护照芯片，屏幕提示 `Please wait...` / `Remove your passport`。
3. 闸门短暂关闭，屏幕提示看向摄像头（`Look at the camera`）。
4. 系统面部识别比对护照照片，匹配成功 → 闸门打开 → **取回护照** → 通过。
5. 全程约 15-30 秒，**不需要说任何话**，是纯自助操作。

### 2.3 失败转人工（常见）

- 机器报 `See a member of staff` / 红灯 → 屏幕上会显示去人工柜台。
- 常见失败原因：面部识别不匹配（发型/眼镜/化妆/年龄变化）、护照芯片损坏、未成年或身高不足、护照非生物识别、系统随机抽查。
- 失败时**不要反复重试**同一台机器，按提示找工作人员/走人工通道。
- 家庭带小孩：8-17 岁与成人**必须一起**通过（同组）。

## 3. Real-world English

### 3.1 标识与屏幕提示

- `UK Border` / `Arrivals` / `All Passports`
- `ePassport gates` / `eGates`
- `Please place your passport on the scanner` / `facing down`
- `Remove your passport`
- `Look at the camera`
- `Please wait`
- `See a member of staff` / `Please see an officer`
- `Proceed` / `Gate open` / `Welcome to the UK`

### 3.2 学习者可能需要说的话（极少）

- 机器失败后找工作人员：`The gate didn't work — it said to see a member of staff.`
- `Can I use the eGates with this passport?`（不确定资格时）
- `My daughter is with me — can we go through together?`
- `Where do I go if the eGates don't work?`
- 听不懂机器指令：`Sorry, what should I do now?`

## 4. Common failure points

### 4.1 不知道自己的护照能不能用 eGates

非英/欧盟护照持有人不确定资格，排错队。训练识别生物识别标志 + 提前查证。

### 4.2 放护照方式不对（方向/位置）

机器图标有明确图示，但紧张时容易放反。训练"看图操作 + 一次放好"。

### 4.3 面部识别失败后慌张

摘下眼镜/口罩可能改善；失败后应转人工而非反复重试。训练 `The gate didn't recognise me — what should I do?`

### 4.4 家庭/儿童规则不清

8-17 岁必须成人陪同同行，成人不能自己先过。训练一起通过的说法。

### 4.5 没有 ETA/签证就到达

2026 年起非英爱游客普遍需要 ETA，未提前申请会被拦。虽然本场景不教申请流程，但必须让学习者知道"没有 ETA 进不来"。

## 5. Current rules / policy-sensitive facts

`policy_sensitive: true`

`last_verified: 2026-08`

- eGates 资格：英国公民 8 岁+ 且 ≥120cm；8-17 岁需成人陪同；欧盟/瑞士/挪威/冰岛/列支敦士登公民可用；**部分其他国家护照**（美国、加拿大、澳新、日韩、新加坡等）也可用——**清单会变，以 gov.uk 为准**。
- 2026-05 起 8-9 岁儿童（≥120cm、有成人陪同）纳入 eGates 资格（GOV.UK 新闻）。
- ETA：非英/爱尔兰护照、免签短期访客需 £20 ETA（gov.uk/eta），可停留 6 个月；未持有 ETA/签证无法通过边境。
- eGates 使用**面部识别**技术比对护照照片；失败转人工，无惩罚，但反复重试无益。
- 身高低于 120cm 或不满 8 岁必须走人工通道。

## 6. Sources

### Tier 1 — Official / primary

1. GOV.UK — At border control（uk-border-control/at-border-control）
   https://www.gov.uk/uk-border-control/at-border-control
   - eGates 资格与操作要求（8 岁+、120cm、生物识别标志、家庭同行）
   - 边境检查通用要求（证件备好、摘墨镜口罩、家庭一起过）
2. GOV.UK — Get an electronic travel authorisation (ETA)
   https://www.gov.uk/eta
   - ETA 费用、有效期、适用人群
3. GOV.UK 新闻 — More children eligible for eGates (2026-05/07)
   https://www.gov.uk/government/news/more-children-eligible-for-egates-in-boost-for-families-this-summer
   - 2026 年儿童资格扩展（8-9 岁）

### Tier 2 — Industry

4. London Gatwick Airport — Passports and Visas
   https://www.gatwickairport.com/passenger-guides/passport-visa.html
   - 机场端对 eGates 的旅客指引（"scan your passport on arrival"、不适用时转人工）

### Tier 3 — corroboration

5. 旅客社区/旅行指南对 eGates 屏幕提示语的实拍描述（"place passport facing down"、"look at camera"）——仅用于选取真实机器提示语。

## 7. Course design decisions

### Keep in Scene 027

- 识别 eGates 资格（生物识别标志、年龄身高、国籍清单逻辑）
- 下机到闸机的路线（Arrivals / UK Border / ePassport gates 标识）
- 闸机操作步骤（放护照 → 等待 → 看摄像头 → 取护照 → 通过）
- 识别机器提示语（reading-focused，不是听力）
- 失败处理（转人工、找工作人员的说法）
- 家庭/儿童同行规则
- 明确 ETA 前提（没有它进不来，但不深入申请流程）

### Move out of Scene 027

- 人工柜台问询 → Scene 028（manual immigration interview）
- 解释旅行计划/资金 → Scene 029
- 被要求补材料 → Scene 030
- ETA/签证申请流程本身 → 前置知识，不在此场景教学
- 取行李 → Scene 031

### Reusable patterns (PATTERN_BANK.md)

- P016 — `Did you say + 信息?`（确认提示）
- P003 — `Could you + 动作, please?`
- P055 — `Which + 名词?`（Which gate/desk）
- Universal repair phrases

## 8. What we intentionally do NOT teach

- ETA 在线申请流程（表格、支付）——属于出行前准备，另做前置说明即可
- 签证类型详解
- 边检官面谈技巧（028 专训）
- eGates 故障排除（机器维护问题）
- 美国 ESTA/其他国境闸机——专注英国
