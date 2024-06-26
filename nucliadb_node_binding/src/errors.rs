// Copyright (C) 2021 Bosutech XXI S.L.
//
// nucliadb is offered under the AGPL v3.0 and as commercial software.
// For commercial licensing, contact us at info@nuclia.com.
//
// AGPL:
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Affero General Public License as
// published by the Free Software Foundation, either version 3 of the
// License, or (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU Affero General Public License for more details.
//
// You should have received a copy of the GNU Affero General Public License
// along with this program. If not, see <http://www.gnu.org/licenses/>.

use nucliadb_core::protos::{op_status, OpStatus};
use prost::Message;
use pyo3::create_exception;
use pyo3::exceptions::PyException;
use pyo3::prelude::Python;
use pyo3::types::PyList;

// Base exception for all custom errors produced by this library
create_exception!(nucliadb_node_binding, IndexNodeException, PyException);

create_exception!(nucliadb_node_binding, LoadShardError, IndexNodeException);
create_exception!(nucliadb_node_binding, ShardNotFound, IndexNodeException);

pub fn op_status_error(py: Python<'_>, msg: impl Into<String>) -> &PyList {
    PyList::new(
        py,
        OpStatus {
            status: op_status::Status::Error.into(),
            detail: msg.into(),
            ..Default::default()
        }
        .encode_to_vec(),
    )
}
