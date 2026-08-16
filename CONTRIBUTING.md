# Contributing Your Findings

If you've independently observed a corporate phenomenon precise enough to
record properly, we want it — this is exactly how the rest of the volume
got here. This document is the practical mechanics of getting a finding out
of your own notes and into the shared archive; read `README.md` and
`TEMPLATE.md` first if you haven't, this file is just the submission
process. (We are aware that formalizing a submission process is itself the
kind of thing this whole project exists to document. We chose not to let
that stop us.)

## Recording a new spell

1. Pick a discipline from the table in `README.md` (also see `SCHOOLS.md`
   for the full rationale behind each one).
2. Copy `TEMPLATE.md` to `spells/<domain>/<spell-name-kebab-case>.md` and
   fill it in. Delete the template's HTML comment block when done.
3. Add YAML front matter at the very top of the file (see any existing
   spell for the exact shape):

   ```yaml
   ---
   layout: spell
   title: "Your Spell Name"
   level: 3
   domain: finance
   tradition: Evocation
   ---
   ```

   `domain` must match the folder you put the file in. `tradition` must
   match that domain's entry in `_data/schools.yml` / `SCHOOLS.md`.
4. Before naming a new saving throw, stat, resource pool, or condition,
   check `MECHANICS.md` — reuse an existing one if it's a reasonable fit.
   If you've genuinely found something new, log it in `MECHANICS.md` in the
   same submission.
5. Keep it clinical: no winking asides, no "unlike other spells..."
   commentary, no narration noticing its own joke. `TEMPLATE.md` carries
   the full reasoning, if you want it.
6. Submit it for review as a pull request. An automated check confirms the
   entry is structurally sound (front matter, required stat-block fields,
   domain/school consistency) — it has no opinion on whether what you
   observed is real, funny, or advisable to have written down. That
   judgment stays with the rest of us.

## Reporting a finding without recording it properly

If you have an idea but don't have the bandwidth — there's a word we picked
up somewhere and can't seem to put back down — to draft the full entry,
open an issue using the "Spell proposal" template instead.

## Proposing a new discipline

The eight Chartered disciplines (mapped to the eight classical schools of
magic) are closed — see `SCHOOLS.md`. A Provisional discipline is still
possible, and doesn't need to map onto an existing school; open an issue
with the "New school proposal" template to discuss it with the rest of the
Working Group before drafting anything for it.

## Viewing the archive locally

The site is a plain Jekyll site. If you have Ruby installed:

```
bundle install
bundle exec jekyll serve
```

then visit `http://localhost:4000` to see how a finding actually renders
before you submit it.
