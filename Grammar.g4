grammar Grammar;

program: statement* EOF;

statement: ifStatement
         | switchStatement
         | assignment
         | forLoop
         ;

ifStatement: 'if' condition 'then' statement;

switchStatement: 'switch' expression 'case' expression statement;

assignment: IDENTIFIER '=' expression;

forLoop: 'for' IDENTIFIER 'in' 'range' '(' NUMBER ',' NUMBER ')' ':' statement;

condition: expression;

expression: STRING
          | NUMBER
          | IDENTIFIER
          ;

IF: 'if'; 
THEN: 'then'; 
SWITCH: 'switch';
FOR: 'for';
IN: 'in';
RANGE: 'range';

NUMBER : [0-9]+ ;
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
STRING: '"' .*? '"';
WS: [ \t\n\r\f]+ -> skip ;
COMMENT: '#' ~[\r\n]* -> skip;
