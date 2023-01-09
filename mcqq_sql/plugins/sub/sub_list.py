from typing import Union

from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot_plugin_guild_patch import GuildMessageEvent

from ...database import DB as db

from ...utils import (
    get_type_id,
    permission_check
)

sub_list = on_command("互通列表", priority=3, block=True)
sub_list.__doc__ = """互通列表"""

sub_list.handle()(permission_check)


@sub_list.handle()
async def _(event: Union[GroupMessageEvent, GuildMessageEvent]):
    """发送当前位置的互通列表"""
    message = "互通列表（所有群/频道都是分开的）\n\n"
    subs = await db.get_sub_list(event.message_type, await get_type_id(event))

    for sub in subs:
        server = await db.get_server(server_name=sub.server_name)
        assert server is not None
        message += f"{server.server_name}\n"

    await sub_list.finish(message)