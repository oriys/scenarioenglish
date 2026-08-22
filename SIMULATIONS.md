# Scenario English — End-to-End Simulations

> 目标：取消 Scene 边界提示，把多个已学场景串成真实旅程，让学习者证明自己能在连续压力下完成任务，而不是只会单课作答。

## 1. 使用原则

Simulation 不讲新课，主要用于整合与验证：

- 不告诉学习者当前 Scene ID；
- 不提供逐句中文；
- 工作人员可以换表达；
- 至少包含 1 个异常；
- 至少包含 1 个数字 / 时间 / 金额确认；
- 至少出现 1 次必须主动 conversation repair 的位置；
- 最终只按“任务是否完成”评分。

## 2. Simulation A — China → Heathrow → London Hotel

### 目标

从出发机场值机开始，一直到抵达伦敦酒店完成入住。

### 推荐依赖

- 001 柜台值机
- 006 安检标识与排队
- 007 液体、电子设备与随身物品
- 012 找登机口
- 013 登机分组与验票
- 017 找座位与放置行李
- 027 UK eGate
- 028 人工入境问询
- 031 行李提取
- 040 机场交通与问路
- 041 线路图与方向
- 043 Oyster / contactless
- 077 酒店入住

### Injected Problems

随机加入 2 个：

- 行李比额度重 2 kg；
- Gate 从 23 改到 32；
- 入境官要求补充住宿地址；
- 行李转盘临时变更；
- contactless 第一次刷卡失败；
- 到酒店时房间还没准备好。

### Critical Information

每次随机生成：

- flight number
- gate
- boarding time
- hotel postcode
- room number
- deposit amount

## 3. Simulation B — London → Oxford Day Trip

### 目标

从酒店出发，坐地铁 / 火车前往 Oxford，完成一次当天往返。

### 推荐依赖

- 041 看懂线路图、站名与方向
- 044 找站台与确认列车
- 045 换乘
- 056 问路
- 059 单程 / 往返 / off-peak
- 060 Advance vs flexible
- 063 站台变化
- 064 取消与替代交通
- 123 景点购票
- 133 找公共厕所

### Injected Problems

- platform 从 4 改为 14；
- 原列车 cancelled；
- 下一班车需要换乘；
- 学习者误以为 ticket 可以坐任意车次；
- 回程错过原定列车。

## 4. Simulation C — Restaurant → Payment Problem → Support

### 目标

独立完成餐厅用餐，并处理支付异常。

### 推荐依赖

- 092 Walk-in dining
- 094 点菜
- 095 推荐
- 097 饮食限制
- 098 漏单 / 上错菜
- 101 结账、分单与小费
- 141 刷卡
- 142 卡被拒 / 重复扣款

### Injected Problems

- 菜品漏单；
- 服务员说的价格没听清；
- 银行卡第一次 declined；
- terminal 显示交易失败，但手机银行出现 pending；
- bill 多了一项。

### 通过条件

学习者需要做到：

1. 清楚描述问题；
2. 不重复支付造成双扣；
3. 主动确认金额；
4. 提出可执行的下一步方案；
5. 礼貌结束交流。

## 5. Simulation D — Major Travel Disruption

### 目标

训练真实旅行中最需要恢复能力的连续异常。

### 起始情境

你在英国旅行途中收到消息：原航班取消。

### 可随机组合

- 航班取消；
- 客服排队；
- 当晚没有同路线航班；
- 被安排第二天早班；
- 需要确认酒店 / 餐券；
- 托运行李状态不清楚；
- 新航班 Gate 临时变化。

### 核心评分

- 是否能描述现状；
- 是否主动问 `What are my options?`；
- 是否确认新航班日期、时间、机场；
- 是否确认行李去向；
- 是否确认住宿 / 餐食安排；
- 是否在关键信息不确定时主动 repair。

## 6. Simulation Runtime Format

用于 AI Role Play 或教师执行时，建议使用：

```yaml
simulation_id: SIM-A
level: A2-B1
scenes: [001, 006, 007, 012, 013, 017, 027, 028, 031, 040, 041, 043, 077]
required_failures: 2
required_repairs: 1
critical_info_items: 5
show_scene_ids: false
allow_chinese_help: false
```

执行过程：

1. 系统只向学习者说明旅行目标；
2. 每个工作人员角色只知道自己的局部任务；
3. 学习者必须主动推进；
4. 系统按条件随机注入异常；
5. 不因语法小错中断；
6. 只有影响任务的信息错误才需要立即纠正；
7. 结束后统一复盘。

## 7. Scoring Rubric

每项 0–4 分：

| Dimension | 4 分标准 |
|---|---|
| Task Completion | 独立完成全部关键任务 |
| Listening | 能抓住意图和关键数据 |
| Critical Information | 时间、金额、地点等无关键误判 |
| Conversation Repair | 听不懂时主动且有效修复 |
| Problem Recovery | 出现异常后继续推进 |
| Output Usability | 表达简洁、可理解、足以完成任务 |

总分 24。

建议：

- 20–24：Independent
- 15–19：Functional with support
- 10–14：Needs targeted review
- <10：返回对应 Core Scene 训练

## 8. 12 周路线中的位置

建议：

- Week 4 后：Simulation A 的前半段（机场 + 落地交通）
- Week 8 后：Simulation B
- Week 10 后：Simulation C
- Week 12：Simulation A 完整版 + Simulation D

Final Test 不再告诉学习者“这是酒店课 / 火车课 / 支付课”，只给真实任务。
