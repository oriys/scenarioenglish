# Research — Scene 004 Seat selection & changes

> Purpose: verify British Airways seat-selection and change rules at check-in before Scene 004 is finalised. Seat selection/change is the most airline- and fare-dependent of the three scenes; the figures and age rules below are BA-specific and marked as such.

`policy_sensitive: false` (seat selection is a paid/optional interaction; the underlying process is stable, but fees and rules change — keep `last_verified` honest)

`last_verified: 2026-08`

## 1. Research question

Which seat-selection and seat-change facts should Scene 004 teach, and which figures must not be hard-coded?

Specific points to verify:

1. Is seat selection free or charged, and for which seat types (standard / preferred / extra legroom / exit row)?
2. When free seat selection becomes available (relative to check-in).
3. Rules and age/eligibility limits for exit-row seats.
4. Rules for travelling companions wanting to sit together (same booking vs different bookings).
5. Whether a seat can be changed after check-in and before boarding, and how fees/refunds work on a change.

## 2. Real-world flow

### 2.1 Existing allocation vs choosing

On most fares the system allocates a seat; the passenger can either keep it or choose a different one. At check-in (counter, kiosk, or online) the seat you request is confirmed against the remaining inventory. This matches Scene 004's "system allocated a seat, you want to change it" framing and the reality that remaining choice at check-in is limited.

### 2.2 When seat selection is free

British Airways ("Choosing your seat"):

- "You can choose your seat **for free from 24 hours before departure when check-in opens**" — on most fares.
- **Basic ticket (economy, hand-baggage only):** the seat is **allocated free when check-in opens**; you may then pay to change to a different seat, though choice may be limited. Alternatively you can pay to choose from booking until check-in opens.
- Frequent-flyer tiers (BA Club / oneworld) get free seat selection earlier (Bronze/Ruby from 7 days; Silver/Sapphire from booking excluding exit rows; Gold/Emerald from booking for the whole party). Exit-row seats on long-haul become selectable free from 24 hours before departure for some tiers.

Course implication: Scene 004 is correct that the free-selection window is narrow and that at check-in the free choices are often the leftover middle seats. The distinction between a "standard free seat" and "paid preferred/extra-legroom/exit-row" seats is accurate.

### 2.3 Paid seat types

British Airways:

- The cost of seat selection varies by seat type and cabin; prices show at booking or in Manage My Booking.
- **Extra legroom / preferred seats** are generally chargeable (paid seating).
- **Bulkhead seats may not be selectable** — usually reserved for customers with a disability or travelling with an infant.
- Seat prices differ by route, cabin and fare; **do not publish one price** (Scene 004's `£15` examples are fictional and should stay marked as such).

Course implication: `extra legroom`, `preferred seat`, `exit row`, `bulkhead` as *categories* match BA; any currency figure in the scene must be clearly fictional/an example.

### 2.4 Exit-row eligibility and the age rule — IMPORTANT (conflict)

British Airways exit-row requirements (official):

> "you must: be **over the age of 12 years old**, not be pregnant, not have accessibility needs or be substantially blind or deaf, be fit enough to operate an emergency exit door, be able to understand printed or verbal instructions given in English, and be willing, as well as able, to assist in the case of an emergency evacuation."

**Conflict found:** Scene 004's Role Play / bad-news text says exit-row requires being "over sixteen". British Airways' published minimum is **over 12 years old**. If BA (UK-first) is the reference carrier, the scene should say **over 12 / 12 or older**, not "over sixteen". (Other airlines may differ; 16 is not BA's figure.)

### 2.5 Sitting together / family seating

British Airways:

- If seats are not chosen in advance, BA "will do our best to seat your family together by assigning seats a few days before" departure, but "seating may be limited... and your seats may be split across different rows or the aisle."
- "We'll make sure each **child under 12 years** sits next to an adult from your booking, but children **over 12 years are booked as an adult**... and may sit separately."
- On different bookings, to guarantee sitting together you generally need to choose seats in advance (potentially paid).
- Travelling with an infant (under 2, not in own seat): seats are free, and the party can choose seats free from booking (subject to availability/carrycot position).

Course implication: Scene 004's "request two seats together; sometimes only same-row or nearby is possible; anywhere-is-fine is the right ask" is accurate. The "children under 12 guaranteed next to an adult" detail is a useful, BA-specific fact but is a policy that can change — mark it as such.

### 2.6 Changing a seat after check-in and before boarding

British Airways (seating Terms & Conditions):

- "On British Airways marketed and operated flights, you may **change your seat (subject to availability) at any time**."
- "If you change your seat to a **lower-priced seat**, we will **not refund the difference** in price. If you change to a **higher-priced seat**, you must pay the difference."
- **Paid seating is not guaranteed** — seats may need to change for operational/safety/security reasons, even after boarding; BA will attempt a suitable alternative, and refunds apply in defined cases.
- At the gate / on board, if something "frees up", a polite request may succeed (Scene 004 and Scene 018's premise).

Course implication: "you can keep asking at the gate if something frees up" is supported. The change rules (no refund of the difference to a lower-priced seat; pay the difference to a higher-priced seat) are useful and BA-specific.

### 2.7 Payment method for paid seats

British Airways: seat payments are made by credit/debit card or Avios (where eligible). "Like many airlines, we only accept debit or credit card payments at many of the airports we operate from, including London Heathrow, London Gatwick and North America." Consistent with the card-only reality in Scene 003.

## 3. Real-world English

- `seat selection`
- `window seat` / `aisle seat` / `middle seat`
- `extra legroom` / `preferred seat`
- `exit row` / `bulkhead seat`
- `Standard seat` vs `chargeable` / `Preferred`
- `allocated`
- `sit together` / `travelling together` / `side by side`
- `free up` / `taken`
- `reprint your boarding pass`
- `a one-off charge` vs `per flight`

## 4. Common failure points

### 4.1 Hearing "over twelve" and Scene 004 printing "over sixteen"

The age rule in the scene body contradicts BA's published rule. Fix the figure to BA's (over 12) or mark the age as an example ("age rules vary; in BA's case, 12+").

### 4.2 Assuming free = any seat

Free seat selection from check-in only covers non-Basic fares and whatever is left; preferred/extra-legroom/exit-row seats are often paid. Teach recognition of `chargeable` / `additional charge applies`.

### 4.3 Believing a paid seat is guaranteed

Even a paid seat is not guaranteed (operational/security changes can move it). Not a refund guarantee — check terms.

### 4.4 Expecting a price to be fixed

Prices vary by route, cabin and fare, and change. Any number in the scene must be an example.

### 4.5 Over-negotiating pooling/seats when not possible

If checked-allowance pooling is disallowed (BA, Scene 003) — separate issue; for seats, being flexible ("anywhere is fine") is more effective than insisting on a specific seat.

## 5. Current rules / policy-sensitive facts

`policy_sensitive: false`

`last_verified: 2026-08`

Dynamic facts; each can change by operator/airport/route/time:

- **Free seat selection from 24 hours before departure when check-in opens** on most BA fares; Basic (hand-baggage-only) fares allocate a free seat and charge to change. BA seating. `last_verified: 2026-08` — **varies by airline and fare.**
- **Exit-row eligibility (BA): over 12 years old**, not pregnant, no accessibility needs, fit, understand English instructions, willing to assist. BA seating T&Cs. `last_verified: 2026-08` — **age/eligibility can vary by airline.**
- **Paid seat types:** extra-legroom, preferred, and (selectable) exit-row seats are generally chargeable; bulkhead seats are often not selectable (reserved for disability/infant). BA seating. `last_verified: 2026-08` — **which seats are paid varies.**
- **Children under 12 are seated next to an adult on the same booking**; over-12s are booked as adults and may sit separately. BA family seating. `last_verified: 2026-08` — **varies by airline.**
- **Seat can be changed any time subject to availability; no refund of difference to a lower-priced seat; pay the difference to a higher-priced seat.** BA seating T&Cs. `last_verified: 2026-08` — **policy varies.**
- **Paid seats not guaranteed**; may be moved for operational/safety/security reasons with a suitable alternative sought. BA seating T&Cs. `last_verified: 2026-08` — **varies.**
- **Seat payments by card/Avios; card-only at many airports (incl. Heathrow/Gatwick).** BA seating. `last_verified: 2026-08` — **varies.**

## 6. Sources

### Tier 1 — Official / primary

1. British Airways — Choosing your seat / Reserving your seat
   https://www.britishairways.com/content/information/seating/reserving-your-seat

   Used for:
   - free seat selection from 24 hours before departure;
   - Basic-ticket seat allocation & pay to change;
   - paid seat types vs free;
   - exit-row eligibility (over 12, not pregnant, no accessibility needs, English, willingness to assist);
   - changing a seat before boarding and the lower/higher-priced change rules;
   - family seating (under-12 next to an adult; over-12 booked as adult);
   - paid-seating refund/change Terms & Conditions;
   - card-only airport payment note.

2. British Airways — Seating (hub)
   https://www.britishairways.com/content/information/seating

   Used for:
   - the authoritative index of BA seating options and seat maps;
   - recognising standard vs paid seat categories.

3. British Airways — Family seating
   https://www.britishairways.com/content/information/family-travel/seating

   Used for:
   - the under-12 / over-12 seating guarantee nuance;
   - infants and travelling-together guidance.

### Tier 2 — Industry

4. IATA —(context) seat-assignment conventions / airline ancillary revenue
   https://www.iata.org/
   Used for:
   - the industry framing that seat selection is a paid/optional ancillary whose price and rules are airline/fare-defined;
   - no universal seat price.

## 7. Course design decisions

### Keep in Scene 004

- stating a preference (`I'd prefer an aisle seat, if possible`);
- asking for alternatives after a refusal (`Is there any ... closer to the front?`);
- confirming whether a seat costs (`Is there any charge for that one?` / `a one-off charge or per flight?`);
- exit-row eligibility conversation (with the corrected, BA figure over 12);
- travelling together (`Could I have two seats together?` / `We'd just like to sit together — anywhere is fine.`);
- reprinting the boarding pass and verifying the seat number;
- the gate "try again if something frees up" follow-up.

### Move out of Scene 004

- **seat fee economics and FEE AMOUNTS** → keep purely as fictional examples; never a "the price" figure (part of Scene 004's boundary: recognise `chargeable`, don't teach a price list);
- **on-board seat interactions, allowing others past, adjusting seat** → Scene 018;
- **actual boarding-process seat checks / groups** → Scene 013 (boarding groups, priority);
- any detailed seat-map / aircraft-config teaching (over-scoped for this lesson).

## 8. What we intentionally do NOT teach

- a single/universal seat price (BA prices vary by route/fare and change; keep example-only);
- a single universal minimum age (correct BA to 12+ but warn other airlines differ);
- full aircraft seat-map layouts;
- frequent-flyer seat-benefit tiers (only touch the concept that tiers unlock free selection);
- whether a specific seat is "worth it" (a judgement, not a fact).

Scene 004 should leave a learner able to: state a seat preference, react to "all taken", find alternatives, understand the free-vs-paid distinction, handle exit-row eligibility questions, arrange to sit with a companion, and re-verify the seat number on the boarding pass.

## 9. Conflicts with the current scene body (for the author)

- **Exit-row age: Scene 004 says "over sixteen"; BA's published minimum is 12.** Update to `over 12` (or mark clearly as a variable example) — this is the most important factual fix in Scene 004.
- Scene 004's `£15` / `£12` prices are fictional examples and should be explicitly marked as such (BA publishes no single seat price; it varies by route/fare and changes over time).
- The scene correctly treats the paid-vs-free distinction as key; make sure the wording "extra legroom is almost always paid" stays a generalisation, not a guarantee (some tiers get exit/extra-legroom free at 24h).
- The scene implies a seat change is closed after check-in; BA's terms allow changing the seat at any time before boarding subject to availability. Keep the gate-follow-up, but note the change window is not strictly closed at check-in.