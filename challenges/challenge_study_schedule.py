def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for hour in permanence_period:
            entry, exit = hour
            if target_time >= entry and target_time <= exit:
                counter += 1
        return counter
    except TypeError:
        return None
