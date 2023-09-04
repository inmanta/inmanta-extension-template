{%- if cookiecutter.license == "ASL 2.0" -%}
"""
    Copyright {{ cookiecutter.copyright }}

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Contact: {{ cookiecutter.author_email }}
"""
{%- else -%}
"""
    :copyright: {{ cookiecutter.copyright }}
    :contact: {{ cookiecutter.author_email }}
    :license: {{ cookiecutter.license }}
"""
{%- endif %}

from typing import List

from inmanta.protocol.decorators import method
from inmanta.server import SLICE_TRANSPORT, protocol
from inmanta.server.protocol import Server, ServerSlice
from inmanta.types import Apireturn


@method(path="/hello-world", operation="GET", client_types=["api"])
def hello_world():
    """
    Basic hello-world API endpoint.
    """


class {{ cookiecutter.slice_class_name }}(ServerSlice):
    def __init__(self) -> None:
        super().__init__("{{ cookiecutter.extension_name }}.{{ cookiecutter.slice_name }}")

    async def prestart(self, server: Server) -> None:
        await super({{ cookiecutter.slice_class_name }}, self).prestart(server)

    async def start(self) -> None:
        await super({{ cookiecutter.slice_class_name }}, self).start()

    async def prestop(self) -> None:
        await super({{ cookiecutter.slice_class_name }}, self).prestop()

    async def stop(self) -> None:
        await super({{ cookiecutter.slice_class_name }}, self).stop()

    def get_dependencies(self) -> List[str]:
        return []

    def get_depended_by(self) -> List[str]:
        # Ensure we are started before the HTTP endpoint becomes available
        return [SLICE_TRANSPORT]

    @protocol.handle(hello_world)
    async def hello_world_handle(self) -> Apireturn:
        """
        Handle for the hello_world API endpoint.
        """
        return 200, {"data": "hello-world"}
