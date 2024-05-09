# Python Polysyllabic Randomiser
Inspired by one of the many [Steamed Hams edits](https://www.youtube.com/results?search_query=Steamed+Hams+but+it%27s) on Youtube. Specifically, this one:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/mqxysHMnUD0/0.jpg)](https://www.youtube.com/watch?v=mqxysHMnUD0)

# Usage
1. Generate a dictionary file from some source online.
```sh
./dictionaryLoader.py
```
2. Run the randomiser.
```sh
./randomise.py -h
```

# Examples
You can run it in interactive mode
```
./randomise.py -i
> Linux is a clone of the operating system Unix, written from scratch by Linus Torvalds with assistance from a loosely-knit team of hackers across the Net.
Likes is a clone of the operator symbol Unless, writer from scratch by Listed Toolbar with assignment from a loosely-knit team of handhelds acids the Net.
>
```

You can provide is STDIN.
```
$ fortune | ./randomise.py
You will have a long and unified discounted with your sufficiently.
```

You can pipe it into `cowsay`!
```
$ fortune | ./randomise.py | cowsay
 ___________________
< Are you a turned? >
 -------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

# TODO List
- Support brackets, like `[]{}()`.
- Split words that have `-` or `/` in them into individual words, replace those, and retain the original `/` or `-`