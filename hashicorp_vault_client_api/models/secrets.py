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
from typing import Any, Callable, Optional

from base_client_api.models.record import Record


class SecretOptions(Record):
    """Secret Options"""
    cas: Optional[int]


class SecretData(Record):
    """Secret Data"""
    namespace: Optional[str] = ''
    secret_name: str
    key: str
    value: str
    path: Optional[str] = None

    def dict(self, *,
             include: set = None,
             exclude: set = None,
             by_alias: bool = False,
             skip_defaults: bool = None,
             exclude_unset: bool = False,
             exclude_defaults: bool = False,
             exclude_none: bool = True) -> dict:
        """Dictionary

        Args:
            include (set):
            exclude (set):
            by_alias (bool):
            skip_defaults (bool):
            exclude_unset (bool):
            exclude_defaults (bool):
            exclude_none (bool):

        Returns:
            dct (Dict[str, Any])"""
        return {self.key: self.value}


class CreateUpdateSecret(Record):
    """Secret -> Create/Update

    POST /{namespace}/kv/data/{path}{secret_name}

    Create or update a secret."""
    options: Optional[SecretOptions] = None
    data: Optional[SecretData] = None

    class Config:
        """Config

        Pydantic configuration"""
        alias_generator = None

    def dict(self, *,
             include: set = None,
             exclude: set = None,
             by_alias: bool = False,
             skip_defaults: bool = None,
             exclude_unset: bool = False,
             exclude_defaults: bool = False,
             exclude_none: bool = True) -> dict:
        """Dictionary

        Args:
            include (set):
            exclude (set):
            by_alias (bool):
            skip_defaults (bool):
            exclude_unset (bool):
            exclude_defaults (bool):
            exclude_none (bool):

        Returns:
            dct (Dict[str, Any])"""
        return super().dict(include=include,
                            exclude=exclude,
                            by_alias=by_alias,
                            skip_defaults=skip_defaults,
                            exclude_unset=exclude_unset,
                            exclude_defaults=exclude_defaults,
                            exclude_none=exclude_none)

    def json(self, *,
             include: Optional[set] = None,
             exclude: set = None,
             by_alias: bool = False,
             skip_defaults: bool = None,
             exclude_unset: bool = False,
             exclude_defaults: bool = False,
             exclude_none: bool = True,
             encoder: Optional[Callable[[Any], Any]] = None,
             **dumps_kwargs: Any) -> str:
        """JSON as String

        Args:
            include (set):
            exclude (set):
            by_alias (bool):
            skip_defaults (bool):
            exclude_unset (bool):
            exclude_defaults (bool):
            exclude_none (bool):
            encoder (Callable):

        Returns:
            (str)"""
        return super().json(include=include,
                            exclude=exclude,
                            by_alias=by_alias,
                            skip_defaults=skip_defaults,
                            exclude_unset=exclude_unset,
                            exclude_defaults=exclude_defaults,
                            exclude_none=exclude_none,
                            encoder=encoder)

    @property
    def endpoint(self) -> str:
        """Endpoint

        The suffix end of the URI

        Returns:
            (str)"""
        return f'{self.data.namespace}/kv/data/{self.data.path}/{self.data.secret_name}'

    @property
    def method(self) -> Optional[str]:
        """Method

        The HTTP verb to be used
         - Must be a valid HTTP verb as listed above in METHODS

        Returns:
            (str)"""
        return 'POST'

    @property
    def parameters(self) -> Optional[dict]:
        """URL Parameters

        If you need to pass parameters in the URL

        Returns:
            (dict)"""
        return None

    @property
    def json_body(self) -> Optional[dict]:
        """Request Body"""
        return {'data': {self.data.key: self.data.value}}
