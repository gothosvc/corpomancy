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

| Save | Represents | Introduced in |
|---|---|---|
| Tenure | Seniority, leverage, and political protection — resisting a personnel-targeting or persuasion effect | `spells/finance/reduction-in-force.md` (also: `nondisclosure.md`, `charm-stakeholder.md`, `all-hands.md`, `objection-handling.md`, `org-design/hostile-takeover.md`, `stakeholder-management/activist-campaign.md`, `stakeholder-management/poach.md`, `legacy-systems/rip-and-replace.md`, `finance/impossible-deadline.md`, `compliance-risk/golden-parachute.md`, `org-design/return-to-office-mandate.md`, `org-design/move-hq-to-austin.md`, `procurement/acquihire.md`, `compliance-risk/bind-subordinate.md`, `stakeholder-management/reply-all.md`, `stakeholder-management/expand-territory.md`) |
| Solvency | Whether the org can absorb a shock without collapsing, rolled when a resource pool (e.g. Runway) hits 0 or when a shifted liability lands; also used directly as a materiality yardstick (a fraction of current Solvency setting the ceiling a lesser effect can reach) | `spells/finance/burn-rate.md` (also: `compliance-risk/indemnification.md`, `org-design/hostile-takeover.md`, `compliance-risk/cease-and-desist.md`, `finance/short-position.md`, `procurement/bid-war.md`, `compliance-risk/litigation-blitz.md`, `procurement/power-word-approved.md`) |
| Maintenance | Whether a legacy system holds together for another stretch of time, keyed to Technical Debt score | `spells/legacy-systems/animate-legacy-system.md` (also: `legacy-systems/power-word-forced-restart.md`) |
| Discovery | Whether a warded record, process, or claim resists a formal attempt to verify or compel disclosure of the truth behind it | `spells/compliance-risk/document-retention.md` (also: `procurement/three-bids-and-a-buy.md`, `marketing-optics/greenwash.md`, `compliance-risk/chapter-11.md`, `marketing-optics/crisis-management.md`, `marketing-optics/smear-campaign.md`, `procurement/vendor-lock-in.md`, `marketing-optics/work-from-beach-home.md`, `analytics-forecasting/leak-the-roadmap.md`, `legacy-systems/add-new-column.md`, `marketing-optics/viral-tweet.md`, `analytics-forecasting/performance-review.md`, `stakeholder-management/reply-all.md`, `analytics-forecasting/power-word-directionally-correct.md`) |

## Derived Stats / Scores

| Stat | Used for | Introduced in |
|---|---|---|
| Technical Debt score | Drives Maintenance saving throws for legacy/undead systems — higher score, harder save | `spells/legacy-systems/animate-legacy-system.md` (also: `legacy-systems/add-new-column.md`) |
| Blamelessness score | Drives whether a post-incident check finds a systemic cause or scapegoats an individual | `spells/analytics-forecasting/root-cause-analysis.md` (also referenced by: `marketing-optics/smear-campaign.md`, `stakeholder-management/activist-campaign.md`, `finance/short-position.md`, `compliance-risk/deflect-accountability.md`) |

## Resource Pools (temporary-HP analogs)

| Pool | Represents | Behavior | Introduced in |
|---|---|---|---|
| Runway | A capital reserve absorbing damage before real HP | Depletes on a fixed per-turn schedule that cannot be prevented, in addition to absorbing damage normally | `spells/finance/burn-rate.md` (also referenced by: `org-design/hostile-takeover.md`, `finance/short-position.md`) |
| Windfall | A reserve of temporary resources gained from a major capital event, spendable to cast another spell without expending a spell slot | Granted once, expires if unspent after a stated window; a few spells can also cause a *target* to gain one as an ironic side effect of the caster's own failure | `spells/finance/ipo.md` (also: `finance/short-position.md`, `compliance-risk/golden-parachute.md`, `analytics-forecasting/leak-the-roadmap.md`, `marketing-optics/viral-tweet.md`) |

## Deferred Effects

| Effect | Represents | Behavior | Introduced in |
|---|---|---|---|
| Amortized Loss | Damage deferred and spread across future turns instead of taken immediately | Total damage taken is never less than the amount originally deferred, and increases with each schedule extension (interest) | `spells/finance/capitalize-the-loss.md` (also referenced by: `compliance-risk/chapter-11.md`, `procurement/vertical-integration.md`, `compliance-risk/litigation-blitz.md`) |

## Conditions / Statuses

| Condition | Effect | Removed by | Introduced in |
|---|---|---|---|
| Insolvent | Incapacitated-equivalent; the org cannot act | Chapter 11 is now a spell that directly interacts with this condition (it doesn't remove it, but suspends its consequences); no spell removes it outright yet — we keep meaning to look into that | `spells/finance/burn-rate.md` (also referenced by: `compliance-risk/chapter-11.md`, `finance/short-position.md`) |
| Documented (status, not condition) | Satisfies any other spell/effect's prerequisite that requires accurate documentation, regardless of whether documentation actually exists | N/A — persists with the system | `spells/legacy-systems/animate-legacy-system.md` (also granted by: `marketing-optics/greenwash.md`, at higher levels; `analytics-forecasting/performance-review.md`, `compliance-risk/power-word-per-my-last-email.md`) |
| Misaligned | Multiple creatures agree something was decided or compelled, each privately certain of a different, often mutually exclusive interpretation of what that was | Not removed — resolves only when the affected creatures act and the divergence becomes visible | `spells/stakeholder-management/power-word-buzzword.md` |

## Damage / Effect Types

| Type | Represents | Introduced in |
|---|---|---|
| Severance damage | Damage dealt by dismissal/termination effects | `spells/finance/reduction-in-force.md` |

## Recurring Non-Caster Roles

Mechanical roles a spell can require be staffed/assigned, distinct from the
`Classes` field (which lists who can *cast* the spell):

| Role | Required by | Introduced in |
|---|---|---|
| On-Call Engineer | Legacy Servants (must be permanently assigned one; cannot be reassigned without reversing the spell) | `spells/legacy-systems/animate-legacy-system.md` |
| Records Custodian | Any Document Retention ward (a Discovery save is auto-failed if none can be identified) | `spells/compliance-risk/document-retention.md` |

## Recurring Creature/Entity Types

Named creature types a spell conjures or transforms something into,
referenced across more than one finding:

| Type | Represents | Introduced in |
|---|---|---|
| Contractor | A temporary conjured worker; vanishes with all accumulated knowledge when its spell ends unless a Knowledge Transfer is separately arranged | `spells/procurement/conjure-contractor.md` (also targeted by: `org-design/convert.md`) |
| Legacy Servant | An undead-equivalent risen from a decommissioned system or project | `spells/legacy-systems/animate-legacy-system.md` (destroyed, in the one controlled way possible, by `legacy-systems/system-sunset.md`; also referenced by `org-design/hostile-takeover.md` and `legacy-systems/rip-and-replace.md`) |
| HR Representative | An investigatory entity summoned by formal complaint; loyal to minimizing the organization's own Solvency exposure, not to whichever party summoned it | `spells/compliance-risk/summon-human-resources.md` |

## Recurring Target Types

| Target | Represents | Introduced in |
|---|---|---|
| Rival Organization | The standard targeting phrase for adversarial ("combat") spells: "one organization you can identify as a competitor." Casting Competitive Intelligence on an org formally satisfies this requirement if you don't already qualify some other way (e.g. public knowledge, a prior encounter). | `spells/analytics-forecasting/competitive-intelligence.md` (used as a target by: `marketing-optics/smear-campaign.md`, `stakeholder-management/poach.md`, `compliance-risk/cease-and-desist.md`, `finance/short-position.md`, `org-design/hostile-takeover.md`, `legacy-systems/rip-and-replace.md`, `procurement/acquihire.md`, `procurement/bid-war.md`, `analytics-forecasting/leak-the-roadmap.md`, `compliance-risk/litigation-blitz.md`) |

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
action, but/though/contingent on X." Examples:
`procurement/conjure-contractor.md`, `procurement/conjure-headcount.md`,
`org-design/reorg.md`.

**"Power Word: X" naming.** Reserve this prefix for an incantation that
requires no saving throw and instead gates its effect on some threshold
unrelated to the target's resistance — a materiality threshold, a
seniority difference, whether a prior record exists. The gating threshold
should be structural, not a reskinned saving throw wearing a different
name; potency is beside the point, several of the smallest recorded
instances document the pattern most cleanly. Examples:
`legacy-systems/power-word-forced-restart.md`,
`stakeholder-management/power-word-buzzword.md`,
`compliance-risk/power-word-per-my-last-email.md`,
`procurement/power-word-approved.md`, `finance/power-word-write-off.md`,
`legacy-systems/power-word-blocked.md`,
`analytics-forecasting/power-word-directionally-correct.md`,
`marketing-optics/power-word-on-brand.md`.

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
   description and the spell file that introduced it.
3. Keep the description generic enough that a *different* discipline could
   plausibly reuse the phenomenon later (e.g. Tenure isn't finance-specific
   — any discipline with a personnel-targeting effect could use it).
