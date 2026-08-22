# Research — Scene 005 Connecting flights and through-checked baggage

> Purpose: verify the real-world connecting-flights / through-checked-baggage process before Scene 005 is finalised. This file records the transfer journey, the booking-shape rule that decides whether a bag is checked through, security/terminal realities at Heathrow, policy-sensitive facts, and the course-design boundary with Scene 001. It is deliberately written wider than the final lesson.

`policy_sensitive: true`

`last_verified: 2026-08`

## 1. Research question

What does a traveller with a *connecting itinerary* actually need to understand and ask at and after check-in, and which parts of that belong in Scene 005 rather than Scene 001 (counter) or later disruption scenes?

Scene 001 (2.5) already hands off the two core confirmation questions (`Is my bag checked through to my final destination?`), and Scene 002 ends with "转机时挂牌上会印两段航段" (the bag tag prints two segments). Scene 005 therefore must:

1. Define **through-checked baggage** and the **booking-shape rule** that decides whether a bag is checked through (single booking reference / same reservation vs separate bookings).
2. Teach the **arrival-and-connect flow**: follow `Connections` / `Flight Connections` signs, re-security where required, find the next gate/terminal, and whether immigration/visas are involved.
3. Train the four high-frequency questions:
   - `Is my bag checked through to my final destination?`
   - `Do I need to collect and recheck it?`
   - `Which terminal is my next flight?`
   - `How much time do I need?`

The research question for this note: which of these facts are **stable English / stable process** (teachable) and which are **airline/airport/route-specific rules** (flag, don't hard-code)?

## 2. Real-world flow

### 2.1 The booking rule that decides baggage handling — the heart of the scene

The single most important fact, confirmed consistently across BA, Heathrow, KLM and IATA-framed industry sources:

- **Same booking reference / same reservation (one PNR), on one ticket — or oneworld / alliance flights booked under the same reference** → checked baggage is tagged and transferred through to the **final destination**. You do **not** normally collect it at the connection.
- **Separate reservations / different booking references** (even on the same airline) → **each flight is a separate journey**; you must collect your bag in baggage reclaim, exit to airside arrivals as needed, then go to departures, check the bag in again, and re-clear security.

Course implication: the correct teachable frame is **"same booking reference (PNR)"**, not "same airline" and not strictly "same ticket." BA states that oneworld flights under the *same booking reference* (`same ticket number`) are checked through even with different ticket numbers. So the discriminating variable the learner should be able to *name and check* is the **booking reference / whether it's one reservation**.

Practical check: when in doubt, **ask at first check-in** (this ties directly to Scene 001's handoff) and **read the bag tag for the destination city** (Scene 002's "两段航段"). If only your first airport is printed, the bag is not checked through to the end.

### 2.2 Check-in: confirming through-check

At the counter/kiosk (Scenes 001/002), the learner should routinely confirm through-check when the itinerary has a connection. This is where `Is my bag checked through to my final destination?` lives.

Real-world staff input (intent family):
- `Your bag is checked through to […].`
- `You'll need to collect and recheck it in […].`
- `Bags are tagged through to your final destination.`
- `Check the destination on your bag tag.`

BA: *"If you are connecting onto another flight, you can check your bags through to your final destination, providing: all your flights are on one booking reference with the same ticket number, or all your flights are with oneworld airlines booked under the same booking reference…"* — and for separate references: *check in for first flight → follow Arrivals/Baggage Reclaim → check in again → allow time.*

### 2.3 Arrival and the connection corridor (the new part Scene 005 adds)

Once on the ground at the hub, the through-check decision mostly resolves, and the learner's job becomes **finding the connection**:

Heathrow real-world flow for a same-terminal / airside connection:

1. Disembark; follow the purple **`Flight Connections`** signs (BA: "follow the purple 'Flight Connections' signs").
2. **Go through Security again** — Heathrow: *"All connecting passengers must go through security again at Heathrow."* (Liquids/large electronics up to 2L may stay in cabin baggage; UK-wide rule.)
3. **Passport/border** — normally **no** immigration for international→international airside connection. Exception: international → UK/Ireland domestic flights require Passport Control + a facial biometric image. KLM/Amsterdam: Schengen↔non-Schengen transfer requires passport control again.
4. **Inter-terminal transfer** — if the next flight is in another terminal:
   - Heathrow T2 and T3 are connected (short walk); T3↔T5 use free Flight Connections buses (every 6–10 min); T4 connect via the free shuttle/Heathrow Express.
   - **Gate info only appears on screens after you clear security**, so check the departure board for the onward *terminal*, then the gate later.
5. Collect any onward **boarding pass** at a kiosk / transfer desk if not already issued (most airlines issue all boarding passes at first check-in — KLM: "In most cases you'll receive your boarding pass for your connecting flight already when you check in for your first flight").
6. Proceed to the onward gate; be at the gate **20 minutes before** departure (BA).

### 2.4 When you DO have to collect the bag (and exit and re-enter)

- **Separate bookings** (different PNR) → collect, exit through Arrivals, re-check at Departures, re-clear security. Heathrow: "If you've booked two flights separately, you'll most likely need to collect checked bags and check them back in… simply exit through Arrivals and check-in at Departures."
- **Certain jurisdictions require bag reclaim even on a single ticket** — e.g. first point of entry into the **US, and China** (KLM: "If you're having a transfer in the United States or China, you probably do have to collect your luggage… because of local regulations"). This is a strong example of *route-specific* over-rides that Scene 005 should mention, not encode as universal.
- **Airport transfer that forces border control** (e.g. Madrid T1-3 → T4/T4S) may turn an "airside transit" into an "entry" with visa implications (see §5).

### 2.5 Watching the clock

- **Minimum connection time (MCT)** only really applies to tickets booked on one reservation with an airline/travel agent; it is airport/route specific (Amsterdam: ~40 min Schengen / 50 min non-Schengen; varies by airport). BA notes *same-ticket* connections get reduced connection times shown in Manage My Booking.
- **Separate bookings have no MCT protection** — Heathrow explicitly: "if you booked your flights separately, these minimum connection times don't apply. Allow plenty of extra time."
- **Missed connection due to delay on one ticket** → airline rebooks at no cost; BA: go to the Customer Service desk in Flight Connections to rebook; oneworld Global Support can help.
- **Missed connection on separate bookings** → the airline is not obliged to rebook/reprotect you (BA + KLM both state this).

## 3. Real-world English

### 3.1 Signs / screens

- `Flight Connections` / `Connections` (purple signs at Heathrow) — recognition critical
- `Arrivals / Baggage Reclaim` — where you go **only if** you must collect the bag
- `Departures` — where you re-check after collecting
- `Transfer` (sometimes `Transit` varies by region; many UK/EU sites now avoid "transit")
- `Gate` / `Boarding` — after security
- `International / Domestic` (continental split, e.g. Schiphol, Madrid)
- `Transfer desk` / `Connections desk` — where to get onward boarding pass / rebook

### 3.2 Documents / objects

- `booking reference` / `PNR` (the discriminating variable) — review from Scene 001
- `through-checked` / `checked through` (adj: `through-checked baggage`; verb: `to check your bag through (to …)`)
- `final destination`
- `connection` / `connecting flight` (`onwards` / `onward flight`)
- `bag tag` / `baggage tag` (read the printed destination city) — review from Scene 002
- `baggage reclaim` / `baggage claim` (UK vs US)
- `airside` / `landside` (conceptual; teach as recognition: airside = past security, landside = public area)
- `minimum connection time (MCT)` (recognition)
- `transfer desk`

### 3.3 High-probability staff intentions

1. confirm the onward flight / terminal;
2. tell the passenger whether the bag is checked through;
3. direct to `Flight Connections` / the correct terminal shuttle;
4. tell the passenger if they must collect and recheck;
5. advise on time / missing the connection;
6. rebook if the connection is missed (on one ticket).

Representative natural wording:
- `Your bags are checked through to [final destination].`
- `You'll need to collect and recheck your bag in [hub].`
- `Follow the purple Flight Connections signs.`
- `Your next flight is in Terminal 5 — take the free bus.`
- `You'll need to go through security again.`
- `You don't need to go through immigration.`
- `Your gate will show on the screens after security.`
- `You need to be at the gate 20 minutes before.`
- `Don't worry — we'll rebook you on the next available flight.`
- `Check the destination on your bag tag.`

## 4. Common failure points

### 4.1 Assumption that a bag is always checked through
A learner may assume one booking / one airline guarantees through-check, or that a bag always reaches the final destination. The rule is **booking-reference based** and has **route exceptions** (US, China). → Teach explicit confirmation, not assumption.

### 4.2 Tight connection / running out of time
Real and high-frequency. → Train `How much time do I need?`, `Will I have enough time to make it?` (P049, already in the bank), and recognising that a single-ticket connection is usually protected while a separate-booking "self-connect" is not. Route time questions to the airline at the transfer desk, not to memorising MCT numbers.

### 4.3 Next flight in a different terminal (or different airline)
Heathrow T3↔T5 buses, T2↔T3 walk; at some airports (e.g. Madrid, Schiphol) terminal change can mean border control. → Train `Which terminal is my next flight?` and the terminal/airline dimension.

### 4.4 Re-security / visa surprises
- Heathrow: **all** connecting passengers re-clear security.
- Schengen reality: a purely **airside** transit usually needs only an airport-transit visa for listed nationalities; but any transfer that **forces border control** (terminal change, or entering Schengen to connect to an internal flight, reaching baggage reclaim because bags must be collected) requires a **full Schengen visa** / entry clearance. See §5. → The course should teach that the *visa question* is itinerary-specific and worth confirming, not bake in one answer.

### 4.5 Missed connection whose bag / ticket is separate
Aspirational belief that the airline will always look after you. → State the single-ticket vs separate-ticket protection difference (BA/KLM: separate bookings are separate contracts; no automatic rebooking, no automatic through-transfer).

### 4.6 Not keeping the boarding pass / bag tag
If you must collect the bag, you need the tag/receipt. — review from Scene 001.

## 5. Current rules / policy-sensitive facts

`policy_sensitive: true`

`last_verified: 2026-08`

Each fact below **can change by operator / airport / route / time** — Scene 005 must present the language and process, not hard-code the exceptions as permanent.

- **Through-check depends on the booking, not the airline.** On one booking reference (same ticket, or oneworld/alliance flights under the same reference) bags are usually checked through; on separate references each flight is a separate journey and baggage must be collected and re-checked. **BA — Connection page & Separate-tickets FAQ.** *May vary by airline/interline agreement.*
- **Some countries require bag reclaim even on one ticket** — notably **first point of entry into the US and China** because of local regulations / customs-first-of-entry. **KLM.** *Route/regulation-specific.*
- **All connecting passengers re-clear security at Heathrow**; liquids ≤2L may stay in cabin baggage during the connection (UK-wide security rule). **Heathrow — Connecting flights.** *Security regimes vary by country; may tighten/relax (e.g. EU new liquid detectors rollout).*
- **International → international airside connections at Heathrow normally need no immigration**; international → UK/RoI domestic connections need Passport Control + a facial biometric check. **Heathrow / BA.** *Route-specific; check current border rules.*
- **Inter-terminal transfer at Heathrow:** T2↔T3 walkable; T3↔T5 free Flight Connections buses (≤10 min); gate info appears on boards only **after** security. **BA / Heathrow.** *Airport-specific.*
- **Separate bookings have no minimum connection time protection.** Same-ticket connections get an MCT from the airline/travel-agent; separate self-connects require self-allotted extra time (BA suggests ≥4h at Heathrow for separate tickets). **Heathrow / BA.** *Numbers vary by airport/airline; use only as example.*
- **Missed connection (one ticket) ⇒ airline rebooks at no cost; separate bookings ⇒ separate contract, no obligation to rebook or transfer.** **BA / KLM.** *Policy-sensitive; operator terms differ.*
- **Schengen airport-transit vs entry:** a purely airside (international area) transit may need only an airport-transit visa (Type A) for certain nationalities; any transfer that **requires border control** (terminal change that enforces entry, or collecting baggage to enter) needs a **full Schengen visa** / entry clearance. **Spanish Ministry of Foreign Affairs (EU/Schengen).** *Nationality and route specific; check per itinerary.*

## 6. Sources

### Tier 1 — Official / primary

1. **British Airways — Flight connections (London Heathrow & beyond)**
   https://www.britishairways.com/content/information/airport-information/flight-connections
   Used for:
   - purple `Flight Connections` signs;
   - same-ticket reduced connection times;
   - separate-tickets ≥4h guidance at Heathrow;
   - T2/T3 connected; T3↔T5 free Flight Connections buses; T5 A/B/C gates and transit;
   - Passport Control needed only for UK/RoI connections;
   - gate 20 minutes before departure;
   - **through-check rule** (one booking reference / oneworld same reference) vs separate-booking reclaim;
   - Customer Service desk rebooking on a missed connection; oneworld Global Support.

2. **British Airways — Travelling on separate tickets (baggage FAQ)**
   https://www.britishairways.com/content/information/help/faq/baggage/travelling-on-separate-tickets
   Used for:
   - each separate booking = a separate journey, even same airline;
   - bags are **not** transferred on different booking references;
   - limited assistance on delay/cancellation for separate tickets;
   - the collect → re-check steps.

3. **Heathrow — Connecting flights**
   https://www.heathrow.com/connecting-flights
   Used for:
   - **all connecting passengers re-clear security** at Heathrow;
   - most passengers don't collect baggage (airline transfers it);
   - separate bookings ⇒ collect + exit via Arrivals + check in at Departures;
   - separate bookings have no MCT; allow extra time;
   - gate info shown on boards only after security;
   - same-terminal vs inter-terminal vs self-connect; purple signs;
   - missed connection ⇒ go to airline desk to rebook.

4. **KLM — Transfers (connecting flights)**
   https://www.klm.com/information/airport/transfers
   Used for:
   - European (SkyTeam) operator confirming most transfers don't require bag collection;
   - US / China bag reclaim exception (local regulations);
   - separate ticket + non-partner airline ⇒ collect and recheck;
   - boarding passes for all legs issued at first check-in;
   - Schengen↔non-Schengen ⇒ passport control again;
   - Schiphol minimum transfer times (~40 min Schengen / 50 min non-Schengen) — example only;
   - missed connection: SkyTeam rebooks automatically vs unprotected separate airline.

5. **Spain — Spanish Ministry of Foreign Affairs, EU & Cooperation (Schengen airport transit visa)**
   https://www.exteriores.gob.es/…/Visado-de-transito-aeroportuario.aspx
   Used for:
   - airport transit visa (Type A) covers airside international-area transit only, does **not** permit entry;
   - a connection requiring **border control** (terminal change, entering Schengen, collecting bags) needs a full Schengen visa;
   - concrete example: Madrid T1-3 → T4/T4S **implies entering the Schengen area**;
   - confirms nationality-based lists.

### Tier 2 — Industry (cross-carrier standards)

6. **IATA — Interline Considerations on Baggage Standards / IATA Baggage**
   https://www.iata.org/baggage
   Used for:
   - interline baggage acceptance / transfer / final-delivery framing;
   - through-check where interline agreement exists vs not.

7. **oneworld — connection / baggage and global support framing**
   https://www.oneworld.com/
   Used for:
   - oneworld same-booking-reference through-check (used by BA) and oneworld Global Support on missed connections.

8. **Travelport / OAG — Minimum Connect Time (MCT) definitions**
   https://support.travelport.com/… & https://www.oag.com/blog/minimum-connection-times-insiders-guide
   Used for:
   - MCT defined as the shortest interval to transfer a passenger *and their luggage*;
   - MCT varies by airport → reinforce "don't memorise a universal figure".

### Tier 3 — Industry / consumer summaries (corroboration only, never sole basis)

9. **Trip.com — Check-Through Baggage Guide (recheck rules for connecting flights)**
   https://www.trip.com/guide/info/check-through-baggage.html
   Used for:
   - plain-language summary of when you must collect and recheck (incl. US/China, separate tickets) — consistent with Tier 1, used only to validate natural wording.

## 7. Course design decisions

### Keep in Scene 005

- the **through-check / booking-reference rule** as the central concept:
  - `Is my bag checked through to my final destination?`
  - `Do I need to collect and recheck it?`
  - reading the destination city printed on the bag tag (ties to Scenes 001/002);
- the **connection corridor** after landing:
  - follow `Flight Connections` / `Connections` signs;
  - re-clear security (Heathrow reality), with the practical note that resecurity is the norm;
  - find the next gate on the board **after** security;
  - `Which terminal is my next flight?` and terminal-transfer language (`shuttle`, `walk`, `bus`);
- the **time question**: `How much time do I need?`, `Will I have enough time to make it?` (P049, reuse from the bank) — with the operational truth that a same-ticket connection is airline-protected while a separate-booking self-connect is not;
- the **rebooking move** on a missed connection (go to the transfer/connections desk), but as recognition-level handling, not a full disruption scenario (full detail → Scene 022+);
- high-frequency vocabulary: `connection`, `connecting flight`, `final destination`, `through-checked`, `booked separately`, `transfer desk`, `resecurity / go through security again`, plus recognition of `airside`, `minimum connection time`.

### Move out of Scene 005

- detailed **flight-delay / cancellation recovery and EU261-style money rights** → disruption scenes (022, 023…);
- **individual route/airline mechanics** (who rebooks, which partner agreements, each airport's MCT) → mention "check with your airline", do not encode;
- **visa / immigration depth** (who needs a Type A vs full Schengen visa by nationality) → a dedicated documents/visa scene; Scene 005 only teaches the *sentence* for asking whether a transfer requires entering the country (e.g. documents for re-entry);
- gate-arrival / boarding-group detail → Scenes 012/013.

### Scenes 001 ↔ 005 linkage (authoring notes)

- **From Scene 001** (2.5): already hands off `Is my bag checked through…?` / `Do I need to collect and recheck it?`. Scene 005 must **reuse** these two verbatim (mark as review patterns from 001) and add the arrival-side questions (`Which terminal…?`, `How much time…?`). Do not re-teach from zero; extend.
- **From Scene 002**: the note that "转机时挂牌上会印两段航段" — Scene 005 should explicitly call back to reading the **bag tag** as the physical proof of through-check and add the caveat that a tag showing only the first airport means the bag stops there. Add to Scene 002's Related Scenes that bag-tag use is the concrete bridge to Scene 005.
- **No conflict with Scene 001's rule** that the lesson must not teach "you never collect your bag on a connection" as universal — Scene 005 owns the exceptions (separate tickets, US/China first-point-of-entry). Scene 001 can keep its brief mention.
- **Pattern reuse:** P049 (`Will I have enough time + V?`) and P055 (`Which gate/terminal…?`) already exist; consider adding one new Scene-005-native pattern such as `Is my bag checked through to + place?` (locative confirmation) only if it genuinely increases cross-scene value — otherwise reuse P050 / P058 phrasing. New player-check questions (`Is my connection protected?`) are more suited to the later disruption scenes.

## 8. What we intentionally do NOT teach

Scene 005 will **not** require the learner to memorise:

- a universal minimum connection time (figures vary by airport/airline, e.g. ≠ Schiphol 40/50);
- which specific nationalities need a Schengen airport-transit visa vs a full visa;
- each airline's interline/codeshare agreement matrix;
- US/China customs-first-point-of-entry detail beyond "some countries make you collect the bag";
- EU261-style protection amounts and claims procedure;
- rebooking logic for every operator.

The learner should leave Scene 005 able to:

1. state whether their bag is checked through (and how to check: booking reference + bag-tag destination);
2. ask `Do I need to collect and recheck it?` when uncertain, and act on the answer;
3. follow `Connections` signage, re-clear security where required, and locate the next terminal/gate;
4. ask `Which terminal is my next flight?` and `How much time do I need?`;
5. know that a single-ticket connection is generally protected while a separate-booking self-connect is not, and where to go on a missed connection.

## 9. Conflicts / reconciliation notes

1. **Through-check "rule" wording varies by source.** BA frames it around "one booking reference with the same ticket number **or** oneworld under the same booking reference"; KLM frames it around SkyTeam partner flights / single reservation; IATA frames it around the existence of an **interline agreement** plus the itinerary. These agree on the *practical* learner takeaway (same reservation → checked through; separate → recheck), but Scene 005 should teach the **booking-reference test**, then note that airlines may additionally require an interline/agreement link — so "ask when in doubt." **No core conflict; frame carefully.**

2. **"Immigration not needed" is not universal.** Heathrow: international→international airside needs no immigration; but international→UK/RoI needs Passport Control + biometrics; Schiphol Schengen↔non-Schengen needs passport control. So Scene 005 must say "you *may* need to go through passport control / immigration, depending on route", never "you never need it" — otherwise it would contradict the Schengen reality in §5.

3. **MCT vs "protected connection".** Same-ticket connections carry an MCT and are protected (rebooked on delay). Separate self-connects have no MCT and no protection. These are two separate concepts that a naive scene might conflate — Scene 005 should distinguish "enough time" (MCT) from "protected against delay" (single ticket) so it doesn't mislead learners into thinking a long gap on separate tickets makes the connection safe if the first flight is late.

4. **Bag-tag "two segments" (Scene 002)** is a useful *happy-path* hint but not a universal guarantee — some itineraries legitimately show a through-tagged single destination lacking visible "two segments", and route exceptions (US/China) force collection despite a plausible through-tag. Scene 005 should present the bag tag as supporting evidence, not proof, to stay consistent with Scene 001's "never universal" rule.