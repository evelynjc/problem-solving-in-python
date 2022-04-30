import re


def solution(new_id):
    # Step 1
    new_id = new_id.lower()
    # Step 2
    new_id = re.sub(r"[^a-z0-9-_\.]", "", new_id)
    # Step 3
    new_id = re.sub(r"\.+", ".", new_id)
    # Step 4
    new_id = re.sub(r"^\.|\.$", "", new_id)
    # Step 5
    if not new_id:
        new_id = "a"
    # Step 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:14]
    # Step 7
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    # END STEPS
    return new_id
