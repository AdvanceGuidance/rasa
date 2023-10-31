from rasa.dialogue_understanding.patterns.continue_interrupted import (
    ContinueInterruptedPatternFlowStackFrame,
)


def test_continue_interrupted_pattern_flow_stack_frame_type():
    frame = ContinueInterruptedPatternFlowStackFrame()
    assert frame.type() == "pattern_continue_interrupted"


def test_continue_interrupted_pattern_flow_stack_frame_from_dict():
    frame = ContinueInterruptedPatternFlowStackFrame.from_dict(
        {
            "frame_id": "test_id",
            "step_id": "test_step_id",
            "previous_flow_name": "x_flow",
        }
    )
    assert frame.frame_id == "test_id"
    assert frame.step_id == "test_step_id"
    assert frame.previous_flow_name == "x_flow"
    assert frame.flow_id == "pattern_continue_interrupted"
    assert frame.type() == "pattern_continue_interrupted"
