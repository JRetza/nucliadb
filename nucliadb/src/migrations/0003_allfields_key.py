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
#
from typing import Optional

from nucliadb.common import datamanagers
from nucliadb.migrator.context import ExecutionContext
from nucliadb.migrator.migrator import logger
from nucliadb_protos.resources_pb2 import AllFieldIDs, FieldID


async def migrate(context: ExecutionContext) -> None: ...


async def migrate_kb(context: ExecutionContext, kbid: str) -> None:
    async for resource_id in datamanagers.resources.iterate_resource_ids(kbid=kbid):
        async with context.kv_driver.transaction() as txn:
            resource = await datamanagers.resources.get_resource(txn, kbid=kbid, rid=resource_id)
            if resource is None:
                logger.warning(f"kb={kbid} rid={resource_id}: resource not found. Skipping...")
                continue

            all_fields: Optional[AllFieldIDs] = await resource.get_all_field_ids(for_update=True)
            if all_fields is not None:
                logger.warning(f"kb={kbid} rid={resource_id}: already has all fields key. Skipping...")
                continue

            # Migrate resource
            logger.warning(f"kb={kbid} rid={resource_id}: migrating...")
            all_fields = AllFieldIDs()
            async for (
                field_type,
                field_id,
            ) in resource._deprecated_scan_fields_ids():
                fid = FieldID(field_type=field_type, field=field_id)
                all_fields.fields.append(fid)
            await resource.set_all_field_ids(all_fields)
            await txn.commit()
