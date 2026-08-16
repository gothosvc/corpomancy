<!--
This is the standard recording format for a new finding. Copy this file
into the relevant spells/<domain>/ directory as <spell-name-kebab-case>.md,
fill it in, and delete this comment block before submitting it for review.

A note on method:
- Not every finding is a corporate translation of an incantation already
  catalogued elsewhere. Most of what we record are original observations
  that simply happen to fall within a discipline's territory — don't force
  a translation if the honest original finding is stronger. If a finding
  does happen to echo something from another tradition, that's a private
  note for your own drafting process, never something that should surface
  in the visible entry.
- Record every finding the way a field researcher records a specimen:
  clinically, precisely, without commentary on how strange it is. No
  winking asides, no "unlike other findings..." remarks, no observation
  that pauses to note its own absurdity. If the entry is doing its job, the
  strangeness is entirely load-bearing in what the specimen actually does —
  never something the person recording it needs to point out. We have all
  read entries that broke this rule. None of us enjoyed reviewing them.
- Phenomena (saving throw types, resource pools, conditions, etc.) may be
  named freely and referenced as though already an established part of
  this field — this isn't a playable ruleset, so nothing needs a prior
  formal definition. Check `MECHANICS.md` first, though: reuse a phenomenon
  already logged there if it fits, and log anything genuinely new in the
  same submission.
- `Classes` (who is capable of casting this) stays a flat, undecorated
  list of 2-4 roles. No parentheticals, no conditions, no exceptions. If a
  finding truly needs a casting caveat, it belongs in the body as a
  one-off detail for that entry, not as a precedent set in the header.
  This field is deliberately not tracked in `MECHANICS.md` — who casts
  something is local color, not a taxonomy we're trying to keep
  consistent, and it should stay that way.
- Level is a rough proxy for the scope and standing required to cast it —
  the same convention every other tradition uses. Higher level, wider
  blast radius, more authority needed to attempt it, and a correspondingly
  worse time for whoever's on the receiving end.
- The site's renderer treats a run of lines with no blank line between them
  as one paragraph, and collapses the line breaks to spaces — it will not
  put Casting Time, Range/Area, Components, Duration, and Classes on their
  own lines by default. End each of those four lines (every field except
  the last, Classes) with a literal `<br>` so they render as intended. If a
  field's own value happens to wrap across more than one source line for
  readability, don't add `<br>` at that internal wrap point — only at the
  true end of the field, right before the next one starts. See any existing
  spell for the pattern.
-->

# Spell Name

*Nth-level [corporate domain]*

**Casting Time:** ...<br>
**Range/Area:** ...<br>
**Components:** V, S, M (...) — verbal (what's said), somatic (what's done),
material (what's spent/consumed — budget, headcount, political capital)<br>
**Duration:** ...<br>
**Classes:** ...

Description of what the spell does, played completely straight as a rules
entry. This is where the joke lives — precise mechanical language applied to
mundane/absurd corporate behavior.

***At Higher Levels.*** (optional) How the effect scales if cast using a
higher-level slot — i.e. with more seniority, budget, or org-wide reach
behind it.

---
**Flavor:** *(optional italicized flavor quote — the line an NPC would say,
or a line from a performance review, Slack message, all-hands transcript,
etc.)*
