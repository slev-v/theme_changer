#!/usr/bin/env python3

import os
from typing import List

from gumpython import Choose
from iterm2 import Connection, PartialProfile, async_get_app, run_until_complete


async def get_all_themes(connection: Connection) -> List[str]:
    all_profiles = await PartialProfile.async_query(connection)
    profiles = []
    for profile in all_profiles:
        profiles.append(profile.name)
    return profiles


async def choose_theme(connection: Connection) -> str:
    print("• Choose theme:")
    all_profiles = await get_all_themes(connection)
    choose = Choose(all_profiles)
    result = choose.run()
    if not result:
        print("No theme selected")
        exit()
    return result[0]


async def change_iterm2_theme(connection: Connection, theme_name: str) -> None:
    app = await async_get_app(connection)
    all_profiles = await PartialProfile.async_query(connection)
    for profile in all_profiles:
        if profile.name == theme_name:
            await profile.async_make_default()
            full = await profile.async_get_full_profile()
            await app.current_terminal_window.current_tab.current_session.async_set_profile(  # type: ignore
                full
            )
            return


def change_nvim_theme(theme_name: str) -> None:
    home_directory = os.path.expanduser("~")

    file_path = os.path.join(
        home_directory, ".config", "nvim", "lua", "plugins", "colorscheme.lua"
    )

    with open(file_path, "r") as file:
        lines = file.readlines()

    for i in range(len(lines)):
        if lines[i].startswith('      colorscheme = "'):
            lines[i] = f'      colorscheme = "{theme_name}",\n'

    with open(file_path, "w") as file:
        file.writelines(lines)


async def main(connection: Connection):
    theme_name = await choose_theme(connection)
    await change_iterm2_theme(connection, theme_name)
    change_nvim_theme(theme_name)
    print(f"Theme changed to {theme_name}")


if __name__ == "__main__":
    run_until_complete(main)
