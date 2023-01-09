from nonebot import on_message
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
from nonebot_plugin_guild_patch import GuildMessageEvent

from .data_source import send_msg_to_mc
from ...utils import msg_rule
from typing import Union

mc_qq = on_message(priority=5, rule=msg_rule, block=False)


# 收到 群/频 道消息时
@mc_qq.handle()
async def handle_first_receive(bot: Bot, event: Union[GroupMessageEvent, GuildMessageEvent]):
    await send_msg_to_mc(bot=bot, event=event)