-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` genere una tabla que contenga la primera columna,
-- la cantidad de elementos en la columna 2 y la cantidad de elementos en la 
-- columna 3 separados por coma. La tabla debe estar ordenada por las 
-- columnas 1, 2 y 3.
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
fs -rm -f data.tsv;
fs -put data.tsv;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
data= LOAD 'data.tsv' AS (upper_letter:CHARARRAY, lower_letter: BAG{tup: TUPLE(letter:CHARARRAY)}, exam:MAP[]);
data = FOREACH data GENERATE upper_letter, COUNT($1), SIZE($2);
ordered = ORDER data BY upper_letter, $1, $2;
STORE ordered INTO 'output' USING PigStorage(',');
fs -get output/ .