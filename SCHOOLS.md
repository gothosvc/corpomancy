# Taxonomy of Disciplines

The organizing axis of this whole endeavor is the **corporate domain** (the
directory name under `spells/`), not the classical tradition it's bound
to — that tradition is
recorded alongside it as flavor and mechanical basis, the way a specimen's
genus doesn't dictate which drawer of the cabinet it goes in. This document
is where we keep the taxonomy straight: which disciplines are chartered,
which lines of inquiry we opened and abandoned, and which phenomena we've
noticed but haven't yet earned a proper chartering.

## Chartered Disciplines

| Corporate Domain | Directory | Classical Tradition | Status | Flavor |
|---|---|---|---|---|
| Compliance & Risk | `compliance-risk/` | Abjuration | Chartered | Wards, shields, blocking — legal, HR, audit, insurance |
| Procurement & Resourcing | `procurement/` | Conjuration | Chartered | Summoning headcount, budget, and vendors from nothing |
| Analytics & Forecasting | `analytics-forecasting/` | Divination | Chartered | Dashboards, KPIs, market research, seeing the roadmap |
| Sales & Stakeholder Management | `stakeholder-management/` | Enchantment | Chartered | Persuasion, buy-in, negotiation as mind control |
| Finance & Cost-Cutting | `finance/` | Evocation | Chartered | Burn rate, budget axes, scorched-earth cuts |
| Marketing & Optics | `marketing-optics/` | Illusion | Chartered | Spin, greenwashing, brand narrative, "the numbers look fine" |
| Legacy Systems & Zombie Projects | `legacy-systems/` | Necromancy | Chartered | Reviving dead initiatives, maintaining code no one understands |
| Org Design & Process Change | `org-design/` | Transmutation | Chartered | Reorgs, pivots, "digital transformation" |

"Chartered" means the discipline is formally bound to one of the eight
classical schools of magic. All eight are now spoken for. We are aware
this means the Working Group closed its own founding charter after exactly
eight entries, which several of us find suspicious and none of us are
willing to investigate further.

## Abandoned Lines of Inquiry

Kept here so nobody re-opens one of these from scratch in eighteen months,
having forgotten we already had this argument.

- **Evocation** — also considered: *Incident Response / Site Reliability
  Engineering* (a strong fit — "everything's on fire," "war room," "blast
  radius" — but reserved as a strong candidate for a Provisional discipline
  rather than spending it here); *Aggressive Sales / Closing* (risked
  cannibalizing Enchantment's territory); *Litigation / Legal Offense*
  (risked cannibalizing Abjuration's territory). Finance won on the
  strength of "burn rate" already being literal fire language in the
  vocabulary practitioners were using anyway, long before any of us thought
  to write it down.

## Provisional Disciplines (observed, not yet chartered)

Unlike a Chartered discipline, a Provisional one has no obligation to map
onto an existing school — it may exhibit its own signature entirely, the
way a genuinely new phenomenon sometimes does, provided it's a coherent
corporate domain nobody's chartered yet. Currently on the board, none yet
written up:

- **Site Reliability / Incident Response** — passed over for Evocation (see
  above); still open, and arguably the strongest unclaimed candidate we
  have on file.
- **Ops & Manufacturing** — supply chain, logistics, the physical/production
  side of an organization as opposed to the software side.
- **Marketing (broad/legitimate)** — brand, content, campaigns, creative —
  the non-deceptive counterpart to Illusion's spin/optics angle. **Note:**
  this overlaps with `marketing-optics/` (Illusion); if this discipline is
  ever chartered, revisit whether Illusion's domain should narrow to just
  "spin/optics/deception" specifically, ceding general marketing craft to
  the new one.
- **Bureaucromancy** — forms, approvals, red tape, sign-off chains, the
  specific and very real magic of a document that cannot proceed because
  the one person who can sign it is currently out of office. Floated early
  as a name for the entire field, before we settled on Corporate
  Thaumaturgy instead (two disciplines ending in "-mancy" in the same
  volume was, on reflection, one too many). Still a fine name for a single
  discipline, and still unclaimed.

## Chartering a New Discipline

1. Pick a corporate domain not already claimed (check the tables above).
2. Decide Chartered vs. Provisional — Chartered is closed (all eight
   classical schools are spoken for), so realistically this means
   Provisional.
3. Add a row to whichever table above fits, with a one-line flavor
   description.
4. `mkdir spells/<domain-slug>/` (kebab-case, matches the `Directory`
   column style).
5. Add `spells/<domain-slug>/README.md` following the pattern in the
   existing domain READMEs (field notes on tone + a jargon word bank),
   including the `layout: domain` front matter block (copy an existing one
   and adjust).
6. Add the domain to the table in the top-level `README.md`.
7. Add a matching entry to `_data/schools.yml` — it's the site's
   machine-readable mirror of the Chartered Disciplines table above, and it
   will not notice a new discipline on its own.
