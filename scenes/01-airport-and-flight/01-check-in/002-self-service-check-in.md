# Scene 002 — 自助值机与自助行李托运 / Self-service check-in and bag drop

```yaml
scene_id: 002
type: core
priority: P1
level: A2-B1
estimated_time: 30m
region: UK-first
prerequisites: [001]
related_scenes: [001, 003, 004, 005]
new_patterns: [P050, P053, P054, P058]
review_patterns: [P001, P006, P016, P018]
policy_sensitive: true
last_verified: 2026-08
```

> **Path:** 01 机场与飞行 → 01 值机与托运 → 自助值机与自助行李托运

## 1. 场景介绍

英国大多数机场（Heathrow、Gatwick、Manchester、Edinburgh 等）现在把值机拆成两步：先在自助机器（kiosk / self-service machine）上打印登机牌和行李挂牌，再到 bag drop 柜台或自助传送带交行李。人工柜台通常只处理特殊情况。

你在出发大厅（departures）看到一排触屏机器，机器旁边站着穿背心的引导员（agent / host）。你要做的事：扫护照或输入订位号，确认航班，选行李件数，打印 boarding pass 和 bag tag，把挂牌自己贴到行李把手上，然后把行李放上 bag drop 的传送带。

顺利结束的样子是：你手上有一张 boarding pass（如果你已经在手机上值过机，直接用 App 里的数字登机牌就可以，不必重打纸质版），行李已经进入传送带并且屏幕显示 `Bag accepted`，你知道自己的登机口在哪里查、什么时候必须到。

## 2. 任务目标

完成本场景后，你应该能：

- 在自助机器上独立完成扫护照、确认航班、选行李件数、打印 boarding pass 与 bag tag
- 听懂引导员的祈使句指令（`Tap here.` / `Scan your passport.` / `Place your bag on the belt.`）
- 用英文问清自己是否排对了队、是否需要把某样东西取出来、行李件数与重量限制
- 机器报错或行李被退回时，能主动叫引导员并说明卡在哪一步
- 拿到登机牌后确认 gate 信息的查看方式与最晚到闸口时间

## 3. 正常流程

1. 在出发大厅找到你的航空公司区域，看屏幕上的 `Self-service check-in` / `Bag drop` 标识。
2. 走到空闲的 kiosk 前，按屏幕提示选语言（English）。
3. 扫护照资料页，或输入 booking reference（订位号，长度因航司而异的字母数字串）。
4. 屏幕显示你的航班与姓名，确认无误后按 `Confirm`。
5. 选择托运行李件数（`How many bags are you checking in?`）。
6. 机器打印 boarding pass 和 bag tag。
7. 把 bag tag 自己贴到行李把手上，条码朝外，环扣拉紧。
8. 到 bag drop 通道，把行李平放上传送带，箱轮朝下，把手不要朝上翘。
9. 扫 boarding pass 条码，屏幕称重并显示 `Bag accepted`，行李被送走。
10. 收好 boarding pass 与行李凭条（baggage receipt），去安检。

## 4. 常见异常

- 异常 1：机器读不到护照。屏幕提示 `Passport not recognised`，需要引导员手动输入。
- 异常 2：打印机没纸，boarding pass 或 bag tag 没出来。
- 异常 3：行李超重，bag drop 屏幕显示 `Bag too heavy` 并把行李退回。
- 异常 4：行李尺寸超出传送带范围，需要走 outsize / oversized baggage 通道。
- 异常 5：同行人在另一台机器上操作，行程被分开处理，需要合并。
- 异常 6：挂牌贴错位置或贴反，扫码失败。

## 5. 加分场景

- 主动问引导员这一排机器是不是你航班用的（避免排错队）。
- 行李箱有旧的挂牌残留，主动问是否需要撕掉。
- 帮同行的长辈完成同一流程，用英文替他说明情况。
- 打印失败后，问能否在人工柜台补打，而不是重新排整队。

## 6. 你会看到的英文

| English | 中文 | 场景含义 |
| --- | --- | --- |
| Self-service check-in | 自助值机 | 这一排机器打印登机牌 |
| Bag drop | 行李托运处 | 打印完挂牌后来这里交行李 |
| Scan your passport | 扫描护照 | 把资料页朝下放到扫描窗 |
| Booking reference | 订位号 | 字母数字串（长度因航司而异），也叫 PNR |
| Print boarding pass | 打印登机牌 | 机器出票 |
| Bag tag | 行李挂牌 | 自己贴到行李把手上 |
| Attach tag to handle | 把挂牌贴在把手上 | 环绕把手后粘死 |
| Place bag on belt | 把行李放上传送带 | 平放，轮子朝下 |
| Bag accepted | 行李已接收 | 可以离开了 |
| Bag too heavy | 行李超重 | 需要处理后重放 |
| Remove old tags | 请撕掉旧挂牌 | 避免扫错条码 |
| Oversized baggage | 超尺寸行李 | 走专门通道 |
| Baggage receipt | 行李凭条 | 行李丢失时要用 |
| Please see an agent | 请找工作人员 | 机器无法继续 |
| Out of service | 暂停使用 | 换另一台机器 |

## 7. 工作人员最可能说的话

1. **Are you checking in a bag today?**  
   听力抓手：`checking in a bag`
2. **Just tap the screen to start.**  
   听力抓手：`tap the screen`
3. **Scan your passport, photo page down.**  
   听力抓手：`photo page down`
4. **How many bags are you checking?**  
   听力抓手：`how many bags`
5. **Attach the tag to the handle, barcode facing out.**  
   听力抓手：`barcode facing out`
6. **Place your bag on the belt, wheels down.**  
   听力抓手：`wheels down`
7. **Scan your boarding pass here, please.**  
   听力抓手：`scan ... here`
8. **That bag's a bit over, I'm afraid.**  
   听力抓手：`a bit over`
9. **You'll need to take out about two kilos.**  
   听力抓手：`take out ... kilos`
10. **Any old tags on there? Take them off, please.**  
    听力抓手：`old tags ... take them off`
11. **The machine's out of service, use the one on the end.**  
    听力抓手：`out of service`
12. **Your gate will show on the screens about forty minutes before.**  
    听力抓手：`show on the screens`
13. **Boarding closes at 10:20, so don't leave it too late.**  
    听力抓手：`boarding closes at`
14. **That one's too big for the belt — take it to the oversized desk.**  
    听力抓手：`too big for the belt`
15. **All done, you're checked in.**  
    听力抓手：`all done ... checked in`

## 8. 你应该说的话

1. **Am I in the right queue for the Edinburgh flight?** — 确认排对机器区域。
2. **Am I allowed to check in two bags on this ticket?** — 问件数是否允许。
3. **Is there a limit on how heavy each bag can be?** — 问单件重量上限。
4. **Do I need to take the old tag out of the sleeve?** — 问旧挂牌要不要处理。
5. **Could you help me with the machine, please? It won't read my passport.** — 求助并说明卡点。
6. **Sorry, could you say that again?** — 没听清时的第一句。
7. **Sorry, did you say wheels down?** — 复述确认操作。
8. **So I attach this to the handle myself, is that right?** — 确认理解。
9. **The boarding pass didn't print. What should I do?** — 报告打印失败。
10. **Could I have a receipt for the bag, please?** — 索取行李凭条。
11. **Which desk do I need for oversized baggage?** — 问超尺寸通道位置。
12. **How long does it take to get through security from here?** — 问后续时间。
13. **Can I check my daughter's bag on the same booking?** — 问同行合并。
14. **Sorry, one more thing — where do I see the gate number?** — 补问登机口信息。

## 9. 高频词汇

### New Vocabulary

| English | 中文 | 使用提示 |
| --- | --- | --- |
| kiosk | 自助机器 | 英国口语里也常说 machine |
| self-service check-in | 自助值机 | 标识上的正式说法 |
| bag drop | 行李托运处 | 打完挂牌后交行李的地方 |
| bag tag | 行李挂牌 | 动词搭配 attach / put on |
| barcode | 条码 | facing out 朝外 |
| belt | 传送带 | 全称 conveyor belt |
| touchscreen | 触摸屏 | 动词用 tap，不用 press |
| tap | 轻触 | `tap the screen` 最常听到 |
| agent | 引导员 / 工作人员 | 穿背心站在机器旁 |
| out of service | 暂停使用 | 机器故障标识 |
| oversized | 超尺寸的 | 也写 outsize |
| baggage receipt | 行李凭条 | 行李丢失时的凭据 |
| handle | 把手 | 挂牌绕在这里 |
| sleeve | 挂牌套 | 老式行李箱上的透明卡套 |
| kilo | 公斤 | 口语常省略 kilogram |

### Review Vocabulary

| English | 来源 Scene | 本场景用途 |
| --- | --- | --- |
| boarding pass | 001 | 机器打印出来的登机牌 |
| booking reference | 001 | 护照扫不出来时手动输入 |
| checked baggage | 001 | 托运行李件数确认 |
| hand luggage | 001 | 超重时把东西挪进随身包 |
| queue | 001 | 确认自己排对了队 |
| gate | 001 | 登机牌上或屏幕上确认 |
| departures | 001 | 自助机器所在的大厅 |

### Recognition Vocabulary

| English | 中文 | 为什么需要认识 |
| --- | --- | --- |
| Passport not recognised | 护照无法识别 | 屏幕报错原文 |
| Please retry | 请重试 | 报错后的提示 |
| Excess baggage | 超额行李 | 超重时屏幕跳出的字样 |
| Do not leave bags unattended | 请勿留下无人看管的行李 | 大厅广播与告示 |
| Proceed to security | 请前往安检 | 流程完成后的指引 |
| Assistance required | 需要协助 | 机器呼叫工作人员的状态 |

## 10. Patterns

### New Patterns

- P050 — `Am I allowed to + 动作?` —— 问是否允许托运两件、是否允许自己贴挂牌。
- P053 — `Do I need to take + 名词 + out?` —— 问旧挂牌、充电宝要不要取出来。
- P054 — `Am I in the right queue for + 名词?` —— 确认这排机器是不是你的航班用的。
- P058 — `Could you help me with + 名词?` —— 机器卡住时叫引导员。

### Review Patterns

- P001 — `Could you help me + 动作?` —— 请对方帮忙操作屏幕（比 P058 更口语）。
- P006 — `Do I need to + 动作?` —— 确认流程步骤是否必需。
- P016 — `Sorry, did you say + 内容?` —— 复述 `wheels down` 之类的操作词。
- P018 — `So + 我的理解 + , is that right?` —— 复述整个操作顺序。

## 11. Role Play A — Normal

目标：顺利完成任务。

**You:** Excuse me, am I in the right queue for the Edinburgh flight?  
**Agent:** Yes, any of these machines. The one on the left's free.  
**You:** Thanks. Am I allowed to check in two bags on this ticket?  
**Agent:** Let's see — yes, two bags, twenty-three kilos each.  
**You:** Great. Do I scan my passport first?  
**Agent:** Tap the screen to start, then scan your passport, photo page down.  
**You:** Like this?  
**Agent:** That's it. Now select two bags. The tags will print underneath.  
**You:** Do I attach them myself?  
**Agent:** Yes, round the handle, barcode facing out.  
**You:** So I attach it to the handle and then put the bag on the belt, is that right?  
**Agent:** Correct. Wheels down, and scan your boarding pass here.  
**You:** It says "Bag accepted".  
**Agent:** Perfect. Second bag now.  
**You:** Done. Could I have a receipt for the bags, please?  
**Agent:** It's printed on the back of your boarding pass. Security's straight ahead.

## 12. Role Play B — Problem

目标：出现一个常见异常后仍完成任务。

**You:** Excuse me, could you help me with this machine? It won't read my passport.  
**Agent:** Let me have a look. Sometimes the glass is dirty. Try again, photo page down.  
**You:** Still nothing. It says "Passport not recognised".  
**Agent:** No problem. I'll type your booking reference in. Have you got it?  
**You:** Yes, it's K, 7, 2, R, L, M.  
**Agent:** K-seven-two-R-L-M. And how many bags?  
**You:** One, please.  
**Agent:** Right, that's you checked in. Tag's printing now.  
**You:** Do I need to take the old tag out of the sleeve?  
**Agent:** Yes, take it off, otherwise the scanner reads the wrong one.  
**You:** Sorry, did you say the scanner reads the wrong one?  
**Agent:** That's right. Old barcodes confuse it.  
**You:** Okay, it's off. Putting the bag on the belt now.  
**Agent:** Hmm, that bag's a bit over. Twenty-five kilos.  
**You:** What happens if I move something into my hand luggage?  
**Agent:** That's fine, as long as it comes down to twenty-three.  
**You:** I've taken out my coat and my laptop. Can I try again?  
**Agent:** Twenty-two point six. Bag accepted. You're all set.

## 13. Role Play C — Pressure Test

目标：加入真实压力：

- 工作人员语速快
- 数字或时间中途变化
- 你没听清一次
- 对方换一种表达重复
- 环境嘈杂（广播、行李箱轮子声）

**Agent:** Right, next — checking bags? Passport on the glass, tap start, how many going in the hold?  
**You:** Sorry, could you say that a little more slowly, please?  
**Agent:** No worries. How many bags are you putting in the hold?  
**You:** Two. Am I allowed two on this booking?  
**Agent:** Two's fine. Tags printing — attach both, barcode out, then belt three, not this one.  
**You:** Sorry, did you say belt three?  
**Agent:** Belt three, on the far end. This one's out of service now.  
**You:** Am I in the right queue for belt three, or do I go round?  
**Agent:** Straight past the pillar and turn left. Boarding closes at 10:20, by the way — actually they've moved it to 10:05.  
**You:** Sorry, 10:05, not 10:20?  
**Agent:** 10:05. Earlier than printed.  
**You:** So I need to be at the gate by 10:05 at the latest, is that right?  
**Agent:** Yes. Gate shows on the screens about forty minutes before.  
**You:** Could you help me with the second bag? It's too big for the belt, I think.  
**Agent:** It is. Oversized desk, same direction, next to the lift.  
**You:** Thank you. How long does it take to get through security today?  
**Agent:** Twenty minutes, give or take.

## 14. 听不懂时的万能应对句

- **Sorry, could you say that again?**
- **Could you say that a little more slowly, please?**
- **Sorry, did you say ___?**
- **Could you write that down for me, please?**
- **Could you show me where that is?**
- **What does ___ mean?**

## 15. 英国本地表达

| 表达 | 地区 | 含义 / 使用说明 |
| --- | --- | --- |
| bag drop | UK | 自助托运处；美国多说 baggage drop-off |
| hold luggage | UK | 托运行李；美国说 checked baggage |
| a bit over | UK | 「稍微超了」，说超重时很常用的委婉说法 |
| pop it on the belt | UK | 「放上传送带」，pop 是英式高频动词 |
| give or take | UK | 「上下」，`twenty minutes, give or take` |
| out of service | General | 设备暂停使用 |
| trolley | UK | 行李推车；美国说 cart |
| lift | UK | 电梯；美国说 elevator |
| queue | UK | 排队；美国说 line |
| you're all set | US | 「都办好了」，英国更常说 that's you done |
| no worries | AU/NZ | 「没事」，英国也广泛使用 |
| straight ahead | General | 直走 |

## 16. 易错点

### 易错 1

❌ Please press the screen.  
✅ Just tap the screen.

### 易错 2

❌ How many baggages can I check?  
✅ How many bags can I check?

### 易错 3

❌ My bag is over-weight two kilos.  
✅ My bag's two kilos over.

### 易错 4

❌ I can check in two luggages?  
✅ Am I allowed to check in two bags?

### 易错 5

❌ Where I put the tag?  
✅ Where do I put the tag?

### 易错 6

❌ Give me the receipt.  
✅ Could I have a receipt for the bag, please?

## 17. 扩展说明

自助值机的界面语言、可选行李件数、免费额度和是否允许自己贴挂牌，取决于航空公司和机场，同一家公司在不同机场也可能不同。费用、限额与流程可能变化，以航空公司官网、机场现场标识或监管机构公告为准。

三个稳定不变的操作习惯值得记住。第一，挂牌一定要绕过把手并把条码朝外，因为分拣线是靠激光扫条码的。第二，行李平放、轮子朝下，把手不要竖起来，否则容易在传送带拐弯处卡住。第三，boarding pass 与行李凭条要留到落地取到行李为止，行李没出来时这两张纸就是你唯一的凭据。

语言上要注意，英国工作人员在机器旁大量使用祈使句，而且省略主语：`Tap start.` / `Passport on the glass.` / `Wheels down.` 这些不是不礼貌，而是效率导向。你听不懂时用 §14 的六句去修复，比猜着做更安全。相反，你自己提要求时仍要保留 `please` 和 `could`。

## 18. 练习题

### A. 识别

1. 屏幕出现 `Bag accepted`，说明什么已经完成？
2. 引导员说 `That bag's a bit over` —— 他在说重量还是尺寸？
3. `Remove old tags` 要求你做什么？
4. `Out of service` 出现在机器上时你该怎么办？

### B. Pattern 替换

1. 用 P050 问：是否允许把行李箱当随身行李带上机。
2. 用 P053 问：笔记本电脑要不要从包里拿出来。
3. 用 P054 问：这是不是飞曼彻斯特那班的队。
4. 用 P058 请对方帮你操作打印挂牌。

### C. 即时应答

1. 工作人员说：**How many bags are you checking?**  
   你的回答：________
2. 工作人员说：**Attach the tag to the handle, barcode facing out.**  
   你的回答：________
3. 工作人员说：**You'll need to take out about two kilos.**  
   你的回答：________
4. 工作人员说：**Your gate will show on the screens about forty minutes before.**  
   你的回答：________

### D. 异常处理

1. 情境：机器打印出了 boarding pass，但 bag tag 没打出来，你后面还有人排队。要求：不用逐句翻译，自己完成任务。
2. 情境：你的行李箱比传送带宽，屏幕要你去 oversized desk，但你不知道在哪儿。要求：不用逐句翻译，自己完成任务。
3. 情境：你和同行的朋友分别在两台机器上操作，系统说你们不在同一订位上。要求：不用逐句翻译，自己完成任务。

### E. 迁移练习

把本课 Pattern 用到另一个旅行场景。

1. 在火车站自助取票机前，用 P058 请工作人员帮忙。
2. 在超市自助收银机前，用 P054 确认自己排的队对不对。
3. 在博物馆入口，用 P050 问是否允许带大背包进展厅。

## 19. 场景通关标准

- [ ] 10 秒内说明自己的任务
- [ ] 听懂并回答至少 8/10 个高频问题
- [ ] 主动使用本课 New Patterns
- [ ] 能迁移至少 2 个 Review Patterns
- [ ] 至少会 3 种对话修复方法
- [ ] 遇到一个常见异常仍能把事情办成

## 20. Related Scenes

- Scene 001 — 柜台值机 / Counter check-in — 人工柜台流程，机器失败时的退路
- Scene 003 — 行李超重与超尺寸 / Overweight and oversized baggage — bag drop 报超重后的处理
- Scene 004 — 选座与同行同座 / Seat selection and sitting together — 自助机上也能改座位
- Scene 005 — 转机与行李直挂 / Connecting flights and through-checked baggage — 转机时挂牌上会印两段航段





