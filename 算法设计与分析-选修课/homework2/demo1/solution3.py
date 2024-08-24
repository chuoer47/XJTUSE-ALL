def build_dfa(pattern):
    states = []
    transitions = {}
    accepting_states = set()
    state_counter = 0

    def add_state():
        nonlocal state_counter
        state = state_counter
        state_counter += 1
        states.append(state)
        return state

    def add_transition(source, symbol, target):
        if source not in transitions:
            transitions[source] = {}
        transitions[source][symbol] = target

    def match_dfa(text):
        current_states = {0}  # 初始状态为0
        for symbol in text:
            next_states = set()
            for state in current_states:
                if state in transitions and symbol in transitions[state]:
                    next_state = transitions[state][symbol]  # 根据当前字符进行状态转换
                    next_states.add(next_state)
            current_states = next_states

        return any(state in accepting_states for state in current_states)

    def process_pattern(index):
        if index >= len(pattern):
            accepting_states.add(state)
            return

        symbol = pattern[index]
        if symbol == "*":
            next_state = add_state()
            add_transition(state, "", next_state)  # 空字符转换
            add_transition(state, pattern[index + 1], next_state)  # 下一个字符转换
            add_transition(next_state, pattern[index + 1], next_state)  # 下一个字符转换
            process_pattern(index + 1)
            return

        if symbol == "?":
            next_state = add_state()
            add_transition(state, pattern[index + 1], next_state)  # 下一个字符转换
            process_pattern(index + 1)
            return

        next_state = add_state()
        add_transition(state, symbol, next_state)
        process_pattern(index + 1)

    state = add_state()
    process_pattern(0)
    accepting_states.add(state)

    return match_dfa

# 示例用法
pattern = "a*b"
matcher = build_dfa(pattern)
text = "aaaab"
result = matcher(text)
