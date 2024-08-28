[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=14098031)

# [Download executable for Windows systems](https://github.com/Living-Tribunal/SDEV-220-UTTT/releases/download/game/U.TTT.zip)

If you want to run the game from files

1. Make sure python is installed, you can download it [here](https://www.python.org/downloads/)
2. in console, run these 2 commands (for Windows)
   #### pip install pygame
   #### pip install numpy
3. Execute the code in main

This program is set up to be converted to a WASP format to be used as a webapp. However, it contains mp3 files in its assets which are not usable in HTML, they must be converted to something like .ogg. If you wish to convert after changing the sound files however (or want to run it as a test) then please do the following

1. In console, run the following command
   #### pip install pygbag
2. In console, run the following command
   #### pygbag folder (type your working directory with all the files, including main)
3. Follow the on screen instructions

If you wish to convert to a file format, run the following command 
  #### pygbag --archive --build folder

should work on Windows 64 bit systems. If you download the exe, Chrome / Windows will say it's a virus because it's not signed in any way. It's not a virus though, **Github themselves have checked the file to let me keep up this repository. It is safe!
**
