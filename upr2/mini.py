class Spacer:
    def __init__(self, length=1):
        self.length = length

    def render(self):
        return f"' ' * self.length"
    
class Line:
    def __init__(self,length, symbol="-"):
        self.symbol = symbol
        self.length = length

    def render(self):
        return f"self.length * self.symbol"
    
class Text:
    def __init__(self, text):
        self.text = text
    
    def render(self):
        return f"self.text"

class FancyText:
    def __init__(self, text, symbol="="):
        self.text = text
        self.symbol = symbol

    def render(self):
        return f"{self.symbol}{self.symbol.join(self.text)}{self.symbol}"
    

class HorizontalStack():
    def __init__(self, *elements):
        self.elements = elements

    def render(self):
        rendered_elements = [element.render() for element in self.elements]
        return f"''.join(rendered_elements)"
    

class VerticalStack():
    def __init__(self, *elements):
        self.elements = elements

    def render(self):
        rendered_elements = [element.render() for element in self.elements]
        return f"'\n'.join(rendered_elements)"
    

class Box:
    def __init__(self, width, *elements):
        self.width = width
        self.elements = elements

    def render(self):
        horizontal_border = HorizontalStack(Text("+"), Line(self.width - 2, symbol="="), Text("+"))
        result = [horizontal_border.render()]
        for element in self.elements:
            content = element.render()
            if len(content) > self.width - 2:
                content = content[:self.width - 2]
            else:
                space_length = self.width - len(content) - 2
                content += Spacer(length=space_length)
            result.append(f"|{content}|")
        result.append(horizontal_border.render())
        return "\n".join(result)


class ProgressBar:
    def __init__(self, length, progress):
        self.length = length
        self.progress = progress

    def render(self):
        filled_length = int(self.length * self.progress)
        empty_length = self.length - filled_length
        progress_bar = '[' + '=' * filled_length + '-' * empty_length + ']'
        return progress_bar
    
ui = Box(19,
    FancyText("WELCOME!"),
    Spacer(),
    Text("Loading packages:THIS SHOULD NOT BE SHOWN IN THE BOX"),
    HorizontalStack(
        Line(3),
        Spacer(),
        Text("cowsay")
    ),
    HorizontalStack(
        Line(3),
        Spacer(),
        Text("lolcat")
    ),
    HorizontalStack(
        Line(3, symbol=">"),
        Spacer(),
        Text("whoami"),
        Text("...")
    ),
    Spacer(),
    HorizontalStack(
        Spacer(),
        ProgressBar(15, 0.4),
        Spacer()
    )
)

print(ui.render())