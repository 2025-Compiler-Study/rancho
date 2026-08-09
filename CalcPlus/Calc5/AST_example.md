
graph TD
  classDef binop stroke:#333,stroke-width:2px;
  classDef value stroke:#333,stroke-width:1px;

  Root(('+')):::binop

  L1(('*'))::::binop
  L1_Val1[5]:::value 
  L1_Val1[3]:::value 

  R1_Sub(('-'))::binop
  R1_Sub_Val[5]:::value

  R1_Deep(('/')):::binop
  R1_Deep_Val1[9]:::value
  R1