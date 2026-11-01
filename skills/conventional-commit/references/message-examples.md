# Message examples

Calibration for the grammar and compatibility rules in [SKILL.md](../SKILL.md).

## Subjects

| Weak | Strong |
| --- | --- |
| "fixed stuff" | "fix(export): preserve filters across paginated queries" |
| "Update README" | "docs: document the retry budget in the CLI reference" |
| "feat: add sorting, fix the date bug, and bump deps" | split into three commits by intent |
| "fix bug as discussed in turn 2" | "fix(auth): retry token exchange on connection reset" |
| "feat(misc): handle disconnect" | "feat(transport): handle abrupt peer disconnects" |

A subject names one coherent change, uses the imperative, and has no trailing period.

## Body

Atomic, self-explanatory commits may omit the body:

```text
docs(readme): correct repository clone URL
```

When any mandatory trigger applies, write a body explaining the problem, the rejected alternatives, and invariants. Do not narrate the sequence of edits, restate the diff, or include agent session leakage.

### Non-obvious trade-offs and root causes

Weak (diff restatement and session leakage):

```text
fix(cache): update cache invalidation logic

In this commit, I updated cache.ts to add an expiration check inside
read() and deleted the key. Also resolved the user review comments.
```

Strong (problem condition, rejected alternative, trade-off):

```text
fix(cache): invalidate expired entries lazily during read

Under concurrent write bursts, the background sweeper lagged behind TTL
expiration, serving stale entries to concurrent readers.

Evicting expired entries inline upon read guarantees read freshness.
A global synchronous sweep was rejected because lock contention on the
hot path degraded p99 read latency by 4x.
```

### Invariants and red lines

Document non-local constraints so future maintainers reading `git blame` do not re-introduce the failure:

```text
refactor(worker): release pool mutex before dispatching completion

Acquiring the queue notification mutex while holding the worker pool
lock inverted lock acquisition ordering with consumer threads, causing
sporadic deadlocks under pipeline saturation.

Explicitly drop pool_lock before dispatching completion signals.
Future changes must preserve this ordering: never emit queue signals
while holding pool-level mutexes.
```

## Breaking changes

Mark a breaking contract with `!` or an uppercase `BREAKING CHANGE:` footer, and explain the migration.

```text
feat(api)!: rename the session cursor field

BREAKING CHANGE: cursor_id is now cursorId. Update clients that read
the field by name.
```

## Footers

Use trailer forms such as `Refs: #123` or `Fixes #123`; hyphenate multiword tokens except `BREAKING CHANGE`. Include only real references and attribution.

## Splitting

Split by intent when it improves review or reversal, not merely because files differ. Implementation, tests, and their documentation may share one commit; independent changes should not.
