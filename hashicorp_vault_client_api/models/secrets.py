#!/usr/bin/env python3.9
"""HashiCorp Vault Client API -> Models -> Secrets
Copyright (C) 2021 Jerod Gawne <https://github.com/jerodg/>

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
from typing import Optional

from base_client_api.models.record import Record


class SecretOptions(Record):
    """Secret Options"""
    cas: int = 0


class CreateUpdateSecret(Record):
    """Secret -> Create/Update

    POST /kv/data/{secret_name}

    Create or update a secret."""
    options: Optional[SecretOptions]
    data: dict
    namespace: Optional[str]
    secret_name: str

    class Config:
        """MyConfig

        Pydantic configuration"""
        alias_generator = None

    @property
    def endpoint(self) -> str:
        """Endpoint

        The suffix end of the URI

        Returns:
            (str)"""
        return f'/kv/data/{self.secret_name}'

    @property
    def method(self) -> Optional[str]:
        """Method

        The HTTP verb to be used
         - Must be a valid HTTP verb as listed above in METHODS

        Returns:
            (str)"""
        return 'POST'

    @property
    def json_body(self) -> Optional[dict]:
        """Request Body"""

        return self.dict(include={'options', 'data'})
