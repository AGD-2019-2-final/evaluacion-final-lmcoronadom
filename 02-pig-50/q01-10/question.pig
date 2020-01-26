-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` compute la cantidad de registros por letra. 
-- Escriba el resultado a la carpeta `output` del directorio actual.
--
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
lines= LOAD 'data.tsv' AS (line:CHARARRAY, date:CHARARRAY, number:INT);
words = FOREACH lines GENERATE line;
grouped = GROUP words BY line;
wordcount = FOREACH grouped GENERATE group, COUNT(words);
STORE wordcount INTO 'output';
fs -get output/ .