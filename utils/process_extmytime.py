import re
import datetime

pat_hours = re.compile(r"\d+:\d+")
pat_time = re.compile(r"\d{2}:\d{2}")
pat_task = re.compile(r"(?<=Task: )\d+")


def _convert_time_to_float(time_str: str) -> float:
    hours, minutes = map(int, time_str.split(":"))
    return hours + minutes / 60.0


def process_extmytime(text: str) -> tuple[float, float]:
    lines = text.split("\n")

    # identify total hours
    for line in lines:
        if "Hours declared:" in line:
            total_hours = pat_hours.search(line).group()
            # from a string to a float representing the total hours
            total_hours = _convert_time_to_float(total_hours)
            break
    # count all hours
    tasks_hours = {}
    message = ""
    for line in lines:
        if "Task:" in line:
            task_number = int(pat_task.search(line).group())
            hours = pat_time.findall(line)
            # subtract the two times to get the number of hours in the
            # interval
            assert len(hours) == 2  # if not we have a problem
            start_time = datetime.datetime.strptime(hours[0], "%H:%M")
            end_time = datetime.datetime.strptime(hours[1], "%H:%M")
            if start_time.minute % 15 != 0 or end_time.minute % 15 != 0:
                message = "There are time slots that do not comply with the 15 minutes granularity rule. Please, " \
                          "correct the hours in ExtMyTime before proceeding with the Monthly Report."
                return total_hours, tasks_hours, message
            hour_interval = end_time - start_time
            hour_interval = hour_interval.total_seconds() / 3600
            if task_number in tasks_hours:
                tasks_hours[task_number] += hour_interval
            else:
                tasks_hours[task_number] = hour_interval
    # make sure that the total hours and sum of tasks give the same result
    assert round(sum(tasks_hours.values())) == round(float(total_hours))
    return total_hours, tasks_hours, message



