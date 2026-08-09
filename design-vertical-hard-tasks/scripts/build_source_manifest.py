#!/usr/bin/env python3
"""Build an UNVERIFIED source manifest with SHA-256 hashes for local files."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path, help="Local source files")
    parser.add_argument("--output", type=Path, help="Write UTF-8 JSON to this path; otherwise print")
    args = parser.parse_args()

    generated_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    attachments = []
    for index, raw_path in enumerate(args.files, 1):
        path = raw_path.expanduser().resolve()
        if not path.is_file():
            parser.error(f"Not a file: {raw_path}")
        stat = path.stat()
        attachments.append(
            {
                "id": f"A{index:02d}",
                "name": path.name,
                "kind": path.suffix.lower().lstrip("."),
                "language": "",
                "publisher": "",
                "published_at": "",
                "source_url": "",
                "local_path": str(path),
                "downloaded_at": generated_at,
                "size_bytes": stat.st_size,
                "sha256": sha256_file(path),
                "supports": [],
                "sensitive": False,
                "anonymized": False,
                "anonymization_confirmed": False,
                "english_whitelist_confirmed": False,
                "status": "UNVERIFIED",
            }
        )

    payload = {
        "generated_at": generated_at,
        "notice": "哈希仅证明本地字节；逐项阅读核验后才能将 status 改为 VERIFIED。",
        "attachments": attachments,
    }
    text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
