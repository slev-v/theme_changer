# Theme Changer
Theme changer - python script to change iterm2 and nvim themes

## Demo
https://github.com/slev-v/theme_changer/assets/120958402/49c4ea1c-ae6c-452d-b794-9c1cd2579f65

## Requirements
- python
- iterm2
- nvim
- [gum](https://github.com/charmbracelet/gum)

### You need to avtivate api in iterm2
go to general -> magic -> enable python api
<img width="897" alt="image" src="https://github.com/slev-v/theme_changer/assets/120958402/cad32fdb-197d-4e65-8a31-dc9c96f7c56a">


## Python Requirements
- gumpython 
- iterm2

## Setup
You should have profiles in iterm2 with names corresponding to the names of nvim colorschemes.

In nvim config you should have a string like this:
```lua
  colorscheme = "tokyonight-night",
```
This string would change with theme change.
