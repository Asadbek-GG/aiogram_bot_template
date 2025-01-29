# from typing import Optional
#
# from aiogram import types
#
#
# class Bot:
#     def __init__(self, env_: Env, path_env: Optional[str] = None):
#         env_.read_env(path_env)
#         self._TOKEN: str = env_.str("BOT_TOKEN")
#         self._ADMIN_IDS: list[int] = env_.list("ADMINS", subcast=int)
#         self._USE_REDIS: bool = env_.bool("USE_REDIS")
#         self._BOT_URL: str = env_.str("BOT_URL")
#         self._CHANEL_URL: str = env_.str("CHANEL_URL")
#         self._GROUP_URL: str = env_.str("GROUP_URL")
#         self._CHANEL_ID: str = env_.str("CHANEL_ID")
#         self._GROUP_ID: str = env_.str("GROUP_ID")
#         self._CHANEL_NAME: str = env_.str("CHANEL_NAME")
#         self._GROUP_NAME: str = env_.str("GROUP_NAME")
#
#     @property
#     def token(self) -> str:
#         return self._TOKEN
#
#     @property
#     def admin_ids(self) -> list[int]:
#         return self._ADMIN_IDS
#
#     @property
#     def use_redis(self) -> bool:
#         return self._USE_REDIS
#
#     @property
#     def bot_url(self) -> str:
#         return self._BOT_URL
#
#     @property
#     def chanel_url(self) -> str:
#         return self._CHANEL_URL
#
#     @property
#     def group_url(self) -> str:
#         return self._GROUP_URL
#
#     @property
#     def chanel_id(self) -> str:
#         return self._CHANEL_ID
#
#     @property
#     def group_id(self) -> str:
#         return self._GROUP_ID
#
#     @property
#     def chanel_name(self) -> str:
#         return self._CHANEL_NAME
#
#     @property
#     def group_name(self) -> str:
#         return self._GROUP_NAME
#
#     @property
#     async def default_commands(self):
#         commands = [
#             types.BotCommand(command="start", description="Ботни ишга тушуриш"),
#             types.BotCommand(command="help", description="Ёрдам"),
#         ]
#         return commands