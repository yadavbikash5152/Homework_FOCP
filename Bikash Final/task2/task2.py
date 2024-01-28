import collections

def process_log_entry(line):
    """Parses a single log entry and extracts relevant data."""
    parts = line.strip().split(",")
    if len(parts) != 3:
        return None  # Handle invalid lines gracefully
    cat, entry_time, exit_time = parts
    return cat, int(entry_time), int(exit_time)

def analyze_log(log_data):
    """Analyzes the log data and calculates statistics for our cat."""
    cat_visits = collections.Counter()
    total_time_ours = 0
    visit_lengths_ours = []

    for line in log_data:
        data = process_log_entry(line)
        if data is None:
            continue  # Skip invalid lines
        cat, entry_time, exit_time = data
        cat_visits[cat] += 1
        if cat == "OURS":
            visit_lengths_ours.append(exit_time - entry_time)
            total_time_ours += exit_time - entry_time

    average_visit_ours = total_time_ours / cat_visits["OURS"] if cat_visits["OURS"] else 0
    longest_visit_ours = max(visit_lengths_ours) if visit_lengths_ours else 0
    shortest_visit_ours = min(visit_lengths_ours) if visit_lengths_ours else 0
    total_time_ours_hours, total_time_ours_minutes = divmod(total_time_ours, 60)

    return (
        cat_visits["OURS"],
        sum(cat_visits.values()) - cat_visits["OURS"],
        f"{total_time_ours_hours} Hours, {total_time_ours_minutes} Minutes",
        f"{average_visit_ours:.2f} Minutes",
        longest_visit_ours,
        shortest_visit_ours,
    )

def main():
    """Reads the log file, analyzes it, and prints the results."""
    filename = "first.log"
    try:
        with open(filename, "r") as file:
            log_data = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return

    cat_visits, other_cats, total_time_ours, average_visit_ours, longest_visit_ours, shortest_visit_ours = analyze_log(
        log_data
    )

    print("Log File Analysis")
    print("==================")
    print(f"Cat Visits: {cat_visits}")
    print(f"Other Cats: {other_cats}")
    print(f"Total Time in House: {total_time_ours}")
    print(f"Average Visit Length: {average_visit_ours}")
    print(f"Longest Visit:        {longest_visit_ours}")
    print(f"Shortest Visit:       {shortest_visit_ours}")

if __name__ == "__main__":
    main()
