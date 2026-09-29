# Changelog

Since we follow [Conventional
Commits](https://decisions.seedcase-project.org/why-conventional-commits/) for
commit messages, we can automatically create releases of the Python package
based on those messages. The releases are also published to Zenodo for easier
discovery, archiving, and citation.

We use
[Cocogitto](https://decisions.seedcase-project.org/why-semantic-release-with-cocogitto/)
to automate releases, which uses [SemVar](https://semverdoc.org) as the version
numbering scheme, and [Git
Cliff](https://decisions.seedcase-project.org/why-changelog-with-git-cliff/) to
generate the changelog from commit messages.

Because releases are generated automatically, new versions are released
often---sometimes several times in a day--- and each release usually contains
only a small number of changes. Below is a list of the releases and the changes
within each one.

Commits from bots, like `dependabot` or `pre-commit-ci`, are not included in the
changelog. ##
[0.16.1](https://github.com/seedcase-project/seedcase-soil/compare/0.16.0..0.16.1) -
2026-09-25

### ♻️ Refactor

- Add trailing newline when writing JSON
  [#122](https://github.com/seedcase-project/seedcase-soil/pull/122) by
  [`@martonvago`](https://github.com/martonvago)
  ([fcb24bf](https://github.com/seedcase-project/seedcase-soil/commit/fcb24bf3a4623689ba39769b5afcba9bee3bf3da))

### 📝 Documentation

- Update docs from template
  [#82](https://github.com/seedcase-project/seedcase-soil/pull/82) by
  [`@signekb`](https://github.com/signekb)
  ([a9ba83d](https://github.com/seedcase-project/seedcase-soil/commit/a9ba83d6f41f904b26c86436ca2c6c6030d0fd46))
- Format docstrings
  [#96](https://github.com/seedcase-project/seedcase-soil/pull/96) by
  [`@signekb`](https://github.com/signekb)
  ([5fdcfc9](https://github.com/seedcase-project/seedcase-soil/commit/5fdcfc9a275bdb269fa7fbb02244dc170a262aea))
- Add guidebook link to CONTRIBUTING
  [#103](https://github.com/seedcase-project/seedcase-soil/pull/103) by
  [`@signekb`](https://github.com/signekb)
  ([e01665d](https://github.com/seedcase-project/seedcase-soil/commit/e01665de6f92fbb849b35ace858cdcd92b0fde01))

### 💄 Style

- Update Quarto theme
  [#59](https://github.com/seedcase-project/seedcase-soil/pull/59) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([3c6796f](https://github.com/seedcase-project/seedcase-soil/commit/3c6796ffd7a0e4b7e466fc0bb4242cad60c32882))
- Fix Ruff and Pyrefly errors
  [#95](https://github.com/seedcase-project/seedcase-soil/pull/95) by
  [`@signekb`](https://github.com/signekb)
  ([6a8e9e3](https://github.com/seedcase-project/seedcase-soil/commit/6a8e9e334258df859b34dd272fd9c6b248a99921))
- Format `.md`
  [#105](https://github.com/seedcase-project/seedcase-soil/pull/105) by
  [`@signekb`](https://github.com/signekb)
  ([a2e99a2](https://github.com/seedcase-project/seedcase-soil/commit/a2e99a2edca1ace3390b180e32855727373dbaf2))
- Fix indents and newlines in `.yml` and `.toml`
  [#104](https://github.com/seedcase-project/seedcase-soil/pull/104) by
  [`@signekb`](https://github.com/signekb)
  ([a7b7457](https://github.com/seedcase-project/seedcase-soil/commit/a7b74574157201143d2c673e5d5b0b337b613e44))

### 👷 CI/CD

- Update GitHub workflows from template
  [#79](https://github.com/seedcase-project/seedcase-soil/pull/79) by
  [`@signekb`](https://github.com/signekb)
  ([cc6b228](https://github.com/seedcase-project/seedcase-soil/commit/cc6b228ff897bd9d94f949827caa55495257b79e))
- Move `--config` flag forward in release workflow
  [#100](https://github.com/seedcase-project/seedcase-soil/pull/100) by
  [`@signekb`](https://github.com/signekb)
  ([b8bdb31](https://github.com/seedcase-project/seedcase-soil/commit/b8bdb317dc0fada8cf5e7fa3e76c585add40dfab))
- Only run checks workflow in PRs
  [#106](https://github.com/seedcase-project/seedcase-soil/pull/106) by
  [`@signekb`](https://github.com/signekb)
  ([5e5b2ff](https://github.com/seedcase-project/seedcase-soil/commit/5e5b2ffba14995b196f7f1c382cf8c84e946810c))

### 🧱 Build system

- Update `uv.lock` to resolve security notices
  [#58](https://github.com/seedcase-project/seedcase-soil/pull/58) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([4f64b2b](https://github.com/seedcase-project/seedcase-soil/commit/4f64b2ba80dd22997dd268600d650a28a8ad24d9))
- Rename quartodoc renderer to `quartodoc_style`
  [#94](https://github.com/seedcase-project/seedcase-soil/pull/94) by
  [`@signekb`](https://github.com/signekb)
  ([4389a76](https://github.com/seedcase-project/seedcase-soil/commit/4389a76f1b555af30376049295c457c566faf71b))
- Remove Commitizen from pre-commit
  [#99](https://github.com/seedcase-project/seedcase-soil/pull/99) by
  [`@signekb`](https://github.com/signekb)
  ([3856a92](https://github.com/seedcase-project/seedcase-soil/commit/3856a92470c8bd0c17cb085f5fd2d86e0ef20024))

### 🧹 Chores

- Update website navbar
  [#77](https://github.com/seedcase-project/seedcase-soil/pull/77) by
  [`@signekb`](https://github.com/signekb)
  ([2c1e67d](https://github.com/seedcase-project/seedcase-soil/commit/2c1e67dd56526d178484d98d8b82a915c3aa3123))
- Update configuration files from template
  [#80](https://github.com/seedcase-project/seedcase-soil/pull/80) by
  [`@signekb`](https://github.com/signekb)
  ([2d6531b](https://github.com/seedcase-project/seedcase-soil/commit/2d6531ba9937ddb2641382c3704a2b0bdc886bdc))
- Update VScode settings and recommended extensions from template
  [#92](https://github.com/seedcase-project/seedcase-soil/pull/92) by
  [`@signekb`](https://github.com/signekb)
  ([be4984b](https://github.com/seedcase-project/seedcase-soil/commit/be4984b31ddb9d7412f5896d01668c5a40b8ad85))
- Update tools from template
  [#93](https://github.com/seedcase-project/seedcase-soil/pull/93) by
  [`@signekb`](https://github.com/signekb)
  ([000ec6e](https://github.com/seedcase-project/seedcase-soil/commit/000ec6ebe960ac4be2c69f3a576a3500520e4aaa))
- Update justfile from template
  [#97](https://github.com/seedcase-project/seedcase-soil/pull/97) by
  [`@signekb`](https://github.com/signekb)
  ([125ccae](https://github.com/seedcase-project/seedcase-soil/commit/125ccaefe0ecc6564e3fd3aac09f44bf8a7efb68))
- Update `just list-todos` to include hidden files and exclude more dirs
  [#101](https://github.com/seedcase-project/seedcase-soil/pull/101) by
  [`@signekb`](https://github.com/signekb)
  ([6dcbe24](https://github.com/seedcase-project/seedcase-soil/commit/6dcbe24c2d7020b8cdffee2f4afc2c6accf1c7c9))
- Update CODEOWNERS to be the platform-tools team
  [#102](https://github.com/seedcase-project/seedcase-soil/pull/102) by
  [`@signekb`](https://github.com/signekb)
  ([e365e16](https://github.com/seedcase-project/seedcase-soil/commit/e365e16cf29577de0720dcdadece8870219f20e5))

### ❤️ New contributors

- [`@martonvago`](https://github.com/martonvago) made their first contribution
  in [#122](https://github.com/seedcase-project/seedcase-soil/pull/122) ##
  [0.16.0](https://github.com/seedcase-project/seedcase-soil/compare/0.15.0..0.16.0) -
  2026-06-10

### ✨ Features

- Add enum constraints to flora
  [#54](https://github.com/seedcase-project/seedcase-soil/pull/54) by
  [`@joelostblom`](https://github.com/joelostblom)
  ([7ca5a22](https://github.com/seedcase-project/seedcase-soil/commit/7ca5a2226cdeab81047db81b0aa4ed72566ee26b))

## [0.14.0](https://github.com/seedcase-project/seedcase-soil/compare/0.13.0..0.14.0) - 2026-05-06

### ✨ Features

- Add `file_tree()`
  [#39](https://github.com/seedcase-project/seedcase-soil/pull/39) by
  [`@signekb`](https://github.com/signekb)
  ([8c97fb7](https://github.com/seedcase-project/seedcase-soil/commit/8c97fb7ad586625160565ac932dc28e27303e98f))

## [0.12.0](https://github.com/seedcase-project/seedcase-soil/compare/0.11.0..0.12.0) - 2026-04-30

### ✨ Features

- Beautify CLI output in docs
  [#31](https://github.com/seedcase-project/seedcase-soil/pull/31) by
  [`@joelostblom`](https://github.com/joelostblom)
  ([cd2c343](https://github.com/seedcase-project/seedcase-soil/commit/cd2c343a65ffb41b1b39a019e00f2d7b00afab68))

### 🧹 Chores

- Update Quarto theme
  [#32](https://github.com/seedcase-project/seedcase-soil/pull/32) by
  [`@joelostblom`](https://github.com/joelostblom)
  ([19b3568](https://github.com/seedcase-project/seedcase-soil/commit/19b3568a7946a382ad4d6acd8d3b26d16423c5e8))

## [0.11.0](https://github.com/seedcase-project/seedcase-soil/compare/0.10.0..0.11.0) - 2026-04-24

### ✨ Features

- Add possibility to return example path
  [#29](https://github.com/seedcase-project/seedcase-soil/pull/29) by
  [`@joelostblom`](https://github.com/joelostblom)
  ([a15477b](https://github.com/seedcase-project/seedcase-soil/commit/a15477bbd0bbb1135f334a58870410f789fc776b))

## [0.10.0](https://github.com/seedcase-project/seedcase-soil/compare/0.9.0..0.10.0) - 2026-04-24

### ✨ Features

- Improve example I/O syntax
  [#26](https://github.com/seedcase-project/seedcase-soil/pull/26) by
  [`@joelostblom`](https://github.com/joelostblom)
  ([71967d1](https://github.com/seedcase-project/seedcase-soil/commit/71967d19cdedfb5a777d26b5858a2f26e2cf2000))

## [0.9.0](https://github.com/seedcase-project/seedcase-soil/compare/0.8.0..0.9.0) - 2026-04-23

### ✨ Features

- Add woolly example package
  [#28](https://github.com/seedcase-project/seedcase-soil/pull/28) by
  [`@joelostblom`](https://github.com/joelostblom)
  ([fea7480](https://github.com/seedcase-project/seedcase-soil/commit/fea7480fbb14f81dc46b2f74fecab4e5bf30bf7e))

## [0.8.0](https://github.com/seedcase-project/seedcase-soil/compare/0.7.1..0.8.0) - 2026-04-23

### ✨ Features

- Add `write_properties()`
  [#27](https://github.com/seedcase-project/seedcase-soil/pull/27) by
  [`@joelostblom`](https://github.com/joelostblom)
  ([2c83ae2](https://github.com/seedcase-project/seedcase-soil/commit/2c83ae2247bc0b5d2f038f67d2799c8dbbb67de5))

## [0.7.1](https://github.com/seedcase-project/seedcase-soil/compare/0.7.0..0.7.1) - 2026-04-21

### 🐛 Fixes

- Export example name enum
  [#25](https://github.com/seedcase-project/seedcase-soil/pull/25) by
  [`@joelostblom`](https://github.com/joelostblom)
  ([bc9c3ad](https://github.com/seedcase-project/seedcase-soil/commit/bc9c3ad6558565e12f8859b201a2d8e66709a3bf))

### ❤️ New contributors

- `@pre-commit-ci[bot]` started making automated contributions ##
  [0.7.0](https://github.com/seedcase-project/seedcase-soil/compare/0.6.0..0.7.0) -
  2026-04-20

### ✨ Features

- Allow config file to be optional
  [#23](https://github.com/seedcase-project/seedcase-soil/pull/23) by
  [`@joelostblom`](https://github.com/joelostblom)
  ([11029c9](https://github.com/seedcase-project/seedcase-soil/commit/11029c9e4b7d3a7108ee5f878dfe6327ab71afe1))

### 📝 Documentation

- Add PyPI badge after officially publishing
  [#22](https://github.com/seedcase-project/seedcase-soil/pull/22) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([6a747c9](https://github.com/seedcase-project/seedcase-soil/commit/6a747c9cc608ce26bfd52fd9d9195facd93aee22))

## [0.6.0](https://github.com/seedcase-project/seedcase-soil/compare/0.5.1..0.6.0) - 2026-04-17

### ✨ Features

- `read_example_datapackage()` and (re)organize examples
  [#15](https://github.com/seedcase-project/seedcase-soil/pull/15) by
  [`@joelostblom`](https://github.com/joelostblom)
  ([1d5d5e5](https://github.com/seedcase-project/seedcase-soil/commit/1d5d5e581122c846fe241059739e8c29a8370e93))

## [0.5.1](https://github.com/seedcase-project/seedcase-soil/compare/0.5.0..0.5.1) - 2026-04-17

### ♻️ Refactor

- Use descriptive return type
  [#21](https://github.com/seedcase-project/seedcase-soil/pull/21) by
  [`@joelostblom`](https://github.com/joelostblom)
  ([f74e12e](https://github.com/seedcase-project/seedcase-soil/commit/f74e12e10ec8293311dcc83dfe93ea94e3a02a2f))

### 📝 Documentation

- Update `CITATION.cff` file
  [#19](https://github.com/seedcase-project/seedcase-soil/pull/19) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([06ebfec](https://github.com/seedcase-project/seedcase-soil/commit/06ebfec220cb4307810a3c0f6df1a4dec6db5adb))

### 🧱 Build system

- Update pre-commit hook versions
  [#17](https://github.com/seedcase-project/seedcase-soil/pull/17) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([0951bd9](https://github.com/seedcase-project/seedcase-soil/commit/0951bd9a1cfeb2233fc4df7b39cd8b978c2b659a))
- Ignore `tests/` files for URL checker
  [#18](https://github.com/seedcase-project/seedcase-soil/pull/18) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([07b9568](https://github.com/seedcase-project/seedcase-soil/commit/07b95686cf43b5fc4608860a5f94501ea36146ea))
- Setup files to build the website
  [#16](https://github.com/seedcase-project/seedcase-soil/pull/16) by
  [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([6aa329d](https://github.com/seedcase-project/seedcase-soil/commit/6aa329d840c5b13aa88a7e52528d080d1008be1e))

## [0.5.0](https://github.com/seedcase-project/seedcase-soil/compare/0.4.0..0.5.0) - 2026-04-15

### ✨ Features

- Add example datapackage jsons
  [#10](https://github.com/seedcase-project/seedcase-soil/pull/10) by
  [`@signekb`](https://github.com/signekb)
  ([e6ec95b](https://github.com/seedcase-project/seedcase-soil/commit/e6ec95b09862a9a6e511e0e5871909538b127170))

### ❤️ New contributors

- [`@signekb`](https://github.com/signekb) made their first contribution in
  [#10](https://github.com/seedcase-project/seedcase-soil/pull/10) ##
  [0.4.0](https://github.com/seedcase-project/seedcase-soil/compare/0.3.0..0.4.0) -
  2026-04-14

### ✨ Features

- Add functional helpers
  [#9](https://github.com/seedcase-project/seedcase-soil/pull/9) by
  [`@joelostblom`](https://github.com/joelostblom)
  ([483159b](https://github.com/seedcase-project/seedcase-soil/commit/483159bd75eff03605dac187ef7ccf7ea75cd876))

## [0.3.0](https://github.com/seedcase-project/seedcase-soil/compare/0.2.0..0.3.0) - 2026-04-13

### ✨ Features

- Add `parse_source()` and `read_properties()`
  [#8](https://github.com/seedcase-project/seedcase-soil/pull/8) by
  [`@joelostblom`](https://github.com/joelostblom)
  ([1a1557a](https://github.com/seedcase-project/seedcase-soil/commit/1a1557a99be5a957223d70fbff82a10b8bdfc8cd))

## [0.2.0] - 2026-04-07

### ✨ Features

- Add CLI beautification functionality
  [#5](https://github.com/seedcase-project/seedcase-soil/pull/5) by
  [`@joelostblom`](https://github.com/joelostblom)
  ([7a9d510](https://github.com/seedcase-project/seedcase-soil/commit/7a9d510dfe773b4325bb0fa111ec7d25c68481ee))

### 🧹 Chores

- Start of package by [`@lwjohnst86`](https://github.com/lwjohnst86)
  ([2e4df9f](https://github.com/seedcase-project/seedcase-soil/commit/2e4df9f120f8a8f8e39b8264c9492bcb02a91ce9))

### ❤️ New contributors

- `@github-actions[bot]` started making automated contributions

- [`@joelostblom`](https://github.com/joelostblom) made their first contribution
  in [#5](https://github.com/seedcase-project/seedcase-soil/pull/5)

- `@dependabot[bot]` started making automated contributions

- [`@lwjohnst86`](https://github.com/lwjohnst86) made their first contribution
