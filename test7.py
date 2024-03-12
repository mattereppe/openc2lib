import dataclasses

class Action:
	pass

class Target:
	pass

class Args:
	pass

class Content:
	pass

@dataclasses.dataclass
class Command(Content):
	action: Action
	target: Target
	args: Args = None
	command: int = None

	def __post_init__(self):
		self.command = 3
