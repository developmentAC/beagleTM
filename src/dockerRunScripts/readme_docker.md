### OS-specific scripts to build and run containers
The following bash scripts simplify building the container.

| OS  | Building  | Running  |
|---|---|---|
| MacOS  		|  `./build_macOS.sh` |  `./run_macOS.sh` |
| Linux   	|  `./build_linux.sh` | `./run_linux.sh`  |
| Windows 	|  `build_win.bat` 		|  `run_win.bat` |

These files may be found in the directory, `dockerRunScripts/` and the builder require a copy of `Dockerfile` to run which is in the `src` directory, hence why these command should be run from the `src` directory like in the example above.

### build container
`sh dockerRunScripts/build_macOS.sh`
`sh dockerRunScripts/build_linux.sh`
`dockerRunScripts/build_win.bat`

### run container
`sh dockerRunScripts/run_macOS.sh`
`sh dockerRunScripts/run_linux.sh`
`dockerRunScripts/run_win.bat`

Run the scripts as appropriate for your OS.

