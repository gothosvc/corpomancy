---
layout: default
title: Mechanics
permalink: /mechanics/
wide: true
---

[&larr; Corpomancy]({{ '/' | relative_url }})

# Lexicon of Recorded Phenomena

Certain effects keep turning up across findings recorded independently, by
different members of the Working Group, at different companies that have
never had any contact with one another — the same resistance an
organization's leadership seems to muster against a personnel-targeting
effect, the same slow bleed of capital reserves regardless of what anyone
does about it. Past a certain point, that stops looking like coincidence.
This document is where we keep those phenomena named consistently, so
nobody spends an afternoon re-deriving Tenure under a different word
because they didn't check first.

This is **not** a ruleset. Nothing here needs exact math, a DC table, or a
formal definition beyond what a given entry already states — we are
cataloguing, not legislating. Before naming a new phenomenon for a finding,
check the tables below; reuse an existing one if it's a reasonable match,
name a new one if it isn't, and record it here in the same submission that
introduces it.

## Saving Throw Types

| Save | Represents | Examples |
|---|---|---|
| Tenure | Seniority, leverage, and political protection — resisting a personnel-targeting or persuasion effect | [Reduction in Force]({{ '/spells/finance/reduction-in-force/' | relative_url }}), [Hostile Takeover]({{ '/spells/org-design/hostile-takeover/' | relative_url }}), [Poach]({{ '/spells/stakeholder-management/poach/' | relative_url }}) |
| Solvency | Whether the org can absorb a shock without collapsing, rolled when a resource pool (e.g. Runway) hits 0 or when a shifted liability lands; also used directly as a materiality yardstick (a fraction of current Solvency setting the ceiling a lesser effect can reach) | [Burn Rate]({{ '/spells/finance/burn-rate/' | relative_url }}), [Litigation Blitz]({{ '/spells/compliance-risk/litigation-blitz/' | relative_url }}), [Short Position]({{ '/spells/finance/short-position/' | relative_url }}) |
| Maintenance | Whether a legacy system holds together for another stretch of time, keyed to Technical Debt score | [Animate Legacy System]({{ '/spells/legacy-systems/animate-legacy-system/' | relative_url }}), [Rip and Replace]({{ '/spells/legacy-systems/rip-and-replace/' | relative_url }}) |
| Discovery | Whether a warded record, process, or claim resists a formal attempt to verify or compel disclosure of the truth behind it | [Document Retention]({{ '/spells/compliance-risk/document-retention/' | relative_url }}), [Greenwash]({{ '/spells/marketing-optics/greenwash/' | relative_url }}), [Performance Review]({{ '/spells/analytics-forecasting/performance-review/' | relative_url }}) |

## Derived Stats / Scores

| Stat | Used for | Examples |
|---|---|---|
| Technical Debt score | Drives Maintenance saving throws for legacy/undead systems — higher score, harder save | [Animate Legacy System]({{ '/spells/legacy-systems/animate-legacy-system/' | relative_url }}), [System Sunset]({{ '/spells/legacy-systems/system-sunset/' | relative_url }}) |
| Blamelessness score | Drives whether a post-incident check finds a systemic cause or scapegoats an individual | [Root Cause Analysis]({{ '/spells/analytics-forecasting/root-cause-analysis/' | relative_url }}), [Short Position]({{ '/spells/finance/short-position/' | relative_url }}) |

## Resource Pools (temporary-HP analogs)

| Pool | Represents | Behavior | Examples |
|---|---|---|---|
| Runway | A capital reserve absorbing damage before real HP | Depletes on a fixed per-turn schedule that cannot be prevented, in addition to absorbing damage normally | [Burn Rate]({{ '/spells/finance/burn-rate/' | relative_url }}), [Hostile Takeover]({{ '/spells/org-design/hostile-takeover/' | relative_url }}), [Litigation Blitz]({{ '/spells/compliance-risk/litigation-blitz/' | relative_url }}) |
| Windfall | A reserve of temporary resources gained from a major capital event, spendable to cast another spell without expending a spell slot | Granted once, expires if unspent after a stated window; a few spells can also cause a *target* to gain one as an ironic side effect of the caster's own failure | [IPO]({{ '/spells/finance/ipo/' | relative_url }}), [Golden Parachute]({{ '/spells/compliance-risk/golden-parachute/' | relative_url }}) |

## Deferred Effects

| Effect | Represents | Behavior | Examples |
|---|---|---|---|
| Amortized Loss | Damage deferred and spread across future turns instead of taken immediately | Total damage taken is never less than the amount originally deferred, and increases with each schedule extension (interest) | [Capitalize the Loss]({{ '/spells/finance/capitalize-the-loss/' | relative_url }}), [Chapter 11]({{ '/spells/compliance-risk/chapter-11/' | relative_url }}) |

## Conditions / Statuses

| Condition | Effect | Removed by | Examples |
|---|---|---|---|
| Insolvent | Incapacitated-equivalent; the org cannot act | Chapter 11 is now a spell that directly interacts with this condition (it doesn't remove it, but suspends its consequences); no spell removes it outright yet — we keep meaning to look into that | [Burn Rate]({{ '/spells/finance/burn-rate/' | relative_url }}), [Chapter 11]({{ '/spells/compliance-risk/chapter-11/' | relative_url }}) |
| Documented (status, not condition) | Satisfies any other spell/effect's prerequisite that requires accurate documentation, regardless of whether documentation actually exists | N/A — persists with the system | [Animate Legacy System]({{ '/spells/legacy-systems/animate-legacy-system/' | relative_url }}), [Performance Review]({{ '/spells/analytics-forecasting/performance-review/' | relative_url }}), [Greenwash]({{ '/spells/marketing-optics/greenwash/' | relative_url }}) (at higher levels) |
| Misaligned | Multiple creatures agree something was decided or compelled, each privately certain of a different, often mutually exclusive interpretation of what that was | Not removed — resolves only when the affected creatures act and the divergence becomes visible | [Power Word: Buzzword]({{ '/spells/stakeholder-management/power-word-buzzword/' | relative_url }}) |

## Damage / Effect Types

| Type | Represents | Examples |
|---|---|---|
| Severance damage | Damage dealt by dismissal/termination effects | [Reduction in Force]({{ '/spells/finance/reduction-in-force/' | relative_url }}), [Chapter 11]({{ '/spells/compliance-risk/chapter-11/' | relative_url }}) |

## Recurring Non-Caster Roles

Mechanical roles a spell can require be staffed/assigned, distinct from the
`Classes` field (which lists who can *cast* the spell):

| Role | Required by | Examples |
|---|---|---|
| On-Call Engineer | Legacy Servants (must be permanently assigned one; cannot be reassigned without reversing the spell) | [Animate Legacy System]({{ '/spells/legacy-systems/animate-legacy-system/' | relative_url }}), [System Sunset]({{ '/spells/legacy-systems/system-sunset/' | relative_url }}) |
| Records Custodian | Any Document Retention ward (a Discovery save is auto-failed if none can be identified) | [Document Retention]({{ '/spells/compliance-risk/document-retention/' | relative_url }}) |

## Recurring Creature/Entity Types

Named creature types a spell conjures or transforms something into,
referenced across more than one finding:

| Type | Represents | Examples |
|---|---|---|
| Contractor | A temporary conjured worker; vanishes with all accumulated knowledge when its spell ends unless a Knowledge Transfer is separately arranged | [Conjure Contractor]({{ '/spells/procurement/conjure-contractor/' | relative_url }}), [Convert]({{ '/spells/org-design/convert/' | relative_url }}), [Rip and Replace]({{ '/spells/legacy-systems/rip-and-replace/' | relative_url }}) |
| Legacy Servant | An undead-equivalent risen from a decommissioned system or project | [Animate Legacy System]({{ '/spells/legacy-systems/animate-legacy-system/' | relative_url }}), [System Sunset]({{ '/spells/legacy-systems/system-sunset/' | relative_url }}) (destroys it, the one controlled way), [Hostile Takeover]({{ '/spells/org-design/hostile-takeover/' | relative_url }}) |
| HR Representative | An investigatory entity summoned by formal complaint; loyal to minimizing the organization's own Solvency exposure, not to whichever party summoned it | [Summon Human Resources]({{ '/spells/compliance-risk/summon-human-resources/' | relative_url }}) |

## Recurring Target Types

| Target | Represents | Examples |
|---|---|---|
| Rival Organization | The standard targeting phrase for adversarial ("combat") spells: "one organization you can identify as a competitor." Casting Competitive Intelligence on an org formally satisfies this requirement if you don't already qualify some other way (e.g. public knowledge, a prior encounter). Cease and Desist targets a broader "infringing" criterion, not competitor status, and deliberately does not use this phrase. | [Competitive Intelligence]({{ '/spells/analytics-forecasting/competitive-intelligence/' | relative_url }}), [Smear Campaign]({{ '/spells/marketing-optics/smear-campaign/' | relative_url }}), [Hostile Takeover]({{ '/spells/org-design/hostile-takeover/' | relative_url }}) |

Use this exact phrase ("one organization you can identify as a competitor")
in any future combat spell's Range/Area rather than inventing new wording
for the same requirement.

## Recording Conventions (not mechanically tracked)

Not phenomena in themselves, but two write-up conventions the Working Group
has settled on for consistency across findings filed independently:

**Casting Time hedging.** Several findings give a short, official-sounding
Casting Time (often "1 action") immediately qualified by the real
bureaucratic delay before anything actually happens — a Lead Time, a
Headcount Approval check, a multi-month rollout. Where a finding's nominal
instant of casting and its practical timeline diverge, record both: "1
action, but/though/contingent on X."

**"Power Word: X" naming.** Reserve this prefix for an incantation that
requires no saving throw and instead gates its effect on some threshold
unrelated to the target's resistance — a materiality threshold, a
seniority difference, whether a prior record exists. The gating threshold
should be structural, not a reskinned saving throw wearing a different
name; potency is beside the point, several of the smallest recorded
instances document the pattern most cleanly.

## Explicitly Not Tracked Here

**`Classes`** (who can cast a given spell) is intentionally excluded from
this lexicon. Unlike saves/stats/pools/conditions, caster roles are local
color for a single spell, not a shared system — there's no goal of a
consistent IC/Manager/Director/Exec taxonomy across findings, and the field
should stay a flat list with no conditions or exceptions attached. If this
ever changes, it changes on purpose, not by accretion.

## Recording a New Phenomenon

1. Check the tables above — if an existing save/stat/pool/condition covers
   what the finding needs, reuse it rather than naming a near-duplicate.
2. If it's genuinely new, add a row to the relevant table with a one-line
   description and the spell file it appears in.
3. Keep the description generic enough that a *different* discipline could
   plausibly reuse the phenomenon later (e.g. Tenure isn't finance-specific
   — any discipline with a personnel-targeting effect could use it).
