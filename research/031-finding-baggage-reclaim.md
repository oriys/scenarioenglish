# Research — Scene 031 Finding baggage reclaim

> 过了入境边检，下一步是找自己的托运行李。本场景训练：看懂标识、找到对应转盘、确认是自己的箱子。简单但高频——大机场第一次来很容易找错。

## 1. Research question

落地后怎么从边检走到行李提取区？怎么知道自己的行李在哪个转盘？怎么确认箱子是自己的？

The lesson should train the smallest complete task:

> 出边检 → 跟随 `Baggage Reclaim` 标识 → 看大屏找航班对应的行李转盘号 → 到转盘等行李 → 核对行李牌确认是自己的 → 取走。

## 2. Real-world flow

1. 出边检后跟随 **`Baggage Reclaim` / `Luggage` / `Baggage Hall`** 标识。
2. 在行李大厅大屏（flight information screen）上找到**自己的航班号** → 看对应的**转盘号**（belt / carousel number）。
3. 到转盘旁等待（有时要等 10-20 分钟）。
4. 看到箱子过来，**核对行李牌/名字标签**（别只看外形）。
5. 取下行李，检查无遗漏，前往海关通道（035 衔接）。

### 关键点

- 转盘号在大屏上**随航班动态更新**，出发前看一眼最准。
- 多航段/联程行李：确认转盘可能是**最终目的地**的（行李直挂时）。
- 没有托运行李（只有随身行李）→ 直接走 `Nothing to declare` 通道离开。

## 3. Real-world English

### 3.1 标识与屏显

- `Baggage Reclaim` / `Baggage Hall` / `Luggage`
- `Carousel` / `Belt` / `Carousel 3`
- `Flight BA123 — Carousel 4`
- `Please wait for your baggage`
- `Delayed`（该转盘行李未到）

### 3.2 学习者可能说的话

- `Excuse me, which carousel is for flight BA123?`
- `Where is the baggage reclaim area?`
- `Is this the right carousel for my flight?`
- `Is there another carousel? I can't see my bag.`
- 核对：`My bag is black with a green tag.`

## 4. Common failure points

- 找不到行李大厅：标识没看懂 → 训练 `Baggage Reclaim` 识别。
- 等错转盘：没看大屏/看错航班号 → 训练"航班号→转盘"匹配。
- 拿错行李：只看外形不看标签 → 训练标签核对。
- 联程行李在错误转盘干等 → 训练问地勤确认。

## 5. Current rules / policy facts

`policy_sensitive: false`

- 转盘号由机场大屏动态发布，无固定规则；联程直挂行李在最终目的地提取。
- 无统一标准布局——训练通用流程而非某机场布局。

## 6. Sources

### Tier 1

1. Heathrow — Baggage reclaim（arrivals/baggage-reclaim）
   https://www.heathrow.com/arrivals/baggage-reclaim
   - "Check the information screens for your flight number. The screen will show which baggage belt your bags will arrive on."

### Tier 3

2. 机场实拍/旅客经验（转盘标识、大屏格式）——用于选取自然标识语。

## 7. Course design decisions

### Keep

- 标识识别（Baggage Reclaim / Carousel / Belt）
- 大屏航班号→转盘匹配
- 标签核对（防拿错）
- 问路/确认句式

### Move out

- 行李未到 → 032；损坏 → 033；拿错 → 034；海关 → 035

### Patterns

- P055 `Which + 名词?`、P057 `Is this the right + 名词?`、P016 确认信息

## 8. NOT taught

- 具体机场布局；托运流程本身（001 已教）；行李索赔法律细节（032+）
