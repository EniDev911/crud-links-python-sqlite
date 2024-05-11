DROP TABLE IF EXISTS category;

CREATE TABLE IF NOT EXISTS category(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL
);

DROP TABLE IF EXISTS link;

CREATE TABLE link(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    url VARCHAR(55) NOT NULL,
    category_id INTEGER,
    foreign key(category_id) references category(id)
);

INSERT INTO category (name) VALUES ('frontend');
INSERT INTO category (name) VALUES ('backend');

INSERT INTO link (name, url, category_id) 
VALUES 
('bootstrap','https://getbootstrap.com/docs/5.3/',1),
('tailwindcss','https://tailwindcss.com/',1),
('django','https://docs.djangoproject.com/es/',2),
('nodejs doc','https://nodejs.org/docs/latest/api/',2);