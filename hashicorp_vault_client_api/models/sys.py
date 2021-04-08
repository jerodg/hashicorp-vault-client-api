#!/usr/bin/env python3.8
"""HashiCorp Vault Client API -> Models -> Sys
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
from typing import List, Optional

from base_client_api.models.record import Record


class CreateUpdateNamespace(Record):
    """Sys/Namespaces -> Create/Update

    POST /sys/namespaces/{namespace}

    Create or Update a Namespace"""
    namespace_prefix: Optional[str] = ''
    namespace_suffix: str

    @property
    def endpoint(self) -> str:
        """Endpoint

        The suffix end of the URI

        Returns:
            (str)"""
        return f'{"/" if self.namespace_prefix else ""}{self.namespace_prefix}/sys/namespaces/{self.namespace_suffix}'

    @property
    def method(self) -> Optional[str]:
        """Method

        The HTTP verb to be used
         - Must be a valid HTTP verb as listed above in METHODS

        Returns:
            (str)"""
        return 'POST'


class Policy(Record):
    """Policy"""
    path: List[str]
    capabilities: List[List[str]]


class CreateUpdatePolicy(Record):
    """Sys/Policies -> Create/Update

    PUT /sys/policy/{policy_id}

    Create or Update a Policy"""
    policy_id: str
    body: Policy

    @property
    def endpoint(self) -> str:
        """Endpoint

        The suffix end of the URI

        Returns:
            (str)"""
        return f'/sys/policy/{self.policy_id}'

    @property
    def method(self) -> Optional[str]:
        """Method

        The HTTP verb to be used
         - Must be a valid HTTP verb as listed above in METHODS

        Returns:
            (str)"""
        return 'PUT'

    @property
    def json_body(self) -> Optional[dict]:
        """Request Body"""
        cap = (f'["{",".join(x)}"]' for x in self.body.capabilities)
        pc = zip(self.body.path, cap)
        return {'policy': ' '.join([f'path "{p}" {{capabilities = {c}}}' for p, c in pc])}
