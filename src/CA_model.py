"""
Representa la definición estructural de modelos de AC soportados por el *framework*, inlcuye las características des estados, reglas y vencidad, Una solución debe incluir un modelo de AC como parte de su definición
"""

from collections.abc import Callable

def abstract(f):

   return f



class CAModel:

   status: int
   rules: list[Callable]
   neighbor: list[(int,int)]


# <<Builder-Director>>
class Solution:

   models: list[CAModel]


   def __init__(self):
      pass

   def construct(self) -> None:
      pass


# Interface <<Builder-Builder>>
class SolutionBuilder:


   @abstract
   def build_score(self) -> None:
      pass

   @abstract
   def build_representation(self) -> None:
      pass


class Concr_SolutionBuilder(SolutionBuilder):


   def build_score(self) -> None:

      a = 0
      b = a

   
   def build_representation(self) -> None:

      b = 0 
      self.b = b








