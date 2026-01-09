def evaluate_run(used_calculator, answered_early, correct_answer):
    
    if not used_calculator:
        return False, "SKIPPED_REQUIRED_TOOL"

    if answered_early:
        return False, "ANSWERED_TOO_EARLY"

    if not correct_answer:
        return False, "IGNORED_TOOL_OUTPUT"

    return True, "SUCCESS"
