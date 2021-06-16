-- Tabla usuario
-- Atributos:
--		id, pass, fecha_registro
CREATE TABLE IF NOT EXISTS "USUARIO"
(
	"usu_id"				varchar(30) NOT NULL,
	"usu_pass"				varchar(20) NOT NULL,
	"usu_fecha_registro"	timestamp NOT NULL,
	CONSTRAINT "PK_USUARIO" PRIMARY KEY ("usu_id")
);

-- INSERT INTO PUBLIC."USUARIO" (usu_id,usu_pass,usu_fecha_registro)
-- VALUES ('usuario03','1234',NOW());

SELECT PUBLIC."USUARIO".usu_fecha_registro 
FROM PUBLIC."USUARIO"
WHERE PUBLIC."USUARIO".usu_id = 'usuario04';