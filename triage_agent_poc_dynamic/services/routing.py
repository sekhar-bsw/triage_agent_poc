
from models.models import DecisionSpec, TraitRule
from typing import Dict, Optional

def evaluate_rule(rule: TraitRule, data: Dict) -> bool:
    value = data.get(rule.trait_target_key)
    if rule.operator == "==":
        return value == rule.value
    elif rule.operator == "!=":
        return value != rule.value
    elif rule.operator == ">":
        return value > rule.value
    elif rule.operator == "<":
        return value < rule.value
    elif rule.operator == ">=":
        return value >= rule.value
    elif rule.operator == "<=":
        return value <= rule.value
    elif rule.operator == "in":
        return value in rule.value
    elif rule.operator == "not_in":
        return value not in rule.value
    elif rule.operator == "exists":
        return rule.trait_target_key in data
    return False

def simulate_routing(spec: DecisionSpec, data: Dict) -> Optional[Dict]:
    for outcome in spec.outcomes:
        if all(evaluate_rule(rule, data) for rule in outcome.immediate_select_if):
            return {"outcome": outcome.outcome_id, "rationale": outcome.description}
    for outcome in spec.outcomes:
        if all(evaluate_rule(rule, data) for rule in outcome.decision_rules):
            return {"outcome": outcome.outcome_id, "rationale": outcome.description}
    return None
