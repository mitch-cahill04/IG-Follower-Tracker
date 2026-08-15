import json
import csv
import sys


def main():
    if len(sys.argv) != 3:
        print("incorrect amount of command line arguments")
    followers = load_users(sys.argv[1])
    following = load_users(sys.argv[2])
    not_following_back = sorted(following - followers)
    write_csv("not_following_back.csv", followers, following, not_following_back)


def write_csv(filename, followers, following, not_following_back):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["you follow", len(following)])
        writer.writerow(["followers", len(followers)])
        writer.writerow(["dont follow you back", len(not_following_back)])
        writer.writerow([])
        writer.writerow(["usernames:"])
        for user in not_following_back:
            writer.writerow([user])


def username_from_href(href):
    return href.rstrip("/").split("/")[-1]


def load_users(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, dict):
        for v in data.values():
            if isinstance(v, list):
                data = v
                break
    users = set()
    for item in data:
        sld = item.get("string_list_data", [])
        if not sld:
            continue
        entry = sld[0]
        username = entry.get("value")
        if not username:
            href = entry.get("href", "")
            if href:
                username = username_from_href(href)
        if username:
            users.add(username)
    return users


def unfollowed(following, followers):
    return following - followers


if __name__ == "__main__":
    main()
