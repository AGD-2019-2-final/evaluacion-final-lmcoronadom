-- Pregunta
-- 
-- 
-- Ordene el archivo `data.tsv`  por letra y valor (3ra columna).
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
-- 
--  >>> Escriba el codigo del mapper a partir de este punto <<<
-- 
lines = LOAD 'data.tsv' AS (line:CHARARRAY, date:CHARARRAY, number:INT);
words = ORDER lines BY line, number;
STORE words INTO 'output';
fs -get output/ .
