<div align="center">
  <img src="assets/logo.png">
  <br>
  <br>
  <i>Yet another gravitational physics simulator</i>
</div>

<hr>

**Cavendish** is a gravitational physics simulator written wholly in Python with the aid of pygame and tkinter. It was developed in under a week as a proof of concept for my physics class, and it shall be regarded as such.

Its name comes from my far better-renowned namesake **Sir Henry Cavendish**, the first measurer of $G$—the universal gravitational constant—, a magnitude profoundly intertwined with the formulae of this program.

# Running the simulation
In order to execute this program, you have two different options at your disposal. You can either download the pre-compiled Windows binaries from the ["Releases"](https://github.com/h3nry-d1az/cavendish/releases) section, or whether not suitable, utilize the `main.py` script. A third possible alternative is to compile your own build of the project, yet it is not necessary by any means.

Nonetheless, further instructions on the latter two procedures will be developed below.

## Executing `main.py`
The `main.py` script contains the launcher of the simulation, so executing it is the recommended way to proceed.

Firstly, ensure pygame is installed on your system by running
```bash
pip install pygame
```

Finally, run `main.py` with Python (no command line arguments are accepted):
```
python ./main.py
```

## Compiling with pyinstaller
This method demands an additional dependency, namely pyinstaller, which can be obtained likewise via pip:
```bash
pip install pyinstaller
```
The `Makefile` will be in charge of all the magic, so one only needs to invoke it:
```bash
make
```

Your fresh, newly-compiled binaries will be available at `dist/cavendish`.

# [License](LICENSE)
[...]

Creative Commons Attribution-ShareAlike 4.0 International Public
License

By exercising the Licensed Rights (defined below), You accept and agree
to be bound by the terms and conditions of this Creative Commons
Attribution-ShareAlike 4.0 International Public License ("Public
License"). To the extent this Public License may be interpreted as a
contract, You are granted the Licensed Rights in consideration of Your
acceptance of these terms and conditions, and the Licensor grants You
such rights in consideration of benefits the Licensor receives from
making the Licensed Material available under these terms and
conditions.

[...]
