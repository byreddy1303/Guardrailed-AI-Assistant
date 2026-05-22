import pytest
from ulid import ULID
from app.graph.state import PipelineState


def make_state(query: str = "What is the annual leave policy?", session_id: str = None) -> PipelineState:
    return PipelineState(
        session_id=session_id or str(ULID()),
        raw_query=query,
        sanitized_query="",
        input_guard_passed=False,
        input_guard_reason=None,
        injection_score=0.0,
        pii_detected_in_input=False,
        retrieved_docs=[],
        raw_response="",
        generation_attempts=0,
        output_valid=False,
        toxicity_score=0.0,
        bias_flag=False,
        validation_failure_reason=None,
        redacted_response="",
        pii_entities_found=[],
        grounding_passed=False,
        ungrounded_claims=[],
        route="auto_respond",
        confidence_score=1.0,
        escalation_reason=None,
        final_response="",
        audit_trail=[],
    )
