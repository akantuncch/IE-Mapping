CREATE TABLE Programs (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    website VARCHAR(255),
    efficiency FLOAT
);

CREATE TABLE TechTypes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    program_id INT,
    techtype VARCHAR(255),
    FOREIGN KEY (program_id) REFERENCES Programs(id)
);

CREATE TABLE Resources (
    id INT PRIMARY KEY AUTO_INCREMENT,
    program_id INT,
    resource_type VARCHAR(255),
    FOREIGN KEY (program_id) REFERENCES Programs(id)
);

CREATE TABLE ResourceDetails (
    id INT PRIMARY KEY AUTO_INCREMENT,
    resource_id INT,
    type VARCHAR(255),
    details TEXT,
    FOREIGN KEY (resource_id) REFERENCES Resources(id)
);

CREATE TABLE Affiliations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    program_id INT,
    affiliation VARCHAR(255),
    FOREIGN KEY (program_id) REFERENCES Programs(id)
);

CREATE TABLE Expertise (
    id INT PRIMARY KEY AUTO_INCREMENT,
    program_id INT,
    expertise VARCHAR(255),
    FOREIGN KEY (program_id) REFERENCES Programs(id)
);

CREATE TABLE OfferedResources (
    id INT PRIMARY KEY AUTO_INCREMENT,
    program_id INT,
    resource_offered VARCHAR(255),
    FOREIGN KEY (program_id) REFERENCES Programs(id)
);
