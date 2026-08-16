# Corpomancy

*Field notes on Corporate Thaumaturgy, recorded in the only vocabulary any
of us found precise enough: level, school, casting time, range, components,
duration, classes.*

**The archive is live: [gothosvc.github.io/corpomancy](https://gothosvc.github.io/corpomancy/)**

Corpomancy is a shared grimoire kept by a loose, largely unaccredited
fellowship of researchers — we call ourselves the Working Group, mostly
because none of us could agree on anything more dignified — who arrived
independently, at different companies, in different years, at the same
uncomfortable conclusion: the modern corporate environment is not merely
dysfunctional. It is *animate*. Standups, budget cuts, reorgs, all-hands —
we no longer believe these are metaphors for magic. We believe they are
magic, competently disguised as management practice, and this volume is our
attempt to document it with the rigor we would bring to any other plane of
study.

We do not know whether corporate environments generate this magic, or
whether something already magical simply found corporate environments to
be excellent camouflage. We have not ruled out the second possibility.
Several of us would prefer not to think about it further. The observations
keep arriving regardless, and Corpomancy is where we keep them, entry by
entry, so that no two of us record the same phenomenon twice under
different names.

A note on method, since a few early contributors asked: not every spell
here is a corporate translation of a specific incantation from other
traditions. Most are original findings that simply happen to fall within a
discipline's territory. "Fireball (Mass Layoff)" is a fine joke, when it
happens to fit; a wholly original finding that only makes sense inside an
office is equally welcome, and considerably more common.

## The Disciplines

Eight disciplines have been confirmed so far — the same eight schools of
magic every other tradition already recognizes, which we take as mild
evidence that whatever we're studying still obeys some older structure
underneath the fluorescent lighting. Each discipline maps to exactly one
corporate domain:

| Corporate Domain | Classical Tradition | Flavor |
|---|---|---|
| **Compliance & Risk** | Abjuration | Wards, shields, blocking — legal, HR, audit, insurance |
| **Procurement & Resourcing** | Conjuration | Summoning headcount, budget, and vendors from nothing |
| **Analytics & Forecasting** | Divination | Dashboards, KPIs, market research, seeing the roadmap |
| **Sales & Stakeholder Management** | Enchantment | Persuasion, buy-in, negotiation as mind control |
| **Finance & Cost-Cutting** | Evocation | Burn rate, budget axes, scorched-earth cuts |
| **Marketing & Optics** | Illusion | Spin, greenwashing, brand narrative, "the numbers look fine" |
| **Legacy Systems & Zombie Projects** | Necromancy | Reviving dead initiatives, maintaining code no one understands |
| **Org Design & Process Change** | Transmutation | Reorgs, pivots, "digital transformation" |

The full record of how we arrived at each mapping — including lines of
inquiry we opened and abandoned — lives in [`SCHOOLS.md`](SCHOOLS.md),
which also serves as the field's working taxonomy.

## How the Archive Is Organized

```
corpomancy/
├── README.md              this file — pitch + taxonomy table (GitHub-facing)
├── CONTRIBUTING.md         how to submit a finding for peer review
├── SCHOOLS.md              the taxonomy: chartered disciplines, abandoned inquiry, how to propose a new one
├── TEMPLATE.md              the standard format for recording a finding
├── MECHANICS.md              lexicon of phenomena observed across more than one finding
├── index.md                site homepage content (site-facing, distinct from this README)
├── _config.yml             Jekyll site config
├── _data/schools.yml        machine-readable mirror of SCHOOLS.md's chartered table, for site templates
├── _layouts/               site page templates (default, home, domain, spell)
├── assets/css/             site stylesheet
├── .github/                PR/issue templates, CI validation, Pages deploy workflow
└── spells/
    ├── compliance-risk/
    ├── procurement/
    ├── analytics-forecasting/
    ├── stakeholder-management/
    ├── finance/
    ├── marketing-optics/
    ├── legacy-systems/
    └── org-design/
```

Directories are named for the **corporate domain**, not the underlying
school — the school is recorded as metadata (in `SCHOOLS.md` and in each
finding's own stat block), not the organizing axis. We tried it the other
way once and several of us got lost in our own archive. Each
`spells/<domain>/` directory carries its own `README.md` with field notes
on that discipline's tone and a jargon bank worth mining for future
findings, plus one file per confirmed spell.

Effects that keep reappearing across otherwise unrelated findings — saving
throw types, resource pools, conditions — are logged centrally in
[`MECHANICS.md`](MECHANICS.md), so two of us don't independently name the
same phenomenon twice.

## Status

39 findings recorded and awaiting peer review — the original 24 (levels
1-6, one trio per discipline), plus a second pass adding 8 high-level
capstone rituals (levels 7-9, one per discipline) and 7 spells that, for
the first time, target a rival organization rather than the caster's own.
We are choosing not to dwell on how easily that second category came to
us:

- **Compliance & Risk:** Document Retention, Indemnification, Nondisclosure,
  Chapter 11 *(9th, capstone)*, Cease and Desist *(combat)*
- **Procurement & Resourcing:** Conjure Contractor, Conjure Headcount, Three
  Bids and a Buy, Vertical Integration *(7th, capstone)*, Vendor Lock-In
  *(combat)*
- **Analytics & Forecasting:** Forecast, Dashboard, Root Cause Analysis, The
  Algorithm *(9th, capstone)*, Competitive Intelligence *(combat)*
- **Sales & Stakeholder Management:** Charm Stakeholder, All-Hands,
  Objection Handling, Activist Campaign *(8th, capstone)*, Poach *(combat)*
- **Finance & Cost-Cutting:** Reduction in Force, Burn Rate, Capitalize the
  Loss, IPO *(9th, capstone)*, Short Position *(combat)*
- **Marketing & Optics:** Rebrand, Greenwash, Thought Leadership, Crisis
  Management *(8th, capstone)*, Smear Campaign *(combat)*
- **Legacy Systems & Zombie Projects:** Animate Legacy System, Speak with
  Former Employee, Bus Factor, System Sunset *(7th, capstone)*, Rip and
  Replace *(combat)*
- **Org Design & Process Change:** Reorg, Convert, Agile Transformation,
  Hostile Takeover *(8th, capstone + combat in one)*

Combat spells introduce a new targeting convention — "one organization you
can identify as a competitor" — logged in
[`MECHANICS.md`](MECHANICS.md#recurring-target-types).

## The Archive & Correspondence

The grimoire is live: **[gothosvc.github.io/corpomancy](https://gothosvc.github.io/corpomancy/)**.
We debated keeping this in the locked drawer indefinitely and eventually
concluded that a discovery of this size doesn't stay useful if the only
people checking it are the ones who already believe it. The archive is
public now, and so is correspondence.

Findings can be submitted for peer review as a pull request — see
[`CONTRIBUTING.md`](CONTRIBUTING.md). An automated check confirms a
submission is structurally sound (front matter, required fields, discipline
consistency); it cannot and does not judge whether a finding is actually
funny, true, or advisable to have written down. That remains a human —
well, a wizard — judgment call, made in the open now, by whoever shows up.
