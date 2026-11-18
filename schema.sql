CREATE TABLE IF NOT EXISTS members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    last_name TEXT NOT NULL,
    first_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    phone TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS activities (
    code TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    monthly_fee REAL NOT NULL,
    capacity INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS registrations (
    member_id INTEGER NOT NULL,
    activity_code TEXT NOT NULL,
    date TEXT NOT NULL,
    PRIMARY KEY (member_id, activity_code),
    FOREIGN KEY (member_id) REFERENCES members (id) ON DELETE CASCADE,
    FOREIGN KEY (activity_code) REFERENCES activities (code) ON DELETE CASCADE
);
