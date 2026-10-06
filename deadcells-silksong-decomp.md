# Dead Cells × Hollow Knight: Silksong — Decomposition

A breakdown of both games into their core systems, then a mapping of how Dead Cells' structure could sit on top of Silksong. This is a working design doc: sections marked **Options** are choices to make, not decisions.

> Details are from general game knowledge. Verify specific names and numbers in-game before building on them.

---

## 1. Premise

**Working concept:** Dead Cells' run-based roguelite structure (permadeath, procedural levels, build-crafting, meta-progression) layered onto Silksong's movement, combat feel, and world (Pharloom, Hornet).

**Target:** published on Melty so players can install and launch it easily.

**The core tension to solve:** Silksong is a hand-authored, interconnected world where progression comes from *exploration and permanent ability unlocks*. Dead Cells is a *procedural run* where progression comes from *build choices within a run* plus *unlocks between runs*. The mashup has to pick which game owns the macro structure.

---

## 2. Dead Cells — Decomposition

### 2.1 Core loop
1. Start a run at the Prisoners' Quarters with a basic loadout.
2. Move through a chain of biomes, each with branching exits.
3. Fight, collect gold, cells, and scrolls; pick up weapons, skills, and mutations.
4. Die (or win) → cells are banked at the Collector → spend them on permanent unlocks.
5. Repeat with a wider pool of options.

### 2.2 Systems

| System | What it does | Notes |
|---|---|---|
| **Permadeath** | Death ends the run; most items and gold are lost | Defines pacing and tension |
| **Procedural levels** | Each biome is assembled from hand-made room chunks | Layout varies, art and enemies are authored |
| **Biome graph** | Branching paths between biomes with different difficulty and rewards | Run length and route are player-influenced |
| **Weapons & skills** | Two weapon slots, two skill slots, plus an amulet | Items come from drops, chests, and shops |
| **Scrolls of power** | Stat boosts in three colors (Brutality, Tactics, Survival) | Drive the build's scaling identity |
| **Mutations** | Passive perks chosen at altars | Modify combat, healing, and survivability |
| **Healing flask** | Limited-use heal that refills between biomes | Upgradeable through meta-progression |
| **Movement kit** | Roll as dodge, jump, ledge grab; runes unlock traversal | Runes gate optional areas |
| **Currencies** | Gold (spent in-run) and cells (banked after death) | Two-tier economy |
| **Blueprints / Collector** | Found items unlock new gear for future runs | Primary meta-progression hook |
| **Elites, cursed chests, challenge rifts** | Risk/reward side content | Optional difficulty spikes |
| **Boss Stem Cells** | Stacking difficulty levels after beating bosses | Endgame replayability |
| **Daily run** | Fixed-seed shared challenge | Optional live-service piece |

### 2.3 What gives Dead Cells its feel
- **Fast, readable combat** with strong item variety
- **Short feedback loops** (a run in ~30–60 minutes, rooms in seconds)
- **Build identity** emerging from scroll color + weapon synergies
- **Constant forward momentum**, with few reasons to backtrack

---

## 3. Silksong — Decomposition

### 3.1 Core loop
1. Explore Pharloom's interconnected regions.
2. Fight enemies and bosses, gather currency, find ability upgrades.
3. Use benches to save and refresh; die and recover your lost currency.
4. Unlock traversal abilities that open previously blocked routes.
5. Take on quests, side content, and increasingly demanding bosses.

### 3.2 Systems

| System | What it does | Notes |
|---|---|---|
| **Needle combat** | Hornet's primary melee weapon | Fast, precise, built around spacing |
| **Silk** | Resource built by landing hits; spent on Bind and silk skills | Ties offense to defense |
| **Bind** | Spend silk to heal | Risky, since it commits Hornet in place |
| **Tools** | Equippable consumables and gadgets with limited uses | Closest analogue to Dead Cells skills |
| **Crests** | Switchable loadouts that change Hornet's moveset and tool slots | Closest analogue to Dead Cells weapons |
| **Rosary & shell shards** | Currencies for purchases and crafting | Dropped on death, recoverable |
| **Traversal abilities** | Dash, wall cling, glide/float, and others unlocked over time | Gate world progression |
| **Benches** | Save points and respawn anchors | Anchor the exploration rhythm |
| **Map & quests** | Mapping-by-purchase and a large quest board | Reward thoroughness |
| **Bosses** | Hand-authored, pattern-driven fights | Core spectacle |

### 3.3 What gives Silksong its feel
- **Agile, acrobatic movement** with precise air control
- **Punishing but fair** boss and enemy design
- **A hand-authored world** with atmosphere and discovery
- **Resource tension** between offense, healing, and positioning

---

## 4. System Mapping

How each Dead Cells system could translate into Silksong terms.

| Dead Cells | Silksong equivalent | Fit | Notes |
|---|---|---|---|
| Weapon slots | **Crests** and needle upgrades | Strong | Swap crests as "weapons" with distinct movesets |
| Skill slots | **Tools** | Strong | Already cooldown/ammo-limited gadgets |
| Healing flask | **Bind** | Medium | Bind is silk-based; flask is charge-based. Pick one, or combine |
| Roll | **Dash** | Medium | Dead Cells' i-frames vs Silksong's momentum-based dash |
| Scrolls of power | New system | Needs design | No direct counterpart; candidate for a three-stat build axis |
| Mutations | New system, or charms-like passives | Needs design | Could be run-only passives |
| Cells + Collector | Rosary / shell shards + a hub vendor | Medium | Needs a banked, run-surviving currency |
| Blueprints | Unlockable crests/tools/passives | Strong | Natural meta-progression |
| Runes (traversal) | Silksong traversal abilities | Strong | Same function: gate optional areas |
| Biome graph | Pharloom regions as run segments | Needs design | The biggest structural question (see §5) |
| Procedural rooms | Authored room chunks from Silksong-style areas | Needs design | Requires modular room kit |
| Bosses | Silksong bosses at biome ends | Strong | Fits naturally |
| Boss Stem Cells | Difficulty tiers | Strong | Direct port |
| Daily run | Seeded challenge | Optional | Defer until post-MVP |

---

## 5. Open Design Questions

### 5.1 Who owns the macro structure? — **Options**
- **A. Run-first (Dead Cells shape):** a full run is a descent through procedurally assembled Pharloom regions. Death resets to a hub. Traversal abilities become run pickups or meta-unlocks.
- **B. World-first (Silksong shape):** a fixed Pharloom with Dead Cells-style combat items and mutations, plus a roguelite mode (e.g., challenge dungeons) layered on top.
- **C. Hybrid hub:** Silksong-style hub area (benches, vendors, quests) that launches short Dead Cells-style runs into procedural regions.

### 5.2 Movement identity — **Options**
- Keep Silksong's momentum and air control as the baseline, with Dead Cells' quick-restart pacing.
- Or tune toward Dead Cells' tighter, roll-based dodge for faster crowd fighting.

### 5.3 Healing model — **Options**
- Silk-only Bind (Silksong)
- Flask charges that refill per region (Dead Cells)
- Both, with Bind as the in-fight option and flask as the safety net

### 5.4 Build axis — **Options**
- Port the three scroll colors as-is
- Re-theme them around silk (e.g., needle, tool, and bind scaling)
- Skip scrolls and rely on crest + tool + passive synergies alone

### 5.5 Permanence
- What persists after death? (Unlocked items, currency, map knowledge, traversal abilities?)
- What is always reset? (In-run items, gold, health upgrades?)

---

## 6. Content Inventory (to scope)

| Category | Needed |
|---|---|
| Regions / biomes | A small set to start (3–4 for MVP) |
| Room chunks per region | Enough for visible variety on repeat runs |
| Enemy roster | A mix of Silksong-style and new enemies per region |
| Bosses | One per region end |
| Crests / weapons | A handful with distinct movesets |
| Tools / skills | A handful with distinct uses |
| Passives / mutations | A starter set |
| Hub | One area with vendor, bench, and unlocks |

---

## 7. MVP Slice (suggested starting point)

The smallest version that proves the concept:

1. One hub with a bench and an unlock vendor
2. Two procedural regions with a boss at the end of each
3. Two crests and three tools
4. A small passive pool with 6–10 options
5. Permadeath with one persistent currency
6. A basic win/lose screen and run summary

Everything else (daily runs, difficulty tiers, extra regions) comes after the core loop is fun.

---

## 8. Risks

- **Scope:** both games are content-heavy; the MVP has to stay small.
- **Feel clash:** momentum-based movement and room-by-room procedural flow can fight each other.
- **Balance:** combining two item systems (crests/tools and weapons/skills/mutations) multiplies the tuning surface.
- **Asset and IP handling:** confirm what Melty's tooling allows you to use and reference before committing to a content plan.

---

## 9. Next Steps

1. Pick the macro structure from §5.1.
2. Decide the healing and build-axis models (§5.3, §5.4).
3. Define what persists after death (§5.5).
4. Lock the MVP slice and list its assets.
