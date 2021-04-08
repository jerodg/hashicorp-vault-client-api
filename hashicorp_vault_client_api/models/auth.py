#!/usr/bin/env python3.8
"""HashiCorp Vault Client API -> Models -> Auth
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


class AuthAppRole(Record):
    """Authorization -> App Role

    POST /auth/approle/login

    Login using approle credentials"""
    namespace: Optional[str]
    secret_store: str = 'kv'
    role_id: Optional[str]
    secret_id: Optional[str]

    class Config:
        """Pydantic configuration

        Required because the api doesn't conform to JSON spec."""
        alias_generator = None

    @property
    def endpoint(self) -> str:
        """Endpoint

        The suffix end of the URI

        Returns:
            (str)"""
        return '/auth/approle/login'

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

        return self.dict(include={'role_id', 'secret_id'})
