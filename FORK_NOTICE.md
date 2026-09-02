# Fork notice

This repository is a fork of **[Kyubyong/g2p](https://github.com/Kyubyong/g2p)**
by Kyubyong Park and Jongseok Kim, used under the Apache License 2.0. The
upstream `LICENSE.txt` is retained unchanged.

It is published to PyPI as **`espnet-g2p-en`**, not as `g2p_en`. The import name
is unchanged, so `import g2p_en` works either way. This is an unofficial
republication maintained by the ESPnet project. It is **not affiliated with, nor
endorsed by, the original authors**, who are named in the package metadata as
the authors of the work this is derived from.

## Why it exists

`pip install g2p_en` resolves to upstream 2.1.0 (December 2019), which asks NLTK
for the tagger resource `averaged_perceptron_tagger`. NLTK 3.8.2 renamed the
English tagger to `averaged_perceptron_tagger_eng`, so on any current NLTK the
lookup fails and `g2p_en` cannot be imported. Upstream has not released since
2019.

ESPnet declares this package in `pyproject.toml`, and PyPI refuses any
distribution whose metadata contains a direct reference such as
`g2p_en @ git+https://...`. Installing from git therefore made every ESPnet
release upload fail. Publishing the fork under its own name is what lets
`pip install espnet[tts]` work at all.

## Changes from upstream (Apache-2.0 section 4(b))

Against `Kyubyong/g2p` at `c6439c2`, the whole functional difference is two
lines in `g2p_en/g2p.py`:

```diff
-    nltk.data.find('taggers/averaged_perceptron_tagger.zip')
+    nltk.data.find('taggers/averaged_perceptron_tagger_eng.zip')
 except LookupError:
-    nltk.download('averaged_perceptron_tagger')
+    nltk.download('averaged_perceptron_tagger_eng')
```

Everything else is packaging or whitespace, and none of it changes behaviour:

| File | Change |
|---|---|
| `setup.py` | Distribution renamed to `espnet-g2p-en`; version, URLs, maintainer, NLTK floor and `long_description_content_type` set |
| `g2p_en/homographs.en` | Trailing whitespace removed from the header comment. No pronunciation data changed |
| `MANIFEST.in`, `.gitignore`, `README.md`, `README.rst` | Trailing newline / housekeeping |
| `.pre-commit-config.yaml` | Added |
| `FORK_NOTICE.md`, `.github/workflows/publish_python_package.yml` | Added |

Note on the version. Upstream's `setup.py` says `2.0.0` while PyPI serves
`2.1.0`; upstream released 2.1.0 without bumping the file. This package is
versioned `2.1.0.post1` - upstream's released 2.1.0 plus the patch above - so it
does not claim a version number in upstream's own series.

## Retirement

The one change that matters is the NLTK resource name. If upstream applies it
and releases, this package should be retired and ESPnet should depend on
`g2p_en` again.
