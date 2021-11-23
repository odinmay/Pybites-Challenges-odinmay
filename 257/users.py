def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    users = dict()
    for line in passwd.splitlines()[1:]:
        username = line.split(':')[0]
        name = ' '.join(line.split(':')[4].replace(',', ' ').split())
        if len(name) < 1:
            name = 'unknown'
        users[username] = name
    return users
