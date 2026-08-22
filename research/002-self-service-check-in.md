# Research — Scene 002 Self-service check-in & bag drop

> Purpose: verify the real-world self-service check-in / bag-drop flow at UK airports (Heathrow focus, British Airways as reference carrier) before Scene 002 is finalised. This file records process, policy-sensitive facts, sources, and course-design boundaries exactly as Scene 001 did for the counter.

`policy_sensitive: true`
`last_verified: 2026-08`

## 1. Research question

What does a traveller actually encounter at a UK self-service check-in kiosk and bag drop, and which points in Scene 002 need to be factually accurate rather than assumed?

Specific rules to verify:

1. Is check-in genuinely split into a two-step flow — print boarding pass / bag tag at a kiosk, then drop the bag at a separate bag drop?
2. Is the bag actually weighed at bag drop (i.e. can the screen legitimately reject a `Bag too heavy`)?
3. Which passengers/situations cannot use the self-service route and must go to a staffed desk (visa/passport checks, special baggage, minors, pets, groups)?
4. What is the role of the agent / host standing near the kiosks?

## 2. Real-world flow

### 2.1 The two-step flow — CONFIRMED (Heathrow official)

Heathrow's own checking-in page describes exactly the two-step flow Scene 002 teaches:

**Step 1 — Check in and tag your bag at the kiosk**

- use a machine to check in and print a boarding pass, **or scan your digital boarding pass** if already checked in online;
- you can also scan your passport (or another identity document) using the passport reader;
- print your bag tag, remove and **keep the receipt**;
- slide the tag face down through the side handle of your bag;
- join the red dots together and smooth the tag to the bag handle.

**Step 2 — Bag drop**

- have your travel documents ready for inspection;
- head to the bag drop area;
- drop your bag and head to security.

Course implication: the scene's `s扫passport 或输 booking reference → 选件数 → 打印 boarding pass + bag tag → 自贴挂牌 → bag drop` sequence matches Heathrow's official description. Two useful additions supported by official text: (a) note that a **digital boarding pass** can be used instead of printing a paper one; (b) keep the receipt.

### 2.2 What the kiosk accepts (British Airways)

BA officially states: at airport check-in kiosks "all you need is your booking reference (PNR) or passport." This matches Scene 002's "扫护照或输入 booking reference（6 位字母数字）".

Note the scene's "6 位字母数字" detail is a reasonable practical description, but PNR length/format is airline-system specific and not a fixed universal — keep it as an in-scene example, not a hard rule.

### 2.3 Is the bag weighed at bag drop? — YES

- Industry sources describing self-service bag drop consistently describe an **integrated scale** that measures each bag in real time at the drop unit.
- BA's excess-baggage model (Scene 003 research) sets the point where a bag is over its allowance; at a self-service bag drop an overweight bag is not accepted and the passenger is routed to a staffed desk or to repack. Scene 002's `Bag too heavy` reject-and-return behaviour is therefore realistic.
- Courser note: Heathrow's own plain-text check-in page describes the flow without spelling out "the bag is weighed here", but the weighing that Scene 002/003 rely on is real and consistent across airline self-bag-drop systems.

### 2.4 Who cannot use the self-service route — CONFIRMED (multiple official points)

The kiosk/bag-drop route is not universal. Official examples:

- **Visa/passport check (intercontinental from Heathrow T3/T5)** — British Airways states passengers on intercontinental flights from Heathrow T3 or T5 must have passport and visa checked before security; this is done at a Bag Drop / Customer Service desk (or a passport/visa desk / self-service touchpoint for hand-baggage-only). So on those routes the self-service kiosk is not the end of document handling.
- **Unaccompanied minors (BA, Heathrow T5)** — a child travelling alone must go to the Family Check-in (Zone E); a child on a separate booking from an adult goes to a check-in desk (Zone H). These are staffed channels, not the kiosk.
- **Groups of more than nine (BA, Heathrow T5)** — must use a check-in kiosk or the Group Check-in area (Zone G).
- **Passengers needing assistance / special items** — industry self-bag-drop eligibility rules exclude passengers needing assistance and special items (infants, sports equipment, strollers etc.) from the fully automated drop; they are routed to staff.
- **Pets** — pets are not part of the normal baggage allowance and are handled at the airport/desk, not the kiosk.

Course implication: Scene 002 is correct to make the kiosk the "happy path" while keeping the agent call-in and a fall back to a staffed counter. The scene does not need to teach UM/pet/assistance procedures themselves.

### 2.5 Role of the agent / host — CONFIRMED

- Heathrow: "Airline staff will be available on hand to help if you experience any difficulties using the self-check-in machines."
- British Airways (Heathrow T5): describes **"hosted self-service touchpoints"** and **"hosted self-service bag drops"** — i.e. the machines are staffed/hosted.

Course implication: the scene's image of a vest-wearing agent beside the machines is accurate; the agent's practical functions are helping with kiosk difficulties, resolving rejected bags, and routing passengers to the correct desk.

### 2.6 Accessibility features of kiosks

Heathrow notes some kiosks have a headphone jack + volume controls (hearing) and braille buttons (vision). Nice-to-know; not needed for the core lesson.

## 3. Real-world English

Practical terms verified against official UK usage:

- `Self-service check-in` — airport/airline signage.
- `Bag drop` — Heathrow/BA standard UK term (US: baggage drop-off). Used for the drop area.
- `Hosted self-service bag drop` — BA's official name for staffed drop units (useful recognition vocabulary; Scene 002's `agent`/`host` is right).
- `Boarding pass` (also `boarding card`).
- `Bag tag` / `baggage tag`; action: `print`, `attach`, `slide through the handle`.
- `Baggage receipt` — Heathrow explicitly says to keep the receipt.
- `Booking reference` / `PNR` — BA accepts this or passport at the kiosk.
- `Passenger with reduced mobility` / `assistance` — recognition terms for "not for me at this step".
- `Please see an agent` — common self-service fallback.

## 4. Common failure points

### 4.1 Kiosk rejects the passport / identity doc

Real and expected; the passport reader may fail. Official kiosks accept booking reference as the alternative, so Scene 002's "agent types the booking reference in" is a realistic recovery.

### 4.2 `Bag too heavy` at self bag drop

Real (bag is weighed at the drop unit). Route is to move weight into hand baggage or go to a staffed desk. Scene 002 is right to show it; full fee/allowance detail belongs in Scene 003.

### 4.3 Oversized item won't fit the belt

Real. Oversize/outsize items go to a dedicated channel/desk. Scene 002 is right to reference `oversized / outsize` and hand off detail to Scene 003.

### 4.4 Assumption that everyone can self-serve

Real risk if a learner travels with a child, in a group >9, on an intercontinental route needing a visa check, or with special baggage. Scene 002 should teach "if the machine isn't right for you, ask" rather than implying self-service is always available.

### 4.5 Old tags / wrong tag placement

Real — old barcodes can confuse the scanner; Heathrow instructs the tag be slid through the handle with the receipt retained. Keeping the `Remove old tags` thread is justified.

## 5. Current rules / policy-sensitive facts

`policy_sensitive: true`

`last_verified: 2026-08`

Facts to hold steady in Scene 002; each can change by operator/airport/route/time:

- **Two-step self-service flow** (kiosk prints boarding pass + bag tag; separate bag drop; then security). Heathrow, checking-in page. **May vary by airport/airline.**
- **Kiosk accepts passport OR booking reference (PNR).** BA, checking-in. **Airline-system specific.**
- **Bag is weighed at self-service bag drop** and an overweight bag is not accepted. Industry (bag-drop unit scales); BA excess-baggage rules set the threshold. **The threshold itself is airline/fare-specific — do not publish 23kg as universal here; that belongs in Scene 003 as a BA example.**
- **Some passengers must use a staffed desk, not the kiosk:** intercontinental visa/passport checks at Heathrow T3/T5; unaccompanied minors; child on a separate booking; groups >9; assistance needs; special/oversized items; pets. BA/Heathrow. **Airline/airport-specific.**
- **Agents/hosts are present** at kiosk and bag drop to help. Heathrow/BA. **Operationally standard but staffing varies.**
- **Power banks / spare lithium batteries:** consistent with Scene 001 — must not go in checked baggage (UK CAA + BA policy). Relevant if the bag-drop screen or agent flags them.

## 6. Sources

### Tier 1 — Official / primary

1. Heathrow — Checking in
   https://www.heathrow.com/departures/checking-in

   Used for:
   - the exact two-step kiosk → bag drop flow;
   - scanning a digital boarding pass;
   - bag-tag placement and keeping the receipt;
   - agents available to help at the machines;
   - accessibility features of kiosks.

2. British Airways — Checking in
   https://www.britishairways.com/content/information/checking-in-and-boarding/checking-in

   Used for:
   - kiosk accepts booking reference (PNR) or passport;
   - passport/visa check requirement on intercontinental flights from Heathrow T3/T5 before security;
   - bag drop zones at Heathrow T5 (Zones C, D, F) and T3 arrangement;
   - re-printing a boarding pass at a kiosk.

3. British Airways — London Heathrow Terminal 5 airport guide
   https://www.britishairways.com/content/information/airport-information/london-heathrow-airport/heathrow-t5

   Used for:
   - "hosted self-service touchpoints" and "hosted self-service bag drops";
   - which passengers use a check-in desk instead (unaccompanied child → Family Check-in Zone E; child on separate booking → Zone H; groups >9 → Zone G);
   - passport/visa check desks before security.

4. British Airways — Baggage essentials
   https://www.britishairways.com/content/information/baggage-essentials

   Used for:
   - the separate cabin-bag and checked-bag allowances that frame what the kiosk/bag-drop checks;
   - power-bank / spare-battery rule cross-check (must be in hand baggage).

5. UK Civil Aviation Authority — lithium batteries / power banks in baggage
   https://www.caa.co.uk/commercial-industry/airlines/dangerous-goods/changes-to-rules-on-the-carriage-of-lithium-cellsbatteries-and-power-banks/

   Used for:
   - carry-on-only rule for power banks / spare batteries, consistent with Scene 001.

### Tier 2 — Industry

6. SITA-type / bag-drop system descriptions — e.g. airport conveyor / bag-drop unit specs describing an integrated scale and real-time weight measurement
   - used to confirm that automated self-service bag drop physically weighs each bag and rejects overweight items.

7. Airline self-bag-drop eligibility guides (e.g. Korean Air "Self-service bag drop", Bangkok Airways) — used to confirm the general industry pattern that self bag drop excludes passengers needing assistance and special/oversized items.

8. IATA — Baggage / checklist for self-service bag drop (industry standard framing)
   https://www.iata.org/.../baggage-... (see Scene 001 Tier 2)

## 7. Course design decisions

### Keep in Scene 002

- the two-step kiosk → bag drop flow;
- scanning passport vs typing booking reference;
- choosing bag count and printing boarding pass + bag tag;
- self-attaching the tag (slide through handle, barcode out);
- `Bag accepted` / `Bag too heavy` feedback;
- old-tag removal; out-of-service machine; reprint at counter;
- calling the agent / host when stuck;
- handoff to security.

### Move out of Scene 002

- overweight/oversize fee detail and repack economics → Scene 003;
- seat-selection/change depth → Scene 004;
- visa/passport-compliance detail → a later documents scene or Scene 001 note (kiosk cannot clear a required visa check by itself — mention only as "this route may not be right for you; ask");
- unaccompanied-minor, group and assistance-channel procedures → not taught (staffed channels, not a learner kiosk task);
- connections/through-checking depth → Scene 005.

## 8. What we intentionally do NOT teach

- the exact weight threshold (23kg etc.) — Scene 003 owns it as a BA example, not a universal;
- the exact list of who may never use a kiosk (varies by airline/airport);
- UM, group, pet and mobility-assistance booking procedures;
- visa requirements for specific routes;
- all kiosk accessibility features;
- a single "correct" machine brand/interface (interfaces vary by airline).

Instead, Scene 002 should leave a learner able to: operate a self-service kiosk on the happy path, read common on-screen prompts (`Scan your passport`, `Bag accepted`, `Bag too heavy`, `Please see an agent`, `Out of service`), fix a document-read failure, fix a bag-tag problem, and know when to switch to a staffed desk.

## 9. Conflicts with the current scene body (for the author)

- Scene 002's "6 位字母数字" PNR length is an example, not a fixed rule — either mark it as an example or soften to "your booking reference (PNR)".
- The scene implies scanner input is universal; official sources confirm the **digital boarding pass** is also accepted at Heathrow kiosks — worth adding so learners who checked in online don't think they must reprint a paper pass.
- The scene's min-guest/assistance boundary is not overstated, but ensure the "minors" line routes to "ask for a staffed desk", not to navigating self-service.