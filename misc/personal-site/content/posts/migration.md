---
title: "Github Migration (Short)"
author: 'Angus Jellis'
date: 2022-01-03
tags: ["Short"]
---

## Summary

Our legacy SCM system had been in use since ~2015. Five years' worth of technical debt had built up (in terms of usrs, permissions, dependencies, naming conventions, etc). 

I was given the task of planning and implementing our migration to GitHub.

Our old system was an absolutely critical system that supported the entirety of KPMG's Engineering function, with around 600 users, and £millions of revenue dependent upon it.

There were around 3200 repos on the legacy system.

## What was my role?

- Acted as technical lead and project lead
- Spearheaded communications with end users
- Built majority of the KPMG specific migration tooling (3366 lines of code in total, not that number of lines is a sign of quality.....)
- Handled comms with critical business reps
- Trained up other members of the team on the migration tooling as well, delegated actual migrations to them


## What do you think went well?

- Communications with end users
- Taking on board user feedback
- Automation of toil
- Reliability of system
- Minimal end user impact
- Notifications on dependencies

## What do you think could have gone better?

- Should have tested vendor-provided tools earlier on
- Difficulty properly tracking migration (especially at start)
- Overengineered some bits, by writing scripts that never got used
- Reacted to scope creep by constantly pushing deadlines back!

## What do you wish you had looked into/had?

- Could have automated even more
- Would have been great to make self service (links with automation)
- Move out of our local machines

## What lessons did you learn?

- Importance of a dynamic database for migrations on this large a scale
- Automation reduces need for domain knowledge
- Communication with users key to minimising incorrect assumptions, and coming up with better ideas
- Rate limiting (what it is, why it's important), and need for optimisation of large scale software
- Never trust a vendor's promises on what their software can do...