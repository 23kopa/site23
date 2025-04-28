-- SQLite
CREATE TABLE IF NOT EXISTS user_stats (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    command_count INTEGER DEFAULT 0
);