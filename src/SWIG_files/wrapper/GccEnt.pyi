from typing import overload, NewType, Optional, Tuple

from OCC.Core.GccEnt import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *


class GccEnt_Position:
	GccEnt_unqualified: int = ...
	GccEnt_enclosing: int = ...
	GccEnt_enclosed: int = ...
	GccEnt_outside: int = ...
	GccEnt_noqualifier: int = ...

class GccEnt:
	@staticmethod
	def Enclosed(self, Obj: gp_Lin2d) -> GccEnt_QualifiedLin: ...
	@staticmethod
	def Enclosed(self, Obj: gp_Circ2d) -> GccEnt_QualifiedCirc: ...
	@staticmethod
	def Enclosing(self, Obj: gp_Circ2d) -> GccEnt_QualifiedCirc: ...
	@staticmethod
	def Outside(self, Obj: gp_Lin2d) -> GccEnt_QualifiedLin: ...
	@staticmethod
	def Outside(self, Obj: gp_Circ2d) -> GccEnt_QualifiedCirc: ...
	@staticmethod
	def PositionFromString(self, thePositionString: str) -> GccEnt_Position: ...
	@staticmethod
	def PositionFromString(self, thePositionString: str, thePosition: GccEnt_Position) -> bool: ...
	@staticmethod
	def PositionToString(self, thePosition: GccEnt_Position) -> str: ...
	@staticmethod
	def Unqualified(self, Obj: gp_Lin2d) -> GccEnt_QualifiedLin: ...
	@staticmethod
	def Unqualified(self, Obj: gp_Circ2d) -> GccEnt_QualifiedCirc: ...

class GccEnt_QualifiedCirc:
	def __init__(self, Qualified: gp_Circ2d, Qualifier: GccEnt_Position) -> None: ...
	def IsEnclosed(self) -> bool: ...
	def IsEnclosing(self) -> bool: ...
	def IsOutside(self) -> bool: ...
	def IsUnqualified(self) -> bool: ...
	def Qualified(self) -> gp_Circ2d: ...
	def Qualifier(self) -> GccEnt_Position: ...

class GccEnt_QualifiedLin:
	def __init__(self, Qualified: gp_Lin2d, Qualifier: GccEnt_Position) -> None: ...
	def IsEnclosed(self) -> bool: ...
	def IsOutside(self) -> bool: ...
	def IsUnqualified(self) -> bool: ...
	def Qualified(self) -> gp_Lin2d: ...
	def Qualifier(self) -> GccEnt_Position: ...
