# Copyright (C) 2021 Bosutech XXI S.L.
#
# nucliadb is offered under the AGPL v3.0 and as commercial software.
# For commercial licensing, contact us at info@nuclia.com.
#
# AGPL:
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import argparse

from kb_admin import KBNotFoundError, KnowledgeBoxAdmin

INGEST_GRPC_PORT = 8030
API_HTTP_PORT = 8080
TRAIN_GRPC_PORT = 8080
INTERNAL_SERVICES = {
    "writer": "writer.nucliadb.svc.cluster.local",
    "search": "search.nucliadb.svc.cluster.local",
    "reader": "reader.nucliadb.svc.cluster.local",
    "train": "train.nucliadb.svc.cluster.local",
    "ingest": "ingest.nucliadb.svc.cluster.local",
}
KB_BATCH_SIZE = 10


def parse_arguments():
    parser = argparse.ArgumentParser(description="Script to fix production indexes")
    parser.add_argument("--kb", dest="kbid", required=False, help="KB uuid")
    parser.add_argument(
        "--offset", default=0, type=int, help="KB offset for reruns after an error"
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--local", action="store_true")
    args = parser.parse_args()
    return args


def fix_it(kbadmin: KnowledgeBoxAdmin):
    kbadmin.clean_index()
    kbadmin.reprocess(args.offset)


def main(args):
    if args.local:
        # When running against local nucliadb (not the docker version)
        kbadmin = KnowledgeBoxAdmin(
            host="0.0.0.0",
            grpc=8030,
            http=8080,
            train_port=8040,
            dry_run=args.dry_run,
        )
    else:
        # When running directly against the cluster services
        kbadmin = KnowledgeBoxAdmin(
            host=INTERNAL_SERVICES["ingest"],
            grpc=INGEST_GRPC_PORT,
            http=API_HTTP_PORT,
            train_port=TRAIN_GRPC_PORT,
            reader_host=INTERNAL_SERVICES["reader"],
            writer_host=INTERNAL_SERVICES["writer"],
            search_host=INTERNAL_SERVICES["search"],
            train_host=INTERNAL_SERVICES["train"],
            grpc_host=INTERNAL_SERVICES["ingest"],
            dry_run=args.dry_run,
        )
    if args.kbid:
        offset = 0
        to_fix = [args.kbid]
    else:
        offset = args.offset
        all_kbs = kbadmin.client.list_kbs(timeout=10)
        print(f"Found {len(all_kbs)} kbs!")
        to_fix = [kb.kbid for kb in all_kbs][offset : offset + KB_BATCH_SIZE]

    print(f"Fixing {len(to_fix)} kbs:")
    next_offset = offset
    for index, kbid in enumerate(to_fix):
        try:
            kb = kbadmin.set_kb(kbid)
        except KBNotFoundError:
            print(f"KB not found. Moving on...")
            continue

        next_offset = index + offset + 1
        print(f" - {next_offset}: Fixing KB(slug={kb.slug}, kbid={kb.kbid})...")
        fix_it(kbadmin)

    if args.kbid:
        print("Finished fixing kb!")
    else:
        if next_offset >= len(all_kbs):
            print("Finished fixing all kbs!")
        else:
            print(
                f"To continue with next batch, use --offset={next_offset} to continue with next batch"
            )


if __name__ == "__main__":
    args = parse_arguments()
    main(args)