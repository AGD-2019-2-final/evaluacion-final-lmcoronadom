-- Pregunta
-- ===========================================================================
-- 
-- Obtenga los cinco (5) valores más pequeños de la 3ra columna.
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
fs -rm -f data.tsv
fs -put data.tsv
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
lines = LOAD 'data.tsv' AS (line:CHARARRAY, date:CHARARRAY, number:INT);
order1= FOREACH lines GENERATE number;
order2= ORDER order1 BY number;
t= LIMIT order2 5;
STORE t INTO 'output';
fs -get output/ .