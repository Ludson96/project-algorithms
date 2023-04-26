def study_schedule(
    permanence_period: list[tuple[int, int]], target_time: int
) -> None | int:
    result = 0

    for student in permanence_period:
        if (
            not isinstance(target_time, int)
            or not isinstance(student[0], int)
            or not isinstance(student[1], int)
        ):
            return None
        if student[0] <= target_time <= student[1]:
            result += 1

    return result
