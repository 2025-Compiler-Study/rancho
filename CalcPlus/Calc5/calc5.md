# calc5 
parse tree -> AST

즉시 실행이 아닌 AST를 구성한다.

```antlr4
grammar CalcPlus;

program : (stmt)+ EOF;
stmt : 'int' VAR (',' VAR) * ';'

# 구현과제 #1
1. AST의 구성요소를 생각하고 구현해야 한다.
2. ANTLR로 작성한 문법에서 의미를 가지는 시맨틱한 부분이 AST의 노드가 된다.
3. Parse Tree에서 AST로 변환 시 보통 구성 요소가 줄어들지만, 늘어날 수도 있다. 
4. 이전 과제의 테스트용 작성 코드를 AST로 구성하면 어떻게 될 지 직접 구성해본다
```


# Ref
- https://lifework-archive-reservoir.tistory.com/345
- https://jake-seo-dev.tistory.com/124