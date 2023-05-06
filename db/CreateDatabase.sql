USE fab;

CREATE TABLE pessoas (
    id integer not null auto_increment,
    nome varchar(100),
    idade integer,
    PRIVATE KEY (id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_c1;

INSERT INTO pessoas (nome, idade) VALUES ('Fabricio', 19);
INSERT INTO pessoas (nome, idade) VALUES ('Juliana', 26);
INSERT INTO pessoas (nome, idade) VALUES ('Luan', 22);
INSERT INTO pessoas (nome, idade) VALUES ('Mariana', 28);
INSERT INTO pessoas (nome, idade) VALUES ('Carlos', 38);