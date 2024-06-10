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

import asyncio
from typing import Optional

import backoff
from grpc.aio import AioRpcError

from nucliadb_protos.noderesources_pb2 import (
    EmptyQuery,
    Resource,
    ResourceID,
    ShardId,
    ShardIds,
)
from nucliadb_protos.nodewriter_pb2 import IndexMessage, OpStatus
from nucliadb_protos.nodewriter_pb2_grpc import NodeWriterStub
from nucliadb_sidecar import SERVICE_NAME
from nucliadb_utils.grpc import get_traced_grpc_channel


class Writer:
    _stub: Optional[NodeWriterStub] = None
    lock: asyncio.Lock

    def __init__(self, grpc_writer_address: str):
        self.lock = asyncio.Lock()
        self.channel = get_traced_grpc_channel(grpc_writer_address, SERVICE_NAME, max_send_message=250)
        self.stub = NodeWriterStub(self.channel)

    async def set_resource(self, pb: Resource) -> OpStatus:
        return await self.stub.SetResource(pb)  # type: ignore

    async def set_resource_from_storage(self, pb: IndexMessage) -> OpStatus:
        return await self.stub.SetResourceFromStorage(pb)  # type: ignore

    async def delete_resource(self, pb: ResourceID) -> OpStatus:
        return await self.stub.RemoveResource(pb)  # type: ignore

    async def garbage_collector(self, shard_id: str):
        return await self.stub.GC(ShardId(id=shard_id))  # type: ignore

    @backoff.on_exception(backoff.expo, (AioRpcError,), jitter=backoff.random_jitter, max_tries=4)
    async def shards(self) -> ShardIds:
        pb = EmptyQuery()
        return await self.stub.ListShards(pb)  # type: ignore

    async def close(self):
        await self.channel.close()
