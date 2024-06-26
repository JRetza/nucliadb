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
import os

import pytest
from pytest_lazy_fixtures import lazy_fixture


@pytest.fixture(scope="function")
def onprem_nucliadb():
    from nucliadb_utils.settings import nuclia_settings

    original = nuclia_settings.onprem
    nuclia_settings.onprem = True
    yield
    nuclia_settings.onprem = original


@pytest.fixture(scope="function")
def hosted_nucliadb():
    from nucliadb_utils.settings import nuclia_settings

    original = nuclia_settings.onprem
    nuclia_settings.onprem = False
    yield
    nuclia_settings.onprem = original


def get_testing_storage_backend(default="gcs"):
    return os.environ.get("TESTING_STORAGE_BACKEND", default)


def lazy_storage_fixture():
    backend = get_testing_storage_backend()
    if backend == "gcs":
        return [lazy_fixture.lf("gcs_storage")]
    elif backend == "s3":
        return [lazy_fixture.lf("s3_storage")]
    elif backend == "local":
        return [lazy_fixture.lf("local_storage")]
    else:
        print(f"Unknown storage backend {backend}, using gcs")
        return [lazy_fixture.lf("gcs_storage")]


@pytest.fixture(scope="function", params=lazy_storage_fixture())
async def storage(request):
    """
    Generic storage fixture that allows us to run the same tests for different storage backends.
    """
    return request.param
