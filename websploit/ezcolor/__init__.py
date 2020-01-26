from copy import deepcopy
# Ezcolor library for python
#

__version__ = 0.7

# Template builder
class _CPrint:
	def __init__(self):
		self.foreground = 39
		self.background = 49
		self.bold = None
		self.italic = None
		self.underline = None
		self.prefix = None

	def __call__(self, text):
		print(self.__prepare_str(text=text))

	def code(self, text):
		return self.__prepare_str(text=text)

	def __prepare_str(self, text):
		template = self.__pattern_generator()
		template = template.replace("%TEXT%", text)
		return template

	def decorate(self, func):
		def wrapper(*args, **kwargs):
			result = func(*args, **kwargs)
			if isinstance(result, str):
				template = self.__prepare_str(text=result)
				return template
			else:
				return result
		return wrapper

	def __str__(self):
		return f"<Style(foreground={self.foreground}, background={self.background}), bold={self.bold}, " \
			f"italic={self.italic}, underline={self.underline})>"

	def __pattern_generator(self):
		# template = "\033[%BOLD%;%ITALIC%;%UNDERLINE%;%BG%;%FG%m%TEXT%\033[0m"
		start_template = "\033["
		end_template = "m%TEXT%\033[0m"
		# add italic
		if self.italic:
			start_template = f"{start_template}{self.italic};"
		# add underline
		if self.underline:
			start_template = f"{start_template}{self.underline};"
		# add bold
		if self.bold:
			start_template = f"{start_template}{self.bold};"
		# add background
		start_template = f"{start_template}{self.background};"
		# add foreground
		start_template = f"{start_template}{self.foreground}"
		if self.prefix:
			return self.prefix + start_template + end_template
		else:
			return start_template + end_template


class Style:
	def __init__(self, style=_CPrint()):
		self.style = style

	@property
	def add(self):
		return _MakeStyle(style=deepcopy(self.style))

	def apply(self):
		"""return created style object"""
		return self.style


class _MakeStyle(Style):
	def __init__(self, style):
		super().__init__(style)

	def foreground(self, color):
		colors = {
			'default': 39,
			'black': 30,
			'red': 31,
			'green': 32,
			'yellow': 33,
			'blue': 34,
			'magenta': 35,
			'cyan': 36,
			'light_gray': 37,
			'dark_gray': 90,
			'light_red': 91,
			'light_green': 92,
			'light_yellow': 93,
			'light_blue': 94,
			'light_magenta': 95,
			'light_cyan': 96,
			'white': 97}
		try:
			self.style.foreground = colors[color]
		except KeyError:
			print(f"{color} color not supported for foreground! try supported colors :")
			print("\n")
			for c in colors.keys():
				print(c, end=",")
			print("\n")
		return self

	def background(self, color):
		colors = {
			'default': 49,
			'black': 40,
			'red': 41,
			'green': 42,
			'yellow': 43,
			'blue': 44,
			'magenta': 45,
			'cyan': 46,
			'light_gray': 47,
			'dark_gray': 100,
			'light_red': 101,
			'light_green': 102,
			'light_yellow': 103,
			'light_blue': 104,
			'light_magenta': 105,
			'light_cyan': 106,
			'white': 107}
		try:
			self.style.background = colors[color]
		except KeyError:
			print(f"{color} color not supported for background! try supported colors :")
			print("\n")
			for c in colors.keys():
				print(c, end=",")
			print("\n")
		return self

	def prefix(self, type_):
		prefix = {
			"done": "\033[32;m[✔] \033[0m",
			"error": "\033[31;m[✘] \033[0m",
			"warning": "\033[33;m[→] \033[0m",
			"info": "\033[34;m[𝓲] \033[0m"
		}
		try:
			self.style.prefix = prefix[type_]
		except KeyError:
			print(f"{type_} prefix not supported! list of supported items :")
			print("\n")
			for c in prefix.keys():
				print(c, end=",")
			print("\n")
		return self

	@property
	def underline(self):
		self.style.underline = 4
		return self

	@property
	def italic(self):
		self.style.italic = 3
		return self

	@property
	def bold(self):
		self.style.bold = 1
		return self
