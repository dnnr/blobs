# Sketch/WiP for BLoBS: The Big List of Backup Software

## List of criteria

* **Deduplication:** Globally for all backups? Locally with backups? On chunk-level or file-level?
* **Compression:** Choice of algorithms?
* **Access/restore semantics:** Individual file history (like boxbackup)? Full snapshot (like duplicity)? What else?
* **Lifecycle Mechanics:**
  * Individual file deletion possible?
  * Methods of backup deletion:
    * Random access with user discretion (like zbackup)?
    * Autonomous heuristic based on quota/available space (like boxbackup)?
    * Constrained by incrementals (like duplicity)?
* **Secrecy:** Zero-knowledge server yes/no? Metadata protected/exposed?
* **Scope:** User-wide, system-wide, both?
* **Privileges:** Needs root privileges yes/no?
* **Authorization (server on client):** If pulling, server needs/doesn't need (root) shell access on client? Maybe doesn't apply because only pull semantics offered?
* **Authorization (client on server):** If pushing, client needs/doesn't need shell access on server? Maybe doesn't apply because only push semantics offered?
* **Push or Pull:** Push? Pull? Both?
* **Access protocol / server requirements:** Proprietary, requires server process? Generic access protocols, which ones? Left to be defined by lower layers (ie., fuse mounts, etc.)?
* **Encryption:** Which methods/algos?
* **Integrity (server-side):** Data corruption on server mitigated?
* **Integrity (client-side):** Malicious data corruption by compromised client mitigated?
* **Bandwidth efficiency:** Only transfers what needs to be transferred?
* **Storage efficiency (client):** Doesn't consume unreasonably amounts of storage on client?
* **Storage efficiency (server):** (should actually be addressed by Deduplication criterion)
* **File Operation Handling:** Deduplicates across renames?
* **IO efficiency:** Fast incremental backups (by what kind of measurement)?
* **Scalability:** Any upper/lower bounds regarding deployment? Maybe too complex for a single host?
* **Preservation:** POSIX permissions? xattr? Hardlinks? Device nodes?
* **Project health:** Unmaintained? Finished but dead? Alive and well?
* **File selection:** Supports flexible include/exclude lists? CACHEDIR.TAG detection?
* **Browsing:** FUSE? Listing? Is it efficient?
* **Representation of disk usage:** Whether or not it is possible to see the amount of space consumed by each backup and backed up file without disregarding the deduplication (for example: a FUSE mount using hardlinks to indicate at least identical files?) Not sure if this is actually solvable.

## Shortlist of systems to classify

* duplicity
* boxbackup
* rsnapshot
* obnam
* bup
* attic
* restic
* zbackup
