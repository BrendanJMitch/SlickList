CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
    phone_number TEXT NOT NULL UNIQUE,
    premium INTEGER NOT NULL,
    profile_picture TEXT, 
    preferred_store TEXT,
    salt TEXT NOT NULL,
    auth_hash TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS recipe (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    pinned INTEGER NOT NULL,
    url TEXT,

    FOREIGN KEY  (user_id) REFERENCES user(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS list (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    pinned INTEGER NOT NULL,

    FOREIGN KEY  (user_id) REFERENCES user(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS ingredient (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    cost REAL,
    add_to_list INTEGER NOT NULL,
    walmart_id TEXT,
    image TEXT, 
    aisle TEXT,

    FOREIGN KEY  (user_id) REFERENCES user(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS shared_recipe (
    recipe_id INTEGER NOT NULL,
    shared_with INTEGER NOT NULL,

    FOREIGN KEY  (recipe_id) REFERENCES recipe(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY  (shared_with) REFERENCES user(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS shared_list (
    list_id INTEGER NOT NULL,
    shared_with INTEGER NOT NULL,

    FOREIGN KEY  (list_id) REFERENCES list(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY  (shared_with) REFERENCES user(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS recipe_ingredient (
    recipe_id INTEGER NOT NULL,
    ingredient_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,

    FOREIGN KEY  (recipe_id) REFERENCES recipe(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY  (ingredient_id) REFERENCES ingredient(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS list_recipe (
    list_id INTEGER NOT NULL,
    recipe_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,

    FOREIGN KEY  (list_id) REFERENCES list(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY  (recipe_id) REFERENCES recipe(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS list_ingredient (
    list_id INTEGER NOT NULL,
    ingredient_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,

    FOREIGN KEY  (list_id) REFERENCES list(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY  (ingredient_id) REFERENCES ingredient(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);