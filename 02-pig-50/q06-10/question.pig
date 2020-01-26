-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` Calcule la cantidad de registros por clave de la 
-- columna 3. En otras palabras, cuántos registros hay que tengan la clave 
-- `aaa`?
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
data= LOAD 'data.tsv' AS (upper_letter:CHARARRAY, lower_letter: BAG{tup: TUPLE(letter:CHARARRAY)}, exam:MAP[]);
data = FOREACH data GENERATE FLATTEN(exam) AS exam;
grouped = GROUP data BY exam;
letter_count = FOREACH grouped GENERATE group, COUNT($1);
STORE letter_count INTO 'output' USING PigStorage(',');
fs -get output/ .