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

import asyncio
import concurrent
import logging

import pytest

from inmanta import config
from inmanta.server.bootloader import InmantaBootloader

logger = logging.getLogger(__name__)


@pytest.fixture
def {{ cookiecutter.extension_name }}_config(server_config, postgres_db, database_name):
    config.Config.set("server", "enabled_extensions", "{{ cookiecutter.extension_name }}")


@pytest.fixture
async def server({{ cookiecutter.extension_name }}_config, server_config):
    """
    Override standard inmanta server to allow more config to be injected
    """
    ibl = InmantaBootloader()
    await ibl.start()

    yield ibl.restserver

    try:
        await asyncio.wait_for(ibl.stop(), 15)
    except concurrent.futures.TimeoutError:
        logger.exception("Timeout during stop of the server in teardown")

    logger.info("Server clean up done")
