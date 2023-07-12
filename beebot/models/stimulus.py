from typing import TYPE_CHECKING

from langchain.schema import SystemMessage

from beebot.prompting.sensing import stimulus_template
from beebot.utils import list_files

if TYPE_CHECKING:
    from beebot.body import Body


class Stimulus:
    input: SystemMessage

    def __init__(self, input_message: SystemMessage):
        self.input = input_message

    @classmethod
    def generate_stimulus(cls, body: "Body") -> "Stimulus":
        history = body.memories.compile_history()

        functions_summary = ", ".join([f"{pack.name}" for pack in body.packs])
        stimulus_message = stimulus_template().format(
            functions=functions_summary,
            file_list=list_files(body),
            history=history,
            plan=body.current_plan,
            task=body.initial_task,
        )

        return cls(input_message=stimulus_message)
