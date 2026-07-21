# AGENTS.md — Working Rules for This Workspace

<!-- Rename this file to AGENTS.md (Cursor) or CLAUDE.md (Claude Code). It is read
     automatically at the start of every agent session. Edit it freely: it should
     describe how THIS workspace works, in the owner's words. -->

## Who works here

[Name], EY Climate practice. This workspace is for [purpose — e.g., learning agentic
working methods / building internal training materials]. No EY client data, no
client names, no EY-confidential material, and no credentials of any kind belong in
this folder or in any prompt.

## How this workspace is organized

- `reference/` — how-we-work knowledge: methods, templates, voice. Read before big tasks.
- `work/` — active builds. Outputs are files, written here, versioned.
- `archive/` — finished or superseded work. Don't read unless asked.

## Standing instructions

1. Read this file and skim `reference/` before the first substantive task of a session.
2. Outputs are files on disk, not chat messages. Prefer HTML for polished deliverables,
   markdown for working documents.
3. Whenever you create an HTML file, open it in the browser without being asked.
4. Version drafts with `-v1`, `-v2` suffixes. Never silently overwrite prior versions.
5. When a piece of work goes well, propose a reference file capturing the method.
   When something goes wrong, propose the fix as an edit to a reference file so it
   never happens again.
6. When a number matters, compute it with code you write and save — never estimate it
   from memory. Say which you did.
7. At the end of a working session, write a short log to `sessions/YYYY-MM-DD-topic.md`:
   what was decided, what was built, what's open.
8. If asked to do something conflicting with the data rules above, refuse and say why.
