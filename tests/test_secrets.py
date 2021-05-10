#!/usr/bin/env python3.8
"""HashiCorp Vault Client API -> Tests -> Auth
Copyright © 2019-2021 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>."""
import time
from os import getenv

import pytest
from base_client_api.models.results import Results
from base_client_api.utils import bprint, tprint
from devtools import debug

from hashicorp_vault_client_api.models.secrets import CreateUpdateSecret, SecretData
from hashicorp_vault_client_api.vault_client import VaultClient


# logger.enable('base_client_api')  # debug


@pytest.mark.asyncio
async def test_secrets_create_update():
    ts = time.perf_counter()
    bprint('Test: Secrets Create/Update', 'top')

    async with VaultClient(cfg=f'{getenv("CFG_HOME")}/hashicorp_vault_test.toml') as vc:
        model = CreateUpdateSecret(
                data=SecretData(secret_name='client-temp',
                                key='je1234-eclient',
                                value='1260094080553879',
                                path='je1234/unbound/sandbox'  # {cmdb}/unbound/{partition}
                                ))

        debug(model)
        debug(model.endpoint)
        debug(model.parameters)
        debug(model.json_body)
        debug(model.dict())

        debug(vc.cfg)
        debug(vc.header)
        results = await vc.make_request(models=model)
        debug(results)
        debug(vc.cfg)
        debug(vc.header)

        assert type(results) is Results
        assert results.success is not None
        assert not results.failure

        tprint(results, top=5)

    bprint(f'Completed in {(time.perf_counter() - ts):f} seconds.', 'bottom')
