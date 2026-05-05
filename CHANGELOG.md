# Changelog

Since we follow
[Conventional Commits](https://decisions.seedcase-project.org/why-conventional-commits/)
when writing commit messages, we're able to automatically create formal
releases of the Python package based on the commit messages. The
releases are also published to Zenodo for easier discovery, archival,
and citation purposes. We use
[Commitizen](https://decisions.seedcase-project.org/why-semantic-release-with-commitizen/)
to be able to automatically create these releases, which uses
[SemVar](https://semverdoc.org) as the version numbering scheme.

Because releases are created based on commit messages, we release quite
often, sometimes several times in a day. This also means that any
individual release will not have many changes within it. Below is a list
of the releases we've made so far, along with what was changed within
each release.

## 0.13.0 (2026-05-04)

## 0.12.0 (2026-04-30)

### Feat

- ✨ beautify CLI output in docs (#31)

## 0.11.0 (2026-04-24)

### Feat

- ✨ add possibility to return example path (#29)

## 0.10.0 (2026-04-24)

### Feat

- ✨ improve example I/O syntax (#26)

## 0.9.0 (2026-04-23)

### Feat

- ✨ add woolly example package (#28)

## 0.8.0 (2026-04-23)

### Feat

- ✨ add `write_properties()` (#27)

## 0.7.1 (2026-04-21)

### Fix

- 🐛 export example name enum (#25)

## 0.7.0 (2026-04-20)

### Feat

- ✨ allow config file to be optional (#23)

## 0.6.0 (2026-04-17)

### Feat

- ✨ `read_example_datapackage()` and (re)organize examples (#15)

## 0.5.1 (2026-04-17)

### Refactor

- ♻️ use descriptive return type (#21)

## 0.5.0 (2026-04-15)

### Feat

- ✨ add example datapackage jsons (#10)

## 0.4.0 (2026-04-14)

### Feat

- :sparkles: add functional helpers (#9)

## 0.3.0 (2026-04-13)

### Feat

- ✨ add `parse_source()` and `read_properties()` (#8)

## 0.2.0 (2026-04-07)

### Feat

- :sparkles: add CLI beautification functionality (#5)
