def greetings(prefix):
    def names(name):
        print(f"{prefix} {name}")
    return names
hi = greetings("hello,")
tata = greetings("bye bye,")

hi("jim")
hi("lillu")
tata("kyli")